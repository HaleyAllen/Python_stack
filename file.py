
# - variable declaration
# - Data Types
# - Numbers
num1 = 42
num2 = 2.3

# - Boolean
boolean = True

# - Strings
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')

# - log statement
# - initialize
print(type(fruit))
# - access value
print(pizza_toppings[1])
# - Add Value
pizza_toppings.append('Mushrooms')
print(person['name'])
# - change value
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# - conditional
#  - if
if num1 > 45:
    print("It's greater")

# - else
else:
    print("It's lower")

#  - if
if len(string) < 5:
    print("It's a short word!")

# - else if
elif len(string) > 15:
    print("It's a long word!")

# - else
else:
    print("Just right!")

# - for loop
# - start
for x in range(5):
    print(x)
# - stop
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0

# - while loop
# - start
while(x < 5):
    print(x)
    # - increment
    x += 1
# - stop


# - delete value
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

# - for loop
for topping in pizza_toppings:
    #  - if
    if topping == 'Pepperoni':
        # - continue
        continue
    print('After 1st if statement')
    #  - if
    if topping == 'Olives':
        # - break
        break

# - function
#                       - parameter
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        # - return
        print('Hello')

print_hello_x_or_ten_times()
#                         - argument
print_hello_x_or_ten_times(4)


# - comment

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)