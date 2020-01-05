#   This file contains the helper functions for the original script.
#   Please see the top of 'math1Script.py' for more information.

def simpleSort(arr):
    if(len(arr) < 1):
        return
    if(checkSorted(arr)):
        return

    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[j] > arr[i]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

def simpleSortDec(arr): #   TODO
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[j] < arr[i]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp

def checkSorted(arr):
    print('Checking if sorted...')
    for i in range(1,len(arr)):
        if(arr[i-1] > arr[i]):
            print('Not sorted. Sorting...')
            return False;

    print('Already sorted!')
    return True;

def mergeSort(arr):
    pass
