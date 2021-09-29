# Basic - Print all integers from 0 to 150.

for int in range(151):
    print(int)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for int in range(5,151):
    if( int % 5 == 0):
        print(int)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for int in range(1,101):
    if( int % 10 == 0):
        print("Coding Dojo")
    elif( int % 5 == 0):
        print("Coding")
    else:
        print(int)
    

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

sum = 0
for int in range(0,5001):
    if(int % 2 == 1):
        sum = sum + int
print(sum)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for int in range(2018, 0, -4):
    print(int)

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 5
highNum = 101
mult = 10

for int in range(2,101):
    if(int % mult == 0):
        print(int)
