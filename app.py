from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['C+v1U3jF4gVBbb7Fiz5IHCqa4MU6wua4/1PEgeqE/KsmW99zs2dCoJbryJHhrJDj8YWQdmNgw+j08KUCAFLC/s+tLBKlGk7u6lYVdmNgw+j08KUCAFLC/s+tLBKlGk7u6lYVdmNgw+j08KUCAFLC/s+tLBKlGk7u6lYVdmNgw+j08KUCAFLC/s+tLBKlGk7u6lYVdmapHJlJImnosQCpCCuC分鐘t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['431b8a7b59b0d37171c0e6f817994de4'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)