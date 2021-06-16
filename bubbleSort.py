def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr = [5, 7, 2, 1, 7, 9, 4]
bubbleSort(arr)
print(arr)
