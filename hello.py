"""File is for practice purposes only, and will execute various simple lines of Python code.
Created September 27, 2023. Version 1. Author: Sabrina Spruck"""

# Below is practice:

# Lesson 1: Printing in the console with Python
print("Hello World!")
print("Love you Python")
print("Sabrina")
print("Python")
print("Java")

# Lesson 2: Variables
animal = "puppy"
Animal = "Pomeranian"
ANIMAL = "Luma Bean"
lumaAge = 1
print(animal)
print(Animal)
print(ANIMAL)
print(lumaAge)
# Number Variables
integerNumber = 9
floatNumber = 4.5
complexNumber = 5 + 3j
print(integerNumber)
print(floatNumber)
print(complexNumber)
# String Variables
letterString = "L"
wordString = "Luma"
sentenceString = "Luma Bean is a sweet pup."
multilineString = """Luma Bean is actually the sweetest pup.
She deserves all the love.
And brightens everyone's day.
    -Sabrina"""
print(letterString)
print(wordString)
print(sentenceString)
print(multilineString)
# Boolean Variables
isLove = True
hasHate = False
print(isLove)
print(hasHate)
print(6 > 4)
print(4 > 6)
# using the function: type()
print(type(integerNumber))
print(type(1))
print(type(floatNumber))
print(type(1.5))
print(type(complexNumber))
print(type(1 + 5j))
print(type(letterString))
print(type("M"))
print(type(wordString))
print(type("Mine"))
print(type(sentenceString))
print(type("What's yours is mine."))
print(type(multilineString))
print(type("""What's mine is yours.
And what's yours is mine."""))
print(type(isLove))
print(type(hasHate))
print(type(6 > 4))
print(type(4 > 6))
print(type(True))
print(type(False))
"""
# using the function: input()
username = input("Please enter your name:")
print(username)
print(type(username))
age = input("Please enter your age:")
print(age)
# Be Aware: The one above and the one below show differently in the console.
userDog = input("Please enter your dog's name:")
dogAge = input("Please enter your dog's age:")
print(userDog)
print(dogAge)
# input() function always accepts the values as string by default
print(type(userDog))
print(type(dogAge))
# So we are going to do type conversion
dogAgeAsInt = int(input("Please enter your dog's age:"))
print(dogAgeAsInt)
print(type(dogAgeAsInt))
"""

# Operators
# Arithmetic Operators
a = 5
b = 2
c = a + b
print("The math between 5 and 2:")
print("The result when adding is", c)
print("The result when subtracting is", a - b)
print("The result when multiplying is", a * b)
print("The result when dividing is", a / b)
print("The result with modulo is", a % b)
print("The result when calculating the exponent is", a ** b)
print("The result with floor division is", a // b)
# Relational/Comparison Operators
ageOne = 16
ageTwo = 18
requiredAge = 18
print(ageOne > requiredAge)
print(ageOne < requiredAge)
print(ageOne == requiredAge)
print(ageOne != requiredAge)
print(ageTwo >= requiredAge)
print(ageTwo <= requiredAge)
# Logical Operators
x = 18
# One is True, One is False
print(x > 10 and x == 20)
print(x < 20 or x != 18)
print(not (x > 10 and x == 20))
print(not (x < 20 or x != 18))
# Both are True
print(x > 10 and x == 18)
print(x < 20 or x != 20)
print(not (x > 10 and x == 18))
print(not (x < 20 or x != 20))
# Both are False
print(x > 20 and x == 20)
print(x < 10 or x != 18)
print(not (x > 20 and x == 20))
print(not (x < 10 or x != 18))
# Membership Operators
container = [1, 2, 3, 4, 5]
# It's in there.
if 2 in container:
    print("It's in there!")
else:
    print("Sorry, not here.")
# It's not in there.
if 7 in container:
    print("It's in there!")
else:
    print("Sorry, not here.")
# It's in there.
if 2 not in container:
    print("It's not here!")
else:
    print("Hey! It's here.")
# It's not in there.
if 7 not in container:
    print("It's not here!")
else:
    print("Hey! It's here.")
# Identity Operators
# Bitwise Operators
# Walrus Operators
