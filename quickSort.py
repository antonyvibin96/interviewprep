def quickSort(arr, low, high):
    if(low < high):
        p = partion(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)


def partion(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if(arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


arr = [5, 7, 2, 1, 7, 9, 4]
quickSort(arr, 0, 6)
print(arr)
