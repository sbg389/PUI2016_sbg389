#PUI 2016 HW 4

##Assignment I

On this assignment I did a peer review of the HW3 Citibike assignment for Chen Chongyang (cc5502), The assignment can be found at

https://github.com/sbg389/PUI2016_cc5502/blob/master/HW3_cc5022/CitibikeReview_sbg389.md

I worked on this assignment alone.

##Assignment II

This assignment looks at reviewing the chocices for satistical tests in schentiic literature. Two types of tests will be choosen from the  A. Marengo CSU "When to use what test?" document
(http://www.csun.edu/~amarenco/Fcs%20682/When%20to%20use%20what%20test.pdf)

I worked on this assignment with Sofiya Elyukin, each of us focused on one test and its corresponding journal artcile, shared the basic idea and refined it with each other.

###a. Selection of the tests.

I looked at the t-test:

The t-test looks at differences between two groups on some variable of interest, and the independet variable should have only two groups
E.G. (male/female, undergrad/grad): Do males and females differ in the amount of hours they spend shopping in a given month?

Sofiya looked at the path analysis for relationships between dependent and independent variables.

###b. Search for journal papers that uses the selected statistical tests )

The paper selected for the t-test analysis is "Does Cognitive Function Increase over Time in the Healthy Elderly?"

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078646

In this particular paper, the t-score is used to compare the independent variable "Mean cognitive test score" for different groups

The paper selected for the path analysis is "Impact of Maternal Death on Household Economy in Rural China: A Prospective Path Analysis" 

http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134756 

###c. 

####Table I: t-test

| **Statistical Analyses	|  IV(s)  |  IV type(s) |  DV(s)  |  DV type(s)  |  Control Var | Control Var type  | Question to be answered | _H0_ | alpha | link to paper **| 
|:----------:|:----------|:------------|:-------------|:-------------|:------------|:------------- |:------------------|:----:|:-------:|:-------|
T-Test	|  1, Cohorts | Categorical | 1, Mean Cognitive test Score| interval | ---- | ---- | Does Cognitive Function Increase across generations for healthy elder? | Mean Score in Cohort 2001 <= Mean Score in Cohort 2001 | 0.05 | http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0078646 
|
  |||||||||
 
####Table II: Path Analysis

| **Statistical Analyses      | IV(s)    | IV type(s)  | DV(s)  | DV type(s)  | Control Var  | Control Var type |  Question to be answered | _H0_ | alpha | link to paper** |
|:--------------:|:--------------:|:------:|:---------:|:-----------:|:-----------:|:------------:|:------------------:|:-------:|:---------:|:---------|
Path Analysis (1)  |  **True IV**: maternal death; **Mediators**: direct costs, postitive coping, negative coping, husband remarried, newborn alive | **True IV**: categorical; **Mediators**: continuous, continuous, continuous, categorical, categorical | annual income | continuous | n/a | n/a | How does maternal death impact household economy? | Maternal death has no affect on the family's income    |     | [Impact of Maternal Death on Household Economy in Rural China: A Prospective Path Analysis] (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134756) |
Path Analysis (2)  |  **True IV**: maternal death; **Mediators**: direct costs, postitive coping, negative coping, husband remarried, newborn alive | **True IV**: categorical; **Mediators**: continuous, continuous, continuous, categorical, categorical | expenditure per capita | continuous | n/a | n/a | How does maternal death impact household economy? | Maternal death has no affect on the family's expenditure per capita  |     | [Impact of Maternal Death on Household Economy in Rural China: A Prospective Path Analysis] (http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0134756) |
 |||||||||||||||||||||

##Assignment III

On this assignment I reproduced the analysis of the Hard to Employ programs for NY. The notebook is https://github.com/sbg389/PUI2016_sbg389/blob/master/HW4_sbg389/HW4_Prission.ipynb

For this assignment I worked with Sofiya Elyukin and Marc Edward Toneatto, we met and did the calculations individually and later shared and discussed the results.

##Assignment IV

On this assignment I worked with the skeleton notebook provided by federica (https://github.com/fedhere/PUI2016_fb55/blob/master/HW4_fb55/citibikes_compare_distributions.ipynb) to perform a series of tests to assess correlation between 2 samples of citibike data. In particular

  Pearson’s test
  Spearman’s test
  K-S test

For this assignment I discussed part of the solution with Sofiya Elyukin

