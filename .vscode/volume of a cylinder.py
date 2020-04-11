# Inputs

radius = input("Enter the length of the radius: ")
height = input("Enter the length of the height: ")

areaCIRCLE = float(radius) * float(radius) * 3.14
volume = round(areaCIRCLE * float(height),1)

print("The volume of the cylinder is: " , volume , "cubic units.")
