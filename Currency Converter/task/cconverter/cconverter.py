import requests


change_from = input().lower()
infos = requests.get(f"https://www.floatrates.com/daily/{change_from}.json").json()

cache = {}

if change_from == "usd":
    cache["eur"] = infos["eur"]["rate"]
elif change_from == "eur":
    cache["usd"] = infos["usd"]["rate"]
else:
    cache["usd"] = infos["usd"]["rate"]
    cache["eur"] = infos["eur"]["rate"]

while True:

    change_to = input().lower()

    if change_to == "":
        break

    amount_money = int(input())

    print("Checking the cache...")

    if change_to in cache.keys():
        print("Oh! It is in the cache!")
        print(f"You received {amount_money * cache[change_to]} {change_from.upper()}.")
    else:
        print("Sorry, but it is not in the cache!")
        rate = infos[change_to]["rate"]
        print(f"You received {amount_money * rate} {change_to.upper()}")
        cache[change_to] = rate
