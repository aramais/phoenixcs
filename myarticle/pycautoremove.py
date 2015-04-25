#!/usr/bin/env python

import os
directory = os.listdir('.')
for filename in directory:
    if filename[-3:] == 'pyc':
        print '- ' + filename
        os.remove(filename)
