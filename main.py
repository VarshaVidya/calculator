from art import logo
from replit import clear
def add(number1,number2):
  return  number1 + number2
def subtract(number1,number2):
  return  number1 - number2
def multiply(number1,number2):
  return  number1 * number2
def divide(number1,number2):
  return  number1 / number2


result=0
flag=True
operators={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo)
  # first number input
  first_number= float(input("What is the first number: "))
#operator dictionary
  for op in operators:
    print(op)
  flag_continue=True

#while loop

  while flag_continue==True:
    operator = input("Pick an operator: ")
    second_number= float(input("What is the next number: "))
    result = operators[operator](first_number,second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    if input("To continue with the calculation enter'y'. To start a new calculation enter'n': ").lower()=="y":
      first_number = result
    else:
    # flag_continue = False
      clear()
      calculator()
    
calculator()   

