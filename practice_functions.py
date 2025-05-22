### How to Create a Function in Python

def say_hello():   # Define the function
    print("Hello there!")  # What it does

say_hello()    # Call (run) the function    

### Function With an Input (Parameter)

def greet(name): # name is the input
    print("Hi " + name + "!")

greet("Emmanuel")
greet("Oiza")    

### Function With Output (Return Value)

def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The answer is:", result)

### Practice 1: Create a Function That Says "Good Morning"

def say_good_morning():
    print("Good Morning, sunshine")

say_good_morning()    

### Practice 2: Function That Greets by Name

def welcome(name):
    print("Welcome to Python class, " + name + "!")

welcome("Emmanuel") 
welcome("Oiza")   

### Practice 3: Function That Adds 2 Numbers and Returns the Result

def add(a, b):
    return a + b

print("Sum is:", add(10, 5))

### Practice 4: Function That Tells if a Number is Even or Odd

def is_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
    
print(is_even(4))
print(is_even(9))    