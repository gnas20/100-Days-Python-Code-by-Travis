
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
#Write your code below this line 

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

percentage_tip = int(input("What percentage tip would you like to give? "))

numbers_of_people_to_split = int(input("How many people to split the bill? "))

total_tip = total_bill*percentage_tip/100
amount_by_person =(total_bill+total_tip)/numbers_of_people_to_split

final_amount = "{:.2f}".format(amount_by_person)
print(f"Each people should pay: ${final_amount}")
