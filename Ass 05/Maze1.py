# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:37:18 2022

@author: ajitb
"""

import sys
import numpy as np

sys.stdin = open('INPUT','r')

def stepl(i,j,x):
  #if x[i][j+1] != '#': 
   if x[i+1][j] == '#': 
    if x[i+1][j] == '#' and x[i][j+1] == '#' and x[i-1][j] == '#':
        x[i][j] = '.'
        x[i][j-1] = '<'
    elif x[i+1][j] == '#' and x[i][j+1] == '#':
            if x[i-1][j] == '.':
               x[i][j] = '.'
               x[i-1][j] = '^'
               i-=1
    elif x[i][j+1] != '#':
         x[i][j] = '.'
         x[i][j+1] = '>'
         j+=1
         if x[i+1][j] == '#' and x[i][j+1] == '#' and x[i-1][j] == '#':
              x[i][j] = '^'
         elif x[i-1][j] == '#' and x[i][j+1] == '#':
             x[i][j] = '<'
         elif x[i+1][j] == '#' and x[i][j+1] == '#':
                 if x[i-1][j] == '.':
                     x[i][j] = '^'
            
         
   else: 
       if x[i-1][j] == '#' and x[i][j+1] == '#':
           x[i][j] = '.'
           x[i][j-1] = '<'
       else: 
           x[i][j] = '.'
           x[i+1][j] = 'v'
   """elif x[i-1][j] == '#' and x[i][j+1] == '#':
      x[i][j] = '.'
      x[i][j-1] = '<'"""     
   return x

def stepu(i,j,x):
  #if x[i-1][j] == '#' or x[i][j-1] != '#':
   if x[i][j+1] == '#':
    if x[i-1][j] == '#' and x[i][j+1] == '#' and x[i][j-1] == '#':
        x[i][j] = '.'
        x[i+1][j] = 'v'
    elif x[i-1][j] == '#' and x[i][j+1] == '#':
       if x[i][j-1] == '.':
          x[i][j] = '.'
          x[i][j-1] = '<'
          j-=1
    elif x[i-1][j] != '#':
       x[i][j] = '.'
       x[i-1][j] = '^'
       i-=1
       if x[i-1][j] == '#' and x[i][j+1] == '#' and x[i][j-1] == '#':
           x[i][j] = 'v'
       elif x[i-1][j] == '#' and x[i][j+1] == '#':
           x[i][j] = 'v'
   else:
       if x[i-1][j] == '#' and x[i][j-1] == '#':
          x[i][j] = '.'
          x[i+1][j] = 'v'
       else:
           x[i][j] = '.'
           x[i][j+1] = '>'
   """elif x[i-1][j] == '#' and x[i][j-1] == '#':
      x[i][j] = '.'
      x[i+1][j] = 'v'""" 
   return x

def stepb(i,j,x):
   if x[i-1][j] == '#':
    if x[i-1][j] == '#' and x[i][j-1] == '#' and x[i+1][j] == '#':
        x[i][j] = '.'
        x[i][j+1] = '>'
    if x[i-1][j] == '#' and x[i][j-1] == '#':
           if x[i+1][j] == '.':
               x[i][j] = '.'
               x[i+1][j] = 'v'
               i+=1
    elif x[i][j-1] != '#':
         x[i][j] = '.'
         x[i][j-1] = '<'
         j-=1
         if x[i-1][j] != '#':
             x[i][j] = '^'
         elif x[i-1][j] == '#' and x[i][j-1] == '#' and x[i+1][j] == '#':
             x[i][j] = 'v'
   else:
       if x[i+1][j] == '#' and x[i][j-1] == '#':
           x[i][j] = '.'
           x[i][j+1] = '>'
       else:
           x[i][j] = '.'
           x[i-1][j] = '^'
         
   return x

def stepr(i,j,x):
    #print(i, j)
   if x[i][j-1] == '#':
    if x[i+1][j] == '#' and x[i][j-1] == '#' and x[i][j+1] == '#':
        x[i][j] = '.'
        x[i-1][j] = '^'
    if x[i+1][j] == '#' and x[i][j-1] == '#':
       if x[i][j+1] == '.':
          x[i][j] = '.'
          x[i][j+1] = '>'
          j+=1
    elif x[i+1][j] != '#':
       x[i][j] = '.'
       x[i+1][j] = 'v'
       i+=1
       if x[i][j-1] != '#':
           x[i][j] = '<'
       elif x[i+1][j] == '#' and x[i][j-1] == '#' and x[i][j+1] == '#':
           x[i][j] = '>'
   else:
       if x[i+1][j] == '#' and x[i][j+1] == '#':
          x[i][j] = '.'
          x[i-1][j] = '^'
       else: 
           x[i][j] = '.'
           x[i][j-1] = '<'
   return x

def Maze(x, l):
    #print(x)
    column = len(x[0])
    row = len(x)
    #y = x.split()
    #arr = np.array(y)
    #print(arr)
    for k in range(l):
          #print(k)
          a = ([(ix,iy) for ix, row in enumerate(x) for iy, i in enumerate(row) if i == '>'])
          b = ([(ix,iy) for ix, row in enumerate(x) for iy, i in enumerate(row) if i == '<'])
          c = ([(ix,iy) for ix, row in enumerate(x) for iy, i in enumerate(row) if i == '^'])
          d = ([(ix,iy) for ix, row in enumerate(x) for iy, i in enumerate(row) if i == 'v'])
          #print(a[0][1])
          if a:
              #print(a[0])
              x = stepl(a[0][0], a[0][1], x)
          if b:
              x = stepb(b[0][0], b[0][1], x)
          if c:
              #print(c[0])
              x = stepu(c[0][0], c[0][1], x)
          if d:
              x = stepr(d[0][0], d[0][1], x)
    #print('a=',x[a])
    """for i in range(row):
        for j in range(column):
            if x[i][j] == '<' or x[i][j] == '>' or x[i][j] == '^' or x[i][j] == 'v':
                if x[i+1][j] == '#' and x[i][j+1] == '#':
                    if x[i-1][j] == '.':
                       x[i][j] = '.'
                       x[i-1][j] = '^'
                       i-=1
            elif x[i][j+1] != '#':
                 x[i][j] = '.'
                 x[i][j+1] = '>'
                 j+=1
                #x[i][j] = '.'
                 #print(x[i][j], i, j)
        #if k == l:
            #print(k)
         #   break"""
    """for k in range(1,l+1): 
                 try:
                   if x[i+1][j] == '#' and x[i][j+k] == '.':
                       print(k,j)
                       if x[i][j+k]:
                              x[i][j+k] = '>'
                              x[i][j] = '.'
                       #i+=1
                       
                              #j+=1
                       try:
                           if x[i][j+k+1] == '#':
                               x[i][j+k] = '.'
                               j+=k
                               print(k,j)
                       except IndexError:
                                  print('no')
                   elif x[i+1][j] == '#' and x[i][j+1] == '#':
                       if x[i-k][j] == '.' and x[i-k][j+1] == '#':
                           #if k == l:
                            #   break
                           print(k)
                           i-=1
                           x[i-k+1][j] = '.'
                           x[i-k][j] = '^'
                           #i -= 1
                           #print(i)
                           
                 except IndexError:
                       if x[i+1][j] == '#' and x[i][j+1] == '#':
                           if x[i-k][j] == '.' and x[i-k][j+1] == '#':
                               #if k == l:
                                #   break
                               print(k)
                               i-=1
                               x[i+1][j] = '.'
                               x[i][j] = '^'"""
                        
                   
                
                           
    lis = list(x)                    
    for i in range(row):
        for j in range(column):
            try:
               if lis[i][j+1]:
                  print(lis[i][j], end=' ')
            except IndexError:
                  print(lis[i][j])
        #print('')
            #print(lis[i][j]," ")
        #print("\n")
    """for i in range(length//2):
          #print(i)
          if y[i] == '<' or y[i] == '>' or y[i] == '^' or y[i] == 'v':
             #print(x[i])
             y[i] = '.'
             print(y)"""

try:
    arr = []
    k=0
    length = 0
    for line in sys.stdin:
        if k == 0:
            line = line.strip()
            #x = line.split()
            length = int(line)
            k=1
        else:
            line = line.strip()
            if line:
               x = line.split()
           #print(x)
           #for i in x:
               arr.append(x)
               
               #Maze(line)
               #print(result)
    #print(length, len(arr))
    Maze(arr, length)
except ValueError: 
    sys.exit("Error")
except IndexError: 
    sys.exit("Error")