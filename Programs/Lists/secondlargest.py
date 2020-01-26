

def secondlargest(arr1):
    maximum = max(arr1[:])
    n = arr.index(maximum)
    p = len(arr1)
    seclarge = 0
    for i in range(0, p):
        if i != n:
            if arr1[i] > seclarge:
                seclarge = arr1[i]
    return seclarge


def scdlarge(arr1):
    maximum = max(arr1[:])
    arr1.remove(maximum)
    return max(arr1)


arr = [55, 24, 45, 88, 102, 156, 78, 2, 156, 102]
print(secondlargest(arr))
print(scdlarge(arr))
