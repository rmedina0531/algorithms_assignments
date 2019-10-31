from math import log
import random
from datetime import datetime
import time
import sys


def check_hires(array):
    count = 0
    best = 99 #make sure this will fail
    for e in array:
        if best > e:
            best = e
            count += 1
            
    return count

def part1(candidates):
    total = 0.0
    for i in range(1,len(candidates)+1):
        total = total + (1.0/i)
    return total

def random_array(elements):
    inarr = []
    for e in elements:
        inarr.append(e)
    if len(inarr) == 1:
        return inarr
    output = []
    element = random.choice(inarr)
    output.append(element)
    inarr.remove(element)
    output.extend(random_array(inarr))
    return output
    
def part2(candidates):
    count = 0.0
    tests = 10000
    for i in range(0,tests):
        count = count + check_hires(random_array(candidates))
        #print(check_hires(random_array(candidates)))
        #print(random_array(candidates))
    return (count/tests)

def all_arrays(array):
    output = []
    #base case
    if len(array) == 1:
        output.append(array)
        return output
    #recursion
    for e in array:
        #copy the array
        tail = []
        for f in array:
            tail.append(f)
        
        #split the array
        head = e
        tail.remove(e)
        tail_list = all_arrays(tail)
        
        for ele in tail_list:
            ele.insert(0, head)
            output.append(ele)
    return output

def part3(candidates):
    count = 0.0
    tests = 0.0
    arrays = all_arrays(candidates)
    for arr in arrays:
        tests += 1
        count += check_hires(arr)

    return (count/tests)

def part4(candidates):
    return log(len(candidates), 2.0)


def hires_tests(n):
    cand = n
    candidates = []
    
    for i in range(1,cand + 1):
        candidates.append(i)
        
    expected = []
    time_elapsed = []
    
    #part1
    start_time = time.time()
    expected.append(part1(candidates))
    time_elapsed.append(time.time() - start_time)
    
    #part2
    start_time = time.time()
    expected.append(part2(candidates))
    time_elapsed.append(time.time() - start_time)
    
    part3
    start_time = time.time()
    expected.append(part3(candidates))
    time_elapsed.append(time.time() - start_time)
    
    #part4
    start_time = time.time()
    expected.append(part4(candidates))
    time_elapsed.append(time.time() - start_time)
    
    print("========================================")
    print("Number of Candidates = " + str(cand))
    
    for i in range(0,len(expected)):
        print("----------Part " + str(i+1) + "----------")
        print("Expected Number of Hires: " + str(expected[i]))
        print("Running Time = " + str(time_elapsed[i]/1000))
    
    
    #part 1 must equal part 3
    

def main():
    if len (sys.argv) != 2:
        print("Error, please use syntax: lab8.py [n]")
    else:
        hires_tests(int(sys.argv[1]));
    #hires_tests(4)
    #hires_tests(8)
    #hires_tests(12)
    
main()
