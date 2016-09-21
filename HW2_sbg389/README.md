#PUI 2016 HW 2

##This directory contains the HW2 deliverables

This HW assignment was done in collaboration with colleagues form the PUI2016 Thursday Night Class.
The corresponding attributions are specified on each of the following sections.

## Assignment 1:  tracking each vehicle for a line

The deliverable for this assignment is a Python script that retrieves and displays information about active vehicles for a given bus line.

The script uses the MTA Bus Time Developer API (http://bustime.mta.info/wiki/Developers/Index) and receives two parameters:

    The API Key (necessary to make calls agains the service)
    The Bus Line itself

The API is based on the SIRI Standard (Service Interface for Real Time Information http://user47094.vs.easily.co.uk/siri/).
In order to obtain the specific information that is needed to craft the desired script output, both the SIRI documentation and POSTMAN were used. (https://www.getpostman.com/)
    
    Example:
    
        python show_bus_locations.py xxxx-xxxx-xxxx-xxxx B62
        
        Bus Line: B62
        Number of Active Buses: 9
        Bus 0 is at latitude 40.729862 and longiture -73.954117
        Bus 1 is at latitude 40.707503 and longiture -73.959922
        Bus 2 is at latitude 40.707408 and longiture -73.959968
        Bus 3 is at latitude 40.730361 and longiture -73.95429
        Bus 4 is at latitude 40.707464 and longiture -73.960538
        Bus 5 is at latitude 40.701746 and longiture -73.963551
        Bus 6 is at latitude 40.690353 and longiture -73.98797
        Bus 7 is at latitude 40.701516 and longiture -73.963838
        Bus 8 is at latitude 40.690899 and longiture -73.989258

The script implementation is relatively simple, and it mainly relies on three libraries:

     argparse (https://docs.python.org/2/library/argparse.html)
     json (https://docs.python.org/2/library/json.html)
     urllib2 (https://docs.python.org/2/library/urllib2.html)
    
These packages provide clases and methods for handling Arguments, JSON enconding and making HTTP requests, two mechanisms that are  at the center of the interaction with the MTA API.

The script flow follows:

    -Import the required packages
    -Parse the arguments from the script
    -Build the URL using the known MTA API method and parameters (passed as script arguments)
    -Invoke the api using the urllib2.urlopen method.
    -Encode the response into a JSON object using the json.loads method
    -Iterate through the response, fetch the desired elements and print using the desired format
    
### Work Breakdown: 

Mockup by Sebastian Bania. Peer refinements by 

Sofiya Elyukin
Jonathan D Geis
Luis Fernando Melchor Fernandez

## Assignment 2: next stop information

The deliverable for this assigment builds upon the previous assignment, but in this case, the output will be written to a csv file.

The script shares the first two parameters with the previous, but adds a third parameter that is used to specify the output file location.

I choose to use a pandas Data Frame to store and format the results from the API and write the csv.

    The API Key (necessary to make calls agains the service)
    The Bus Line itself
    The location of the csv file
    
    Example: 
    
        python get_bus_info.py xxxx-xxxx-xxxx-xxxx B62 B62.csv
        
        CSV Output:
        
        Latitude,Longitude,Stop Name,Stop Status
        40.714593,-73.961191,BEDFORD AV/GRAND ST,at stop
        40.723781,-73.950797,MANHATTAN AV/NASSAU AV,approaching
        40.69602,-73.986602,JAY ST/TILLARY ST,approaching
        40.749103,-73.939623,28 ST/QUEENS PZ S,approaching
        40.701974,-73.963196,WYTHE AV/KEAP ST,approaching
        40.693796,-73.987201,JAY ST/WILLOUGHBY ST,< 1 stop away
        40.738108,-73.952888,JACKSON AV/11 ST,< 1 stop away

The script, buils upon the previous script, adding the pandas library, that is used mainly to store the data and output to CSV:

     pandas (http://pandas.pydata.org/)
    
Pandas provides high-performance, easy-to-use data structures and data analysis tools. We will specifcally use the dataframe structure and its native capabilities to export to csv

The script flow follows:

    -Import the required packages
    -Parse the arguments from the script
    -Build the URL using the known MTA API method and parameters (passed as script arguments)
    -Invoke the api using the urllib2.urlopen method.
    -Encode the response into a JSON object using the json.loads method
    -Iterate through the response, fetch the desired elements and add them to a pandas dataframe
    -Use the dataframe.to_csv
    
### Work Breakdown:

Mockup by Sebastian Bania. Peer refinement, handling empty values and output formatting by 

Sofiya Elyukin
Jonathan D Geis
Luis Fernando Melchor Fernandez

## Assignment 3 and Extra Credit Assignment: Read CSV files with pandas, work with dates in Pandas

The deliverable for this assignment is a jupyter notebook ( HW2_sbg389.ipynb) that uses two different datasets from the CUSP data facility that matched the requirements from the assignment:

- The Energy and Water Data Disclosure for Local Law 84 (2012) (https://datahub.cusp.nyu.edu/dataset/5gde-fmj3)
- The Wathershed Quality Data (https://datahub.cusp.nyu.edu/dataset/y43c-5n92)

The notebook uses pandas dataframes in order to read the csv formatted datasets (directly from the CUSP data facility), manipulate its content and plot it.

In the case of the second dataset, where we have to manipulate the string representation of dates and convert them to date objects (so pandas can plot them adequately) I used the dataframe.to_datetime method

### Work Breakdown:

General idea and walk through by Luis Fernando Melchor Fernandez (presented to the group (Sebastian Bania, Sofiya Elyukin Jonathan D Geis)

Coding for this particular notebook instance Sebastian Bania.
