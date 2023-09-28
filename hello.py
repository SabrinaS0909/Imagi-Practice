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
complexNumber = 5+3j
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
print(type(1+5j))
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


