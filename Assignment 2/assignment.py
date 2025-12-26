# Wap that prompts user to enter a number and divides it by 2 and handle the zero division error.   
try:
    num = float(input("Enter a number: "))
    result = num / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a numeric value.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Division performed successfully.")
finally:
    print("Program execution completed.")


#Wap that asks for the user's age. Check if the input is an integer and raise a value error if not. Print different messages based on the age categories(e.g.child,adult,senior)
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age has to be an integer.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 59:
        print("You are an adult.")
    else:
        print("You are a senior.")
except ValueError as ve:
    print("ValueError:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Age category determined successfully.")
finally:
    print("Program execution completed.")


#Wap that performs a calculation involving multiple variables. Use as single expect block to catch any potential type error or value errror raised during the calculation. Handle each type differently, providing informative messages.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = input("Enter an operator (+, -, *, /): ")

    if c == '+':
        result = a + b
    elif c == '-':
        result = a - b
    elif c == '*':
        result = a * b
    elif c == '/':
        result = a / b
    else:
        raise ValueError("Invalid operator. Please use one of +, -, *, /.")

    print("Result:", result)
except TypeError as e:
    print("TypeError:", e)
except ValueError as e:
    print("ValueError:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Calculation performed successfully.")
finally:
    print("Program execution completed.")