

def elmtcheck(arr, e):
    n = 0
    for i in range(len(arr)):
        if arr[i] == e:
            print("Element exist in the list")
            break
    else:
        print("Element doesnt exist in the list")


element = input("Element to be checked in the list: ")
arr1 = [1, 3, 55, '23', 'asd', 'swqe']
elmtcheck(arr1, element)
