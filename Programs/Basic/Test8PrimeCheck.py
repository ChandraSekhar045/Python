number = int(input("NUmber check: "))
if number>1:
    for i in range(2, number):
        if number % i == 0:
            print("Number is not a prime")
            break
    else:
        print("Number is prime")
else:
    print("Number is not a prime")
