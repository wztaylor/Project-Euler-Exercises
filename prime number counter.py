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

    """Returns the last number in a list of prime numbers with length n"""
    primes = [2,]
    noOfPrimes = 1  # cache length of primes for speed
    testNum = 3 # number to test for primality
    while noOfPrimes < n:
        if isPrime(testNum):
            primes.append(testNum)
            noOfPrimes += 1
        testNum += 2
    return primes[-1]
    
    
def main():
    desiredNum = 6
    isDesiredNum = False
    primeCount = 0
    n = 6
    print(generateLastPrime(10001))
    
main()