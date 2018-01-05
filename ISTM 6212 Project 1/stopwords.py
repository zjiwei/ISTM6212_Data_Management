#!/usr/bin/env python

"""
A filter that _________.
"""

import re 
import fileinput

def process(line):
    """For each line of input, _____."""
    if len(line) == 3:
        line = re.sub('am|an|as|at|be|by|do|he|if|in|is|it|me|my|no|of|on|or|so|to|us|up|we', "\n", line)
    elif len(line) == 4:
        line = re.sub('all|and|any|are|but|can|did|for|get|got|had|has|her|his|him|how|its|let|may|nor|not|our|out|own|say|she|the|tis|too|was|who|why|yet|yes|you', "\n", line)
    elif len(line) == 5:
        line = re.sub('able|also|been|does|down|else|ever|from|have|hers|into|just|most|more|much|must|only|over|said|some|such|than|that|them|then|they|this|upon|were|what|when|whom|will|with|your', "\n", line)
    elif len(line) == 6:
        line = re.sub('about|after|among|could|shall|every|least|might|never|often|other|quite|since|their|there|these|where|which|while|would', "\n", line)
    elif len(line) == 7:
        line = re.sub('across|almost|before|cannot|either|likely|rather|should', "\n",line)
    elif len(line) == 8:
        line = re.sub('because|however|neither', "\n", line)
#    print(line[:-1])
    pattern = '\w{2,}'
    com = re.compile(pattern)
    text = com.findall(line)
    for i in range(0,len(text)):
        print(text[i])
    

for line in fileinput.input():
    process(line)

    
