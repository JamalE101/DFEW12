# countdown

# var = 5

# while var > 0:
#     print(var)
#     var = var -1 
# var = int(input("enter a number:"))
# while var > 0 and var <2000:
#     if var%2 == 0: 
#      var = var -1

# for i in range(5):
#     print("output", i)

# count = 0
# name = str(input("What is your name? "))
# while count < 5:
#     print(name,"is awesome!")
#     count +=1
# for i in range(5,11):
#     print(i)

# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

count = 5

while count > 0:
        name = (input("What is your name? "))
        print(name,"is awesome!")
        count = count -1 

# by using a list

count = 5
list = []
while count > 0:
    list.append(input("What is your name?: "))
    count = count - 1

for i in list:
    print(f"{i} is awesome!")
