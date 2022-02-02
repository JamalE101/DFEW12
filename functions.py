def reverseword(inword):
    lenword = len(inword)-1
    revword = ""
    for letter in range(lengword,-1,-1):
        revword = revword + inword[letter]
    return revword

def palindrometest(typeword, reversedword):
    if userinputvar == capturedword:
        return True
    else:
        return False

# Palimdrome finder

userinputvar = input("Typo a word")
capturedword = reverseaword(userinputvar)
isplaindrome =palindromertest(userinputvar,capturedword)
print(f"{userinputvar} tested: {ispalindrome}")








