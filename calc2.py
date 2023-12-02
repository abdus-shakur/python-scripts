print("Enter the operation for calculator : ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice : "))
num1 = float(input("Enter first Numbers : "))
num2 = float(input("ENter second number : "))
if(choice==1):
        ans =  num1 + num2
elif(choice==2):
        ans = num1 - num2
elif(choice==3):
        ans =  num1 * num2
elif(choice==4):
        ans = num1 / num2

print("Answer "+str(ans))

