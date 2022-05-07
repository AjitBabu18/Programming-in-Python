# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:48:02 2022

@author: ajitb
"""

import json
import sys
from datetime import date, timedelta

#sys.stdin = open('INPUT','r')



with open('data2.json') as json_file:
    data = json.load(json_file)
    #print(type(data))


"""if data['Prague']['20210205']['temp']:
    print(data['Prague']['20210205']['temp'])"""





for line in sys.stdin:
       line = line.strip()
       try:
        if line:
           x = line.split()
           x = list(x)
           #print(x)
           #print(x)
           req = x[0]
           x.pop(0)
           x = [i.split(':')[1] for i in x]
               #print(x)
               
           
           try:
            if req == 'temp':
               if data[x[0]][x[1]][req]:
                   print('city:%s' %x[0],' date:%s' %x[1],' temp:%s' %data[x[0]][x[1]][req])
            elif req == 'humidity':
               if data[x[0]][x[1]]['relhum']:
                   print('city:%s' %x[0],' date:%s' %x[1], ' humidity:%s' %round((data[x[0]][x[1]]['relhum'])*100))
            elif req == "pressure":
                if data[x[0]][x[1]]['ap']:
                    print('city:%s' %x[0],' date:%s' %x[1],' pressure:%s' %data[x[0]][x[1]]['ap'])
            elif req == "maxtemp":
                if data[x[0]][x[1]]['temp'] and data[x[0]][x[2]]['temp']:
                    x1 = int(x[1])
                    x2 = int(x[2])
                    y1 = round(x1/10000)
                    y2 = round(x2/10000)
                    m1 = round((x1%10000)/100)
                    m2 = round((x2%10000)/100)
                    d1 = round(x1%100)
                    d2 = round(x2%100)
                    #print(d1, d2)

                    sdate = date(y1,m1,d1)  
                    edate = date(y2,m2,d2)  

                    delta = edate - sdate     
                    day=[]
                    for i in range(delta.days + 1):
                        day.append((sdate + timedelta(days=i)).strftime('%Y%m%d'))
                    res=[]
                    for i in day:
                        res.append(data[x[0]][i]['temp'])
                    
                    #lis = { your_key: data[x[0]][your_key] for your_key in range(data[x[0]][x[1]], data[x[0]][x[2]]) }
                    
                    maxtemp = max(res)
                    ind = res.index(maxtemp)
                    print('city:%s' %x[0],' date:%s' %day[ind],' temp:%s' %maxtemp)
            elif req == "coldestcity":
                try:
                    if x[1]:
                        print("Invalid input")
                
                except IndexError:
                    k=list(data.keys())
                    t=[]
                    for i in k:
                       if data[i][x[0]]['temp']:
                           t.append(data[i][x[0]]['temp'])
                    mintemp = min(t)
                    ind = t.index(mintemp)
                    print('city:%s' %k[ind],' date:%s' %x[0],' temp:%s' %mintemp)
                
            elif req == "warmestcity":
                try:
                    if x[1]:
                        print("Invalid input")
                        
                except IndexError:
                    k=list(data.keys())
                    t=[]
                    for i in k:
                       if data[i][x[0]]['temp']:
                           t.append(data[i][x[0]]['temp'])
                    maxtemp = max(t)
                    ind = t.index(maxtemp)
                    print('city:%s' %k[ind],' date:%s' %x[0],' temp:%s' %maxtemp)
                
            elif req == "maxhumidity":
                if data[x[0]][x[1]]['relhum'] and data[x[0]][x[2]]['relhum']:
                    x1 = int(x[1])
                    x2 = int(x[2])
                    y1 = round(x1/10000)
                    y2 = round(x2/10000)
                    m1 = round((x1%10000)/100)
                    m2 = round((x2%10000)/100)
                    d1 = round(x1%100)
                    d2 = round(x2%100)
                    #print(d1, d2)

                    sdate = date(y1,m1,d1)  
                    edate = date(y2,m2,d2)  

                    delta = edate - sdate     
                    day=[]
                    for i in range(delta.days + 1):
                        day.append((sdate + timedelta(days=i)).strftime('%Y%m%d'))
                    res=[]
                    for i in day:
                        res.append(round((data[x[0]][i]['relhum'])*100))
                    
                    #lis = { your_key: data[x[0]][your_key] for your_key in range(data[x[0]][x[1]], data[x[0]][x[2]]) }
                    
                    maxhum = max(res)
                    ind = res.index(maxhum)
                    print('city:%s' %x[0],' date:%s' %day[ind],' humidity:%s' %maxhum)
            elif req == "maxpressure":
                if data[x[0]][x[1]]['ap'] and data[x[0]][x[2]]['ap']:
                    x1 = int(x[1])
                    x2 = int(x[2])
                    y1 = round(x1/10000)
                    y2 = round(x2/10000)
                    m1 = round((x1%10000)/100)
                    m2 = round((x2%10000)/100)
                    d1 = round(x1%100)
                    d2 = round(x2%100)
                    #print(d1, d2)

                    sdate = date(y1,m1,d1)  
                    edate = date(y2,m2,d2)  

                    delta = edate - sdate     
                    day=[]
                    for i in range(delta.days + 1):
                        day.append((sdate + timedelta(days=i)).strftime('%Y%m%d'))
                    res=[]
                    for i in day:
                        res.append(data[x[0]][i]['ap'])
                    
                    #lis = { your_key: data[x[0]][your_key] for your_key in range(data[x[0]][x[1]], data[x[0]][x[2]]) }
                    
                    maxpre = max(res)
                    ind = res.index(maxpre)
                    print('city:%s' %x[0],' date:%s' %day[ind],' pressure:%s' %maxpre)
            elif req == "graphtemp":
                x1 = int(x[1])
                x2 = int(x[2])
                y1 = round(x1/10000)
                y2 = round(x2/10000)
                m1 = round((x1%10000)/100)
                m2 = round((x2%10000)/100)
                d1 = round(x1%100)
                d2 = round(x2%100)
                #print(d1, d2)

                sdate = date(y1,m1,d1)  
                edate = date(y2,m2,d2)  

                delta = edate - sdate     
                day=[]
                for i in range(delta.days + 1):
                    day.append((sdate + timedelta(days=i)).strftime('%Y%m%d'))
                res=[]
                for i in day:
                    res.append(data[x[0]][i]['temp'])
                mintemp = min(res)
                maxtemp = max(res)
                step = (maxtemp - mintemp)/19
                #print(len(res))
                n=[]
                if len(res) > 50:
                    #t = sum(res)
                    m = len(res)
                    m %= 50
                    #print(m)
                    if m != 0:
                        p = (len(res)//50)+1
                        p*=m
                        #print(p)
                       # print(m)
                        s=0
                        #for i in range(m):
                         #   s+=res[i]
                        #print(mintemp)
                        for i in range(0,p,p//m):
                            #print(n[1])
                            #t = (60//50)+1
                            #print(t,end=' ')
                            t=0
                            #print(i+1)
                            for a in range(p//m):
                                t += res[i+a]
                            t /= (p/m)
                            #print(i)
                            #print((t - mintemp)/ step)
                            n.append((int ((t - mintemp) / step))+1)
                            
                            #print(n)
                        q = len(res)//50
                        #print(q)
                        for i in range(p, len(res), q):
                            #t = 60//50
                            t=0
                            for a in range(q):
                                t += res[i+a]
                            t /= q
                            #print(i)
                            n.append((int ((t - mintemp) / step))+ 1)
                            #print(t)
                    else: 
                        p = len(res)//50
                        for i in range(0,len(res),p):
                            #print(n[1])
                            #t = (60//50)+1
                            #print(t,end=' ')
                            t=0
                            #print(i+1)
                            for a in range(p):
                                t += res[i+a]
                            t /= p
                            #print(i)
                            #print((t - mintemp)/ step)
                            n.append((int ((t - mintemp) / step))+1)
                        #print(p)
                        
                    
                
                else:
                  for t in res:
                    n.append(round ((t - mintemp) / step) + 1)
                #print(n)
                z=[]
                c=0
                for i in range(20):
                  for j in range(len(n)):
                      if n[j] == (20-i):
                         z.append('#')
                          #break
                  try:
                    if z[0] == None:
                      break
                  except IndexError: 
                        c+=1
                        #print(c)
                #c=0
                for i in range(c,20):
                  for j in range(len(n)): 
                    #print('x')
                    if n[j] == (20-i):
                        n[j]-=1
                        print('#',end='')
                        
                    else: print(' ',end='')
                          
                  print('',end='\n')
            elif req == "graphpressure":
                x1 = int(x[1])
                x2 = int(x[2])
                y1 = round(x1/10000)
                y2 = round(x2/10000)
                m1 = round((x1%10000)/100)
                m2 = round((x2%10000)/100)
                d1 = round(x1%100)
                d2 = round(x2%100)
                #print(d1, d2)

                sdate = date(y1,m1,d1)  
                edate = date(y2,m2,d2)  

                delta = edate - sdate     
                day=[]
                for i in range(delta.days + 1):
                    day.append((sdate + timedelta(days=i)).strftime('%Y%m%d'))
                res=[]
                for i in day:
                    res.append(data[x[0]][i]['ap'])
                minpre = min(res)
                maxpre = max(res)
                step = (maxpre - minpre)/19
                n=[]
                if len(res) > 50:
                    #t = sum(res)
                    m = len(res)
                    m %= 50
                    if m != 0:
                        p = (len(res)//50)+1
                        p*=m
                        #print(p)
                        #print(m)
                        s=0
                        #for i in range(m):
                         #   s+=res[i]
                        #print(mintemp)
                        for i in range(0,p,p//m):
                            #print(n[1])
                            #t = (60//50)+1
                            #print(t,end=' ')
                            t=0
                            #print(i+1)
                            for a in range(p//m):
                                t += res[i+a]
                            t /= (p/m)
                            #print(i)
                            #print((t - mintemp)/ step)
                            n.append(int ((t - minpre) / step)+1)
                            
                            #print(n)
                        q = len(res)//50
                        #print(q)
                        for i in range(p, len(res), q):
                            #t = 60//50
                            t=0
                            for a in range(q):
                                t += res[i+a]
                            t /= q
                            #print(i)
                            n.append((int ((t - minpre) / step)) + 1)
                    else: 
                        p = len(res)//50
                        for i in range(0,len(res),p):
                            #print(n[1])
                            #t = (60//50)+1
                            #print(t,end=' ')
                            t=0
                            #print(i+1)
                            for a in range(p):
                                t += res[i+a]
                            t /= p
                            #print(i)
                            #print((t - minpre)/ step)
                            n.append((int ((t - minpre) / step))+1)
                    
                else:
                  for t in res:
                    n.append((int ((t - minpre) / step)) + 1)
                    
                #print(n)
                c=0
                z=[]
                for i in range(20):
                  for j in range(len(n)):
                      if n[j] == (20-i):
                         z.append('#')
                          #break
                  try:
                    if z[0] == None:
                      break
                  except IndexError: 
                        c+=1
                for i in range(c,20):
                  for j in range(len(n)): 
                    #print('x')
                    if n[j] == (20-i):
                        n[j]-=1
                        print('#',end='')
                    else: print(' ',end='')
                  print('',end='\n')
            else: print("Invalid input")
           except KeyError:
               print("Invalid input")
           except ValueError:
               print("Invalid input")
    
               #print(x)
           #print(req)
           #x = x.split(":")
           #print(x)
       except ValueError: 
             print("Invalid input")
       except IndexError: 
             print("Invalid input")