# World Development 2007
## About this Project
This data science project provides a scatter plot diagram on country development based on their GDP and life expectancy.  There are also variables that contain conditions to subset the data.
## The Data
![scatter plot](https://i.imgur.com/BoDYbCs.png)
Each blue dot on the diagram represents a country. The larger the dot, the higher the population of that country. The diagram illustrates that generally if a country has a higher GDP, their population lives longer. It also shows a majority of higher populated countries have a middle to high GDP over the smaller countries.

Using the low_dev and high_dev variables, we're able to subset the data and find which countries are considered low and high developed based on GDP and life expectancy conditions. Based on those conditions, there are 56 low developed countries and 40 high developed countries in the data frame.
## How it Works
To begin, the pandas library allows the CSV file to be read. Dataframe variables are created to correspond with the relevant columns within the CSV file. Using the matplotlib library, a scatter plot diagram is created to visualise the data. The life_exp and gdp variables are used in the diagram, the pop variable dictates the size of each country's dot on the diagram. Custom labels and ticks allow the diagram to be understood by the reader.

Finally, there are conditional variables for low and high developed countries that allow the data to be subset and categorised accordingly to those conditions.
