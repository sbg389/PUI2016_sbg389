#PUI 2016 HW 3

##This directory contains the HW3 deliverables, as defined in 

https://github.com/fedhere/PUI2016_fb55/tree/master/HW3_fb55

This HW assignment was done in collaboration with colleagues form the PUI2016 Thursday Night Class.
The corresponding attributions are specified on each of the following sections.

## Assignment 1:  Jupyter notebook that demonstrates visually in a data-driven way the Central Limit Theorem.

This deliverable provides a view of the central limit theorem by generating different types of random sized distirbutions and ploting the means against their size.

The general flow of the notebook follows:

1) GENERATE 100 samples of different sizes N (N>10 & N<2000) from each of 5 different distributions (500 samples in total), ## all with the same population mean. Include a Normal, a Poisson, a Binomial, a Chi-Squared distribution, and 1 more of your choice.

2) For each sample plot the sample mean (dependent var.) against the sample size N (independent var.) (if you want you can do it with 
the sample standard deviation as well).

3) Describe the behavior you see in the plots in terms of the law of large numbers.

4) PLOT the distributions of all sample means (together for all distributions). Mandatory: as a histogram. Optional: in any other way you think is convincing ## Extra Credit: FIT a gaussian to the distribution of means

### Work Breakdown: 

Mockup by Sebastian Bania. Peer refinements by 

Sofiya Elyukin
Jonathan D Geis
Luis Fernando Melchor Fernandez
Benjamin Joseph Alpert
Scott Smith

## Assignment 2: basic work for data-driven inference based on CitiBike data

This deliverable presents the initial steps of a data analysis using the Citibike Punblic Datasets.

The general flow of the notebook follows:

1) Fetch the Citibike Data from the AWS Blob and store a local copy

2) Use pandas to read in the local copy of the CitiBike files,into a DF

3) Display the top few rows of the DF in your notebook. This table must be rendered.

4) Display the reducted dataframe. This table must be rendered.

5) Plot the data distributions.

### Work Breakdown:

General idea and walk by Jonathan D Geis (presented to the group (Sebastian Bania, Sofiya Elyukin,Luis Fernando Melchor Fernandez, Benjamin Joseph Alpert )

Coding for this particular notebook instance by Sebastian Bania.

## Assignment 3: Notebook presenting the complete the z-test lab from lecture 3 

This notebook orgnizes the problem presented at the end of lecture two where we looked into the changes of a bus route and we tried to discern if the new route was in average more or less lengthy than the original one. 

The notebook presents a Null/alternative hypothesis statement and treatment, the adquisition of the data samples from the source file on a github repo, the z-test and an interpretation of the Z value obtainined and its relation with the Null Hypothesis.

### Work Breakdown:

This assignment was done mainly individually, following the available sample / guidance from the class material
