from slack_bot import SlackBot
from slack_sdk import WebClient
import config

if __name__ == "__main__":
    client = WebClient(config.SLACK_TOKEN)

    bot = SlackBot(client)
    bot.post_message(config.CHANNEL, "My office hours are now over for today.")
