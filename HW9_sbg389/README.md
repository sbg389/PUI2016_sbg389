#PUI 2016 HW 9

##This directory contains the HW9 deliverables, as defined in

https://github.com/fedhere/PUI2016_fb55/blob/master/HW9_fb55/subway_timeseries_instructions.ipynb

This HW assignment was done in collaboration with colleagues form the PUI2016 Thursday Night Class.
The corresponding attributions are specified on each of the following sections.

## Assignment 1:  Jupyter notebook presenting a time series analysis with the MTA turnstile data

The goal of this analysis is to find outliers, trends and periodicity in the MTA turnstile data.
The dataset used contains weekly data for 600 Manhattan stations for each of the 23 different subway cards. This dataset was organized by Sina Kashuk (srk325(at)nyu.edu) at CUSP.

There are three parts to the analysis:

#### Analysis I: Event Detection
The first part of the analysis will attempt to identify the most prominent event. This event is defined as a very significant drop (>3-sigma) in all time series. The general flow of this part follows:

1) Sum the timeseries for all stations and fares (we are looking fpr an event that we know is common to all time series)
2) Identifying the event: Take the mean and standard deviation and find points that deviate from the mean by more than 3 standard deviations.
3) Get the date for the event and try to explain what it might be related to

#### Analysis II: Trend Analysis
The second part of the analysis will attempt to identify trends on the ridership types. In particular, those ridership types that have either steadily increased or decreased in popularity. We will try to quantify those changes by calculating the ratio of ussage between the first 10 and last 10 weeks. The general flow of this part follows:

1) Sum the time series for all stations (we are going to be evaluating the time series for each of the different types of fares)
2) Visually explore the data (plot all the time series)
3) Filter: if the time series is continuous (doesnt have weeks with 0 rides) this seems to us a good criteria to rule out upfront things that wont steaditly increase or decrease
4) Idenitfy and present the one that increased the most and the one that decreased the most


#### Analysis 3: Trend Analysis
The third part of the analysis will attempt to identify the five stations that show the most prominent periodic trend on an anual period. We will attempt to explain the reason for this periodic peak

1) Collapse the fare types dimension of the cube (we care about stations here!)
2) Visually inspect all the stations plotting their power spectrum (excluding the first two elements on the X)
3) Create a dictionary to store the frequency bin centers in cycles per week (X Axis) and the Fourier Transform value (Y) for eac of the stations
4) Explore the frequency bins and select the one more appropiate for the year periodicity analysis
5) Based on that bin, get the stations with the higher values for the relevant bin
6) Visualize the power spectrum only for those five stations (cleaner chart!)
7) Visualize the number of  station swipes and dates to try to find possible events that explain the preiodicity
8) Refine the visualization (three stations, one year period)
9) Try to exaplin the observed phenomena


### Work Breakdown: 

Discussion on Analysis I, II and III and draft notebook review with  

Sofiya Elyukin
Jonathan D Geis
Luis Fernando Melchor Fernandez
Benjamin Joseph Alpert
Scott Smith

Current instance of the notebook written by Sebastian Bania, except plot_rtype function, written as part of the general group discussion by Scott Smith.

