import random
import sys
import time

import matplotlib.pyplot as plt
import os
import psutil

sys.setrecursionlimit(9999)

def memory_usage():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    # print("Memory utilized:", mem)
    return mem

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


# Iterative mergesort function to sort arr[0...n-1]
def mergeSortIterative(a):
    current_size = 1

    # Outer loop for traversing Each sub array of current_size
    while current_size < len(a) - 1:

        left = 0
        # Inner loop for merge call in a sub array
        # Each complete Iteration sorts the iterating sub array
        while left < len(a) - 1:
            # mid index = left index of sub array + current sub array size - 1
            mid = min((left + current_size - 1), (len(a) - 1))

            # (False result,True result)
            # [Condition] Can use current_size
            # if 2 * current_size < len(a)-1
            # else len(a)-1
            right = ((2 * current_size + left - 1,
                      len(a) - 1)[2 * current_size
                                  + left - 1 > len(a) - 1])

            # Merge call for each sub array
            merge(a, left, mid, right)
            left = left + current_size * 2

        # Increasing sub array size by multiple of 2
        current_size = 2 * current_size


# Function to do Quick sort
def quickSort(x, l, r):
    i = l
    j = r
    p = x[l + (r - l) // 2]  # pivot element in the middle
    while i <= j:
        while x[i] < p:
            i += 1
        while x[j] > p:
            j -= 1
        if i <= j:  # swap
            x[i], x[j] = x[j], x[i]
            i += 1
            j -= 1
    if l < j:  # sort left list
        quickSort(x, l, j)
    if i < r:  # sort right list
        quickSort(x, i, r)
    return x


# Function takes last element as pivot,
# places the pivot element at its correct position in sorted array,
# and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot
# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    i = (l - 1)
    x = arr[h]

    for j in range(l, h):
        if arr[j] <= x:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l --> Starting index,
# h --> Ending index
def quickSortIterative(arr, l, h):
    # Create an auxiliary stack
    size = h - l + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and l
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        # Set pivot element at its correct position in sorted array
        p = partition(arr, l, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h


def printList(arr, n):
    for i in range(len(arr)):
        print("For ", n[i], " values it takes ", arr[i], " seconds.")
        # memory_usage()
    print()

def printLis(arr, n):
    for i in range(len(arr)):
        print("For ", n[i], " values it takes ", arr[i], " MB.")
        # memory_usage()
    print()

# Driver code

Mr = []
Qr = []
Mi = []
Qi = []
n = []
mmr = []
mqr = []
mmi = []
mqi = []
s = int(input("No. of inputs you want to test : "))
for i in range(0, s):
    n.append(int(input("Enter a limit:")))

for i in range(0, len(n)):
    randomlist = random.sample(range(n[i]), n[i])
    #recursive merge sort
    start = time.time()
    mergeSort(randomlist, 0, n[i] - 1)
    end = time.time()
    Mr.append(end - start)
    mmr.append(memory_usage())

    # starting time
    start = time.time()
    # program body starts
    quickSort(randomlist, 0, n[i] - 1)
    # program body ends
    # end time
    end = time.time()
    Qr.append(end - start)
    mqr.append(memory_usage())
    #Iterative merge sort
    start = time.time()
    mergeSortIterative(randomlist)
    end = time.time()
    Mi.append(end - start)
    mmi.append(memory_usage())
    #Iteretive
    start = time.time()
    quickSortIterative(randomlist, 0, n[i] - 1)
    end = time.time()
    Qi.append(end - start)
    mqi.append(memory_usage())

print("Merge sort Recursive: ")
printList(Mr, n)
printLis(mmr, n)
print("Quick sort Recursive: ")
printList(Qr, n)
printLis(mqr, n)
print("Merge sort Iterative: ")
printList(Mi, n)
printLis(mmi, n)
print("Quick sort Iterative: ")
printList(Qi, n)
printLis(mqi, n)

plt.plot(n, Mr, marker="+", label="Recursive Merge")
plt.plot(n, Qr, marker="^", label="Recursive Quick")
plt.plot(n, Mi, marker="*", label="Iterative Merge")
plt.plot(n, Qi, marker="+", label="Iterative Quick")
# plt.xticks(n)
plt.title("Iterative and Recursive methods")
plt.xlabel("Number of inputs")
plt.ylabel("Time taken (in seconds)")
plt.legend()
# plt.show()

plt.plot(n, mmr, marker="+", label="Recursive Merge")
plt.plot(n, mqr, marker="^", label="Recursive Quick")
plt.plot(n, mmi, marker="*", label="Iterative Merge")
plt.plot(n, mqi, marker="", label="Iterative Quick")
plt.xticks(n)
plt.title("Iterative and Recursive methods")
plt.xlabel("Number of inputs")
plt.ylabel("Memory usage (in MB)")
plt.legend()
plt.show()
