"""File is for practice purposes only, and will execute various simple lines of Python code.
Created September 27, 2023. Version 1. Author: Sabrina Spruck"""

# Below is practice:
import math

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

# Lesson 3: Operators

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
m = 70
n = 70
o = 60
if m is n:
    print("They have the same identity")
else:
    print("They don't have the same identity")
if m is o:
    print("They have the same identity")
else:
    print("They don't have the same identity")
if m is not n:
    print("They have the same identity")
else:
    print("They don't have the same identity")
if m is not o:
    print("They have the same identity")
else:
    print("They don't have the same identity")

# Bitwise Operators
"""
First lets learn conversion, as it's important for bitwise operators.
*bits = (bi)nary dig(its)*
I. Number Systems: 
     A. Decimal - Range 0 to 9 (Base 10)
     B. Binary - Range 0 to 1 (Base 2)
     C. Octal - Range 0 to 7 (Base 8)
     D. Hexadecimal - Range 0 to 9, then 10 to 15 are represented by letters A to F (Base 16)

II. Conversion:
     A. Decimal -> Binary:
          1. Steps:
               a) Divide the number in question by 2 (the base);
               b) Write down the remainder and divide the quotient by 2 again;
               c) Repeat this until your quotient reaches 0.
               d) The remainders, from last to first, is your new binary number.
          2. Example:
               a) (25)Base 10 to ( )Base 2 *Bases are usually represented as subscripts*
                  25/2 = 12 with remainder 1
                  12/2 = 6 with remainder 0
                  6/2 = 3 with remainder 0
                  3/2 = 1 with remainder 1
                  1/2 = 0 with remainder 1
                  (25)Base 10 => (11001)Base 2
               b) (90)Base 10 to ( )Base 2
                  90/2 = 45 with remainder 0
                  45/2 = 22 with remainder 1
                  22/2 = 11 with remainder 0
                  11/2 = 5 with remainder 1
                  5/2 = 2 with remainder 1
                  2/2 = 1 with remainder 0
                  1/2 = 0 with remainder 1
                  (25)Base 10 => (1011010)Base 2
     B. Binary -> Decimal:
          1. Steps:
               a) Separate the individual digits of the number.
               b) Give each number their positional weight, from right to left.
                    i. Starting from 0, assign increments of 1 to each digit. Don't forget, right to left!
               c) Multiply each digit by the Base number to the power of their positional weight.
               d) Add it all up.
          2. Example:
               a) (1011010)Base 2 to ( )Base 10
                  From right to left:
                  0 x 2^0 = 0 x 1 = 0
                  1 x 2^1 = 1 x 2 = 2
                  0 x 2^2 = 0 x 4 = 0
                  1 x 2^3 = 1 x 8 = 8
                  1 x 2^4 = 1 x 16 = 16
                  0 x 2^5 = 0 x 32 = 0
                  1 x 2^6 = 1 x 64 = 64
                  0 + 2 + 0 + 8 + 16 + 0 + 64 = 90
                  (1011010)Base 2 -> (90)Base 10
                  *No need in the future to include the digits multiplied by 0*
"""
d = 10
e = 5
# d(10) in binary = 1010
# e(5) in binary = 0101
"""
AND (&) Bitwise Operator
      1010   | Compare each column,
    & 0101   | If both bits are 1, return 1,
    -------  | else return 0
      0000   V
"""
fBinary = bin(d & e)
print(fBinary)
# It returns only one 0 because a single 0 is enough to represent binary 0; even though there are four
# Also 0b is the prefix that tells us this is in binary
"""
Now convert the binary number obtained to decimal
(0000)Base 2 -> (0)Base 10
"""
fDecimal = d & e
print(fDecimal)
"""
OR (|) Bitwise Operator
     1010   | Compare each column,
   | 0101   | If any bits are 1, return 1,
   -------  | else return 0
     1111   V
"""
gBinary = bin(d | e)
print(gBinary)
"""
Now convert the binary number obtained to decimal
(1111)Base 2 -> (15)Base 10
"""
gDecimal = d | e
print(gDecimal)
"""
NOT (~) Bitwise Operator
     Returns one's complement of a number.
     d = 10
     d(10) in binary is 1010
     But dont forget about the sign bit!
     So because 10 is a positive number, add a 0 to the start of the binary number.
     If it were negative, you would add a 1 instead.
     So actually, d = 01010
     which makes ~d = ~01010
     which equates to 10101
     Now identify the decimal equivalent to 10101
     However, keep in mind the sign bit, it is -2 to the power of its positional weight
     So ( -2^4 )0101
     But for whatever reason, it is still negative, even though it's an even exponent, for whatever reason:
     Soooo... -16 + 4 + 1 = -11
"""
hBinary = bin(~d)
print(hBinary)
hDecimal = ~d
print(hDecimal)
# XOR ^
j = 10
k = 9
"""
     1010   | Compare each column,
   ^ 1001   | If ONLY one of the bits are 1, return 1,
   -------  | else return 0
     0011   V

(0011)Base 2 -> (3)Base 10
Again, the console won't care about the 0s
"""
iBinary = bin(j ^ k)
print(iBinary)
iDecimal = j ^ k
print(iDecimal)

