import requests
from tabulate import tabulate
import os
import pandas as pd

api_key = 'YOUR-API-KEY-GET-IT-IN-COINMARKETCAMP'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    currencies = data['data']
    table = []
    for currency in currencies:
        table.append([
            currency['cmc_rank'],
            currency['name'],
            f"${currency['quote']['USD']['price']:.2f}",
            f"{currency['quote']['USD']['percent_change_1h']:.2f}%",
            f"{currency['quote']['USD']['percent_change_24h']:.2f}%",
            f"{currency['quote']['USD']['percent_change_7d']:.2f}%",
            f"${currency['quote']['USD']['market_cap']:.2f}",
            f"${currency['quote']['USD']['volume_24h']:.2f}"
        ])

    headers = ["Rank", "Name", "Price", "1h %", "24h %", "7d %", "Market Cap", "Volume (24h)"]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    df = pd.DataFrame(table, columns=headers)
    if not os.path.exists('coin_dataapi.csv'):
        df.to_csv('coin_dataapi.csv', mode='w', header=True, index=False)
    else:
        df.to_csv('coin_dataapi.csv', mode='a', header=False, index=False)
else:
    print(f'Error: {response.status_code}')
