# Inputs

length = input("Enter a length in feet: ")
width = input("Enter a width in feet: ")

areaSQFT = float(length) * float(width)
areaACRE = round(areaSQFT / 43560,2)

print("The area is: " , areaACRE , " acres ")