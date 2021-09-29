num1 = 42 # variable declaration 
num2 = 2.3 # variable declaration
boolean = True # Data Type / Primitive / Boolean Data Primitive
string = 'Hello World' # String # Data Type / Primitive / String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Data Type / Composite / List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Data Type / Composite / Dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Data Type / Composite / Tuples
print(type(fruit)) # Type check
print(pizza_toppings[1]) # Data Type / Composite / List / Access Value
pizza_toppings.append('Mushrooms') # Data Type / Composite / List / Add Value
print(person['name']) # Print list value
person['name'] = 'George' # Access value
person['eye_color'] = 'blue' #Access value
print(fruit[2]) # Print list value

if num1 > 45: # If statement
    print("It's greater")
else: # Else statement
    print("It's lower")

if len(string) < 5: # Length check
    print("It's a short word!") 
elif len(string) > 15: # ifelse statement + length check
    print("It's a long word!")
else: # else statement
    print("Just right!")

for x in range(5): # for loop with a stop
    print(x)
for x in range(2,5): #for loop with a start and stop
    print(x)
for x in range(2,10,3): #for loop with a start, stop and iteration
    print(x)
x = 0
while(x < 5): # while loop with a start at 0 stop
    print(x)
    x += 1 # while loop increment

pizza_toppings.pop() # List remove value
pizza_toppings.pop(1) # List remove value at element 1

print(person) # print statement
person.pop('eye_color') #removes value from person
print(person) #prints new person value

for topping in pizza_toppings: # For loop in variable range
    if topping == 'Pepperoni': # If topping = Pepperoni
        continue 
    print('After 1st if statement')
    if topping == 'Olives': # for loop end statment
        break # Break statement

def print_hello_ten_times(): #declares function
    for num in range(10): #declares parameter
        print('Hello')

print_hello_ten_times() # Function

def print_hello_x_times(x): #Declares Function
    for num in range(x): # For loop in range x
        print('Hello') #Prints "Hello" x times

print_hello_x_times(4) # Hello Hello Hello Hello 

def print_hello_x_or_ten_times(x = 10): 
    for num in range(x):
        print('Hello') # Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello 

print_hello_x_or_ten_times() # No Output
print_hello_x_or_ten_times(4) # Hello Hello Hello Hello 


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