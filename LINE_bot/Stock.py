import twstock
from threading import Timer
import requests


def stock_2330():
    stock = twstock.realtime.get('2330')
    if stock['success']:
        name = stock['info']['name']
        code = stock['info']['code']
        high_price = stock['realtime']['high']
        low_price = stock['realtime']['low']
        message = f"\n{name}({code}):\n[High]{high_price}\n[Low]{low_price}"
        response = requests.get("http://127.0.0.1/test/LINE_notify.php?message=" + message)
        print(f"Status : {response.json()['message']}")
    Timer(3, stock_2330).start()


if __name__ == "__main__":
    stock_2330()
