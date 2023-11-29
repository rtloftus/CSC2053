#try except- like throwing an exception (inside the try, put what could cause the error)
try:
    #input is like scanner
    num = int(input("enter a number: "))
    num += 10
    print(num)
#if a number is not entered
except:
    print("you did not enter a number")

#reads in a file
with open("movies.txt") as file:
    #take each element of file and store in line
    for line in file:
        print(line.strip())

with open("heights.txt") as file:
    for line in file:
        #strip revomes space in between line
        stripped_line = line.strip()
        #creates a list tokens that splits a line into elements
        tokens = stripped_line.split()
        print(tokens)
        print (tokens[0], tokens[1], "is", int(tokens[2]), "inches tall." )




