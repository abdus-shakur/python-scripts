num = int(input("Enter the number to calculate factorial for : "))

def fact(a):
    ans = 1
    for x in range(1,a+1):
        ans = ans * x
    return ans

ans = fact(num)
print(f"Factorial of {num} is {ans}")