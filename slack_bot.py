import config
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackBot:
    def __init__(self, client: WebClient) -> None:
        self.client = client

    def post_message(self, channel_name: str, text: str) -> None:
        channel_id = self.get_channel_id_from_name(channel_name)
        try:
            response = self.client.chat_postMessage(
                channel=channel_id, text=text)
            assert response.data.get("ok")

        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["error"]

    def get_channel_id_from_name(self, channel_name: str):
        response = self.client.conversations_list()
        channels = response["channels"]
        for channel in channels:
            if channel["name"] == channel_name:
                return channel["id"]
