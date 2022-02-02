# Write a Python program that accepts a word from the user and reverse it.

# Aceept a word from the user
# displays the word in reverse order
# range()

var1 = input("Type a word you want to be reversed: ")
var2 = len(var1) -1
var3= ""
for i in range(var2, -1, -1):
    var3 = var3 + var1[i]

print(var3)


# 