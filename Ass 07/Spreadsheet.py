# -*- coding: utf-8 -*-
"""
Created on Sun May 22 09:11:44 2022

@author: ajitb
"""

import sys
import csv
#import numpy as np
#import pandas as pd
#import csv


ass = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}

#print(data[0][0])
#sys.stdin = open('INPUT01','r')
x=[]

         #print(', '.join(row))
c = '='
d = '/0'
s = 'SUM('
avg = 'AVG('
p = '+'
sub = '-'
mul = '*'
div = '/'
for line in sys.stdin:
       line = line.strip()
       #try:
       if line:
           x.append(line.split(';'))
           #x[i][j] = x.replace('=','')
           #x = list(x)
for i in range(len(x)):
    for j in range(len(x[i])):
        
        if x[i][j] == '':
            x[i][j] = '0'
            continue
        co = 0
        
        for k in x[i][j]:
                     if k.isalpha():
                         co+=1
        
        if co == 1:
          #print(x[i][j], len(x[i][j]))
          ou=0
          bo=0
          c1 = 0
          for k in x[i][j]:
            #print(i, k, c1, ou)
            c1+=1
            if ou==1:
                if int(k) != i+1:
                        #print(int(k))
                        ou=0
                        bo=1
                        break
            if  k.isalpha():
               #print((x[i][j].find(div)))
               #if (x[i][j].find(div) > -1 or (x[i][j].find(p) > -1) or (x[i][j].find(mul) > -1) or (x[i][j].find(sub) > -1)) == False: 
                z = ass.get(k)
                
                if x[i][z] == x[i][j]:
                   #print(x[i][z], x[i][j])
                   #t1= x[i][j]
                   #x[i][j] = '#CYCLE'
                 #  continue
                   ou+=1
                   
            
          if ou==1 and len(x[i][j]) == 3:
              #print(i+1)
              #if int(k) != i+1:
                  
                  x[i][j] = '#CYCLE'
                  #ou=0
          else: continue
