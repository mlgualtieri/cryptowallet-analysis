import requests
# A Python3 script to calculate the total balance of VerusCoin transferred from wallet

# Set wallet address
WALLET     = ""

# URL of blockchain explorer
BASE_URL   = "https://explorer.verus.io/ext/getaddresstxsajax/" + WALLET

# Max API page length
MAX_PAGE_LENGTH   = 100

# Amount to divide number returned by API
CONVERSION_FACTOR = 100000000


def fetch_data():
    start = 0
    total_tx = 0
    while True:
        response = requests.get(BASE_URL, params={"start": start, "length": MAX_PAGE_LENGTH})
        response.raise_for_status()
        json_data = response.json()
        
        data = json_data.get("data", [])
        
        # Break when no more data from API
        if not data:
            break
        
        for item in data:
            if len(item) > 4:
                if(item[3] > 0):
                    total_tx = total_tx + item[3]
                    print("Transferred on", item[0], ":", (item[3] / CONVERSION_FACTOR))
        
        # Increment the offset for the next page
        start += MAX_PAGE_LENGTH
    
    total_tx = total_tx / CONVERSION_FACTOR
    print("Total transferred:", total_tx)

fetch_data()

