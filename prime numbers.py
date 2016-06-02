# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:45:04 2016

@author: Zac
#"""

def primeFactorList(n):        #determines largest prime factor of n
    amtOfPrime = 1    
    primes = [2,]
    testNum = 3
    while amtOfPrime < n:
        if isPrime(testNum) == True:
            primes.append(testNum)
            amtOfPrime += 1
        testNum +=2
    return primes
  

def generatePrimes(n):

    """Returns a list of prime numbers with length n"""
    primes = [2,]
    noOfPrimes = 1  # cache length of primes for speed
    testNum = 3 # number to test for primality
    while noOfPrimes < n:
        if isPrime(testNum):
            primes.append(testNum)
            noOfPrimes += 1
        testNum += 2
    return primes



      
def isPrime(n):               #determines whether n is prime
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    

    
    
def main():
   # print(generatePrimes(20))
    print(primeFactorList(20))
main()