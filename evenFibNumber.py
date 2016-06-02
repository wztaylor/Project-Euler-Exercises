# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 00:54:36 2015

@author: Zac
"""

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def efficientFib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
    
def fibList(n):      #creates list of Fibonacci #'s less than n
    fibList = []     
    for i in range(2,100):
        if efficientFib(i) < n:
            fibList.append(efficientFib(i))
    return fibList

def isEvenFibSum(n):   #checks to see if the fibonacci number is even, if it is it adds it to the sum
    sum = 0
    for i in n:
        if i % 2 == 0:
            sum += i
    return sum

    
def main():
#    print(fibList())
#    print("")     
    print(isEvenFibSum(fibList(4000000)))
   # print(evenFibNumber(4000000))     
        
main()