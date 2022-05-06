from ssl import CHANNEL_BINDING_TYPES
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask # //future lambda revision
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter('d22e100a6800c2c18c7910ea92aaccbb','/slack/events',app) #destroy this and fix it

client = slack.WebClient(token='xoxb-3279337373456-3487658046995-xg9GB3H2whsfT7UC9uFx5mLT') #token destroyed code broken fix this

client.chat_postMessage(channel='#social networking project', text="hello world")

BOT_ID = client.api_call("auth.test")['user_id']
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    
    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)

if __name__ == "__main__":
    app.run(debug=True)