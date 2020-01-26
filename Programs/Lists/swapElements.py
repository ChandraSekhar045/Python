arr = [1, 20, 12, 310, 15, 1, 46, 89, 687, 84]


def swap(arr1, a, b):
    x = arr1[a]
    arr1[a] = arr1[b]
    arr1[b] = x
    return arr1


c = int(input("Swap Elements : "))
d = int(input("Swap Elements : "))
print(swap(arr, c-1, d-1))
