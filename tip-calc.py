# Assignment: Tip Calculator
# By raghav664 (Raghav)

bill = float(input("What's your bill amount? $"))  # Take the bill amount
tip_percentage = input("What percentage would you like to give as tip? ") # Take the tip percentage

if "%" in tip_percentage:
	tip_percentage = tip_percentage.replace("%" , "")

tip_percentage = float(tip_percentage)

tip_amount = (tip_percentage/100) * bill # Calculate the tip

total_amount = tip_amount + bill

print(f"Your bill of ${bill:.2f} and your tip of ${tip_amount:.2f} has a total of ${total_amount:.2f}.")

exit()