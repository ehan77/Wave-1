# Inputs

days = int(input("Enter the number of days: "))
hrs = int(input("Enter the number of hours: "))
mins = int(input("Enter the number of minutes: "))
secs = int(input("Enter the number of seconds: "))

secsDAYS = days * 24 * 60 * 60
secsHRS = hrs * 60 * 60
secsMINS = mins * 60

total = secsDAYS + secsHRS + secsMINS

print("The duration you inputed is a total of" , total , "seconds.")