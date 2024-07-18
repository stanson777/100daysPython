#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill=float(input(f"What was the total bill?"))
#Format the result to 2 decimal places = 33.60
tip=int(input(f"How much tip would you like to give? 10, 12, or 15?"))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
people=int(input(f"How many people to split the bill?"))
#Write your code below this line👇
bill=round(bill,2)
tip_as_percent=(bill/100)*tip
total_bill=bill+tip_as_percent
bill_per_person=total_bill/people
print(f"Each person should pay: ${round(bill_per_person,2)}")