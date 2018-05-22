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
    OneToOneField = 'OneToOneField'
    ForeignKey = 'ForeignKey'

class ModelField:

    def __init__(self, sourceModel, type, origin_type, name, description, unique=False, required=True, server=True, client=True):
        self.sourceModel = sourceModel
        self.type = type
        self.origin_type = origin_type
        self.name = name
        self.description = description
        self.unique = unique
        self.required = required
        self.server = server
        self.client = client
        self.foreignKey = None

    def __str__(self):
        return u'ModelField {}'.format(self.name)

    def AddDefine(self, content, part):
        ret = content
        if content != '':
            ret += ', '
        ret += part
        return ret

    def GetRelatedName(self):
        related_name = self.name
        if self.foreignKey:
            related_name = self.foreignKey
        elif 'Next' in self.name:
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
            content = self.AddDefine(content, 'default=False')
        if self.type == ModelFieldType.IntegerField:
            content = self.AddDefine(content, 'default=0')
        if self.type == ModelFieldType.FloatField:
            content = self.AddDefine(content, 'default=0')
        if self.type == ModelFieldType.CharField:
            content = self.AddDefine(content, 'max_length=255')
        if self.type == ModelFieldType.OneToOneField:
            # parse related field
            related_field = parser.ParseOneToOneFieldName(self.origin_type)
            content = self.AddDefine(content, "'{}'".format(related_field))
            content = self.AddDefine(content, 'on_delete=models.CASCADE')
            content = self.AddDefine(content, 'related_name=' + "'{}'".format(self.GetRelatedName()))
        if self.type == ModelFieldType.ForeignKey:
            content = self.AddDefine(content, "'{}'".format(self.sourceModel.name))
            content = self.AddDefine(content, 'on_delete=models.CASCADE')
            content = self.AddDefine(content, 'related_name=' + "'{}'".format(self.GetRelatedName()))
        if self.unique:
            content = self.AddDefine(content, 'unique=True')
        # BooleanField do not accept null values
        if not self.required and self.type != ModelFieldType.BooleanField:
            content = self.AddDefine(content, 'null=True, blank=True')
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