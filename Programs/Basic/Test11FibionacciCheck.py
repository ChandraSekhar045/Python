n = int(input("Sequence Number:"))


def fibionacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        x = fibionacci(n-1) + fibionacci(n-2)
        return x


for i in range(1, n+2):
    if n == fibionacci(i):
        print("A fibionacci number")
        break
    elif fibionacci(i) > n:
        print("Not a Fibionacci number")
        break
