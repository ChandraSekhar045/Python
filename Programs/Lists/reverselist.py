

def reverselist(arr1):
    arr2 = []
    n = len(arr1)
    for i in range(0, n):
        arr2.append(arr1[n - (i+1)])
    return arr2


def reverse(arr1):
    n = len(arr1)
    if n % 2 == 0:
        for i in range(0, int(n/2 + 1)):
            a = arr1[i]
            arr1[i] = arr1[n - i - 1]
            arr1[n - i - 1] = a
        return arr1
    else:
        for i in range(0, int((n + 1)/2)):
            a = arr1[i]
            arr1[i] = arr1[n - i - 1]
            arr1[n - i - 1] = a
        return arr1


arr = [55, '23', 'asd', 'swqe', 45, 88]
arr3 = arr[:]
print(arr3)
print(reverselist(arr))
print(reverse(arr))
