STA380 Exercises
================

**Kevin Brill, Ananya Garg, Hannah Ho, Shane Kok**

Below are the results of our team’s work on Dr. Scott’s STA380
Predictive Modeling exercises.

Visual Story Telling Part 1: Green Buildings
--------------------------------------------

![](Case_HW_files/figure-markdown_strict/GreenBuilding-1.png)![](Case_HW_files/figure-markdown_strict/GreenBuilding-2.png)
Class ‘A’ green status buildings charge lower mean rents per square
foot, implying that green status is not correlated with premium rates
when compared with buildings of a similar class. It might look like
class c green buldings can charge a higher rent. However, there are so
few class b and c green buildings in the dataset that the premium is
unlikely to carry statistical significance.

Given that there is no premium for green status after holding class
constant and most green buildings are class ‘A’ buildings, we will
investigate whether there is a premium charged for class ‘A’ buildings.
![](Case_HW_files/figure-markdown_strict/green2-1.png) Most class ‘A’
buildings are not located in particularly expensive cluster rents. This
means that the apparent premium on green buildings are not coming from
being located in nicer areas as signalled by having higher rents
overall. ![](Case_HW_files/figure-markdown_strict/green3-1.png) green
buildings have a higher rent across all kinds of cooling days (barring
1000-2000 days), so we can conclude that no of cooling days does not
contribute to the rent of the building
![](Case_HW_files/figure-markdown_strict/green4-1.png) From the graph we
see that green\_rated buildings charga a higher rent when:

1.  The no of heating degree days are low, implying that the region is
    hot, or warm enough to not require heating.

2.  The no of heating degree days are high, implying that there is a
    need for heating on most days. This implies that the savings in
    energy costs are higher than the rent of a green building

In places with heating degree days between 2000-5000, green buildings
are in fact commanding a lower rent One reason for this could be that
for places which are moderately cold, the savings in energy costs are
higher than the rent of a green building. We need to check with the
total no of degree days to further understand the correlation between
these phenomenon. ![](Case_HW_files/figure-markdown_strict/green5-1.png)
We can now confidently say that (a) in places that have less than 5000
degree days (moderate temperatures) and (b) places that have more than
8000 degree days (extreme temperatures), green buildings charge a higher
rent. For (b), we can hypothesise the reason for higher rent is the
savings in energy costs. We will not hold the degree days constant and
check if there is another feature that can attributed to the variation
in rent.

Feature 1: class of the building

It is possible that because buildings with degree days &gt; 2000 are
better built, and hence charge a premium rent
![](Case_HW_files/figure-markdown_strict/green6-1.png)![](Case_HW_files/figure-markdown_strict/green6-2.png)
This is telling us for sure that there is a higher rent asscociated with
a green building, if it is class\_a and in an area with degree days &gt;
8000 ![](Case_HW_files/figure-markdown_strict/green7-1.png)

Once again, we see that the number of buildings is too low class\_c, to
understand if the green premium significant enough. So from the next
graph, we take a look at only the class A and B buildings
![](Case_HW_files/figure-markdown_strict/green8-1.png) This too assures
us that there is a green premium for areas with 2000-3000 degree days
![](Case_HW_files/figure-markdown_strict/green1-1.png)![](Case_HW_files/figure-markdown_strict/green1-2.png)![](Case_HW_files/figure-markdown_strict/green1-3.png)![](Case_HW_files/figure-markdown_strict/green1-4.png)
Within class ‘A’ buildings, investing in a green building is not
associated with being able to charge higher rents. However, we see that
the no. of degree days is correlated with the green premium on the rent.
In all areas with greater than 2000 degree days, we see that across the
class of the buildings (wherever significant/relevant), the rent is
higher for green\_rated buildings. Hence we should invest in a green
building if they are going to be built in areas with a high number of
degree days (&gt;2000), ie areas with extremes of temperature.
Conversely, do not invest in green buildings if they are located in
areas with moderate weather.

Visual Story Telling Part 2: Flights at ABIA
--------------------------------------------

![](Case_HW_files/figure-markdown_strict/ABIA%20Departures-1.png)

![](Case_HW_files/figure-markdown_strict/ABIA%20Arrivals-1.png)

Our visualizations depict the average monthly arrival and departure
delays, in terms of minutes, for all the airlines that fly into the
Austin Airport. Therefore, it shows which airlines are the best for
flying into and departing the Austin Airport, for a specific month, if
you want to minimize your chance of delays.

Portfolio Modeling
------------------

![](Case_HW_files/figure-markdown_strict/ETF%20Output-1.png)

