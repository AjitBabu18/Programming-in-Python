# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 00:43:02 2022

@author: ajitb
"""

import sys
#import math

#sys.stdin = open('INPUT', 'r')

def operation(sign, operand1, operand2):
        if sign == '*':
            return(int(operand1) * int(operand2))
        elif sign == '+':
           return(int(operand1) + int(operand2))
        elif sign == '-':
           return(int(operand1) - int(operand2))
        elif sign == '/':
            if operand2 != '0':
                return(int(operand1) // int(operand2))
            else: return("Zero division")

def calculator(inp):
    s = []  
    if len(inp) <= 2:
        return("Malformed expression")
    else:
        for sign in inp:
            if sign.isdigit():
                s.append(sign)
            elif sign is '+' or '/' or 'x' or '*':
                if len(s) >=2:
                    operand1 = s.pop()
                    operand2 = s.pop()
                    a = operation(sign, operand2, operand1)
                    s.append(a)
                else:
                    return("Malformed expression")
            else:
                return("Malformed expression")
        if len(s) > 1:
            return("Malformed expression")
        else:
            return s.pop()
        
for line in sys.stdin:
    line = line.strip()
    if line:
       x = line.split()
       output = calculator(x)
       print(output)
    else: continue
