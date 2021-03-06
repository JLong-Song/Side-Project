import twstock
from threading import Timer
import requests


def stock_2330():
    stock = twstock.realtime.get('2330')
    if stock['success']:
        price = stock['realtime']['latest_trade_price']
        if price != '-':
            response = requests.get(
                "http://127.0.0.1/test/LINE_notify.php?message=" + price)
            print(f"Status : {response.json()['message']}")
        else:
            print('Status : Waiting...')
    Timer(3, stock_2330).start()


if __name__ == "__main__":
    stock_2330()
