from replit import clear

auction_info = []
auction = True

def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {}
    new_bidder["bid"] = bidder_amount
    new_bidder["name"] = bidder_name
    auction_info.append(new_bidder)

while auction:
  print("Welcome to the private bidding auction")
  name  = input("What is your name?: ").title()
  bid = float(input("How much would you like to bid?: $"))
  add_new_bidder(bidder_name = name, bidder_amount = bid)

  others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n")
  if others == 'no':
    auction = False
    highest_bidder = 0
    count = -1
    for e in auction_info:
      if e['bid'] > highest_bidder:
          highest_bidder = e['bid']
          count += 1
    winner = auction_info[count]['name']
    print(f"The highest bidder is {winner} with a ${highest_bidder}")
    print("Thank you for your participation.")
  else:
    clear()
  

import sys
if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

print (f"Reading from file: {sys.argv[1]}")
sys.exit(0)

import csv
# file = open("file.csv", "a")
name = input(" Name: ")
number = input(" Number: ")
with open("file.csv", "a", newline='') as file:
  # writer = csv.writer(file)
  writer = csv.DictWriter(file, fieldnames=["Name", "Number"])
  writer.writeheader()
  writer.write({"Name": name, "Number": number})

# file.close()

