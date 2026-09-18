import json
from urllib.request import urlopen

EVENT_TICKER = "KXHIGHTSEA-26SEP18"
BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

url = f"{BASE_URL}/events/{EVENT_TICKER}/"

with urlopen(url, timeout=20) as response:
    data = json.load(response)

print(data["event"]["title"])

for market in data["markets"]:
    label = market["yes_sub_title"]
    bid = market["yes_bid_dollars"]
    ask = market["yes_ask_dollars"]
    status = market["status"]

    print(f"{label}: Bid: {bid}, Ask: {ask}, Status: {status}")