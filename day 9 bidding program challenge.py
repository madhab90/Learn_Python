from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print (logo)
bidding_records = {}
keep_checking = True 

def find_highest_bidder(bidding_records):
  highest_bid = 0
  winner = ""
  for bidder in bidding_records:
    if bidding_records[bidder] > highest_bid:
      highest_bid = bidding_records[bidder]
      winner = bidder
  print (f'Winner is {winner} with winning bid {highest_bid} ')

while keep_checking:
  name = input ("What is your name ?")
  amount = float(input("What is your bidding amount ?"))
  bidding_records[name] = amount
  more_bidders = input ("Any more bidders ? Type Yes if there are else No to proceed to next stage.")
  if more_bidders == "No":
   keep_checking = False
  else :
   clear()
find_highest_bidder(bidding_records)


  


 

