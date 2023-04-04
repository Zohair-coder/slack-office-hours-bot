from dotenv import load_dotenv
import os

load_dotenv()

CHANNEL = "announcements"
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
ZOOM_LINK = "https://drexel.zoom.us/j/89238745476"
START_TIME = "8:00 pm"
END_TIME = "10:00 pm"
