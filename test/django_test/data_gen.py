#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, os
from django.apps import apps
from gen_utils import writer, parser
from gen_utils.model import ModelFieldType, ParseOneToOneFieldName, ParseForeignKeyName

APP_LABEL = 'app' # your app name here
XLS_FOLDER = '../xls' # your xls file folder here, relative path

def main():
    ret = parser.ParseModel(XLS_FOLDER)
    if not ret:
        # parse failed
        return
    (gen_models, gen_enums) = ret
    print("Writing data...")
    pending_models = list(gen_models)
    written_model_names = set()
    for model in pending_models:
        # check if model has relation field
        related_model_tup = list() # (0: field_name, 1: field_type)
        for field in model.fields:
            if field.type == ModelFieldType.OneToOneField or field.type == ModelFieldType.ForeignKey:
                if field.type == ModelFieldType.OneToOneField:
                    related_field = ParseOneToOneFieldName(field.origin_type)
                elif field.type == ModelFieldType.ForeignKey:
                    related_field = ParseForeignKeyName(field.origin_type)
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
            # instance = ModelClass()
            parser.ParseData(model.xls_name, model.sheet_name)


main()