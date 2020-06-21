#/usr/local/bin/python3.7
"""laundrycost.py: Determine the cost of a laundry session """
__author__      = "Axel K"

#washer: $1.50 per load
#dryer: $1.00 for 45 min (minimum time to start dryer) and $.25 for each additional 15 min
#typical laundry habit is to set the dryer to 60 min and reload dryer before 60 minutes is up

loadnumber = int(input('How many laundry loads?: '))
firsthourdry = float(1.25)
subsequentdry = int((loadnumber) - 1)
laundrycost = (loadnumber*1.50) + firsthourdry + (subsequentdry*0.75)
quartersreq = int(laundrycost/0.25)

#Print total cost of laundry session
print("Your laundry cost is:   $%.2f " % laundrycost)
#Print number of quarters needed
print("Number of quarters needed: ", quartersreq)
