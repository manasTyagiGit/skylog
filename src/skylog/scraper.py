"""
Goal : A skylog package with clients for JPL Close-Approach, JPL Sentry, SILSO, SWPC and the Exoplanet Archive. One
request at a time, a User-Agent with your email, retries with backoff, Pydantic models that turn JPL's string
numbers into numbers, raw JSON saved with the time you fetched it

Objective 1 : Let us start with the JPL APIs  -> chose close approach API at : https://ssd-api.jpl.nasa.gov/doc/cad.html
"""

### OPTIONS ###

JPL_API_URL_BASE = "https://ssd-api.jpl.nasa.gov/cad.api"
JPL_API_LIMIT = 100

JPL_API_PARAMS = {
                    'limit' : JPL_API_LIMIT
                    }

SAVE_FILE_PATH = "output_data/jpl_data.json"
JSON_INDENT = 4

### OPTIONS END ###

import requests
import json

def getJPLData() :
    response = requests.get(JPL_API_URL_BASE, params=JPL_API_PARAMS)

    response_json_data = response.json()

    with open(SAVE_FILE_PATH, "w") as file :
        json.dump(response_json_data, file, indent=JSON_INDENT)
    

def main() :
    print ("Hello, this is skylog")

    getJPLData()
  

if __name__ == "__main__" : 
    main()