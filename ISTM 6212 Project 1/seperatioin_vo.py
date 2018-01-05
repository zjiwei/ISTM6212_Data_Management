
#!/usr/bin/env python

"""
A filter that _________.
"""

import re
import fileinput

def process(line):
    pattern = '\w{2,}'
    com = re.compile(pattern)
    text = com.findall(line)
    for i in range(0,len(text)):
        print(text[i])


for line in fileinput.input():
    process(line)