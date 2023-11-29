print("hello world!")

# fast easy comment

'''
This is a long comment
It has more than one line
'''

# Variable
x = 10
print(x)
y = 11.5
x = "this is a string"
print(x)

# math operators
x = 100
y = 10
result = x//y
result = int(x/y)
print(result)

# built in functions
min_val=min(10,1)
print(min_val)

raised=pow(2,4)
print(raised)
raised = 2**4

# if statements
x = -1
if x < 0:
    print("x is negative")
    x += 10

print("out of if statement")

if x < 10:
    x += 1
elif x > 10:
    x -= 1
else:
    x = 0

y = 10
if x < 0 and y > 0:
    x = 1
if x < 0 or y > 10:
    y = 0

count = 0
while count <= 10:
    count += 1
    print(count)

alist = [1,2,3,4,5]
for val in alist:
    print(val)

#equivalent of for (int i = 0; i , alist.length; i++);
#range takes 3 parameters: starting index, num. of repetitions, every nth value.
#this iterates through 1-4.
for i in range(0,len(alist)-1,1):
    print("i is", i, "and the value at i is", alist[i])

for i, value in enumerate(alist):
    print("the value at index place",i,"is",value)

#functions
    '''
    java: int addNumbers (int x, int y) {
        return x+ y;
        }
    '''


def add_numbers(x,y):
    return x + y

result = add_numbers(2,4)
print(result)

def say_hello(name="friend"):
    print("hello",name)

say_hello()

#Strings
fname="Ryan"
lname="Loftus"
full_name=fname+ " " + lname
print(full_name)
print(fname, lname)

first_initial = fname[0]
print(first_initial)

last_char = lname[-1]
print(last_char)

#slicing
#course [ start_index : end_index]
course = "Platform Computing"
platform = course[0:8]
computing = course[9:18]
platform = course[:8]   #same thing
computing = course[9:]
course_copy = course[:] #whole string
print(platform)
print(computing)