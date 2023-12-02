def calculate(a,b,method):
    if(method==1):
        return a + b
    elif(method==2):
        return a - b
    elif(method==3):
        return a * b
    elif(method==4):
        return a / b

print("Enter the operation for calculator : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("Enter your choice : ")
option = int(input())
print("Enter two Numbers : ")
a = int(input())
b = int(input())
ans = calculate(a,b,option)
print("Answer "+str(ans))

