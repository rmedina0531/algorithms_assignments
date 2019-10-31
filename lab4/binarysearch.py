import random
import sys


def randomArray(length, maximum):
    output = []
    for i in range(0,length):
        output.append(random.randint(0,maximum))
    return output

def randomFind(maximum):
    return random.randint(0,maximum)

def recursiveSearch(items, val):
    if len(items) == 1:
        if(items[0] == val):
            return True
        else:
            return False
    else:
        midway = len(items)/2
        search = False;
        search = recursiveSearch(items[:midway], val)
        if (search == True):
            return True
        search = recursiveSearch(items[midway:], val)
        if (search == True):
            return True
        return False
        
def search(maximum, length):
    find = randomFind(maximum)
    numbers = randomArray(length, maximum)
    output  = "The number " + str(find) + " is "
    if (recursiveSearch(numbers, find) == True):
        output += ""
    else:
        output += "not "

    output += "in the array"
    print("numbers in the array")
    print(numbers)
    print("Using programmed Binary Search")
    print(output)
    

    print("Using built in python array search")
    if (find in numbers):
        print("The Number " + str(find) + " is in the Array")
    else:
        print("The Number " + str(find) + " is not in the Array")

    print("")


def main():
    if (len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("binarysearch.py [Maximum Number] [ArrayLength]")
    else:
        maximum = int(sys.argv[1])
        length = int(sys.argv[2])
        print sys.argv
        for i in range(0,20):
            search(maximum, length)

main()
