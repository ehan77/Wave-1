# Inputs

balance = float(input("Enter the balance of your current account: "))
interest = 0.04

amount1 = round(balance * interest, 2) + balance
amount2 = round(balance * interest, 2) * amount1 + balance
amount3 = round(balance * interest, 2) * amount2 + balance

print("In the first, second and third year, the amount you will have is: ", amount1 , amount2 , amount3)
