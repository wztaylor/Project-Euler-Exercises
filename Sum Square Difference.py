# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:54:25 2016

@author: Zac

Problem 6:
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum. 
"""




def sumOfSquares(n):
    sumSquare = 0
    for i in range (n + 1):
        iSquare = i * i
        sumSquare += iSquare
        i += 1
    return sumSquare
    
def squareOfSum(n):
    sum = 0
    for i in range(n + 1):
        sum += i 
        i += 1
    squareSum = sum * sum
    return squareSum
    
def sumSquareDiff(n):
    diff = squareOfSum(n) - sumOfSquares(n)
    return diff


def main():
    n = 100
    print(sumOfSquares(n))
    print(squareOfSum(n))
    print(sumSquareDiff(n))
main()