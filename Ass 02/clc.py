# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 23:07:49 2022

@author: ajitb
"""

#import math
from math import pi
from math import e
import re

import sys
#import math

#sys.stdin = open('INPUT', 'r')

def postfix_calc(seq):
    
    stack = []
    #print("Length: ",len(seq))
    if len(seq) <= 2:
        return("Malformed expression")
    else: 
        for i in range(len(seq)):
            if (re.search(r'\d+|-\d+', seq[i]) is not None) and (re.search(r'[\d]+\.', seq[i]) is None):
                stack.append(int(seq[i]))
            elif re.search(r'[0-9]+\.[0-9]+|-[0-9]+\.[0-9]+', seq[i]) is not None:
                stack.append(int(seq[i]))
            elif re.search(r'\bpi\b', seq[i]) is not None:
                stack.append(pi)
            elif re.search(r'\be\b', seq[i]) is not None:
                stack.append(e)
            elif seq[i] == '+':
                try:
                  y = stack.pop()
                  x = stack.pop()
                  z = x + y
                  stack.append(z)
                except IndexError: return("Malformed expression")
            elif seq[i] == '-':
                try:
                  y = stack.pop()
                  x = stack.pop()
                  z = x - y
                  stack.append(z)
                except IndexError: return("Malformed expression")
            elif seq[i] == '*':
                try:
                  y = stack.pop()
                  x = stack.pop()
                  z = x * y
                  stack.append(z)
                except IndexError: return("Malformed expression")
            elif seq[i] == '/':
                try:
                  y = stack.pop()
                  x = stack.pop()
                  if y != 0:
                      z = x // y
                  else: return("Zero division")
                  stack.append(z)
                except IndexError: return("Malformed expression")
            

        try:
          return stack.pop()
        except IndexError: return("Malformed expression")


for line in sys.stdin:
    line = line.strip()
    if line:
       x = line.split()
       output = postfix_calc(x)
       print(output)
    else: continue
