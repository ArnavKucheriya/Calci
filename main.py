# Function to add two numbers
def add(x, y):
  return x + y


# Function to subtract two numbers
def subtract(x, y):
  return x - y


# Function to multiply two numbers
def multiply(x, y):
  return x * y


# Function to divide two numbers
def divide(x, y):
  return x / y


def square(x):
  return x * x


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")

# Take input fromthe user

choice = input("Enter choice(1/2/3/4/5): ")

if choice == '5':
  num = float(input("Enter a number: "))
  print("Square of", num, "is", square(num))
else:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

if choice == '1':
  print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
  print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
  print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
  print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
  print(num, "=", square(num))
else:
  print("Invalid input")