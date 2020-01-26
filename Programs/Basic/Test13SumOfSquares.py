n = int(input("Number till sum squares: "))
sum = 0
for i in range(1, n+1):
    sum += i*i

squaresSum = n * (n+1) * (2 * n + 1) / 6
cubeSum = (n * (n + 1) / 2) * (n * (n + 1) / 2)
print("Sum of squares of Natural Numbers: ", sum)
print(squaresSum)
print(cubeSum)
