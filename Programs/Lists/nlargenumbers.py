

def nlarge(arr1, n):
    arr2 = []
    for i in range(n):
        a = max(arr[:])
        arr2.append(a)
        arr1.remove(a)
    return arr2


arr = [55, 24, 45, 88, 102, 156, 78, 2]
n = int(input("No of Large numbers: "))
print(nlarge(arr, n))
