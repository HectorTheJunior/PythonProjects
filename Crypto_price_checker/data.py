import requests
from dataclasses import dataclass
from typing import Final
""" Get your Api Key here:
  https://docs.coingecko.com/reference/setting-up-your-api-key """

""" This api key is changed to avoid using it by strangers ;) Get your own api key:) """
API_KEY = 'NOT_API_KEY'

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'

PARAMS = {'vs_currency': 'usd'}


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    high_24h: float
    low_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name} ({self.symbol}): ${self.current_price:,}'


def get_coins():
    header = {'x-cg-pro-api-key': API_KEY}
    params: dict = {'vs_currency': 'usd',
                    'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=params, headers=header)
    json: dict = data.json()
    coin_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(name=item.get('name'),
                                  symbol=item.get('symbol'),
                                  current_price=item.get('current_price'),
                                  high_24h=item.get('high_24h'),
                                  low_24h=item.get('low_24h'),
                                  price_change_24h=item.get('price_change_24h'),
                                  price_change_percentage_24h=item.get("price_change_percentage_24h"))
        coin_list.append(current_coin)
    return coin_list