# Walrus Operators - assign variables in the middle of expressions
withoutWalrus = "This has to be called separately."
print(withoutWalrus)
print(withWalrus := "This can be called together, with the assignment.")

# Lesson 4: Operators
#     If statement
number = int(input("Please type the number 3: "))
if number == 3:
    print("Good job.")
#     If-else statement
favAnimal = input("What's your favorite animal?")
if favAnimal == "dog":
    print("Me too!!!")
else:
    print("Oh, that's cool I guess.")
#     If-elif-else statement
activity = input("There's a lake for swimming, a tree that you can climb, or you can choose to go home. Which do you "
                 "decide to do?")
if activity == "swim":
    print("You swim in the beautifully clear water. It feels cool and you feel refreshed.")
elif activity == "climb":
    print("The tree is tall, but you climb to one of the highest branches. You feel on top of the world.")
elif activity == "go home":
    print("You decide you're done with being outside, and go home.")
else:
    print("Please choose one of the mentioned activities.")
#     Nested If-else statement
yesOrNo = input("A shifty man approaches you and offers several things to buy off of him. Choose to say Yes or No.")
if yesOrNo == "Yes":
    itemChoice = input("He asks with a gravely voice, 'What're ya buyin'?' He shows you a health potion, "
                       "a mana potion, and a weapon upgrade.")
    if itemChoice == "health potion":
        print("You buy the health potion!")
        takeHealth = input("Take it now?")
        if takeHealth == "Yes":
            print("You drink the health potion, and feel a thousand times better. Your wounds are now much less severe.")
        else:
            print("You put the health potion away in your backpack for later.")
    elif itemChoice == "mana potion":
        print("You buy the mana potion!")
        takeMana = input("Take it now?")
        if takeMana == "Yes":
            print("You drink the mana potion, and feel as though you can conjure several more spells before resting.")
        else:
            print("You put the mana potion away in your backpack for later.")
    elif itemChoice == "weapon upgrade":
        print("You buy the weapon upgrade! Your dingy sword becomes a steel sword, and you gain +5 in attack.")
    else:
        print("You decide the man has nothing you want, and you don't buy anything from him.")
elif yesOrNo == "No":
    print("Creeped out by the man, you decide to turn him down and go your own way.")
else:
    print("Please choose Yes or No.")

# Lesson 5: Using the math module; imported at the top
#     Constants
#          showing and using pi
print(math.pi)


def circle_area(radius):
    return math.pi*radius**2


print("Area of the circle =", circle_area(3))

#          showing and using Tau (2π or τ) which is useful for angular measurements
print(math.tau)


def circle_circum(radius):
    return math.tau*radius


print("Circumference of the circle =", circle_circum(3))

#          showing and using Euler's number (e) which is useful for problems involving exponential growth and decay
print(math.e)


def comp_interest(pv, r, t):
    return pv*math.e**(r*t)


print("If you start with $1000 paying 2% interest with continuous compounding, after 3 years it would be: ", comp_interest(1000, .02, 3))

#          showing and using Not a Number (nan) which is useful for representing missing or unknown numbers; not equal to 0
print(math.nan)

