import sys
import random

def exponentRecursive(number, exponent):
    if (exponent == 0):
        return 1
    if (exponent%2 != 0):
        return number * exponentRecursive(number, (exponent-1)/2) * exponentRecursive(number, (exponent-1)/2)
    else:
        return exponentRecursive(number, (exponent)/2) * exponentRecursive(number, (exponent)/2) 

    
def tester():
    for i in range(0,30):
        number = random.randint(0,10)
        exponent = random.randint(0,5)
        expected = number**exponent
        answer = exponentRecursive(number, exponent)
        if (expected != answer):
            print("Maths error")
        print(str(number) + "^" + str(exponent) + "=" + str(answer))

def main():
    number = 3
    exponent = 4
    print(exponentRecursive(number, exponent))

tester()
