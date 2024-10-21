
def second_largest(arr):
    # if the array has less than 2 elements, there can't be a second largest
    if len(arr) < 2:
        return -1

    largest, secondLargest = float('-inf'), float('-inf')

    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num

    return secondLargest if secondLargest != float('-inf') else -1


def secondSmallest(arr):
    smallest, second_smallest = float('inf'), float('inf')
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else -1


arr = [1, 2, 4, 7, 6, 5, 8]
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
second_Largest = second_largest(arr)
second_smallest = secondSmallest(arr)
print("The second largest is:", second_Largest, "\nSecond Minimum:", second_smallest)


