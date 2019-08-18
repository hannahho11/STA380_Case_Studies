STA380 Exercises
================

**Kevin Brill, Ananya Garg, Hannah Ho, Shane Kok**

Maybe a little intro here before we get into the code.

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

![](Case_HW_files/figure-markdown_strict/ABIA%20Arrivals-1.png) \#\#
Portfolio Modeling

Market Segmentation
-------------------

Author Attribution
------------------

Association Rule Mining
-----------------------
