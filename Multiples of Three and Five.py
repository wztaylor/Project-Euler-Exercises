# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:41:07 2015

@author: Zac
"""

def multThreeAndFive(n):
    sum = 0    
    for i in range(n):
        if i % 3 == 0:
            sum += i
            
        elif i % 5 == 0:
            sum += i
        #print(sum)
    return sum
        
        
        
def main():
    print(multThreeAndFive(1000))
main()