#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re

class_name_set = set()

with open('bootstrap.css') as file_handle:
    for line in file_handle:
        line = re.sub(r'".*?"', '', line)
        for class_name in re.findall(r'(\.[a-z][a-z0-9\-]+)', line):
            class_name_set.add(class_name)

print('\n'.join(sorted(class_name_set)))

