
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*":multiply,
  "/": divide
}

num1= int(input("What's the first number?: "))

for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation_symbol from the line above: ")

num2 = int(input("What's the second number?: "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

continuing = True 

while continuing:
  
  be_continue = input("You can be continue, selection another operation with the result. Type 'yes' or 'not'.")
  continuing = (be_continue == "yes")
  if continuing:
    
    for symbol in operations:
      print(symbol)

    operation_symbol = input("Pick an operation_symbol from the line above: ")
    
    another_num = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    another_answer = calculation_function(answer, another_num)
    
    
    
    print(f"{answer} {operation_symbol} {another_num} = {another_answer}")

    answer = another_answer