maryAge = 10
paulAge = 21
bobAge = math.nan
suzyAge = 50


def halved_age(age):
    return age/2


print("Mary's age when halved is: ", halved_age(maryAge))
print("Paul's age when halved is: ", halved_age(paulAge))
print("Bob's age when halved is: ", halved_age(bobAge))
print("Suzy's age when halved is: ", halved_age(suzyAge))

#          Data type of math.nan is float, but it's not considered a valid number
print(type(math.nan))

#          showing and using positive and negative floating-point infinity constants for numbers that approach infinity
print(math.inf)
print(-math.inf)
toFrontDoorFeet = 10
toWalmartFeet = 7920
toEdgeOfUniverseFeet = math.inf
toMyAtomsFeet = -math.inf
print(toWalmartFeet - toFrontDoorFeet)
print(toFrontDoorFeet * toEdgeOfUniverseFeet)
print(toWalmartFeet + toMyAtomsFeet)
print(toEdgeOfUniverseFeet > toMyAtomsFeet)
print(toEdgeOfUniverseFeet < toWalmartFeet)
print(toMyAtomsFeet < toWalmartFeet)

#     Functions
#          Number Functions
#               math.ceil() - rounds up
print(math.ceil(9.1203))
#               math.floor() - rounds down
print(math.floor(9.1203))
#               math.factorial() - multiplies a number by every whole, positive number that comes before it
print(math.factorial(6))
#               math.gcd() - largest common divisor that divides the numbers without a remainder
print(math.gcd(7, 10))
print(math.gcd(10, 100))
#               math.fabs() - returns absolute value of a number
print(math.fabs(4))
print(math.fabs(-4))
#          Power and Logarithmic Functions
#               math.pow() - when (x, y) it returns x to the power of y
print(math.pow(3, 3))
#               math.exp(x) - Euler's number, risen to the power of x
print(math.exp(1))
print(math.exp(2))
#               math.sqrt() - returns the square root of a number
print(math.sqrt(9))
print(math.sqrt(16))
print(math.sqrt(25))
#               math.log() - when (x, y) this returns the exponent that is required for y to become equal to x; so y^(returned#) = x; when a base isn't given, it uses Euler's number
print(math.log(1000, 10))
print(math.log(1000))
#          Trigonometric Functions
#               math.sin() - how far above or below the center of a circle a point is; above the center is positive, below is negative
print(math.sin(10))
#               math.cos() - how far to the left or right the center of a circle a point is; right to the center is positive, left is negative
print(math.cos(10))
#               math.tan() - slope of a line that intersects a curve at exactly one point
print(math.tan(10))

# Lesson 6: Operations on Strings
username = input("Please enter your name:")
print("Hello,", username)

bird = input("What's your favorite bird? ")
whyBird = input("Why is that your favorite? ")
print("My favorite bird is a(n) {}, because {}.".format(bird, whyBird))

#     named indexes method
fish = input("What's your favorite fish? ")
whyFish = input("Why is that your favorite? ")
print("My favorite fish is a(n) {favFish}, because {whyFavFish}.".format(favFish=fish, whyFavFish=whyFish))

#     index value method
mammal = input("What's your favorite mammal? ")
whyMammal = input("Why is that your favorite? ")
print("My favorite mammal is a(n) {0}, because {1}.".format(mammal, whyMammal))

#     empty braces method
manyAnimals = input("What's your favorite animal? ")
animalAmount = input("How many would you want, if you could have as many as you want? ")
print("My favorite animal is a(n) {}, and I would want {} of them.".format(manyAnimals, int(animalAmount)))

# Lesson 7: fStrings

hairStyle = input("What style of hair do you have? Straight, wavy or curly? ")
print(f"I love your {hairStyle} hair! How do you do that?")

num1 = 5
num2 = 10
print(f"Five plus ten is {num1 + num2}")

mainHandWeapon = input("Choose a main hand weapon: ")
favElement = input("What's your favorite element, like water, fire, earth, etc? ")
print(f"You head off on your adventure into the spooky forest, with your {favElement + mainHandWeapon} in hand.")
