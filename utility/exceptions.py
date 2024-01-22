#!/usr/bin/python3
# -*- coding:utf-8 -*-

class EmployeeException(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)

class EmployeeDataNotFound(EmployeeException):
    pass

