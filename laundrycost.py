#/usr/local/bin/python3.7
"""laundrycost.py: Determine the cost of a laundry session """
__author__      = "Axel K"

#Laundry Quarter Calculator
#washer: $1.50 per load
#dryer: $1.00 for 45 min (minimum time to start dryer) and $.25 for each additional 15 min
loadnumber = input('How many laundry loads?: ')
normaldry = 0.45
hourdryer= input("How many 1 hour drying sessions?: ")
laundrycost = (int(loadnumber) * 1.50) + int(normaldry) + (0.25*int(hourdryer))
quartersreq = int(laundrycost/0.25)

#Print total cost of laundry session
print("Your laundry cost is:   $%.2f " % laundrycost)
#Print number of quarters needed
print("Number of quarters needed: ", quartersreq)
