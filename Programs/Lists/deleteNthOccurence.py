

def nthelement(lst, n):
    for i in range(0, len(lst)):
        count = 0
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                count = count + 1
            if count == n:
                del(lst[j])
                j = j - 1
    return lst


def difference(arr1, n):
    arr2 = nthelement(arr1, n)
    if arr1 == arr2:
        print("Array is not modified")
    else:
        print("Array is modified")
    return arr2


occurrence = int(input("Nth occurrence not allowed: "))
arr = ['abc', 'def', 'ghi', 'abc', 'def', 'ghi', 'abc']
print(difference(arr, occurrence))
