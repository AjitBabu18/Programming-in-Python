# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:55:48 2022

@author: ajitb
"""

import sys
#sys.stdin = open('INPUT','r')

"""
class Align(object):
    def Justify(self, words, width):
        def space(i, count, width, last):
            if i < count:
                return 1 if last else (width // count) + int(i < width % count)
            return 0

        def join(words, width, begin, end, length, last):
            s = []
            n = end - begin
            #print(end)
            for i in range(n):
                s += words[begin + i],
                s += ' ' * space(i, n - 1, width - length, last),
            line = "".join(s)
            if len(line) < width:
                line += ' ' * (width - len(line))
            return line

        result = []
        start, length = 0, 0
        for i in range(len(words)):
            if length + len(words[i]) + (i - start) > width:
                result += join(words, width, start, i, length, False),
                #print(result)
                start, length = i, 0
            length += len(words[i])
            #print(length)

        result += join(words, width, start, len(words), length, True),
        return result
"""
class Align:
    def Justify(self, words, L):
        result = []
        
        i = 0
        while i < len(words):
            # count words in one line
            size, begin = 0, i
            while i < len(words):
                if size == 0:
                    newsize = len(words[i])
                else:
                    newsize = size + len(words[i]) + 1
                if newsize <= L:
                    size = newsize
                else:
                    break
                i += 1
                
            spaceCount = L - size
            if i - begin - 1 > 0 and i < len(words):
                everyCount = spaceCount // (i - begin - 1) + 1
                spaceCount %= i - begin - 1
            else:
                everyCount = 1

            j = begin
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' ' * everyCount
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                    s += words[j]
                j += 1
            s += ' ' * spaceCount
            result.append(s)
            
        return result



def assign(s, k):
    #print(type(l), l)
    f=0
    
    for line in s:
        line = line.strip()
        #if s[0] is None:
          #  break
        if line:
           x = line.split()
           #print(x)
           #print(len(x[0]))
           #try:
           if f == 1 and len(x[0]) < k:
              #print(x)
              print("")
           
            
           s = Align().Justify(x, k)
           #s = justify(x, k)
           #print(len(s))
           #print(s)
           for i in s:
               #print(i)
               print("".join(i.strip()))
           f=1
           
        """else: 
           x = line.split()
           #print(x)
           #try: 
           if f == 0 and x is None:
                #print('1',line)
                #f+=1
                continue
            
           #except UnboundLocalError: print("")
           if f == 1:
               f=0
               print("")
               """

if __name__ == "__main__":
    #string = "Error "
    try:
      #print(length)
      if int(sys.argv[1]) and sys.argv[1] or int(sys.argv[1]) == 0:
          k = int(sys.argv[1])
          #print(type(k), k)
          if k < 1:
              sys.exit("Error")
          else:
              #print(sys.stdin)
              
              #print(len(l))
              assign(sys.stdin, k)
    except ValueError: 
        sys.exit("Error")
    except IndexError: 
        sys.exit("Error")
    
    
    sys.stdin.close()