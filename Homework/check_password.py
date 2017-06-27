#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function
import string


def valid_password(pwd):
    if len(pwd) < 3 or len(pwd) > 10:
        return False

    if pwd[0] not in string.ascii_letters:
        return False

    legal_chars = string.ascii_letters + string.digits + "_"
    for char in pwd:
        if char not in legal_chars:
            return False
    if pwd[-1] == "_":
        return False
    return True


print(valid_password('lrt'))
