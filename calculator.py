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
     print("❌Invalid value ,Enter numbers only")
     continue
     
     
     
  choices = "1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n" 
  print("choices you have :",choices)

  choice = input("enter choice/1/2/3/4 :")
  print("you entered choice :",choice)

 

  if choice == "1":
    result = addition(n1,n2)
    operation = "+"
  elif choice == "2":
    result = subtract(n1,n2 )
    operation = "-"
  elif choice == "3":
    result = multiply(n1,n2)
    operation = "*"
  elif choice == "4":
    result = division(n1,n2)
    operation = "/"
  else :
    print("Invalid choice,Try again")
    continue
  print("result:",result)


# saving history of calculation files in to a file
  with open("calculator.txt","a") as file:
     file.write(f"{n1} {operation} {n2}'='{result} \n")

  exit_choose = input("Do you want to continue (y/n) ").lower()

  if exit_choose = "n":

    print("History is saved in calculator.txt file 📄")
    break
 
 
