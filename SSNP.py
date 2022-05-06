from ssl import CHANNEL_BINDING_TYPES
import slack
import os
from pathlib import Path
from flask import Flask # //future lambda revision
from slackeventsapi import SlackEventAdapter
import tokens

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(tokens.AUTH_TOKEN2,'/slack/events',app)

client = slack.WebClient(token=tokens.AUTH_TOKEN)

BOT_ID = client.api_call("auth.test")['user_id']

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    
    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)

def new_func(event):
    text = event.get('text')
    return text

if __name__ == "__main__":
    app.run(debug=True) 