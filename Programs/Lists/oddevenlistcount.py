

def oddevencount(arr):
    evencount, oddcount = 0, 0
    for i in arr:
        if i % 2 == 0:
            evencount += 1
        else:
            oddcount += 1
    return evencount, oddcount


arr1 = [55, 24, 45, 88, 102, 156, 78, 2]
arr2 = oddevencount(arr1)
print("(Even count, Odd count): ", arr2)
