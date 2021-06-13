"""
program is to demonstrate Insertion Sort Algoirthm

"""


def insertionSort(arr):
    n = len(arr)
    j = 0
    for i in range(n):
        j = i-1
        x = arr[i]
        while(j >= 0 and arr[j] > x):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = x
    return arr


print(insertionSort([5, 7, 2, 1, 7, 9, 4]))
