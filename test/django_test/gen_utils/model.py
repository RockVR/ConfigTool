#!/usr/bin/python
# -*- coding: UTF-8 -*-

from enum import Enum
from gen_utils import parser

class ModelFieldType(Enum):
    BooleanField = 'BooleanField'
    IntegerField = 'IntegerField'
    FloatField = 'FloatField'
    CharField = 'CharField'
    TextField = 'TextField'
    ForeignKey = 'ForeignKey'
    ManyToManyField = 'ManyToManyField'

class ModelField:

    def __init__(self, type, origin_type, name, description, unique=False, required=True, server=True, client=True):
        self.type = type
        self.origin_type = origin_type
        self.name = name
        self.description = description
        self.unique = unique
        self.required = required
        self.server = server
        self.client = client

    def __str__(self):
        return u'ModelField {}'.format(self.name)

    def __AddDefine(self, content, part):
        ret = content
        if content != '':
            ret += ', '
        ret += part
        return ret

    def __GetRelatedName(self):
        related_name = self.name + '_Related'
        if 'Next' in self.name:
            related_name = self.name.replace('Next', 'Prev')
        elif 'Nex' in self.name:
            related_name = self.name.replace('Nex', 'Prev')
        elif 'Prev' in self.name:
            related_name = self.name.replace('Prev', 'Next')
        elif 'Pre' in self.name:
            related_name = self.name.replace('Pre', 'Next')
        return related_name

    def FieldDefine(self):
        content = ''
        if self.type == ModelFieldType.BooleanField:
            content = self.__AddDefine(content, 'default=False')
        if self.type == ModelFieldType.IntegerField:
            content = self.__AddDefine(content, 'default=0')
        if self.type == ModelFieldType.FloatField:
            content = self.__AddDefine(content, 'default=0')
        if self.type == ModelFieldType.CharField:
            content = self.__AddDefine(content, 'max_length=255')
        if self.type == ModelFieldType.ForeignKey:
            # parse related field
            related_field = parser.ParseForeignKeyName(self.origin_type)
            content = self.__AddDefine(content, "'{}'".format(related_field))
            content = self.__AddDefine(content, 'on_delete=models.CASCADE')
            content = self.__AddDefine(content, 'related_name=' + "'{}'".format(self.__GetRelatedName()))
        if self.type == ModelFieldType.ManyToManyField:
            # parse related field
            related_field = parser.ParseManyToManyFieldName(self.origin_type)
            content = self.__AddDefine(content, "'{}'".format(related_field))
            content = self.__AddDefine(content, 'related_name=' + "'{}'".format(self.__GetRelatedName()))
        if self.unique:
            content = self.__AddDefine(content, 'unique=True')
        # BooleanField do not accept null values
        if not self.required and self.type != ModelFieldType.BooleanField:
            content = self.__AddDefine(content, 'null=True, blank=True')
        return u'{} = models.{}({})'.format(self.name, self.type.value, content)

class Model:
    def __init__(self, name, description, group, xls_name, sheet_name):
        self.name = name
        self.description = description
        self.group = group
        self.fields = list()
        self.xls_name = xls_name
        self.sheet_name = sheet_name

    def __str__(self):
        return u'Model {}'.format(self.name)

    def AddField(self, field):
        self.fields.append(field)