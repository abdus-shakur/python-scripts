
def calculate(a,b,choice):
    if(choice==1):
        return a + b
    elif(choice==2):
        return a - b
    elif(choice==3):
        return a * b
    elif(choice==4):
        return a / b
    else:
        print("invalid Input")


print("Enter the operation for calculator : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter your choice : "))
num1 = float(input("Enter first Numbers : "))
num2 = float(input("ENter second number : "))
ans = calculate(num1,num2,choice)

print("Answer "+str(ans))

