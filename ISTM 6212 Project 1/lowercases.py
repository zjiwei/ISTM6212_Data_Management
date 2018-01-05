#!/usr/bin/env python

"""
A filter that transform text ino lower case.
"""

import fileinput


def process(line):
    """For each line of input, transform text ino lower case."""
    print(str.lower(line[:-1]))


for line in fileinput.input():
    process(line)
