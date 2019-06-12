### Project Overview

 # Data Visualization using Matplotlib

Problem Statement

The Olympic Games, considered to be the world's foremost sports competition has more than 200 nations participating across the Summer and Winter Games alternating by occurring every four years but two years apart.

We want to know as to what happens during an IPL match which raises several questions in our mind with our limited knowledge about the game called cricket on which it is based. This analysis is done to know as which factors led one of the team to win and how does it matter.


### Learnings from the project

 After completing this project, I became comfortable using:

Dataframe operations

Conditional statement and loops

List operations

Bar Plotting

Mathematical operations


### Approach taken to solve the problem

 Loaded the dataset and renamed some columns.

Used conditional filtering and created two variables and saved the content in it to see which season there are better performer ex: Summer or Winter

Created new dataframe with only country names and medals earned when it was summer, winter and both and dropped countries column. Defined a function which takes in any dataframe as a parameter and returns only 10 largest strings from the list. Ran the function on three different dataframes created before and printed common countries from three variables.

Plotted top 10 country names vs total medals for the three dataframes created in the above i.e summer, winter and total. 

Created a new column in all the three dataframes and subsetted data using iloc to print highest counts and country associated to that value extracted.

Dropped a column and saved in a new dataframe and updated based on few mathematical calculations for Gold, Sliver and Bronze medals.

Plotted a stacked bar plot for medals earned. 


