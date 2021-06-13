"""
merge sort implentation start and end index is inclusive

"""


def mergeSort(arr, start, end):
    if(start < end):
        middle = int((end+start)/2)
        mergeSort(arr, start, middle)
        mergeSort(arr, middle+1, end)
        merge(arr, start, middle, end)


def merge(arr, start, middle, end):
    arr1 = arr[start:middle+1]
    arr2 = arr[middle+1:end+1]
    i = 0
    j = 0
    k = start
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    if(i < len(arr1)):
        while(i < len(arr1)):
            arr[k] = arr1[i]
            i += 1
            k += 1
    else:
        while(j < len(arr2)):
            arr[k] = arr2[j]
            j += 1
            k += 1


arr = [5, 7, 2, 1, 7, 9, 4]
mergeSort(arr, 0, 6)
print(arr)
