import random
import sys
def randomArray():
    output = []    
    for i in range(0,10):
        output.append(random.randint(0,10))
    return output

def join(left, right):
    i = 0
    j = 0
    #to make it similar to infinite
    left.append(99999)
    right.append(99999)
    output = []
    while (i < len(left)-1 or j < len(right)-1):
        if (left[i] < right[j]):
            output.append(left[i])
            i = i+1
        else:
            output.append(right[j])
            j = j+1
    return output

def mergeRecursive(array):
    if(len(array) == 1):
        return array
    else:
        midway = len(array)/2
        return join(mergeRecursive(array[:midway]) ,mergeRecursive(array[midway:]))
    return output

def sort():
    
    numbers = randomArray()
    print("")
    print(numbers)
    print(mergeRecursive(numbers))

def main():
    if(len(sys.argv) != 2):
        print("Invalid Number of Arguments")
        print("mergesort.py [TestCases]")
    else:
        maximum = int(sys.argv[1])
        for i in range(0,maximum):
            sort()

main()
