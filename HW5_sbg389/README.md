#PUI 2016 HW 5

##Assignment I

Assignment 1: Comparisson of Tests for Goodness of fit

This notebook presents a series of tests in which we try to find if particular distributions (Gaussian and Poisson) are a sensible model for the age distribution of citibike drivers.

The notebook reuses a big portion of the data acquisition, transformations and plotting logic from fedhere's skeleton notebook for HW4.

The tests selected were X2 and Anderson-Darling

### Work Breakdown: 

Notebook skeleton by Sebastian Bania

Met and discussed the different tests and the data manipulation with Sofiya Elyukin, Jonathan D Geis, Luis Fernando Melchor Fernandez, Benjamin Joseph Alpert and Scott Smith

##Assignment II

Line fitting and data munging with income gender bias

This notebook presents a series a data analysis on the issue if income gender bias. The notebook uses the US census data to go thgough the initial data manipulation, descriptive phase, exploratory phase, fitting the data with a line using different techniques and finally buiding a model predict the woman income based on a given man invome value. 

### Work Breakdown: 

Most of the work on this notebook instance was done by Sebastian Bania. Luis Fernando Melchor Fernandez guided me with the use of the OLS technique providing me a detailed explanations of its theory and code that he used. My line fit for this particular method follows fernando's work.

I also used the following resrouce:

https://www.datarobot.com/blog/ordinary-least-squares-in-python/

##Assignment III

I worked on this assignment alone:

- Do diets help lose more fat than the exercise? 

Experimental setup: you have a test and a control sample.

$H_0$ The control group (P0) that excersised during the duration of the test loosed equal or more amount of fat than the test group (P1) that conducted a diet during the same period with a p = 0.05.

Delta_BodyFat = Final_BodyFat - Initial_BodyFat

$H_0$ Delta_Bodyfat(P0) => Delta_Bodyfat (p1), alfa=0.05

- Do American trust the president?

POLL RESULTS: On May 16, 1994, Newsweek reported the results of a public opinion poll that asked: “From everything you know about Bill Clinton, does he have the honesty and integrity you expect in a president?” (p. 23).
Poll surveyed 518 adults and 233, or 0.45 of them answered yes.

$H_0$ The number of polled people that considers that Bill Clinton has the honesty and integrity that they expect in a president (P0) is equal or greater than the number of polled people that dont (P1) with a p = 0.05.

$H_0$ P0 - P1 => 0, alfa=0.05

- Effectiveness of nicotine patches to quit smoking. 

Experimental setup: measure cessation rates for smokers randomly assigned to use a nicotine patch versus a placebo patch.

$H_0$ The number of smokers that quitted smoking and were using a non placebo patch (S0) is equal or lower than the number of smokers that didnt quit smoking and were using a non placebo patch (S1) ) with a p = 0.05.

$H_0$ P0 - P1 => 0, alfa=0.05

- Quantify the danger of smoking for pregnant women. 

Experimemtal setup: measure IQ of children at ages 1, 2, 3, and 4 years of age.

$H_0$ The average IQ for each group of ages 1,2,3 and 4 of kids with a smoking mother is the same or higher than the average IQ for each group of ages 1,2,3,4 of kids with a non smoking mother with a p = 0.05

$H_0$ Foreach age group x, AverageIQ(x)(Smoking_Mother) =>  AverageIQ(x)(Non_Smoking_Mother), alfa=0.05
