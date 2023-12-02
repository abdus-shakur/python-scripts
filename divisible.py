number = int(input("Enter a three-digit number: "))
if number % 100 == 0:
    result = "Divisible by 100"
elif number % 50 == 0:
    result = "Divisible by 50"
elif number % 20 == 0:
    result = "Divisible by 20"
elif number % 10 == 0:
    result = "Divisible by 10"
else:
    result = "Try again"
print(result)