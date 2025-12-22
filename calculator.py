#  Simple Calculator program
''' This is a program contains arithmetic operations (basic level)'''
import platform 


print("Simple calaculator")

def addition(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2 
def multiply(n1,n2):
    return n1 * n2
def division(n1,n2):
   
   if n2 == 0:
        return "cannot be divided by zero "
   return n1/n2

while True:
  try :
     
    n1 = float(input("Enter the first number:"))
    n2 =float(input("Enter the second number :"))
  except ValueError:
     print("Invalid value ,try again")
     continue
     
     
     
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
  else :
    print("Invalid choice,Try again")
 
  exit =input("Do you want to continue (y/n)".lower())

  if exit == "n":

    print("Thank for using calculator,see you soon 😊")
    break
 
 
