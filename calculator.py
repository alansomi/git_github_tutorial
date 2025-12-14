#  Simple Calculator program
''' This is a program contains arithmetic operations (basic level)'''
import platform 

n1 = int(input("Enter the first number    :"))
n2 = int(input("Enter the second number   :"))

def addition(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2 
def multiply(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2


choices = "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n" 
print("choices you have :",choices)

choice = input("enter choice/1/2/3/4 :")
print("you entered choice :",choice)

if choice == "1":
   result = addition(n1,n2)
   print("Addition    :", result)
elif choice == "2":
    result = subtract(n1,n2 )
    print("Subtraction   :",result)
elif choice == "3":
    result = multiply(n1,n2)
    print("Multiplication of inputs   :",result)
elif choice == "4":
    result = division(n1,n2)
    print("Division of inputs   :",result)
