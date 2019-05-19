#!/usr/bin/env python
# coding: utf-8

# ## Check if a word exists is an grid? Like the find words we used to solve as kids. For this question, you can go left or right, up or down. To keep it simple, no diagonals
# 
# Example :
# 
#     acdef
#     ghije
#     mopqu
#     swtuv
# 
# return `true` for word `how` and `vue` but `false` for `mope`
# 
# Function Signature
# 
# `def doesWordExist(grid: Array[Array[Char]], word: String): Boolean`


# Python program to convert a list 
# of charcater 

import numpy as np
import sys, getopt

def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 



def doesWordExists(grid, word):
    npgrid = np.array(grid)
    wlen = len(word)

    if (wlen > npgrid.shape[0] and wlen > npgrid.shape[1]):
        return False
    elif (wlen == 0):
        return False
    else:
        for i in range(npgrid.shape[0]):
            for j in range(npgrid.shape[1]):
              rstr = convert(npgrid[i][j:wlen+j])
              if(word == rstr or word == rstr[::-1]):
                return True
            
        npgrid = npgrid.transpose()
        
        for i in range(npgrid.shape[0]):
            #print("i",i)
            for j in range(npgrid.shape[1]):
              #print("j",j)
              #print(convert(npgrid[i][j:wlen+j]))
              rstr = convert(npgrid[i][j:wlen+j])
              if(word == rstr or word == rstr[::-1]):
                return True
            
    return False
        
 

if __name__ == "__main__":
   
   grid  = [['a','c','d','e','f'],
         ['g','h','i','j','e'],
         ['m','o','p','q','u'],
         ['s','w','t','u','v']]

   #sys.argv[1] = "how"
   #sys.argv[1] = "vue"
   #sys.argv[1] = "mope"
   result = doesWordExists(grid,sys.argv[1])
   print(result)
   






