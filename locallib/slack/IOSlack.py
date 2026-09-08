from dotenv import load_dotenv
load_dotenv(override=True)

import io
from slack_bolt import App
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

SLACK_BOT_TOKEN = os.getenv("SLACKBOTTOKEN")
SLACK_APP_TOKEN = os.getenv("SLACKAPPTOKEN")

class SlackWriter(io.TextIOBase):
    def __init__(self, channel: str, encoding="utf-8"):
        super().__init__()
        self.channel = channel
        self.app = App(token=SLACK_BOT_TOKEN)

    def writable(self):
        return True

    def write(self, s: str):
        if not isinstance(s, str):
            raise TypeError("SocketTextWriter.write() requires a str")

        self.app.client.chat_postMessage(channel=self.channel, text=s)
        return len(s)

    def flush(self):
        pass

    def close(self):

        super().close()
