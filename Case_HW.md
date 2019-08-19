STA380 Exercises
================

**Kevin Brill, Ananya Garg, Hannah Ho, Shane Kok**

Below are the results of our team’s work on Dr. Scott’s STA380
Predictive Modeling exercises.

Visual Story Telling Part 1: Green Buildings
--------------------------------------------

    library(mosaic)

    green = read.csv('./data/greenbuildings.csv')

Visual Story Telling Part 2: Flights at ABIA
--------------------------------------------

    library(mosaic)
    library(tidyverse)

    month_arrival_avg=read.csv('./data/Month-Arrival-Avg.csv')
    month_dep_avg=read.csv('./data/Month-Departure-Avg.csv')

    months=c('1','2','3','4','5','6','7','8','9','10','11','12')

    ggplot(data = month_dep_avg) + 
      geom_col(mapping = aes(x = Month, y = DepDelay)) + 
      facet_wrap(~ UniqueCarrier, nrow = 5)+
      labs(title = "Carrier Average Departure Delays by Month")+
      scale_x_discrete(name='Month',limits=months)

![](Case_HW_files/figure-markdown_strict/ABIA%20Departures-1.png)

    ggplot(data = month_arrival_avg) + 
      geom_col(mapping = aes(x = Month, y = ArrDelay)) + 
      facet_wrap(~ UniqueCarrier, nrow = 5)+ 
      labs(title = "Carrier Average Arrival Delays by Month")+
      scale_x_discrete(name='Month',limits=months)

![](Case_HW_files/figure-markdown_strict/ABIA%20Arrivals-1.png)

Portfolio Modeling
------------------

Market Segmentation
-------------------

Author Attribution
------------------

Our analysis of the author text data consisted of the following
framework:

**1. Preprocessing of the training set**

**2. Preprocessing of the test set**

**3. Organization of training and testing variables (feature matrices
and target vectors)**

**4. PCA setup to allow for dimension reduction during modeling**

**5. Modeling and results**

Below, we dive into our processes for each of the above items.

### PREPROCESSING OF THE TRAINING SET

This section contains the bulk of the work done for this problem.

