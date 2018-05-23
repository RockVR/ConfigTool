#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys, os
from datetime import datetime
from gen_utils import writer, parser
from gen_utils.model import ModelFieldType

MODEL_FILE = 'models.py'
ENUM_FILE = 'enums.py'
ADMIN_FILE = 'admin.py'
SERIALIZER_FILE = 'serializers.py'

XLS_FOLDER = 'test/xls/'
TARGET_FOLDER = 'test/django_test/app/'

def GenerateHeader(file):
    writer.I0(file, "# This file is auto-generated, please don't modify it directly.")
    writer.I0(file, "# Modify source xls file and use model_gen to regenerate again.")
    writer.I0(file, "#")
    writer.I0(file, "# Last generate time: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    writer.I0(file)

def main():

    ret = parser.ParseModel(XLS_FOLDER)
    if not ret:
        # parse failed
        return

    if not os.path.isdir(TARGET_FOLDER):
        os.makedirs(TARGET_FOLDER)

    (gen_models, gen_enums) = ret

    # models.py
    model_file = open(TARGET_FOLDER + MODEL_FILE, 'w')
    GenerateHeader(model_file)
    writer.I0(model_file, "from django.db import models")
    writer.I0(model_file)

    # enums.py
    enum_file = open(TARGET_FOLDER + ENUM_FILE, 'w')
    GenerateHeader(enum_file)
    writer.I0(enum_file, "from enum import Enum")
    writer.I0(enum_file)

    # admin.py
    admin_file = open(TARGET_FOLDER + ADMIN_FILE, 'w')
    GenerateHeader(admin_file)
    writer.I0(admin_file, "from django.contrib import admin")
    writer.I0(admin_file, "from .models import *")
    writer.I0(admin_file)

    # serializers.py
    serializer_file = open(TARGET_FOLDER + SERIALIZER_FILE, 'w')
    GenerateHeader(serializer_file)
    writer.I0(serializer_file, "from rest_framework import serializers")
    writer.I0(serializer_file, "from .models import *")
    writer.I0(serializer_file)

    # write models.py
    print("Writing " + MODEL_FILE + " file...")
    for model in gen_models:
        print("Generating model", model.name)
        # model comment
        writer.I0(model_file, "# Description: " + model.description)
        writer.I0(model_file, "# Group: " + model.group)
        # model define
        writer.I0(model_file, "class " + model.name + "(models.Model):")
        # model fields
        for field in model.fields:
            # model will auto define id
            if field.name.lower() == 'id':
                continue
            # model field comment
            writer.I1(model_file, "# Description: " + str(field.description))
            writer.I1(model_file, "# Type: " + str(field.origin_type))
            writer.I1(model_file, "# Unique: " + str(field.unique) + ", Required: " + str(field.required))
            writer.I1(model_file, "# Server: " + str(field.server) + ", Client: " + str(field.client))
            writer.I1(model_file, field.FieldDefine())
            writer.I0(model_file)
        # __str__
        writer.I1(model_file, "def __str__(self):")
        writer.I2(model_file, "return '{}: ' + str(self.id)".format(model.name))
        writer.I0(model_file)

    # write admin.py
    print("Writing " + ADMIN_FILE + " file...")
    for model in gen_models:
        print("Generating", model.name + "Admin")
        writer.I0(admin_file, "class " + model.name + "Admin(admin.ModelAdmin):")
        writer.I1(admin_file, "pass")
        writer.I0(admin_file)
        writer.I0(admin_file, "admin.site.register(" + model.name + ", " + model.name + "Admin)")
        writer.I0(admin_file)

    # write serializers.py
    print("Writing " + SERIALIZER_FILE + " file...")
    pending_models = list(gen_models)
    written_model_names = set()
    for model in pending_models:
        # check if model has relation field
        related_model_tup = list() # (0: field_name, 1: field_type)
        for field in model.fields:
            if field.type == ModelFieldType.ForeignKey or field.type == ModelFieldType.ManyToManyField:
                if field.type == ModelFieldType.ForeignKey:
                    related_field = parser.ParseForeignKeyName(field.origin_type)
                elif field.type == ModelFieldType.ManyToManyField:
                    related_field = parser.ParseManyToManyFieldName(field.origin_type)
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
        # can write current model
        if meet_all:
            print("Generating", model.name + "Serializer")
            writer.I0(serializer_file, "class " + model.name + "Serializer(serializers.ModelSerializer):")
            for model_tup in related_model_tup:
                # skip if is related to self
                if model_tup[1] == model.name:
                    continue
                # related field serializer should already generated
                writer.I1(serializer_file, model_tup[0] + " = " + model_tup[1] + "Serializer(read_only=True)")
            writer.I0(serializer_file)
            writer.I1(serializer_file, "class Meta:")
            writer.I2(serializer_file, "model = " + model.name)
            writer.I2(serializer_file, "fields = [")
            for field in model.fields:
                field_name = field.name
                if field_name == "Id":
                    field_name = "id"
                writer.I3(serializer_file, "'{}',".format(field_name))
            writer.I2(serializer_file, "]")
            writer.I0(serializer_file)
            # mark written model
            written_model_names.add(model.name)
        else:
            # push back current model for next visit
            pending_models.append(model)

    # write enums.py
    print("Writing " + ENUM_FILE + " file...")
    for enum in gen_enums:
        print("Generating enum", enum.name)
        writer.I0(enum_file, "class " + enum.name + "(Enum):")
        for field in enum.fields:
            writer.I1(enum_file, field.name + " = " + str(field.value) + " # " + field.description)
        writer.I0(enum_file)

    # close file
    model_file.close()
    enum_file.close()
    admin_file.close()
    serializer_file.close()

    print("Files generated in", TARGET_FOLDER)
    print("Success!")

main()
