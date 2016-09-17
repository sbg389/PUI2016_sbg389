# Author: Sebastian Bania (sbg389), NYU, September 2016
##############################
# This script retrieves and reports information about active vehicles for a given MTA bus line.
# The script was developed as part of HW2 of PUI2016
##############################
# The script has two arguments: the MTA Bus Time developer Key and the line number to be queried
# i.e. run the code as
#      python show_bus_location.py <MTAKEY> <MTA_BUS_LINE>

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function

# the next import statemens allows to read and parse line input arguments
# the argument validation is based on the argparse doc at https://docs.python.org/3/library/argparse.html
import argparse

# import package to parse the json format from the API output
#https://docs.python.org/2/library/json.html
import json

parser = argparse.ArgumentParser(description='Query MTA Bus Line')
parser.add_argument('MTAKEY', help='The MTA Bus Time API Developer Key')
parser.add_argument('BUSLINE', help='The MTA Bus Line that we want to query')

args = parser.parse_args()

print (args.BUSLINE)
print (args.MTAKEY)


#Load the test API response from the file, we will use this while refining the parsing to avoind API quota depletion
with open('mtaresponse.json') as mtaresponse:
    mtadata = json.load(mtaresponse)

#Print using nice format provided by the json package
#print (json.dumps (mtadata, sort_keys=True, indent=4, separators=(',', ': ')))

#print (mtadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']['VehicleActivity'])

vehicleActivityArray = mtadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

for vehicleActivity in vehicleActivityArray[0]['VehicleActivity']:
    print (vehicleActivity)

    print ('\n')