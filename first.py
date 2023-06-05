from math import *


name = input("Enter your name weary traveller: ")
occupation= input("And occupation: ")
print("Hello "+name+"! I hear it's tough being a "+occupation+" these days")

# maybe expand these inputs/prints to make a short little madlibs game.

# make my summary a string assigned to a variable then make a few simple functions
# that will make the text all uppercase, all lowercase, and/or a different font/color 



#use bang operator/python equivalent and make a little lightmode/darkmode button

def say_hi(name):
    print("Hello "+name)

say_hi("mike")

def cube(num):
    return num*num*num

result= cube(4)

print(result)
is_tall = False 
is_male = False
if is_male and is_tall:
    print ("you're a lanky dude, bro")
elif is_male and not(is_tall):
    print("you are a short king bro")
elif not(is_male) and is_tall:
    print ("you're a tall gal")
else:
    print("you aint a dude, fella and you're short ratio")

# the "or" and the "and" keyword can be used in if statements (pretty self explanatory)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2>= num3:
        return num2
    else:
        return num3
    
print(max_num(400,4,40))

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")