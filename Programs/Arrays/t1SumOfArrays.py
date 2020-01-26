

def sumarray(array, m):
    sum = 0
    for i in range(m):
        sum = arr[i] + sum
    return sum


arr = [1, 14, 30, 45]
n = len(arr)

print(sumarray(arr, n))
