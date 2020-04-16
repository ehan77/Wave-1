# Inputs 

amountDUE = int(input("How much should you pay? (in cents) : "))
amountPAY = int(input("How much are you paying? (in cents) : "))

change = amountPAY - amountDUE

toonie = 200
loonie = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

numT = change // toonie # num_ = number of, re_ = remainder.
reT = change % toonie
numL = reT // loonie
reL = reT % loonie
numQ = reL // quarter
reQ = reL % quarter
numD = reQ // dime
reD = reQ % dime
numN = reD // nickel
reN = reD % nickel
numP = reN // penny

print("The change is: " , change , " cents, with" , numT , "toonies," , numL , "loonies," , numQ , "quarters," , numD , "dimes," , numN , "nickels and" , numP , "pennies.")