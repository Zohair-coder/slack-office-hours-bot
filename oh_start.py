from slack_bot import SlackBot
from slack_sdk import WebClient
import config

if __name__ == "__main__":
    print("Starting script...")
    client = WebClient(config.SLACK_TOKEN)

    bot = SlackBot(client)
    bot.post_message(
        config.CHANNEL, "Hi everyone. My office hours are now live from {} - {} at {}. Feel free to join if you have any questions.".format(config.START_TIME, config.END_TIME, config.ZOOM_LINK))
