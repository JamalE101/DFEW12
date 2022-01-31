
# This is to turn a float number into a rounded interger
number1 = input("enter whole number; ")
number2 = input("enter decimal numebr: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

# This is to turn True or False statements 

name = "pepe"
age = 3
bark = True
tweet = False

print("my pet is called", name, ", he is", age, "years old.")
print("statement:", name, "barks.", bark)
print("statement:", name, "tweets.", tweet)