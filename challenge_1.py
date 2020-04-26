# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE

# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
avg_empty_stocks = round (sum(d['num_docks_available'] for d in divvy_stations)/len(divvy_stations), 2)
print('There are {} empty docks at all stations in the system on average.'.format(avg_empty_stocks))
avg_avail_bikes = round (sum(d['num_bikes_available'] for d in divvy_stations)/len(divvy_stations), 2)
print('There are {} available bikes at all stations in the system on average.'.format(avg_avail_bikes))

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
ratio_of_bikes = sum(d['num_docks_available'] for d in divvy_stations)/(sum(d['num_docks_available'] for d in divvy_stations) + sum(d['num_bikes_available'] for d in divvy_stations))
print('There are {}% of the bikes that are currently rented in the stystem'.format(round(100*ratio_of_bikes,2)))
                                                                         

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%

for d in divvy_stations:  
          percentage = d['num_bikes_available']/(d['num_bikes_available']+d['num_docks_available'])  
          percentage = round(percentage*100, 2)
          d.update({'percent_bikes_remaining': '{}%'.format(percentage)})  