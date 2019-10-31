import random


random_array(elements):
    element = random.choice(elements)
    output.append(element)
    output.extend(random_array(elements.remove(element)))
    
part2(candidates):
    for i in range(0,10000):
        array = random_array([1,2,3,4])
        
