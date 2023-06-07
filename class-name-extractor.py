#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import re

class_name_set = set()

with open('bootstrap.css') as file_handle:
    for line in file_handle:
        line = line.strip()
        if line.startswith('.'):
            for class_name in re.split(r'[\s,\{]+', line):
                class_name = class_name.split(':')[0]
                if class_name.startswith('.'):
                    class_name_set.add(class_name)
            
print('\n'.join(sorted(class_name_set)))

