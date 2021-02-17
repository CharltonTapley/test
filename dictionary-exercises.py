
# --------------------------------- Section 01 -------------------------------------
print('----SECTION 01----')

# Create a Dictionary for a car
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Print out the car dictionary
print(car)

# Print our the year of the car
print(car["year"])

# Print out each key of the car, but on a separate line, so that it's easier to read
for i in car:
    print(i)

# SECTION 1 CHALLENGE
# You can also print out the key and the value separately, can you do that?
for i in car:
    print(i, car[i])

# --------------------------------- Section 02 -------------------------------------
print('----SECTION 02----')

# Create our 2D array
my2DList = [[1, 2, 3],
            [2, 4, 6],
            [9, 8, 7]]

# Print out my2DList
print(my2DList)

# Print out the second list in my2DList
print(my2DList[1])

# Print out the last element of the first list in my2DList
print(my2DList[0][2])
print("")

# SECTION 2 CHALLENGE
# print out each element of each list on a separate line
for set in my2DList:
    for number in set:
        print(number)



# --------------------------------- Section 03 -------------------------------------
print('----SECTION 03----')
# Here are three simply formatted dictionaries so you don't need to type so much
# {"brand": "Ford", "model": "Mustang", "year": 1964}
# {"brand": "Toyota", "model": "Supra", "year": 1993}
# {"brand": "Fiat", "model": "500", "year": 2010}

# Create a list of dictionaries from the above, call it 'cars'
cars = [{"brand": "Ford", "model": "Mustang", "year": 1964},
        {"brand": "Toyota", "model": "Supra", "year": 1993},
        {"brand": "Fiat", "model": "500", "year": 2010}]

# Print out cars
print(cars)

# Print out the data type of cars
print(type(cars))

# Print out the last car
print(cars[2])

# Print out the data type for the last car
print(type(cars[2]))

# Print out each car on a separate line
for car in cars:
    print(car)

# Print out the model of the second car
print(cars[1]["model"])

# SECTION 3 CHALLENGE
# print out each field (key and value) of each car on a separate line
for x in cars:
    for key, value in x.items():
        print(key, "=", value)

# --------------------------------- Extra example -------------------------------------
# Look at the data structure below
# At the top level it's a dictionary
# The first three keys have scalars as their values
# The fourth key has a list as it's value
# the fifth key has a dictionary as it's value
# The sixth is also a list, but each element of that list is a dictionary

example = {
    "text key": "string",
    "integer key": 123,
    "boolean key": True,
    "simple list": [
        "value 1",
        "value 2"
    ],
    "sub_dict": {
        "element 1": "value 1",
        "element 2": "value 2"
    },
    "dict list": [
        {
            "key 1.1": 1.1,
            "key 1.2": 1.2
        },
        {
            "key 2.1": "value 2.1",
            "key 2.2": "value 2.2"
        }
    ]
}

# Try accessing and printing various parts and elements of the structure using indexing
# Try to create a nicely formated output by nesting loops inside loops
# Experiment and learn about it
