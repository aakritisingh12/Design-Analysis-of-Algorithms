import random
import time
import sys
import matplotlib.pyplot as plt


# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Function to do selection sort
def selectionSort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Function to do bubble sort
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


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


# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#         # If current element is smaller than or equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1
#
#
# # The main function that implements QuickSort
# # arr[] --> Array to be sorted,
# # low  --> Starting index,
# # high  --> Ending index
#
# # Function to do Quick sort
# def quickSort(arr, low, high):
#     if len(arr) == 1:
#         return arr
#     if low < high:
#         # pi is partitioning index, arr[p] is now
#         # at right place
#         pi = partition(arr, low, high)
#         # Separately sort elements before
#         # partition and after partition
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)


def qsort(x, l, r):
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
        qsort(x, l, j)
    if i < r:  # sort right list
        qsort(x, i, r)
    return x


def printList(arr, n):
    for i in range(len(arr)):
        print("For ", n[i], " values it takes ", arr[i], " seconds.")
    print()


I = []
S = []
B = []
M = []
Q = []
n = [10, 100, 1000, 10000, 100000]#,1000000]
sys.getrecursionlimit()
sys.setrecursionlimit(9999)
for i in range(0, len(n)):
    randomlist = random.sample(range(n[i]), n[i])
    start = time.time()
    insertionSort(randomlist)
    end = time.time()
    I.append(end - start)
    start = time.time()
    selectionSort(randomlist)
    end = time.time()
    S.append(end - start)
    start = time.time()
    bubbleSort(randomlist)
    end = time.time()
    B.append(end - start)
    start = time.time()
    mergeSort(randomlist, 0, n[i] - 1)
    end = time.time()
    M.append(end - start)
    # starting time
    start = time.time()
    # program body starts
    qsort(randomlist, 0, n[i] - 1)
    # program body ends
    # end time
    end = time.time()
    Q.append(end - start)

print("Insertion sort: ")
printList(I, n)
print("Selection sort: ")
printList(S, n)
print("Bubble sort: ")
printList(B, n)
print("Merge sort: ")
printList(M, n)
print("Quick sort: ")
printList(Q, n)

plt.plot(n, I, label="Insertion")
plt.plot(n, S, label="Selection")
plt.plot(n, B, label="Bubble")
plt.plot(n, M, label="Merge")
plt.plot(n, Q, label="Quick")
plt.title("Sorting Algorithms")
plt.xlabel("Array size")
plt.ylabel("Run Time")
plt.legend()
plt.show()

plt.plot(I, n, label="Insertion")
plt.plot(S, n, label="Selection")
plt.plot(B, n, label="Bubble")
plt.plot(M, n, label="Merge")
plt.plot(Q, n, label="Quick")
plt.title("Sorting Algorithms")
plt.xlabel("Run Time")
plt.ylabel("Array Size")
plt.legend()
plt.show()
