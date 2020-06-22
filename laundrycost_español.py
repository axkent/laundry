#!/usr/local/bin/python3.7
"""laundrycost_español.py: Determine el costo de una sesión de lavandería.  """
__author__      = "axkent"

#washer: $1.50 per load
#dryer: $1.00 for 45 min (minimum time to start dryer) and $.25 for each additional 15 min
#habit is setting the dryer to 60 min and reloading dryer before 60 minutes is up

loadnumber = int(input('¿Cuántas tandas de ropa?: '))
firsthourdry = float(1.25)
subsequentdry = int((loadnumber) - 1)
laundrycost = (loadnumber*1.50) + firsthourdry + (subsequentdry*0.75)
quartersreq = int(laundrycost/0.25)

#Print total cost of laundry session
print("El costo:   $%.2f " % laundrycost)
#Print number of quarters needed
print("Cuartos de moneda: ", quartersreq)
