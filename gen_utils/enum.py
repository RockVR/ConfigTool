#!/usr/bin/python
# -*- coding: UTF-8 -*-

class EnumField:
    def __init__(self, name, value, description):
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        return u'EnumField {}'.format(self.name)

class Enum:
    def __init__(self, name):
        self.name = name
        self.fields = list()

    def __str__(self):
        return u'Enum {}'.format(self.name)

    def AddField(self, field):
        self.fields.append(field)