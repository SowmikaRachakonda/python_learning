a = float(input("Enter the value of a: "))

b = float(input("Enter the value of b: "))

operation = input("Enter the operation: ")

if operation == "+":
    print(a+b)
  
elif operation == "-":
    print(a-b)
  
elif operation == "*":
    print(a*b)
  
elif operation == "/":
  
    if b==0:
        print("Error: Cannot divide by zero!")
    else: 
        print(a/b)
      
elif operation == "//":

    if b == 0:
        print("Error: Cannot divide by zero!")
    else:
        print(a//b)
  
elif operation == "%":

    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print(a%b)
  
else:
    print("Invalid Operation")
