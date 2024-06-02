import os
import logging
import json
import requests
logger = logging.getLogger()
logger.setLevel(logging.INFO)
LINE_CHANNEL_ACCESS_TOKEN   = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

def lambda_handler(event, context):
    for message_event in json.loads(event['body'])['events']:
        # 返信用のURL
        url = 'https://api.line.me/v2/bot/message/reply'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + LINE_CHANNEL_ACCESS_TOKEN
        }

        body = {
            'replyToken': message_event['replyToken'],
            'messages': [
                {
                    'type': 'text',
                    # 一旦はオウム返し
                    'text': message_event['message']['text']
                }
            ]
        }

        res = requests.post(url, data=json.dumps(body).encode('utf-8'), headers=headers)
        

    return