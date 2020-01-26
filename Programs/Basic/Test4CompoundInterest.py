principal = int(input("Principal: "))
time = int(input("Time: "))
rate = float(input("Rate: "))

interest = principal * (pow((1 + rate / 100), time))
print("Interest is: ", interest)
