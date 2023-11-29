alist = [10,20,30,40,50]

#add a value to the list
alist.append(5)
alist.append(6)
alist.append(7)
print(alist)

#remove a value from the list
alist.remove(50)
print(alist)

#remove a value at a certain index
alist.pop(2)
print(alist)
alist.pop() #last value is removed
print(alist)

#sorts list by numeric value
alist.sort()
print(alist)

#add values between 6 and 20 from alist to empty
empty = []
for value in alist:
    if value >= 6 and value <= 20:
        empty.append(value)
print(empty)

#fills an empty array with initial values (1000 0's)
empty =[0] * 1000
empty[10] = 10

#repeats strings (dogdogdog)
dog = "dog"
dogs = dog * 3
print(dogs)

#fills squares with 1000 0's
squares = [0] * 1000
for i in range(len(squares)):
    #assigns a value of index i, squared. Ex. i = 2, place 2 of the array would be 4.
    squares[i] = i*i
print(squares)

#makes a copy of squares (simpler for loop)
squares_copy = [value for value in squares]
print(squares_copy)

#makes a list with only squares over 1000
large_squares = [value for value in squares if value >= 1000]
div_3 = [value for value in squares if value % 3 == 0]
print(div_3)

#comprehension of squares
squares = [i*i for i in range(1000)]
print(squares)

#Sets
#sets do not keep order and does not include duplicates
aset = {1,2,3}
print(aset)

# aset[1]=100 CANNOT DO THIS: NO INDEX PLACES BC NO ORDER

#casting a list to a set to remove duplicates (helpful for hw2)
dups = [1,2,2,2,4,4,5,5,1]
no_dups = set(dups)
print(no_dups)
no_dups = list(no_dups)
print(no_dups)

#Dictionaries
#equivalent to hashmaps in java
#Example:
cities = {}
cities[19333] = "Devon"
city = cities[19333]

fav_foods = {"kathleen" : "pizza",
              "chris" : "pasta", "bob" : "burgers", "josh" : "mac n cheese"}
print(fav_foods)

#recall someones fav food
josh_fav = fav_foods["josh"]
print(josh_fav)

#iterate through the list
for key in fav_foods:
    print(key, "fav food is", fav_foods[key])
#alternative
for key, value in fav_foods.items():
    print(key, "fav food is", value)

#check if key is in dictionary
#this will return error because no kim
#kim = fav_foods["kim"]

#check for kim
if "kim" in fav_foods:
    kim = fav_foods["kim"]
else:
    fav_foods["kim"] = "cereal"