VaR stands for value at risk, and this metric shows the risk of loss for
an investment on a distribution. We calculated the VaR distribution for
three different types of portfolios were tested for our portfolio
modeling: a balanced, an aggressive, and a conservative portfolio.

The aggressive portfolio is composed of small cap growth stock ETF’s,
which means that it is focused on smaller stocks with potential. This is
more risky because small cap companies have a larger chance of going
under and are less stable than their large cap stock counterparts. As
expected, the 5% VaR for the aggressive portfolio is the worst and is
-$8000.

The conservative portfolio is mainly made up of different types of bond
and money market ETF’s, which are one of the safest types of investments
you can make on the financial market. Many of these are either mortgage
or government backed bonds, therefore they are collateralized and this
limits your risk significantly. The 5% VaR for the conservative
portfolio is the best and is only -$1000.

The balanced portfolio contains a wide range of financial products from
across the spectrum. These products contain ETF’s from a wide range of
industries, such as oil and real estate. This spectrum of different
industries helps to balance out the portfolio, and mostly Vanguard
products were chosen for their strong returns and good past performance,
in order to help balance out the risk of this portfolio. A healthcare
ETF is super stable as well, which is why one of these ETF’s was
included in the portfolio too. The 5% VaR for the balanced portfolio is
about -$5000.

The VaR distributions for each portfolio came out as expected, with the
conservative portfolio being the least risky and the aggressive
portfolio being the most.

Market Segmentation
-------------------

    ## [1] "school"        "food"          "parenting"     "religion"     
    ## [5] "sports_fandom"

    ## [1] "religion"         "food"             "outdoors"        
    ## [4] "personal_fitness" "health_nutrition"

    ## [1] "school"        "photo_sharing" "cooking"       "beauty"       
    ## [5] "fashion"

    ## [1] "food"           "tv_film"        "sports_playing" "online_gaming" 
    ## [5] "college_uni"

    ## [1] "home_and_garden" "crafts"          "eco"             "current_events" 
    ## [5] "photo_sharing"   "shopping"

    ## [1] "sports_playing" "family"         "online_gaming"  "shopping"      
    ## [5] "photo_sharing"  "automotive"

    ## [1] "music"      "art"        "tv_film"    "news"       "automotive"

    ## [1] "travel"  "family"  "food"    "cooking" "music"

    ## [1] "outdoors"       "dating"         "business"       "small_business"
    ## [5] "music"

    ## [1] "music"           "dating"          "eco"             "current_events" 
    ## [5] "home_and_garden"

    ## [1] "art"             "home_and_garden" "current_events"  "family"         
    ## [5] "business"

    ## [1] "dating"         "crafts"         "current_events" "music"

    ## [1] "business"       "small_business" "family"         "current_events"
    ## [5] "eco"

    ## [1] "art"             "home_and_garden" "music"           "business"       
    ## [5] "eco"

    ## [1] "eco"             "family"          "small_business"  "home_and_garden"
    ## [5] "business"        "crafts"

The following market segments were identified from our principal
component analysis of the Twitter social marketing data:

1.  parents

2.  active and healthy individuals

3.  young females in school or young mothers

4.  young male students

5.  young homemakers

6.  young fathers

7.  teenagers or young adults

8.  millennials

9.  budding entrepreneurs

10. hippies

11. artistic business people

Further segments were developed, but they did not representative of any
new market segments. These segments were created based on topics of
interest from their tweets. The R code comments have identified
groupings of significant topics that most explain the above categories
that we have developed.

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

**KNN with cosine distance:** 55.24%

**KNN with cosine distance of first 600 principal components:** 58.08%

**Random Forest:** 60.48%

**Random Forest on first 600 principal components:** 55.28%

**Random Forest with m=sqrt(p):** 62.36%

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

The output of the apriori algorithm on the groceries.txt file is shown
below:

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

The above output shows the results of the apriori algorithm with the
following parameters:

support = 0.01

confidence = 0.5

lift &gt; 2

This means that for each association rule, X =&gt; Y, at least 1% of all
baskets contain X and Y and 50% of all baskets that contain X also
contain Y. Finally, setting lift &gt; 2 strengthens our association
rules by accounting for the conditional probabilities between X and Y.

From our above association rules, we see that people who buy various
combinations of fruits, vegetables, and dairy products also tend to buy
whole milk and other vegetables. It makes sense that people who buy
healthy foods would tend to also buy whole milk because there are many
organizations that recommend adults to drink up to 3 cups of milk a day
(livestrong.com and americanbonehealth.org). Thus, it appears that
people who care enough about their health to eat plenty of fruits and
vegetables also care enough about their health to drink plenty of milk.
