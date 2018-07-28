def QuickSort(arr, start, end):
    if(start>=end):
        return 0
    pIndex = Partition(arr, start, end)
    QuickSort(arr, start, pIndex-1)
    QuickSort(arr, pIndex+1, end)

def Partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if(arr[i]<=pivot):
            arr[pIndex], arr[i]=arr[i], arr[pIndex]
            pIndex += 1
    arr[pIndex], arr[end]=arr[end], arr[pIndex]

    return pIndex

arr = [7,2,1,6,8,5,3,4]
QuickSort(arr,0,len(arr)-1)
print(arr)