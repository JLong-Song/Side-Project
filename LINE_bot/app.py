from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('9uxeW5d1r8G2mmtQg7z+U0AsSzaJppLQtI+mbvrudH6ynp+KRKwvwZGnUd81O90UvwdG0IwKj4+54X78iRV07XNEXB/qXlcXVpW2hxAZUac9e71z3wMUFwNIW2Er3CUUUQzXwWjrdzsOJkGBijSPQgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0b6caaf9fea04049ba06471aec26fd1f')

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
    
    return 'OK '

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextMessage(text='test')
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == '__main__':
    app.run()