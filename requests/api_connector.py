import requests

def connecting():
    # Fetching the data from the API
    response = requests.get("https://api.frankfurter.dev/v2/rates")
    data = response.json()

    # This will hold our currencies: {"SEK": {date: rate}, "USD": {date: rate}, ...}
    new_dict = {}

    for item in data:
        currency = item["quote"]
        rate = item["rate"]
        date = item["date"]

        if currency not in new_dict:
            new_dict[currency] = []

        # We append a dictionary with rate first, as you requested earlier
        new_dict[currency].append({"rate": rate, "date": date})

    # Accessing the three specific currencies you want
    sek_rates = new_dict.get("SEK", [])
    usd_rates = new_dict.get("USD", [])
    gbp_rates = new_dict.get("GBP", []) # GBP is the code for British Pounds

    # Return them as a tuple so you can use them all outside the function
    return sek_rates, usd_rates, gbp_rates

# How to use the returned data:
# sek, usd, gbp = connecting()