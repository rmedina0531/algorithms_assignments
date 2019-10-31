from decimal import Decimal
import random
import sys
import datetime

neg_inf = Decimal('-Infinity')


def brute_force_maximum_subarray(A):
    largest_sum = neg_inf
    for i in range(0,len(A)):
        for j in range(i,len(A)):
            sub_array = A[i:j+1]
            #print(sub_array)
            if (sum(sub_array) > largest_sum):
                largest_sum = sum(sub_array)
                largest_array = sub_array
                low = i
                high = j
                #print(sub_array)


    return (low, high, sum(largest_array))


def find_maximum_crossing_subarray(A, low, mid, high):
    left_sum = neg_inf
    summ = 0
    max_left = 0
    max_right = 0

    for i in range(mid, low-1, -1):
        summ = summ + A[i]
        if summ > left_sum:
            left_sum = summ
            max_left = i

    right_sum = neg_inf
    summ = 0
    for j in range(mid+1, high+1):
        summ = summ + A[j]
        if summ > right_sum:
            right_sum = summ
            max_right = j
            
    return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A, low, high):
    if high == low:
        return (low, high, A[low])
    else :
        mid = (low + high)/2
        #(left_low, lef_high, left_sum) 
        temp = find_maximum_subarray(A, low, mid)
        left_low = temp[0]
        left_high = temp[1]
        left_sum = temp[2]

        #(right_low, right_high, right_sum) 
        temp = find_maximum_subarray(A, mid + 1, high)
        right_low = temp[0]
        right_high = temp[1]
        right_sum = temp[2]

        #(cross_low, cross_high, cross_sum) 
        temp = find_maximum_crossing_subarray(A, low, mid, high)
        cross_low = temp[0]
        cross_high = temp[1]
        cross_sum = temp[2]

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)

        else:
            return (cross_low, cross_high, cross_sum)


def randomArray():
    output = []
    for i in range(0,10):
        output.append(random.randint(-10,10))
    return output

def brute_force(array):
    answer = brute_force_maximum_subarray(array)
    print("Maximum Array Using brute force")
    answer_array = array[answer[0]:answer[1]+1]
    print(answer_array)
    print("Sum of Array = " + str(answer[2]))
    print("")


def recursion(array):
    answer = find_maximum_subarray(array, 0, len(array)-1)
    print("Maximum Array Using Recursion")
    answer_array = array[answer[0]:answer[1]+1]
    print(answer_array)
    print("Sum of Array = " + str(answer[2]))
    print("")


def timeElapsed(start):
    delta = datetime.datetime.now() - start
    print(delta)
    return int(delta.total_seconds() * 1000)

def main(maximum):
    for i in range(0,maximum):
        array = randomArray()
        print("===========================================================")
        print("Input Array")
        print(array)
        print("")
        
        #time = datetime.datetime.now()
        recursion(array)
        #print("Time elapsed in milliseconds: " + str(timeElapsed(time)))

        #time = datetime.datetime.now()
        brute_force(array)
        #print("Time elapsed in milliseconds: " + str(timeElapsed(time)))


main(int(sys.argv[1]))
