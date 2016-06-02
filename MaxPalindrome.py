# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:55:29 2015

@author: Zac
"""


def isPalindrome(n):      #tests to see if n is a palindrome   
  
  if str(n) == str(n)[::-1]:    #simple elegant solution found on stack overflow. 
      return True              #Converts n to string representation then checks to make sure it is equal to itself in reverse
  else:
      return False
  


def maxPalindrome():     # a and b are the numbers being multiplied while n is the lower bound. 
                          #I'm assuming that the largest value of list will be a multiple of the palindrome, may need to change later
    palindromeList = []         #having issues getting all of the palindromes to show up in list

    for i in range(100,999):
        for j in range(100,999):
                product = i * j
                palindromeMax = 0
                if isPalindrome(product) == True:
                    if product > palindromeMax:
                        palindromeMax = product
                        palindromeList.append(palindromeMax)

    print("")    
    print(palindromeList)
    print("")  
    print(max(palindromeList))
    #return max(palindromeList)

    
def main():
  #  print(isPalindrome(990099))
    maxPalindrome()
main()