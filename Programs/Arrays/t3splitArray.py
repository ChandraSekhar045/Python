arr = [1, 20, 12, 310, 15, 1, 46, 89, 687, 84]


def splitarray(arr1, m, n):
    for i in range(0, m):
        x = arr[0]
        for j in range(0, n-1):
            arr[j] = arr[j+1]
        arr[n-1] = x
    return arr1


length = len(arr)
m = int(input("Split size: "))
print(splitarray(arr, m, length))
