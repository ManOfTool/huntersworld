from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

from util.config import *
from util.cloudinary import *
from random import randint
import re

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(CHANNEL_SECRET)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text

    exp = r'"(?:[^\\]|(?:\\.))*"'

    if msg in catagory:
        message = TextSendMessage(catagory[msg])
        
        line_bot_api.reply_message(event.reply_token, message)

    elif msg in monsters:
        url = cloudinary.CloudinaryImage(monsters[msg] + '.jpg').image(secure = True)
        url = url[10:-3]

        message = ImageSendMessage(original_content_url = url, preview_image_url = url)
        
        line_bot_api.reply_message(event.reply_token, message)

    elif msg == "rand":
        m_list = list(monsters)
        message = TextSendMessage(m_list[randint(0, len(m_list) - 1)])

        line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
