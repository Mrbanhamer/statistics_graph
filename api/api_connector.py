import requests # Make sure this is the real library!

def connecting():
    # 1. Initialize the dictionary OUTSIDE the loop
    all_currencies = {"SEK": [], "USD": [], "GBP": []}
    for year in range(2026):
        print(year)
        if year >= 1993:
            # Using 2020, 2021, 2022, 2023, 2024
            url = f"https://api.frankfurter.dev/v2/rates?date={year}-01-04"
            response = requests.get(url)
            data = response.json()

        # The Frankfurter API usually returns a list of rate objects
            for item in data:
                currency = item["quote"]
                if currency in all_currencies:
                    all_currencies[currency].append({
                        "rate": item["rate"], 
                        "date": item["date"]
                    })

    # 2. Return the full lists after the loop finishes
    return all_currencies["SEK"], all_currencies["USD"], all_currencies["GBP"]

# How to use the returned data:
# sek, usd, gbp = connecting()