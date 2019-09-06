


# importing required libraries 
import requests, json 
  
# enter your api key here 
api_key ="AIzaSyCDVbeY90ttdf0opw7MImDBfIQgrcNensw" #generated API key
  
# Take source as input 
source = input("Enter Startpoint : ") 
  
# Take destination as input 
dest = input("Enter Endpoint : ") 
  
# url variable store url  
url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
  
# Get method of requests module 
# return response object 
r = requests.get(url + 'origins = ' + source +
                   '&destinations = ' + dest +
                   '&key = ' + api_key)
print(r)
# return json format result 
x = r.json() 
 
  
# print the vale of x 
print(x)




#Second Method



# importing googlemaps module

import googlemaps #pip install googlemaps

# Requires API key 
gmaps = googlemaps.Client(key='') 

# Requires cities name 
dist = gmaps.distance_matrix('Delhi','Mumbai')['rows'][0]['elements'][0] 

# Printing the result 
print(dist)


