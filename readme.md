# Euro to Shekel Currency Conversion App

This Python application fetches real-time conversion rates from Euro to Shekel (EUR to ILS) using the Currency Conversion and Exchange Rates API from RapidAPI. Designed to run over a 24-hour period, it retrieves the conversion rate once every hour and saves the data for later reference.

## Features

- Fetches real-time EUR to ILS conversion rates using a reliable API service.
- I chose Currency Conversion from RapidAPI as it was one of the most recommended source for conversion rates, please check out the webiste for more information: https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates

- Attempts to refetch data if the initial API call is unsuccessful.
- Saves hourly conversion rates for a 24-hour period.
- Displays all fetched conversion rates after completing the 24-hour cycle.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.6 or higher
- `requests` library

You also need a RapidAPI key for accessing the Currency Conversion and Exchange Rates API. You can obtain this key by signing up at [RapidAPI](https://rapidapi.com).
Please note that I used the Currency Conversion and Exhange Rates API from RapidAPI
Link: https://rapidapi.com/principalapis/api/currency-conversion-and-exchange-rates


## Installation

1. Clone this repository or download the source code.
2. Install the packages using the requirements.txt file

```
pip install -r requirements.txt
```

## Usage
To run the application, navigate to the directory containing the script and execute:


The application will start fetching the EUR to ILS conversion rate every hour for 24 hours. After each fetch, the current rate and time will be printed to the console. At the end of the 24-hour period, the application will print out all the hourly rates that were fetched.

