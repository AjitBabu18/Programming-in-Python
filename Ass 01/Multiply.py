# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 00:07:54 2022

@author: ajitb
"""

import sys

if len(sys.argv) == 2:
    x = int(sys.argv[1])
    if sys.argv[1] != None:
        for i in range(1,11):
            print(i," * ",x," = ",x*i)
    else:
        raise ValueError("Enter Number")
        
