# variable declaration
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'

# Composite Data Type - List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# Composite Data Type - Dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# Composite Data Type - Tuple
fruit = ('blueberry', 'strawberry', 'banana')

# type check
print(type(fruit))

# access value - List
print(pizza_toppings[1])

# add value - List
pizza_toppings.append('Mushrooms')

# access value - Dictionary
print(person['name'])

# change value - Dictionary
person['name'] = 'George'

# add value - Dictionary
person['eye_color'] = 'blue'

# access value - Tuple
print(fruit[2])

# conditional - if / else
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# length check + conditional - if / elif / else
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop - start, stop
for x in range(5):
    print(x)

# for loop - start, stop
for x in range(2, 5):
    print(x)

# for loop - start, stop, increment
for x in range(2, 10, 3):
    print(x)

# while loop - start, stop, increment
x = 0
while(x < 5):
    print(x)
    x += 1

# delete value - List
pizza_toppings.pop()
pizza_toppings.pop(1)

# log statement
print(person)

# delete value - Dictionary
person.pop('eye_color')

# log statement
print(person)

# for loop with break and continue
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue  # continue
    print('After 1st if statement')
    if topping == 'Olives':
        break  # break

# function - parameterless
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

# function call
print_hello_ten_times()

# function - with parameter
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

# function call - with argument
print_hello_x_times(4)

# function - default parameter
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# function call - with default
print_hello_x_or_ten_times()

# function call - override default
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# Errors

# NameError: name 'num3' is not defined
# print(num3)
# num3 = 72

# TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'

# KeyError: 'favorite_team'
# print(person['favorite_team'])

# IndexError: list index out of range
# print(pizza_toppings[7])

# IndentationError: unexpected indent
#   print(boolean)

# AttributeError: 'tuple' object has no attribute 'append'
# fruit.append('raspberry')

# AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1)
