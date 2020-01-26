n = int(input("Sequence Number:"))


def fibionacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = fibionacci(n-1) + fibionacci(n-2)
        return x


for i in range(1, n):
    print(fibionacci(i))
