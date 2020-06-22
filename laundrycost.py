#!/usr/local/bin/python3.7
"""laundrycost.py: Determine the cost of a laundry session """
__author__      = "axkent"

#washer: $1.50 per load
#dryer: $1.00 for 45 min (minimum time to start dryer) and $.25 for each additional 15 min
#habit is setting the dryer to 60 min and reloading dryer before 60 minutes is up

#initialize variables
loadnumber = int(input('How many laundry loads?: '))
firsthourdry = float(1.25)
#number of drying sessions starting from 0 minutes is all drying sessions besides the first drying session
subsequentdry = int((loadnumber) - 1)
#compute cost
laundrycost = (loadnumber*1.50) + firsthourdry + (subsequentdry*0.75)
#compute number of quarters needed
quartersreq = int(laundrycost/0.25)

#if user enters less than 1 load
if loadnumber < 1:
    #print error message
    print("Must have at least 1 load")
    #else print total cost of laundry session
else:
    print("Cost:   $%.2f " % laundrycost)
    #Print number of quarters needed
    print("Quarters: ", quartersreq)
