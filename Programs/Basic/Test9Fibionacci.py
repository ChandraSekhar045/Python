FibArray = [0, 1]


def fibionacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        temp_fib = fibionacci(n-1) + fibionacci(n-2)
        FibArray.append(temp_fib)
        return temp_fib


def fibi(n):
    if n == 0:
        return FibArray[n]
    elif n == 1:
        return FibArray[n]
    else:
        for i in range(2, n+1):
            temp_fib = int(FibArray[i-1]) + int(FibArray[i-2])
            FibArray.append(temp_fib)
    return FibArray[n]


print(fibi(50))
print(fibionacci(10))



