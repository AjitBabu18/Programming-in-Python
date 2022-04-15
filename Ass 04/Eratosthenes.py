# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 19:42:16 2022

@author: ajitb
"""
#import math


import sys
#sys.stdin = open('INPUT','r')
def eratosthenes(x):
    A = [True] * x
    output = []
    i = 2
    while i < x:
        output.append(i)
        A[i * 2::i] = [False] * (((x - 1) // i) - 1)
        i += 1
        while i < x and not A[i]:
            i += 1
    return output
    """
	lis = set(range(2, x+1))
	for i in range(2, math.floor(math.sqrt(x))):
		if i in lis:
			j = i*i
			count = 1
			while j <= x:
				if j in lis:
					lis.remove(j)
				j = i*i+count*i
				count +=1
					
	return lis"""
try:
    for line in sys.stdin:
        line = line.strip()
        if line:
           x = line.split()
           x = list(map(int, x))
           #print(x)
           for i in x:
               result = len(eratosthenes(i))
               print(result)
except ValueError: 
    sys.exit("Error")
except IndexError: 
    sys.exit("Error")