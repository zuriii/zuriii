def removeDuplicate(arr, n):
    j = 0

    for i in range(0, n - 1):
        if (arr[i] != arr[i + 1]):
            arr[j] = arr[i]
            j = j + 1

    arr[j] = arr[n - 1]
    j = j + 1

    for i in range(0, j):
        print("%d" % (arr[i]), end=" ")
    print(arr)

arr = [1,3, 3, 5, 5, 6, 8]
n = len(arr)
if (n > 1):
    removeDuplicate(arr, n)