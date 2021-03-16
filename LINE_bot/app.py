from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import twstock

app = Flask(__name__)

line_bot_api = LineBotApi('9uxeW5d1r8G2mmtQg7z+U0AsSzaJppLQtI+mbvrudH6ynp+KRKwvwZGnUd81O90UvwdG0IwKj4+54X78iRV07XNEXB/qXlcXVpW2hxAZUac9e71z3wMUFwNIW2Er3CUUUQzXwWjrdzsOJkGBijSPQgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0b6caaf9fea04049ba06471aec26fd1f')

def stock(num):
    stock = twstock.realtime.get(num)
    if stock['success']:
        name = stock['info']['name']
        code = stock['info']['code']
        high_price = stock['realtime']['high']
        low_price = stock['realtime']['low']
        message = f"{name}({code}):\n[High]{high_price}\n[Low]{low_price}"
    else:
        message = stock['rtmessage']
    return message

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text = True)
    app.logger.info('Request body: ' + body)

    try:
        print(body, signature)
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextMessage(text=stock(event.message.text))
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == '__main__':
    app.run()