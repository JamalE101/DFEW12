# inputvar1 = int(input("type a number: "))
# var1 = 5

# if inputvar1 > 5:
#     print("your input was greater than 5")

# else:
#     print("Your input was less than 5")


# if inputvar1 < 5 and inputvar1 > 0 :
#     print("your input was either less than 5 or a positive number")

# else: 
#     print("Your input was either greater than 5 or negative: ")

# listvar1 = ["todd", "Len", "Dana", "janna"]

# if "janna" in listvar1:
#     print("janna is in the list")
# else:
#     print("janna is not in the list")

inputvar1 = input("Type a letter in the alphabet: ")
vowl = "aeiou"
constonant = "bcdfghjklmnpqrstvwxyz"
if inputvar1 in vowl:
    print("It was a vowl")
elif inputvar1 in constonant:
    print("it was a consoant")
else:
    print("You didn't type an alphabet letter")

