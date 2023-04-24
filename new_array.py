import random

def algorithm(first, second):

    array = []
    
    one = 0
    two = 0
    
    while (one < len(first)) and (two < len(second)):
        if first[one] < second[two]:
            one += 1
        elif second[two] < first[one]:
            two += 1
        else:
            array.append(first[one])
            one += 1
            two += 1

    return array

"""
My algorithm is written to where a new array is made using two given arrays, and the code is set to where the arrays 
have counters to see if they have matching numbers. I am counting eight operations in the code and it uses a while loop,
making it run on an linear (O(n)) runtime. The operations are as follows, the while with the two conditions (3 operations),
the if statement (2 operations), the elif statement (2 operations), and the else(1 operations). 
The results of the sample execution were
 [1, 3, 5, 7, 9]
 [10, 12, 14, 16]
 []
"""

def main():
    print("In this file we will be testing a function that takes two arrays of sorted positive integers as input, and returns an array containing only the numbers found in both arrays.")
    print("We will have three sample test pairs with KNOWN results")
    print("And one sample pair that will be a large set of random numbers")

    # Test pair 1
    # Expected result: [1,3,5,7,9]
    array_one = [1,2,3,4,5,6,7,8,9,10]
    array_two = [1,3,5,7,9,11,13,15,17,19]
    print(algorithm(array_one,array_two))

    # Test pair 2
    # Expected result: [10,12,14,16]
    array_three = [2,4,6,8,10,12,14,16,18,20]
    array_four = [1,3,5,7,9,10,12,14,15,16,17]
    print(algorithm(array_three, array_four))

    # Test pair 3
    # Expected result: []
    array_five = [1,3,5,7,9,11]
    array_six = [2,4,6,8,10,12]
    print(algorithm(array_five, array_six))

    array_seven = []
    array_eight = []

    for i in range(1000):
        num_one = random.randint(0,3000)
        num_two = random.randint(0,3000)
        if num_one not in array_seven:
            array_seven.append(num_one)
        if num_two not in array_eight:
            array_eight.append(num_two)

    array_seven.sort()
    array_eight.sort()

    print("Random array #1 contains %d items" % len(array_seven))
    print(array_seven)
    print("\n\nRandom array #2 contains %d items" % len(array_eight))
    print(array_eight)

    print("Please provide the calls for your method below")
    print("Test with each pair and print the resulting array to the screen")


main()
