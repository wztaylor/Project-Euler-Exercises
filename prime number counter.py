# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:07:52 2016

@author: Zac

Problem: 
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def isPrime(n):               #determines whether n is prime
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
def generateLastPrime(n):

    """Decided to do away with list to save on memory and processing speed"""
    #prime = 0
    noOfPrimes = 1  # cache length of primes for speed
    testNum = 3 # number to test for primality
    while noOfPrimes < n:
        if isPrime(testNum):
            prime = testNum
            noOfPrimes += 1
        testNum += 2 #used 2 here b/c any even number can't be prime
    return prime
    
    
def main():
    print(generateLastPrime(10001))
    
main()