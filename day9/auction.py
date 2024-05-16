from replit import clear
from art import logo

print(logo)
print("Welcome to Blind Auction!")

participants = {}


def add_participants(auction_pars, auction_bid):
    participants[auction_pars] = auction_bid


def calc_highest_bid(bidding_record):
    highest_bid = 0
    winner = ''
    for high in bidding_record:
        bid_amount = bidding_record[high]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = high
    print(f"The winner is {winner} with a bid of {highest_bid}")


end_auction = True
while end_auction:
    name = input("What is your name: ")
    bind = int(input("What is your bind: $"))
    add_participants(name, bind)
    other_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if other_bids == 'no':
        calc_highest_bid(participants)
        end_auction = False
    elif other_bids == 'yes':
        clear()
    else:
        print("Wrong insert!")
