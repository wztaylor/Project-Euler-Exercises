# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:27:17 2015
@author: Zac
Problem 5: 
2520 is the smallest number that can be divided by each 
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is 
evenly divisible by all of the numbers from 1 to 20?
"""
    
def smallestMult():
    isDivisible = False
    n = 100000000    
    while(isDivisible == False):         
        for i in range(2,20):
            if n % i == 0:
                isDivisible = True
            else:
                isDivisible = False
                break
        n += 1
    return n-1


    
def main():

    #print(factor(116396280))
    print(smallestMult())
main()