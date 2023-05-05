from math import *


name = input("Enter your name weary traveller: ")
occupation= input("And occupation: ")
print("Hello "+name+"! I hear it's tough being a "+occupation+" these days")

# maybe expand these inputs/prints to make a short little madlibs game.

# make my summary a string assigned to a variable then make a few simple functions
# that will make the text all uppercase, all lowercase, and/or a different font/color 

# Simple Calculator Function
num1= input("Enter a number:")
num2= input("Enter another number:")

result= float(num1) + float(num2)

print(result)

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
