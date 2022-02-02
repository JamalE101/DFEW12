# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

# Create a new python file. In that file create a program that works out a grade based on marks with the use of functions.
# The program should take the students name, homework score (/25), assessment score (/50) and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

# def studentinfo(homework, assessment, test ):
#     overall_mark = (homework* assessment* test)*100
#     return overall_mark

# students_name = str(input("What is your name? "))
# homework_score = int(input("Enter your score out of 25? "))/25
# assessment_score = int(input ("Enter your score out of 50? "))/50
# test_score = int(input ("Enter your score out of 100? "))/100

# final = studentinfo(homework_score, assessment_score, test_score)
# print(f"Your overall percentage is: {final}")

# Write a Python function to find the Max of three numbers.

def numbers(numb1,numb2,numb3):
    if numb1 >= numb2 and numb1 >= numb3:
        return numb1
    elif numb2 > numb1 and numb2 >= numb3:
        return numb2 
    else:
        return numb3 
    
        
    



number1=int(input("Enter the first number: "))
number2=int(input("Enter the second number: "))
number3=int(input("Enter the third number: "))

Max_number = numbers(number1,number2,number3)

print(f"The Maximum number from the numbers entered is: {Max_number}")