

def largestarray(array, m):
    largest = 0
    for i in range(m):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = [1, 14, 30, 45, 10, 78, 33, 2]
n = len(arr)

print(largestarray(arr, n))
