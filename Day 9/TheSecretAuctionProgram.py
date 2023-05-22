# Logo
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

#Clear screen
import os
clear =lambda: os.system("cls")
# Function to find the highest bid
def find_the_highest_bid(bid_records):
    highest_bid=0
    for bid in bid_records:
        bid_amount=bid_records[bid]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bid
    print(f"The winner is {winner}")        
# Code here
auctioneer_dict={}
continue_bid=True
print("Welcome to the secret auction program!")
while continue_bid:
    auctioneer_name=input("What is your name? ")
    bid_value=int(input("What's your bid? "))
    auctioneer_dict[auctioneer_name]=bid_value
    other_bid=input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bid.lower()!="yes":
        continue_bid=False
    clear()
find_the_highest_bid(auctioneer_dict)


