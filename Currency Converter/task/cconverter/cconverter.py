import requests

currency_code = input()

usd = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json").json()
eur = requests.get(f"http://www.floatrates.com/daily/{currency_code}.json").json()

print(eur["usd"])
print(usd["eur"])