Association Rule Mining
-----------------------

    library(tidyverse)
    library(arules)  # has a big ecosystem of packages built around it
    library(arulesViz)
    library(igraph)
    setwd("~/Grad School/Summer/Predictive Modeling/Second_Half/Homework/STA380_Case_Studies")
    #read .txt file in basket format
    groceries = read.transactions("./data/groceries.txt", format="basket", sep=",")

    ## Cast this variable as a special arules "transactions" class.
    transactions = as(groceries, "transactions")

    #run the apriori algorithm
    apriori_results = apriori(transactions, parameter=list(support=.01, confidence=.5, maxlen=3))

    ## Apriori
    ## 
    ## Parameter specification:
    ##  confidence minval smax arem  aval originalSupport maxtime support minlen
    ##         0.5    0.1    1 none FALSE            TRUE       5    0.01      1
    ##  maxlen target   ext
    ##       3  rules FALSE
    ## 
    ## Algorithmic control:
    ##  filter tree heap memopt load sort verbose
    ##     0.1 TRUE TRUE  FALSE TRUE    2    TRUE
    ## 
    ## Absolute minimum support count: 98 
    ## 
    ## set item appearances ...[0 item(s)] done [0.00s].
    ## set transactions ...[169 item(s), 9835 transaction(s)] done [0.00s].
    ## sorting and recoding items ... [88 item(s)] done [0.00s].
    ## creating transaction tree ... done [0.00s].
    ## checking subsets of size 1 2 3 done [0.00s].
    ## writing ... [15 rule(s)] done [0.00s].
    ## creating S4 object  ... done [0.00s].

    #view results
    inspect(apriori_results)

    ##      lhs                     rhs                   support confidence     lift count
    ## [1]  {curd,                                                                         
    ##       yogurt}             => {whole milk}       0.01006609  0.5823529 2.279125    99
    ## [2]  {butter,                                                                       
    ##       other vegetables}   => {whole milk}       0.01148958  0.5736041 2.244885   113
    ## [3]  {domestic eggs,                                                                
    ##       other vegetables}   => {whole milk}       0.01230300  0.5525114 2.162336   121
    ## [4]  {whipped/sour cream,                                                           
    ##       yogurt}             => {whole milk}       0.01087951  0.5245098 2.052747   107
    ## [5]  {other vegetables,                                                             
    ##       whipped/sour cream} => {whole milk}       0.01464159  0.5070423 1.984385   144
    ## [6]  {other vegetables,                                                             
    ##       pip fruit}          => {whole milk}       0.01352313  0.5175097 2.025351   133
    ## [7]  {citrus fruit,                                                                 
    ##       root vegetables}    => {other vegetables} 0.01037112  0.5862069 3.029608   102
    ## [8]  {root vegetables,                                                              
    ##       tropical fruit}     => {other vegetables} 0.01230300  0.5845411 3.020999   121
    ## [9]  {root vegetables,                                                              
    ##       tropical fruit}     => {whole milk}       0.01199797  0.5700483 2.230969   118
    ## [10] {tropical fruit,                                                               
    ##       yogurt}             => {whole milk}       0.01514997  0.5173611 2.024770   149
    ## [11] {root vegetables,                                                              
    ##       yogurt}             => {other vegetables} 0.01291307  0.5000000 2.584078   127
    ## [12] {root vegetables,                                                              
    ##       yogurt}             => {whole milk}       0.01453991  0.5629921 2.203354   143
    ## [13] {rolls/buns,                                                                   
    ##       root vegetables}    => {other vegetables} 0.01220132  0.5020921 2.594890   120
    ## [14] {rolls/buns,                                                                   
    ##       root vegetables}    => {whole milk}       0.01270971  0.5230126 2.046888   125
    ## [15] {other vegetables,                                                             
    ##       yogurt}             => {whole milk}       0.02226741  0.5128806 2.007235   219

    inspect(subset(apriori_results, subset=lift > 2))

    ##      lhs                     rhs                   support confidence     lift count
    ## [1]  {curd,                                                                         
    ##       yogurt}             => {whole milk}       0.01006609  0.5823529 2.279125    99
    ## [2]  {butter,                                                                       
    ##       other vegetables}   => {whole milk}       0.01148958  0.5736041 2.244885   113
    ## [3]  {domestic eggs,                                                                
    ##       other vegetables}   => {whole milk}       0.01230300  0.5525114 2.162336   121
    ## [4]  {whipped/sour cream,                                                           
    ##       yogurt}             => {whole milk}       0.01087951  0.5245098 2.052747   107
    ## [5]  {other vegetables,                                                             
    ##       pip fruit}          => {whole milk}       0.01352313  0.5175097 2.025351   133
    ## [6]  {citrus fruit,                                                                 
    ##       root vegetables}    => {other vegetables} 0.01037112  0.5862069 3.029608   102
    ## [7]  {root vegetables,                                                              
    ##       tropical fruit}     => {other vegetables} 0.01230300  0.5845411 3.020999   121
    ## [8]  {root vegetables,                                                              
    ##       tropical fruit}     => {whole milk}       0.01199797  0.5700483 2.230969   118
    ## [9]  {tropical fruit,                                                               
    ##       yogurt}             => {whole milk}       0.01514997  0.5173611 2.024770   149
    ## [10] {root vegetables,                                                              
    ##       yogurt}             => {other vegetables} 0.01291307  0.5000000 2.584078   127
    ## [11] {root vegetables,                                                              
    ##       yogurt}             => {whole milk}       0.01453991  0.5629921 2.203354   143
    ## [12] {rolls/buns,                                                                   
    ##       root vegetables}    => {other vegetables} 0.01220132  0.5020921 2.594890   120
    ## [13] {rolls/buns,                                                                   
    ##       root vegetables}    => {whole milk}       0.01270971  0.5230126 2.046888   125
    ## [14] {other vegetables,                                                             
    ##       yogurt}             => {whole milk}       0.02226741  0.5128806 2.007235   219
