import time
import random
import psutil
import os


def memory_usage():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    # print("Memory utilized:", mem)
    return mem


def heapsort(aList):
    # convert aList to heap
    length = len(aList) - 1
    leastParent = length // 2
    for i in range(leastParent, -1, -1):
        moveDown(aList, i, length)

    # flatten heap into sorted array
    for i in range(length, 0, -1):
        if aList[0] > aList[i]:
            swap(aList, 0, i)
            moveDown(aList, 0, i - 1)


def moveDown(aList, first, last):
    largest = 2 * first + 1
    while largest <= last:
        # right child exists and is larger than left child
        if (largest < last) and (aList[largest] < aList[largest + 1]):
            largest += 1

        # right child is larger than parent
        if aList[largest] > aList[first]:
            swap(aList, largest, first)
            # move down to largest child
            first = largest
            largest = 2 * first + 1
        else:
            return  # force exit


def swap(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# n = int(input("Enter n : "))
# randomlist = random.sample(range(1, 1000000), n)
# print(" Given array is", end="\n")
# printList(randomlist)
#
# print(" Sorted array is: ", end="\n")
# printList(randomlist)
# # total time taken
# print(" Runtime of the program is ", )

# Driver code to test above
n = []
runtime = []
memoryused = []
s = int(input("No. of times you want to test : "))
for i in range(0, s):
    n.append(int(input("Enter size of array :")))

    randomlist = random.sample(range(n[i]), n[i])
    # starting time
    start = time.time()
    # program body starts
    heapsort(randomlist)
    # program body ends
    # end time
    end = time.time()
    runtime.append(end - start)
    memoryused.append(memory_usage())

    print("Time taken = ", runtime[i], " seconds.")
    print("Memory occupied ", memoryused[i], " MB.")