for i in range(len(x)):
  for j in range(len(x[i])):
        coun = 0
        #print(len(x[i]), j)
        for lo in x[i][j]:
           if lo.isalpha() == False:
                 #print(x[i][j])
                 
                 coun=1
                 #break
           else:
               coun=0
               
               break
        #print(c1)
        #print(j)
        if coun == 1:
            #print(x[i][j])
            x[i][j] = x[i][j].replace('=','')
            #print(x[i][j])
            #print(x[i][j])
            if x[i][j].find(p) != -1:
               #z = x[i][j].find(p)
               temp = x[i][j].split(p)
            elif x[i][j].find(sub) != -1:
                #z = x[i][j].find(sub)
                temp = x[i][j].split(sub)
            elif x[i][j].find(mul) != -1:
                #z = x[i][j].find(mul)
                temp = x[i][j].split(mul)
            elif x[i][j].find(div) != -1:
                #z = x[i][j].find(div)
                temp = x[i][j].split(div)
            else: continue
            
            if x[i][j].find(p) != -1:
                #print(kq, kp)
                su = int(temp[0])+int(temp[1])
                su = str(su)
                #print(su+'.')
                x[i][j] = su+'.'
            elif x[i][j].find(sub) != -1:
                x[i][j] = str(int(temp[0])-int(temp[1]))+'.'
            elif x[i][j].find(mul) != -1:
                x[i][j] = str(int(temp[0])*int(temp[1]))+'.'
            elif x[i][j].find(div) != -1:
               try:
                x[i][j] = str(int(temp[0])//int(temp[1]))+'.'
               except ZeroDivisionError:
                   if j+1 == len(x[i]):
                      print('#DIV0', end='')
                   else:
                     print('#DIV0', end=';')
#print(x)

for i in range(len(x)):
    for j in range(len(x[i])):
      try:  
          if x[i][j].find(d) != -1:
                  if j+1 == len(x[i]):
                     print('#DIV0', end='')
                  else:
                    print('#DIV0', end=';')
          elif x[i][j] == '0.':
              if j+1 == len(x[i]):
                  print(0, end='')
              else:
                  print(0, end=';')
          elif x[i][j] == '#CYCLE':
                   if j+1 == len(x[i]):
                       print('%s' %x[i][j], end='')
                   else:
                       print('%s;' %x[i][j], end='')
          elif x[i][j] == '0':
              if j+1 == len(x[i]):
                  print('', end='')
              else:
                  print(';', end='')
          elif x[i][j].find(c) != -1: 
            x[i][j] = x[i][j].replace('=','')
            co=0     
            for k in x[i][j]:
                         if k.isalpha():
                             co+=1
                
                
            if x[i][j].find(s) != -1:
                     x[i][j] = x[i][j].replace(s,'')
                     x[i][j] = x[i][j].replace(')','')
                     temp = x[i][j].split(':')
                     #t1 = temp[0].split('')
                     if temp[0][0] != temp[1][0]:
                         count=0
                         y = x[int(temp[0][1])-1]
                         start = ass.get(temp[0][0])
                         end = ass.get(temp[1][0])
                         for k in range(start, end+1):
                             count += int(y[k])
                         if j+1 == len(x[i]):
                             print('%d' %count, end='')
                         else:
                            print('%d;' %count, end='')
                     if temp[0][0] == temp[1][0]:
                         count=0
                         start = int(temp[0][1])
                         end = int(temp[1][1])
                         #print(start, end)
                         for k in range(start,end+1):
                             count += int(x[k-1][ass.get(temp[0][0])])
                         if j+1 == len(x[i]):
                             print('%d' %count, end='')
                         else:
                            print('%d;' %count, end='')
            elif x[i][j].find(avg) != -1:
                        #print(x)
                        x[i][j] = x[i][j].replace(avg,'')
                        x[i][j] = x[i][j].replace(')','')
                        #print(x)
                        temp = x[i][j].split(':')
                        #t1 = temp[0].split('')
                        if temp[0][0] != temp[1][0]:
                            count=0
                            y = x[int(temp[0][1])-1]
                            start = ass.get(temp[0][0])
                            end = ass.get(temp[1][0])
                            #print(start, end)
                            for k in range(start, end+1):
                                count += int(y[k])
                            if j+1 == len(x[i]):
                                print('%d' %int(count/end), end='')
                            else:
                               print('%d;' %int(count/end), end='')
                        if temp[0][0] == temp[1][0]:
                            count=0
                            start = int(temp[0][1])
                            end = int(temp[1][1])
                            #print(start, end)
                            for k in range(start,end+1):
                                count += int(x[k-1][ass.get(temp[0][0])])
                            if j+1 == len(x[i]):
                                print('%d' %int(count/end), end='')
                            else:
                               print('%d;' %int(count/end), end='')
            if co == 1:
                kw=0
                kq=0
                if x[i][j][0].isalpha():
                     if x[i][j].find(p) != -1:
                              #x[i] = x[i].replace(p,'')
                              #x[i] = x[i].replace(')','')
                              #print(x)
                              temp = x[i][j].split(p)
                              #print(temp)
                              add = 0 
                              try:
                                  if int(temp[0][2]):
                                      row1 = int(temp[0][1])*10 + int(temp[0][2])
                              except IndexError:
                                  row1 = int(temp[0][1])
                              for l in temp[1]:  
                                
                                  
                                  if int(l):
                                      kw+=1
                                      if kw > 1:
                                          kq=kq*10+int(l)
                                          #kw+=1
                                          continue
                                      kq = int(l)
                              try:
                                 if x[row1-1][ass.get(temp[0][0])] == '#CYCLE':
                                     if j+1 == len(x[i]):
                                        print('#CYCLE', end='')
                                        continue
                                     else:
                                       print('#CYCLE', end=';')
                                       continue
                                 add = int(x[row1-1][ass.get(temp[0][0])]) + kq
                                 if j+1 == len(x[i]):
                                    print('%d' %add, end='')
                                 else:
                                    print('%d;' %add, end='')
                              
                              except IndexError:
                                 if j+1 == len(x[i]):
                                    print('#ERROR', end='')
                                 else:
                                   print('#ERROR', end=';')
                     elif x[i][j].find(sub) != -1:
                              #x[i] = x[i].replace(p,'')
                              #x[i] = x[i].replace(')','')
                              #print(x)
                              temp = x[i][j].split(sub)
                              #print(temp)
                              add = 0 
                              try:
                                  if int(temp[0][2]):
                                      row1 = int(temp[0][1])*10 + int(temp[0][2])
                              except IndexError:
                                  row1 = int(temp[0][1])
                              for l in temp[1]:  
                                
                                  
                                  if int(l):
                                      kw+=1
                                      if kw > 1:
                                          kq=kq*10+int(l)
                                          #kw+=1
                                          continue
                                      kq = int(l)
                              try:
                                 if x[row1-1][ass.get(temp[0][0])] == '#CYCLE':
                                     if j+1 == len(x[i]):
                                        print('#CYCLE', end='')
                                        continue
                                     else:
                                       print('#CYCLE', end=';')
                                       continue
                                 add = int(x[row1-1][ass.get(temp[0][0])]) - kq
                                 if j+1 == len(x[i]):
                                    print('%d' %add, end='')
                                 else:
                                    print('%d;' %add, end='')
                              
                              except IndexError:
                                 if j+1 == len(x[i]):
                                    print('#ERROR', end='')
                                 else:
                                   print('#ERROR', end=';')   
                     elif x[i][j].find(mul) != -1:
                              #x[i] = x[i].replace(p,'')
                              #x[i] = x[i].replace(')','')
                              #print(x)
                              temp = x[i][j].split(mul)
                              #print(temp)
                              add = 0 
                              try:
                                  if int(temp[0][2]):
                                      row1 = int(temp[0][1])*10 + int(temp[0][2])
                              except IndexError:
                                  row1 = int(temp[0][1])
                              for l in temp[1]:  
                                
                                  
                                  if int(l):
                                      kw+=1
                                      if kw > 1:
                                          kq=kq*10+int(l)
                                          #kw+=1
                                          continue
                                      kq = int(l)
                              try:
                                 if x[row1-1][ass.get(temp[0][0])] == '#CYCLE':
                                     if j+1 == len(x[i]):
                                        print('#CYCLE', end='')
                                        continue
                                     else:
                                       print('#CYCLE', end=';')
                                       continue
                                 add = int(x[row1-1][ass.get(temp[0][0])]) * kq
                                 if j+1 == len(x[i]):
                                    print('%d' %add, end='')
                                 else:
                                    print('%d;' %add, end='')
                              
                              except IndexError:
                                 if j+1 == len(x[i]):
                                    print('#ERROR', end='')
                                 else:
                                   print('#ERROR', end=';')  
                     elif x[i][j].find(div) != -1:
                              #x[i] = x[i].replace(p,'')
                              #x[i] = x[i].replace(')','')
                              #print(x)
                              temp = x[i][j].split(div)
                              #print(temp)
                              add = 0 
                              try:
                                  if int(temp[0][2]):
                                      row1 = int(temp[0][1])*10 + int(temp[0][2])
                              except IndexError:
                                  row1 = int(temp[0][1])
                              for l in temp[1]:  
                                
                                  
                                  if int(l):
                                      kw+=1
                                      if kw > 1:
                                          kq=kq*10+int(l)
                                          #kw+=1
                                          continue
                                      kq = int(l)
                              try:
                                 if x[row1-1][ass.get(temp[0][0])] == '#CYCLE':
                                     if j+1 == len(x[i]):
                                        print('#CYCLE', end='')
                                        continue
                                     else:
                                       print('#CYCLE', end=';')
                                       continue
                                 add = int(x[row1-1][ass.get(temp[0][0])]) // kq
                                 if j+1 == len(x[i]):
                                    print('%d' %add, end='')
                                 else:
                                    print('%d;' %add, end='')
                              
                              except IndexError:
                                 if j+1 == len(x[i]):
                                    print('#ERROR', end='')
                                 else:
                                   print('#ERROR', end=';') 
                              except ZeroDivisionError:
                                  if j+1 == len(x[i]):
                                     print('#DIV0', end='')
                                  else:
                                    print('#DIV0', end=';')
                else:
                    if x[i][j].find(p) != -1:
                       z = x[i][j].find(p)
                    elif x[i][j].find(sub) != -1:
                        z = x[i][j].find(sub)
                    elif x[i][j].find(mul) != -1:
                        z = x[i][j].find(mul)
                    elif x[i][j].find(div) != -1:
                        z = x[i][j].find(div)
                    kw=0
                    kq=0
                    #print(kq)
                    for l in x[i][j]:  
                      if int(l) == kq:
                          break
                      if kw < z:   
                        if int(l):
                            kw+=1
                            if kw > 1:
                                kq=kq*10+int(l)
                                #kw+=1
                                continue
                            kq = int(l)
                      else: break  
                    #print(kq)
                      #except ValueError:
                    if x[i][j].find(p) != -1:
                             #x[i] = x[i].replace(p,'')
                             #x[i] = x[i].replace(')','')
                             #print(x)
                             temp = x[i][j].split(p)
                             #print(temp)
                             add = 0 
                             
                             try:
                                 if int(temp[1][2]):
                                     row2 = int(temp[1][1])*10 + int(temp[1][2])
                             except IndexError:
                                 row2 = int(temp[1][1])
                             try:
                                if x[row2-1][ass.get(temp[1][0])] == '#CYCLE':
                                    if j+1 == len(x[i]):
                                       print('#CYCLE', end='')
                                       continue
                                    else:
                                      print('#CYCLE', end=';')
                                      continue
                                add = kq + int(x[row2-1][ass.get(temp[1][0])])
                                if j+1 == len(x[i]):
                                   print('%d' %add, end='')
                                else:
                                   print('%d;' %add, end='')
                             except TypeError: 
                                 if j+1 == len(x[i]):
                                    print('#CYCLE', end='')
                                 else:
                                   print('#CYCLE', end=';')
                             except IndexError:
                                if j+1 == len(x[i]):
                                   print('#ERROR', end='')
                                else:
                                  print('#ERROR', end=';')   
                    elif x[i][j].find(sub) != -1:
                             #x[i] = x[i].replace(p,'')
                             #x[i] = x[i].replace(')','')
                             #print(x)
                             temp = x[i][j].split(sub)
                             #print(temp)
                             add = 0 
                             
                             try:
                                 
                                 if int(temp[1][2]):
                                     row2 = int(temp[1][1])*10 + int(temp[1][2])
                             except IndexError:
                                 row2 = int(temp[1][1])
                             try:
                                if x[row2-1][ass.get(temp[1][0])] == '#CYCLE':
                                    if j+1 == len(x[i]):
                                       print('#CYCLE', end='')
                                       continue
                                    else:
                                      print('#CYCLE', end=';')
                                      continue
                                add = kq - int(x[row2-1][ass.get(temp[1][0])])
                                if j+1 == len(x[i]):
                                   print('%d' %add, end='')
                                else:
                                   print('%d;' %add, end='')
                             except TypeError: 
                                 if j+1 == len(x[i]):
                                    print('#CYCLE', end='')
                                 else:
                                   print('#CYCLE', end=';')
                             except IndexError:
                                if j+1 == len(x[i]):
                                   print('#ERROR', end='')
                                else:
                                  print('#ERROR', end=';')    
                    elif x[i][j].find(mul) != -1:
                             #x[i] = x[i].replace(p,'')
                             #x[i] = x[i].replace(')','')
                             #print(x)
                             temp = x[i][j].split(mul)
                             #print(temp)
                             add = 0 
                             
                             try:
                                 if int(temp[1][2]):
                                     row2 = int(temp[1][1])*10 + int(temp[1][2])
                             except IndexError:
                                 row2 = int(temp[1][1])
                             try:
                                if x[row2-1][ass.get(temp[1][0])] == '#CYCLE':
                                    if j+1 == len(x[i]):
                                       print('#CYCLE', end='')
                                       continue
                                    else:
                                      print('#CYCLE', end=';')
                                      continue
                                add = kq * int(x[row2-1][ass.get(temp[1][0])])
                                if j+1 == len(x[i]):
                                   print('%d' %add, end='')
                                else:
                                   print('%d;' %add, end='')
                             except TypeError: 
                                 if j+1 == len(x[i]):
                                    print('#CYCLE', end='')
                                 else:
                                   print('#CYCLE', end=';')
                             except IndexError:
                                if j+1 == len(x[i]):
                                   print('#ERROR', end='')
                                else:
                                  print('#ERROR', end=';')        
                    elif x[i][j].find(div) != -1:
                             #x[i] = x[i].replace(p,'')
                             #x[i] = x[i].replace(')','')
                             #print(x)
                             temp = x[i][j].split(div)
                             #print(temp)
                             add = 0 
                             
                             try:
                                 if int(temp[1][2]):
                                     row2 = int(temp[1][1])*10 + int(temp[1][2])
                             except IndexError:
                                 row2 = int(temp[1][1])
                             try:
                                if x[row2-1][ass.get(temp[1][0])] == '#CYCLE':
                                    if j+1 == len(x[i]):
                                       print('#CYCLE', end='')
                                       continue
                                    else:
                                      print('#CYCLE', end=';')
                                      continue
                                add = kq // int(x[row2-1][ass.get(temp[1][0])])
                                if j+1 == len(x[i]):
                                   print('%d' %add, end='')
                                else:
                                   print('%d;' %add, end='')
                             except TypeError: 
                                 if j+1 == len(x[i]):
                                    print('#CYCLE', end='')
                                 else:
                                   print('#CYCLE', end=';')
                             except IndexError:
                                if j+1 == len(x[i]):
                                   print('#ERROR', end='')
                                else:
                                  print('#ERROR', end=';')  
                             except ZeroDivisionError:
                                 if j+1 == len(x[i]):
                                    print('#DIV0', end='')
                                 else:
                                   print('#DIV0', end=';')
            else:
                if x[i][j].find(p) != -1:
                         #x[i] = x[i].replace(p,'')
                         #x[i] = x[i].replace(')','')
                         #print(x)
                         temp = x[i][j].split(p)
                         #print(temp)
                         add = 0 
                         try:
                             if int(temp[0][2]):
                                 row1 = int(temp[0][1])*10 + int(temp[0][2])
                         except IndexError:
                             row1 = int(temp[0][1])
                         try:
                             if int(temp[1][2]):
                                 row2 = int(temp[1][1])*10 + int(temp[1][2])
                         except IndexError:
                             row2 = int(temp[1][1])
                         try:
                            add = int(x[row1-1][ass.get(temp[0][0])]) + int(x[row2-1][ass.get(temp[1][0])])
                            if j+1 == len(x[i]):
                               print('%d' %add, end='')
                            else:
                               print('%d;' %add, end='')
                         except TypeError: 
                             if j+1 == len(x[i]):
                                print('#CYCLE', end='')
                             else:
                               print('#CYCLE', end=';')
                         except IndexError:
                            if j+1 == len(x[i]):
                               print('#ERROR', end='')
                            else:
                              print('#ERROR', end=';')   
                elif x[i][j].find(sub) != -1:
                         #x[i] = x[i].replace(p,'')
                         #x[i] = x[i].replace(')','')
                         #print(x)
                         temp = x[i][j].split(sub)
                         #print(temp)
                         add = 0 
                         try:
                             if int(temp[0][2]):
                                 row1 = int(temp[0][1])*10 + int(temp[0][2])
                         except IndexError:
                             row1 = int(temp[0][1])
                         try:
                             if int(temp[1][2]):
                                 row2 = int(temp[1][1])*10 + int(temp[1][2])
                         except IndexError:
                             row2 = int(temp[1][1])
                         try:
                            add = int(x[row1-1][ass.get(temp[0][0])]) - int(x[row2-1][ass.get(temp[1][0])])
                            if j+1 == len(x[i]):
                               print('%d' %add, end='')
                            else:
                               print('%d;' %add, end='')
                         except TypeError: 
                             if j+1 == len(x[i]):
                                print('#CYCLE', end='')
                             else:
                               print('#CYCLE', end=';')
                         except IndexError:
                            if j+1 == len(x[i]):
                               print('#ERROR', end='')
                            else:
                              print('#ERROR', end=';')    
                elif x[i][j].find(mul) != -1:
                         #print(mul)
                         #x[i] = x[i].replace(p,'')
                         #x[i] = x[i].replace(')','')
                         #print(x)
                         temp = x[i][j].split(mul)
                         #print(temp)
                         add = 0 
                         try:
                             if int(temp[0][2]):
                                 row1 = int(temp[0][1])*10 + int(temp[0][2])
                         except IndexError:
                             row1 = int(temp[0][1])
                         try:
                             if int(temp[1][2]):
                                 row2 = int(temp[1][1])*10 + int(temp[1][2])
                         except IndexError:
                             row2 = int(temp[1][1])
                         try:
                            add = int(x[row1-1][ass.get(temp[0][0])]) * int(x[row2-1][ass.get(temp[1][0])])
                            if j+1 == len(x[i]):
                               print('%d' %add, end='')
                            else:
                               print('%d;' %add, end='')
                         except TypeError: 
                             if j+1 == len(x[i]):
                                print('#CYCLE', end='')
                             else:
                               print('#CYCLE', end=';')
                         except IndexError:
                            if j+1 == len(x[i]):
                               print('#ERROR', end='')
                            else:
                              print('#ERROR', end=';')   
                elif x[i][j].find(div) != -1:
                         #print(mul)
                         #x[i] = x[i].replace(p,'')
                         #x[i] = x[i].replace(')','')
                         #print(x)
                         temp = x[i][j].split(div)
                         #print(temp)
                         add = 0 
                         try:
                             if int(temp[0][2]):
                                 row1 = int(temp[0][1])*10 + int(temp[0][2])
                         except IndexError:
                             row1 = int(temp[0][1])
                         try:
                             if int(temp[1][2]):
                                 row2 = int(temp[1][1])*10 + int(temp[1][2])
                         except IndexError:
                             row2 = int(temp[1][1])
                         try:
                            add = int(x[row1-1][ass.get(temp[0][0])]) // int(x[row2-1][ass.get(temp[1][0])])
                            if j+1 == len(x[i]):
                               print('%d' %add, end='')
                            else:
                               print('%d;' %add, end='')
                         except TypeError: 
                             if j+1 == len(x[i]):
                                print('#CYCLE', end='')
                             else:
                               print('#CYCLE', end=';')
                         except IndexError:
                            if j+1 == len(x[i]):
                               print('#ERROR', end='')
                            else:
                              print('#ERROR', end=';')
                         except ZeroDivisionError:
                             if j+1 == len(x[i]):
                                print('#DIV0', end='')
                             else:
                               print('#DIV0', end=';')
          elif int(x[i][j]):
            if j+1 == len(x[i]):
                print('%s' %x[i][j], end='')
            else:
                print('%s;' %x[i][j], end='')
      except IndexError:
                if j+1 == len(x[i]):
                   print('#ERROR', end='')
                else:
                  print('#ERROR', end=';')
      except ValueError:
          if x[i][j] == '':
              if j+1 == len(x[i]):
                  print('', end='')
              else:
                print('', end=';')
          else:
               if j+1 == len(x[i]):
                  print('#ERROR', end='')
               else:
                 print('#ERROR', end=';')
      except ZeroDivisionError:
          if j+1 == len(x[i]):
             print('#DIV0', end='')
          else:
            print('#DIV0', end=';')
    print()
