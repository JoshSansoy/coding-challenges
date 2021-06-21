import math

class Solution:

    def run(number):

        primeNumbers = 0;
        isSemiprime = False;

        for i in range(2, int(math.sqrt(number)) + 1):
            while number % i == 0:
                number /= i
                primeNumbers += 1
                print(number)
            if primeNumbers >= 2:
                break
        if (number > 1):
            primeNumbers += 1
        
        if primeNumbers == 2:
            print('Here')
            isSemiprime = True
        
        print(isSemiprime)

    run(14)