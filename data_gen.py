#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, os
from django.apps import apps
from gen_utils import writer, parser
from gen_utils.model import ModelFieldType

APP_LABEL = 'app' # your app name here
XLS_FOLDER = '../xls' # your xls file folder here, relative path

# exec(open('data_gen.py').read())

def main():
    ret = parser.ParseModel(XLS_FOLDER)
    if not ret:
        # parse failed
        return
    (gen_models, gen_enums) = ret
    print("Writing model data...")
    pending_models = list(gen_models)
    written_model_names = set()
    # first round
    for model in pending_models:
        # check if model has relation field
        related_model_tup = list() # (0: field_name, 1: field_type)
        for field in model.fields:
            if field.type == ModelFieldType.ForeignKey:
                if field.type == ModelFieldType.ForeignKey:
                    related_field = parser.ParseForeignKeyName(field.origin_type)
                if not related_field:
                    raise Exception('Parse related field error ' + field.origin_type)
                tup = (field.name, related_field)
                related_model_tup.append(tup)
        # check if all related model is written before
        meet_all = True
        for model_tup in related_model_tup:
            # do not count if related to self
            if model_tup[1] not in written_model_names and model_tup[1] != model.name:
                meet_all = False
                break
        # can write current model data
        if meet_all:
            print("Writing " + model.name + " data...")
            ModelClass = apps.get_model(APP_LABEL, model.name)
            data = parser.ParseData(model.xls_name, model.sheet_name)
            # start from 1, skip field name
            i = 1
            while i < len(data):
                field_names = data[0]
                row_data = data[i]
                print("Writing record " + str(i) + ": " + str(row_data))
                row_id = int(row_data[0])
                # if already in db
                model_record = ModelClass.objects.filter(id=row_id).first()
                if not model_record:
                    model_record = ModelClass()
                read_array = False
                storage_array = ""
                pending = False
                # start from 1, skip id
                k = 1
                for j in range(1, len(row_data)):
                    value = row_data[j]
                    storage_value = value
                    field = model.fields[k]
                    if value:
                        # convert value for storage
                        enum = parser.ParseModelFieldEnum(field.origin_type)
                        if enum: # enum type
                            for enum_filed in enum.fields:
                                if enum_filed.description == value:
                                    storage_value = int(enum_filed.value)
                                    break
                        elif field.origin_type.startswith('Enum'): # enum type
                            for enum in gen_enums:
                                # find the enum
                                if enum.name == field.origin_type:
                                    for enum_field in enum.fields:
                                        if enum_field.description == value:
                                            storage_value = int(enum_field.value)
                                            break
                                    break
                        elif field.type == ModelFieldType.IntegerField:
                            storage_value = int(value)
                        elif field.type == ModelFieldType.BooleanField:
                            storage_value = bool(value)
                        elif field.type == ModelFieldType.FloatField:
                            storage_value = float(value)
                        elif field.type == ModelFieldType.ForeignKey:
                            related_field = parser.ParseForeignKeyName(field.origin_type)
                            RelatedModelClass = apps.get_model(APP_LABEL, related_field)
                            # find related record
                            related_record = RelatedModelClass.objects.filter(id=storage_value).first()
                            if related_record:
                                setattr(model_record, field.name, related_record)
                            else:
                                if related_field == model.name:
                                    pending = True
                                else:
                                    raise Exception('No related field model data ' + related_field)
                        elif field.type == ModelFieldType.ManyToManyField:
                            # can't associate it with a ManyToManyField until it's been saved
                            pass
                        elif not read_array and field.origin_type.startswith('array('): # array type
                            read_array = True # start read array
                            storage_array = "[" + str(value)

                        if not read_array and field.type != ModelFieldType.ForeignKey and field.type != ModelFieldType.ManyToManyField:
                            # save storage_value
                            setattr(model_record, field.name, storage_value)

                    if pending:
                        # pending current row to last for visit again
                        data.append(row_data)
                        break

                    # in read array
                    if read_array:
                        if field_names[j] == field_names[j - 1]: # continue read
                            if value:
                                storage_array += "," + str(value)
                        elif not field.origin_type.startswith('array('): # end read
                            storage_array += "]"
                            setattr(model_record, field_names[j - 1], storage_array)
                            read_array = False

                    # if not array type
                    if len(field_names) > j + 1 and field_names[j] != field_names[j + 1]:
                        k += 1

                i += 1

                # save record
                model_record.id = row_id
                model_record.save()

            # mark written model
            written_model_names.add(model.name)
        else:
            # push back current model for next visit
            pending_models.append(model)

    # second round for writing many-to-many field
    print("Writing many-to-many field data...")
    for model in gen_models:
        ModelClass = apps.get_model(APP_LABEL, model.name)
        data = parser.ParseData(model.xls_name, model.sheet_name)
        # start from 1, skip field name
        for i in range(1, len(data)):
            field_names = data[0]
            row_data = data[i]
            row_id = int(row_data[0])
            # should already in db
            model_record = ModelClass.objects.filter(id=row_id).first()
            if not model_record:
                raise Exception('Record not found for model ' + model.name)
            k = 1
            for j in range(1, len(row_data)):
                value = row_data[j]
                field = model.fields[k]
                if value:
                    if field.type == ModelFieldType.ManyToManyField:
                        related_field = parser.ParseManyToManyFieldName(field.origin_type)
                        RelatedModelClass = apps.get_model(APP_LABEL, related_field)
                        # find related record
                        related_record = RelatedModelClass.objects.filter(id=value).first()
                        if not related_record:
                            raise Exception('Record not found for model ' + related_field)
                        m2m_instance = getattr(model_record, field.name)
                        print("Adding many-to-many relation " + model.name + "-" + related_field + " through field " + field.name + " id: " + str(row_id) + "-" + str(value))
                        m2m_instance.add(related_record)

                # if not array type
                if len(field_names) > j + 1 and field_names[j] != field_names[j + 1]:
                    k += 1

    print("Success!")

main()