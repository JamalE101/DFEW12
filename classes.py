class Lettertest:

    def __init__(self,stringin):
        self.stringofletters = stringin

    def testaletter(self,letterin):
        if letterin.upper() in self.stringofletters:
            return True
        else:
            return False



testletter= "f"
isavowel = Lettertest("AEI")
isaconsonant = Lettertest("BCDFGHJKLMNPQRSTVWXYZ")
isaletterwithoneendpoint = Lettertest("P")
#isaconsonant.stringofletters = "BCDFGHJKLMNPQRSTVWXYZ"
print(isaconsonant.stringofletters)
print(isavowel.stringofletters)
print(testletter, "tested as: a vowel", isavowel)
# print(testletter, "tested as a consonant: ", consonantresult)
