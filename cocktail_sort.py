import random

def bubble_sort(my_array):
    num_ops = 4
    n = len(my_array)

    # Traverse through all array elements
    for i in range(n):
        num_ops += 5
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            num_ops += 6
            if my_array[j] > my_array[j+1] :
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                swapped = True
                num_ops += 7

        num_ops += 3
        if (not swapped):
            break
    return num_ops

def cocktail_sort(my_data):

    num_ops = 0
    length = len(my_data)

    for i in range(length // 2):
        swap = False
        for j in range(i, length - i - 1):

            if (my_data[j] > my_data[j + 1]):
                my_data[j], my_data[j + 1] = my_data[j + 1], my_data[j]
                swap = True
                num_ops += 1

        if (not swap):
            break

        swap2 = False
        for k in range(length - i - 2, i - 1, -1):

            if (my_data[k] > my_data[k + 1]):
                my_data[k], my_data[k + 1] = my_data[k + 1], my_data[k]
                swap2 = True
                num_ops += 1

        if (not swap2):
            break    

    return num_ops


def make_arrays(n):
    the_data = []
    for i in range(12):
        the_data.append([])
    # Full random array
    for i in range(n):
        the_data[0].append(random.randint(0,n*2))

    # 25% sorted
    for i in range(n//4):
        the_data[1].append(i)
    for i in range((3*n)//4):
        the_data[1].append(random.randint(0,n*2))
        the_data[2].append(random.randint(0,n*2))
    for i in range(n//4, 0, -1):
        the_data[2].append((n*2)-i)

    # 50% sorted
    for i in range(n):
        if i < n//2:
            the_data[3].append(i)
        else:
            the_data[3].append(random.randint(0, n*2))

    for i in range(n):
        if i < n//4 or i > (3*n)//4:
            the_data[4].append(random.randint(0,n*2))
        else:
            the_data[4].append(i)

    for i in range(n):
        if i > n//2:
            the_data[5].append(i*2)
        else:
            the_data[5].append(random.randint(0,n*2))


    # 75% sorted
    for i in range(n):
        if i < (3*n) // 4:
            the_data[6].append(i)
        else:
            the_data[6].append(random.randint(0,n*2))

    for i in range(n):
        if i > n//4:
            the_data[7].append(i)
        else:
            the_data[7].append(random.randint(0,n*2))

    # 90% sorted
    for i in range(n):
        if i < 0.9*n:
            the_data[8].append(i)
        else:
            the_data[8].append(random.randint(0,n*2))

    for i in range(n):
        if i > 0.1 * n:
            the_data[9].append(i)
        else:
            the_data[9].append(random.randint(0,n*2))

    the_data[11].append(random.randint(0,n*2))
    for i in range(n):
        the_data[10].append(i)
        the_data[11].append(i)
    the_data[10].append(random.randint(0,n*2))
    return the_data

def clone_array(my_data):
	result = []
	for subarray in my_data:
		tmp = []
		for item in subarray:
			tmp.append(item)
		result.append(tmp)
	return result


def main():
    bubble_data = make_arrays(100) # Change this size to test larger (or smaller) datasets
    shaker_data = clone_array(bubble_data)
    print("Our bubblesort arrays:")
    for item in bubble_data:
        print(item)
    print("\nOur arrays for cocktail shaker sort:")
    for item in shaker_data:
        print(item)
    for i in range(len(bubble_data)):
        bubble_count = bubble_sort(bubble_data[i])
        shaker_count = cocktail_sort(shaker_data[i])
        print("To sort array #%d, it took us %d operations! Proof of sortedness below:\n%s" % (i+1, bubble_count, bubble_data[i]))
        print("To sort array #%d, it took us %d operations! Proof of sortedness below:\n%s" % (i+1, shaker_count, shaker_data[i]))
        print("To sort array #%d, it took us %d operations with bubblesort! " % (i+1, bubble_count))
        print("To sort array #%d, it took us %d operations with cocktail shaker sort! " % (i+1, shaker_count))

main()
