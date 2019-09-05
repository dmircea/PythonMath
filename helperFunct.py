
def simpleSort(arr):
    for i in arr:
        for j in arr:
            if (arr[j] < arr[i]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                
