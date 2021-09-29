
# Python Notes

#VsCode Commands
Ctrl + ? # Quotes out all selected lines. Repeat to undo.
Alt + Z # Codewrap for long lines
Alt + Shift + Down-Arrow # Copies a line to the line below
Highlight + Ctrl + D # Continues to select instances of highlighted word in order 


#Discord Comments
```py # formats code posted in discord for Python


# import libraries
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)




#Data Types

# Boolean - T and F must be capitol
is_hungry = True
has_freckles = False

# Numbers
age = 35 # storing a unit (no decimal)
weight = 160.7 # Storing a float (decimal)

# Strings
name = "Joe Blue"


# Composite Types

# Tuples - An IMMUTABLE data type.
dog = ("Bruce", "cocker spaniel", 19, False)
print(dog[0]) # Outputs Bruce
dog[1] = "daschund"  # ERROR: cannot be modified. Item assignment not supported.

# Lists - A mutable group that can hold a group of values:
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) #Output is Oliver
ninjas[0] = 'Francis' 
ninjas.append('Micheal')
print(ninjas) #Ouput is ['Francis', 'KB', 'Oliver, 'Michael']
ninjas.pop()
print(ninjas) #Ouput is ['Francis', 'KB', 'Oliver]
ninjas.pop(1)
print(ninjas) #Ouput is ['Francis', 'Oliver]

#Dictionaries - A group of key value pairs
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}

new_person = ['name'] = 'Jack' # Updates if the key exists, adds a key-value pair if it doesn't

new_person['hobbies'] = ['climbing', 'coding']
print(new_person) #Output {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False, hobbies ['climbing', 'coding']}
w = new_person.pop('weight') #This removes the key and returns the value to the variable.
print(w) #Output 160.2
print(new_person) #Output {'name': 'John', 'age': 38, 'has_glasses': False, 'hobbies':['climbing', 'coding']}


# Common Functions

# Type Function
print(type(2.63)) #Outputs <'class 'float'>
print(type(new_person)) #Outputs <'class 'dict'>

# Len (Length) Function
print(len(new_person)) #output : 4 (the number of key-value pairs)
print(len('Coding Dojo')) #output: 11

# Javascript to Python number types
num = 25  # int (integer)
dec = 4.2 # float
print(num) # Console.log command  
print(type(dec)) #checks type of the variable
num_to_dec = float(num) # Converts floats to nums (Does it do it back?)

# Conversions
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# Random Number
from _typeshed import HasFileno
from os import X_OK
import random
from typing import Sequence
print(random.randint(2,5)) # provides a random number between 2 and 5
# Site for random module here: https://docs.python.org/3/library/random.html




# Strings - Strings are any sequence of characters enclosed in single or double quotes

name = "Zen"
print("My name is", name) #Output "My name is Zen"
# The print() function will add a space between elements seperated by a comma
print("My name is " + name) #Output "My name is Zen"
#This function is concatinating these into a new string

# Explicit Type Conversion
print("Hello" + 42) #Output: Type Error - Cannot concatinate a string and int
print("Hello" + str(42)) #Output: Hello 42
# example
total = 35
user_val = "26"
total = total + user_val # Output: Type Error
total = total + int(user_val) #Output: total will be 61


# String Interpolation

# f-strings (Literal String Interpolation)
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# string.format method
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# Output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# Output: My name is 27 Zen and I am Coder years old.

# %-formatting
hw = "Hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py) #Output: Hello world I love Python 3

name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age)) #Output: My name is Zen and I'm 27

#Built in String Methods
x = "hello world"
print(x.title()) #Output: "Hello World"

string.upper() #Returns a copy of the string with all characters in uppercase
string.lower() #Returns a copy of the string with all characters in lowercase
string.count(substring) #Returns number of occurences of substring in string
string.split(char) #Returns a list of values where string is split at the given character. With no parameter, the default split is every space.
string.find(substring) #Returns the index of the start of the first occurence of the substring within a string
string.isalnum() #Returns boolean depending on whether the string's length is >0 and all characters are alphanumeric (letters and numbers only). Strings that include spaces and punctuation will return Flase for this mehtod. Similar methds include 
.isalpha() .isdigit(), islower(), .isupper() # All return boolean
string.join(list) #Returns a string that is all strings within our set (in this case a list) concatenated
string.endswith(substring) #Returns a boolean based upon whether the last characters of string match substring




# Lists (Arrays in Javascript)

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

fruits = ['apple', 'banana',  'orange']
vegetables = ['lettuce', 'cucumber']
fruits_and_vegetables = ['apple', 'banana',  'orange', 'lettuce', 'cucumber']
print(fruits_and_vegetables) #Output: ['apple', 'banana',  'orange', 'lettuce', 'cucumber']
salad = vegetables * 3
print(salad) #Output: ['lettuce', 'cucumber', 'lettuce', 'cucumber', 'lettuce', 'cucumber']


# Accessing Values
drawer = ['documents', 'envelopes', 'pens']
print(drawer[0]) #output: 'documents'
print(drawer[1]) #output: 'envelopes'


# Manipulating Lists
x = [1,2,3,4,5]
x.append(99)
print(x) #Output: [1,2,3,4,5,99]  

# Python returns lists in [] specified by indices
x = [99,,4,2,5,-3]
print(x[:]]) #Output: [99,4,2,5,-3] 
print(x[1:]) #Output: [4,2,-5,-3]
print(x[4:]) #output: [99,4,2,5]
print(x{2:4]) #output: [2,5]


# len(sequence) (length) - Returns the number of items in a sequence
my_list = [1, 'Zen', 'hi']
print(len(my_list)) #Output: 3

# Built in functions for sequences
enumerate(sequence) # Used in a for-loop context to return two-item-turple for each item in the list indicating the index followed by the value at that index
print(enumerate(my_list)) # Output: ('0:1', '1:Zen', '2:hi')

map(function, sequence) # Applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) # Returns the lowest value in the sequence
sorted(sequence) # Returns a sort sequence

#list.append(value)
my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list) #Output: [1,2,5,8,4]

# Commonly used list methods
list.extend(list2) # Adds all values from a second sequence to the end of the original
list.pop(index) # remove a value at given position. If no parameter is passed, defaults to final value in the list.
list.index(value) #returns the index position in a list for the given parameter




# Tuples (Immutable lists. Created by using parenthesis. Tuple stands for dou'ble', tri'ple', quadr'uple, etc. )

tuple_data = ('physics', 'chemistry', 1997, 2000)

# Tuples are useful for data structures that should not be changed.




# Dictionaries - A type of set that uses a key and a pair. Declared by: variable = {key: value} Each key must be unique

weekend = {"Sun": "Sunday", "Sat": "Saturday"}
capitals = {} #Creates an empty dictionary
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
print(capitals) #Output: {"svk": "Bratislava", "deu": "Berlin", "dnk": "Copenhagen"}

# Accessing values
print(weekend["Sun"]) #Output: "Sunday"
print(capitals["svk"]) #Output: "Bratislava"

# Removing values
value_removed = capitals.pop('svk') #Assigns key-pair "svk" to value_removed, and removes from end of capitals
del capitals['dnk'] #Deletes the key, and returns nothing

#Nested Dictionaries
context = {
    'questions': [
        {'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer'},
        {'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'}
    ]
}

#dict - Functions
cmp(dict1, dict2) # Compares two dictionaries
len() #give the total length of the dictionary
str() #produces a string representation fo a dictionary
type() #returns the type of the passed variable. If passed variable is a dictionary, it will rturn a dict type.


#dict - Dictionary Methods 

# Called by
dict.method(yourDictionary)
yourDictionary.method()

.clear() #removes all elements from the dictionary
.copy() #returns a shallow copy dictionary
.fromkeys(sequenence, [value]) #create a new dictionary with keys from sequence and values set to a value
# Output {'sequence[0]': value, 'sequence[1]': value, 'sequence[2]': value}
.get(key, default=None) # For key (key), returns value or default if key is not in dictionary
.has_key(key) - #Returns true if key is present in dictionary, otherwise it returns false
.items() #Returns a list of the dictionary's (key, value) tuple pairs
.keys() #Return a list of dictionary keys
.setdefault(key, default=None) #Similar to get(), but will set dict[key]=default if key is not already in dictionary. Adds to the dictionary.
.update(dict2) #Adds dictionary dict2 key-values pairs to an existing dictionary
.values() # returns list of dictionary values




# Conditionals - Run code if conditions are met. Conditionals are if(), elif(), and else().

x = 12
if x> 50:
    print("bigger than 50")
else: 
    print("smaller than 50")

x = 55
if x > 10:
    print("bigger than 10") #Output: Only this will execute since it evaluates true first.
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")

if x < 10:
    print("bigger than 10") #Output: This will not execute because it is false.

# operaters
== #Checks if two operands are equal
!+ #Checks if two operands are not equal
> #Checks if left operand is greater
< #Checks if left operand is smaller
>= #Checks if left operand is equal or greater
<= #Checks if left operand is equal or smaller

and #Checks if left and right are both True
or #Checks if either left and right are True
not #Reveres the True-False value of the operand




# Loops - range()

# Range with one argument
range(5) -- stop  #Output: 0,1,2,3,4  Exclusive Stop is 5
# Range with two arguments
range(5,10) -- start, stop  #Output: 5,6,7,8,9  Exclusive Stop is 10
# Range with three arguments
range(5,10,2) -- start, stop, step  #Outputs: 5,7,9  Exclusive Stop is 5

for x in range(0,10,2):
    print(x) # output 0,2,4,6,8
for x in range(5,-1,3):
    print(x) #outputs 5,2

# loops in strings accesses each value in the string
for x in 'Hello':
    print(x) #outputs: 'H' 'e' 'l' 'l' 'o'

# loops in lists
my_list = {"abc", 123, 2 xyz}
for i in range(0, len(mylist)):
    print(i, my_list[i]) #Outputs: 0 abc, 1 123, 2 xyz
for v in my_list:
    print(v) #Outputs: abc, 123, xyz

# loops through tuples
for data in dog:
    print(data)

# loops through dictionaries - dictionaries loop through by key
my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(k) #output: name, language

my_dict = {"name": "Noelle", "language": "Python"}
for k in my_dict:
    print(my_dict[k]) #output Noelle, Python

#other key iterations
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
for key in capitals.values():
    print(key) # output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
for val in capitals.value():
    print(val) # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
for key, val in capitals.item():
    print(key, " = ", val) # output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# While Loops - Another way of looping while a certain condition is true
count = 0;
while count <= 5:
    print("looping - ", count)
    count += 1

while<expression>: #basic syntax for while loops

# while else statements - 
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

#break -exits the current loop permanently

for val in "string": 
    if(val == "i"):
        break
    print(val) # Outputs - s,t,r

# continue - immediately returns control to the beginning of the loop
for val in "string":
    if val == i:
        continue
    print(val)  #outputs s, t, r, n, g

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else: # only executes on a clean exit from the while loop, not a break
    print("Final else statement") #output: 3, 2, 1




# Functions - has a name, parameters, performs instructions, returns something after

# this is our list of ingredients or parameters
def burger(bun, meat, cheese, toppings):
    
    #Instructions or logic in our function
    split bun in half 
    cook meat
    place cheese on meat 
    place meat on bottom bun 
    add toppings on meat 
    place top bun over everything

    # now we can serve up our burger
    return prepared ingredients

#def
def #Keyword that signifies the declaration of a function ( "de"clare "f"unction)

def add(a,b): # function name: 'add', parameters: (a, b)
    x = a + b # process
    return x # returns value x

# calling the function

new_val = add(3,5) # this calls the new function and assigns the returned value to new_val
print(new_val) # This will print the value stored in new_val, which is 8

def say_hi(name): # name is the parameter of the function
    print("Hi, " + name)

say_hi("Michael") # "Michael" is the argument passed into the function. Output: "Hi, Michael"

greeting = say_hi("Michael")
    print(greeting) # This will print the value returned and stored in greeting


# Default Parameters - allows parameters to be optional by providing defaults
def be_cheerful(name='', repeat=2)
    print(f'Good morning {name}\n' * repeat)
be_cheerful() # Will print Good morning (repeated on 2 lines)
be_cheerful("tim") # Will print Good morning tim (repeated on 2 lines)
be_cheerful(name="john") # Will print Good morning john(repeated on 2 lines)
be_cheerful(repeat=6) # Will print Good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5) # Will print Good morning michael (repeated on 5 lines)
be_cheerful(repeat=3, name="kb") # Will print Good morning (repeated on 2 lines)






# Class - Classes are like blue-prints for objects. They have attributes (like properties such as height/weight) and methods (such as run/jump. They are blueprints for creating custom objects.

class User: # This creates a class called User (pass allows the console to move past it)
    pass

michael = User() # This creates new instances of our class
anna = User()

# Attributes: Characteristics shared by all instances of the class type.
# Methods: Actions that an object can perform. A user, for example, should be able to make a deposit or a withdrawal, or maybe send money to another user.

# Instance attributes are defined in a "magic method" called __init__, which is called when a new object is instantiated.

def __init__(self):

# declare a class and give it name User
class User:		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# The first parameter of an instance method within a class will be self, and the instance attributes are also indicated by self. .
# self is a reference to the instance, not the class.

# This will create instances of the class User
User()
guido = User()
monty = User()
# Accessing the instance's attributes
print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# We can also set the values for our instances attributes:
guido.name = "Guido"
print(guido.name) # output: Guido
monty.name = "Monty"
print(monty.name) # output: Monty


# Class Attributes - defined outside of any instance methods, and is shared among all instances of the class. 

# declaring a class attribute
class User:
    bank_name = "First National Dojo"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# Changing attributes on an instance: 
guido = User()
monty = User()
guido.bank_name = "Dojo Credit Union"
print(guido.bank_name) # output: Dojo Credit Union 
print(monty.bank_name) # output: First National Dojo

# Changing attributes on the entire class:
User.bank_name = "Bank of Dojo"
print(guido.bank_name) # output: Bank of Dojo 
print(monty.bank_name) # output: Bank of Dojo


# Now we are going to pass in arguments into the __init__ method to specify a user's instance attributes.

# In our example, even though we have 3 instance attributes, we only require input for 2 of them. When the User instance is created, we should expect to receive specific values for the name and email address. We'll assume, however, that everyone starts with $0 in their account. Let's adjust our code to allow arguments to be passed in upon instantiation:

class User:
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self , name, email_address):
    	# we assign them accordingly
        self.name = name
        self.email = email_address
    	# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python


#Methods - Functions that belong to a class. This means that we can't call them independently as we have called functions previously; rather, methods must be called from an instance of a class.

guido.make_deposit(100) #Calls Method .make_deposit with parameter-100 from Class-User Instance-guido

#Class User with Method .make_deposit
class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# methods also have access to the attributes of a class, as well as parameters

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50




















#Pass Statement to pass empty blocks - Null Operator

class EmptyClass:
    pass

for val in my_string:
    pass



# Questions

#1 Why is this the output? I thought the output would be [2,5];
x = [99,4,2,5,-3]
print(x[2:4])

#2 Can lists hold multiple varible types. (Strings, Integers)

#3 
num_to_dec = float(num) #converts floats to nums? (Does it do it back?)

#4
print(x.title()) #Output: "Hello World" - Does this capitalize the first letter after a space?

#5 Is this correct?
my_list = [1, 'Zen', 'hi']
print(enumerate(my_list)) # Output: ('0:1', '1:Zen', '2:hi')

#6 What is a shallow copy dictionary?
.copy() #returns a shallow copy dictionary

#7 Does this return for all key pairs, or just tuples?
.items() #rReturns a list of the dictionary's (key, value) tuple pairs  