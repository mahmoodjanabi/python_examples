
test_number = int(input("Please input the number under test: "))

divisors = []

#Find which divisors are available for this number
for divisor in range(1,test_number):
    if (test_number % divisor) == 0:
        divisors.append(str(divisor))

divisors.append(str(test_number))
print(divisors)