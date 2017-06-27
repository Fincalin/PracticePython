#!/usr/bin/python
# -*- coding:UTF-8 -*-


from __future__ import print_function


with open('/etc/passwd', 'r') as source, open('/tmp/passwd', 'w') as target:
    for line in source:
        print(line.split(':')[0], line.split(':')[-1], file=target)



