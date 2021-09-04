from art import logo
#add
def add (n1,n2):
  return n1+n2

#substract
def substract(n1,n2):
  return n1-n2

#multiply 

def multiply (n1,n2):
  return n1 * n2


# Divide 
def divide(n1,n2):
  return n1/n2


# create a disctionary 
operator  = {
  "+" : add,
  "-": substract,
  "*": multiply,
  "/": divide
} 

def calculater ():
  print (logo)

  num1 = float (input ("What is the first number ?"))

  for o in operator : 
    print (o)

  should_continue = True
  while should_continue :

    operation_symbol = input ("Pick the operation from line above.")

    num2 = float (input ("What is the next number?"))


    calculation_function = operator[operation_symbol]

    answer = calculation_function(num1, num2)

    print (f"{num1}{operation_symbol}{num2} = {answer}")

    if (input(f"Type 'y' to continue calcualting with {answer}, or type'n' to start a new calculation.")) == 'y':
      num1 = answer
    else :
      should_continue = False
      calculater()

calculater()






