from car import Car

with open("cars.txt") as file:
     carlist = []
     for line in file:
        stripped_line = line.strip()
        tokens = stripped_line.split()
        tokens[2] = int(tokens[2])
        tokens[3] = int(tokens[3])
        car = Car(tokens[0],tokens[1],tokens[2],tokens[3])
        print(car.__str__())
        

