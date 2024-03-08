from data import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price < bottom or coin.current_price > top:
                print(coin, "ALERT!! ACHTUNG")
            else:
                print(coin)


coins = get_coins()

"""Example of using: 
Checking the price of this 3 crypto currency
"""

if __name__ == '__main__':
    while True:
        time.sleep(100)
        alert('btc', bottom=20_000, top=30_000, coins_list=coins)
        alert('eth', bottom=3_000, top=4_000, coins_list=coins)
        alert('steth', bottom=3_000, top=4_000, coins_list=coins)
