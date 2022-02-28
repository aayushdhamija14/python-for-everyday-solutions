"""
Script to identify how many times thanos needs to snap to destroy all the population of your country on selected year
"""

# imports libraries
import requests

# taking user input for the country the want to check and the year
user_country = input("Enter your country name: ")
user_year = input("Enter the year you want to check in YYYY format: ")

# query the API to get country population information
response = requests.post(url="https://countriesnow.space/api/v0.1/countries/population",json={
	"country": user_country
}).json()

if response['data']['populationCounts'] is not None:
  
  # initializing variables
  population = 0
  snap_count = 0

  for year in response['data']['populationCounts']:
    if str(year['year']) == user_year:
      population = year['value']

  if population == 0:
    print("Sorry the year data is not available on the API")
  else:
    # logic to calculate number of snaps
    while population > 1:
      snap_count = snap_count + 1
      population = int(population/2)

  print(snap_count)

else:
  print("No response is from API. Check the input params")
