# Author: Sebastian Bania (sbg389), NYU, September 2016
##############################
# This script retrieves and reports information about the location (lat, lon) and next stop
# for all active vehicles for a given MTA bus line and outputs it on a csv file
# The script was developed as part of HW2 of PUI2016
##############################
# The script has three arguments: the MTA Bus Time developer Key, the line number to be queried and the csv file name
# i.e. run the code as
#      python get_bus_info_sbg389.py <MTAKEY> <MTA_BUS_LINE> <MTS_BUS_LINE>.csv

# the next line import packages that change the python 2 print function
# so that it require the same syntax as python 3
# thus the code will work both in python 2 and python 3
from __future__ import print_function

# the next import statements allows to read and parse line input arguments
# the argument validation is based on the argparse doc at https://docs.python.org/3/library/argparse.html
import argparse

# import package to parse the json format from the API output
#https://docs.python.org/2/library/json.html
import json
import urllib2

#import pandas (we will use dataframe to store the bus info and output to csv)
import pandas as pd

parser = argparse.ArgumentParser(description='Query MTA Bus Line')
parser.add_argument('MTAKEY', help='The MTA Bus Time API Developer Key')
parser.add_argument('BUSLINE', help='The MTA Bus Line that we want to query')
parser.add_argument('OUTFILE', help='The path to thte output csv')

args = parser.parse_args()

#Load the test API response from the file, we will use this while refining the parsing to avoind API quota depletion
#with open('mtaresponse.json') as mtaresponse:
#    mtadataFile = json.load(mtaresponse)

#Print using nice format provided by the json package
#print (json.dumps (mtadata, sort_keys=True, indent=4, separators=(',', ': ')))

#Build the URI for the API Call concatenating the key and bus line from the argument parameters
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&" \
      "LineRef=%s"%(args.MTAKEY, args.BUSLINE)

#Get the response and load the string representation into a dictionary
response = urllib2.urlopen(url)
mtadataString = response.read().decode("utf-8")
mtadata = json.loads(mtadataString)

vehicleActivityArray = mtadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
numberOfActiveBuses = len(vehicleActivityArray[0]['VehicleActivity'])

#Create the pandas dataframe to store the data

columns = ['Latitude','Longitude','Stop Name','Stop Status']

df = pd.DataFrame(columns=columns)

#iterate through all the active buses and dis[play their latitude and longitude
for i in range (0, numberOfActiveBuses):
    df.loc[i,'Latitude'] = vehicleActivityArray[0]['VehicleActivity'][i] \
       ['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    df.loc[i,'Longitude'] = vehicleActivityArray[0]['VehicleActivity'][i] \
       ['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    df.loc[i,'Stop Status'] = vehicleActivityArray[0]['VehicleActivity'][i] \
        ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances'] \
        ['PresentableDistance']
    df.loc[i,'Stop Name'] = vehicleActivityArray[0]['VehicleActivity'][i] \
        ['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']

df.to_csv(args.OUTFILE)