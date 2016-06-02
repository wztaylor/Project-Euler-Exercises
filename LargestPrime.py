# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 02:01:42 2015

@author: Zac
"""
import math


''' main issues were having too mnay elements in list to process. 
To reduce the length of this list I replaced range(2,n) with range(2, int(math.sqrt(n))+2)
To check if a number is prime we only need to check up to it's square root. This is because
if n is not prime it can be factored into "a" and "b". If both "a" and "b" are greater than sqrt(n)
then a*b would also be greater than n. Therefore at least one of those factors must be less than or
equal to the square root n
'''
def largestPrimeFactor(n):        #determines largest prime factor of n
    primeFactors = []
    x = factor(n)
    for i in x:
        if isPrime(i) == True:
            primeFactors.append(i)
    return max(primeFactors)
        
def isPrime(n):               #determines whether n is prime
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def factor(n):              #gives a list of all the factors of n
    factors = []
    for i in range(2,int(math.sqrt(n))+2):
        if n % i == 0:
            factors.append(i)
    return factors            
    
def largestFactor(n):        #factor(n) gave too many items to compute, need to reduce but still didn't compile    
    for i in range(2,int(math.sqrt(n))+2):
        if n % i == 0:
            largestFactor = i
            print(largestFactor)
    return largestFactor
    

def main():    
    #print(isPrime(13185))
    #print(largestFactor(13195))
    #print(factor(13195))    
    #print(largestPrimeFactor(13195))

    print(largestPrimeFactor(600851475143))
main()    