import requests

response = requests.get("https://api.frankfurter.dev/v2/rates")

data = response.json()

new_dict = {}

for item in data:
    currency = item["quote"]
    rate = item["rate"]
    date = item["date"]

    if currency not in new_dict:
        new_dict[currency] = {}

    new_dict[currency][rate] = date

print(new_dict["USD"])
print(new_dict["SEK"])

sek_rates = new_dict["SEK"]
print(sek_rates)