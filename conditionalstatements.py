# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included)
# n1=[]
# for i in range (1500,27001):
#     if (i%7==0) and (i%5==0):
#         n1.append(str(i))
# print(','.join(n1))

#  Write a Python program that accepts a word from the user and reverse it.


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
