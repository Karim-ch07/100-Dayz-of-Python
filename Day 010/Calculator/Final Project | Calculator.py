from art import logo
print(logo)

#Calculator

#Add
def add(n1, n2):
  return n1 + n2

#Substract
def substract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Devide
def devide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : devide,
}

nbr_1 = int(input("What is the first number?\t"))
nbr_2 = int(input("What is the second number?\t"))

for operation in operations:
  print(operation)

operation_symbol = input("Pick an operation from the line above:\t")

result_1 = operations[operation_symbol](nbr_1, nbr_2)

print(f"{nbr_1} {operation_symbol} {nbr_2} = {result_1}")

operation_symbol = input("Pick another operation:\t")
nbr_3 = int(input("What is the next number?\t"))

result_2 = operations[operation_symbol](result_1, nbr_3)

print(f"{result_1} {operation_symbol} {nbr_3} = {result_2}")
