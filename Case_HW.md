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

**3. PCA setup to allow for dimension reduction during modeling**

**4. Modeling and results**

**5. Further considerations**

Below, we dive into our processes for each of the above items.

##### 1. PREPROCESSING OF THE TRAINING SET

This section contains the bulk of the work done for this problem. We
began by reading in the raw .txt files and extracting a list of all
documents and a list of all author names in the training set. We then
used the list of .txt files to construct the corpus for our problem.
From this corpus, we convert all letters into lower case, remov all
numbers; punctuation; and whitespaces, and delete all occurances of
words that are contained in R’s “SMART” stopwords dictionary. With the
corpus fully cleaned, we create a DTM out of the corpus and remove all
words that appear in only 2.5% of documents or fewer. In doing so, we
guarantee that these rare words won’t be given excessive weight in our
models and skew our results. Finally, we replace the contents of our DTM
with the TF-IDF weights of each word rather than simply their counts.

##### 2. PREPROCESSING OF THE TEST SET

In this section, we follow the same processes of the above section on
the test set of documents, all the way up until we create the DTM. Here,
we limit the dictionary of the test set’s DTM to the words contained in
the training set’s DTM dictionary. In doing so, we ensure that both the
training and testing sets’ DTMs consist of the same set of columns when
we begin modeling. Finally, we replace the contents of the test DTM with
the TF-IDF weights of each word (same as above section).

##### 3. PCA SETUP TO ALLOW FOR DIMENSION REDUCTION DURING MODELING

Here, we find the PCAs of the training and testing sets. We find that
the first 600 principal components explain ~80% of the variance in the
training set so we proceed with the first 600 principal components.

##### 4. MODELING AND RESULTS

We obtain results for variations of two types of models: KNN and Random
Forest. The prediction accuracies for each variant are listed below:

**KNN with cosine distance:** 55.24% **KNN with cosine distance of first
600 principal components:** 58.08% **Random Forest:** 60.48% **Random
Forest on first 600 principal components:** **Random Forest with
m=sqrt(p):** 62.36%

As can be seen from the results above, our random forest model with
m=sqrt(p)=37 and no dimensionality reduction yielded the best
classification accuracy at 62.36% of articles attributed to the correct
author.

##### 5. FURTHER CONSIDERATIONS

Our team tried to use Naive Bayes and BART to classify the articles, but
ran into errors that took too long to debug before the deadline of this
assignment. It is likely that these modeling techniques would outperform
our above models.

Further, the best way to improve our classification accuracies would be
to have more robust preprocessing. For example, we could create a dummy
“unknown” variable in our test DTM that would count the number of words
that show up in our test set that didn’t appear in our training set. Our
above test DTM simply ignore new words in the test set, which likely
decreases performance. We could also consider n-gram groupings of words
for more nuanced TF-IDF values in our DTMs.

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
    ## set transactions ...[169 item(s), 9835 transaction(s)] done [0.01s].
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
