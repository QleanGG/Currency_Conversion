import requests
from datetime import datetime
import time

"""
My program will use the currency Conversion and Exchange Rates api for realtime Euro display from rapidapi
If the call will not be succesful, the program will try again until it gets an answer

After searching multiple APIs, I chose the currency conversion from rapid api as it was one of the most reliable and recommended sources for conversion rates.
"""

#declaring variables
rate_save = [] #saves every fetch call
seconds_in_hour = 3600 
hours_in_day = 24

def fetch_euro():
    #defining the URL 
    url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/latest" #api url from rapidapi

    querystring = {"from":"EUR","to":"ILS"} #currency conversion request

    headers = {
	"X-RapidAPI-Key": "f365f42499msh34b56dfc79114ecp157cf2jsn1f00e00dba4b", #my rapidapi key
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com" #The api host 
    }


    try:
        #calling the api
        response = requests.get(url, headers=headers, params=querystring) 
        if response.status_code == 200: #checking if I got a succesfull answer from the server
            rates= response.json()
            conversion_rates = rates["rates"]["ILS"]
            return conversion_rates
        else: 
            #recursively calling the function until I get a succesfull response
            print('didnt get a response from server, trying again')
            return fetch_euro()


    except Exception as e:
        #recursively calling the function until I get a succesfull response
        print('Error:', e)
        print('trying again')
        return fetch_euro()


def fetch_hourly(rate_save):
    for i in range(hours_in_day):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_rate = fetch_euro()
        
        #saving the rate for this hour
        rate_save.append({"current_rate":current_rate,"current_time":current_time})
        print(f'The conversion rate of Euro to Shekels for the time: {current_time} is ₪{current_rate}')
        time.sleep(seconds_in_hour)


def main(rate_save):
    fetch_hourly(rate_save)
    #after the function is done, displaying all hourly calls
    print('the rate for the last 24 hours was:')
    for hourly_rate in rate_save:
        print(hourly_rate)

# starting the program
if __name__ == '__main__':
    main(rate_save)