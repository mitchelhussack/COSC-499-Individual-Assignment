def bubbleSort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print("Bubble Sorted Array:")
    arr2 = []
    for i in range(len(arr)):
        arr2.append(arr[i])
    return arr2

#Hi my name is Mitch