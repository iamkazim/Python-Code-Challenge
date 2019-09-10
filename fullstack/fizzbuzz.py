#In progress, unverified.

#!/usr/bin/env python3
import sys

def fizzbuzz(n):
    #check if number is a multiple of 3 or 5
    if n % 15 == 0:   #if n is divisible by 15 (aka 3 and 5), return fizzbuzz
        return('fizzbuzz')
    elif n % 3 == 0:  #if n divided by 3 is zero, return fizz
        return('fizz')
    elif n % 5 == 0:    #if n is divisible by 5, return buzz
        return('buzz')
    else:
        return n    #if n is not divided by 3 or 5, then return the number


def main():
    large = int(sys.argv[1])    #large is the argument given in command line
    for number in range(1, large+1): #look at each number in range
        print(fizzbuzz(number))
        

if __name__ == '__main__':
    main()