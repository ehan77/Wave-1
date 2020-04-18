# Inputs

secs = int(input("Enter a number of seconds: "))

# 1 day = 86400 seconds, 1 hour = 3600 seconds, 1 minute = 60 seconds.

numDAYS = secs // 86400
remainingDAYS = secs % 86400
numHOURS = remainingDAYS // 3600
remainingHOURS = remainingDAYS % 3600
numMINUTES = remainingHOURS // 60 
remainingMINUTES = remainingHOURS % 60
numSECONDS = remainingMINUTES // 1

print("The amount of seconds you inputed is " , numDAYS , "days," , numHOURS , "hours," , numMINUTES , "minutes and" , numSECONDS , "seconds.")