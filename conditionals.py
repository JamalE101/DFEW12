
# Asks for an input from the user as a mark.
# If the mark is greater that 85 print "Distinction"
# If the mark is between 65 and 85 print "Pass"
# Anything else print "Fail"

usermark = int(input("Enter your mark: "))
if usermark > 85:
    print("Distinction")
elif usermark >=65:
    print("Pass")
elif usermark < 65:
    print("Fail")

if usermark >= 65:
    if usermark >85:
        print("Distinction")
    else: 
        print("Pass")
else:
    print("Fail")

