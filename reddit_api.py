import os
from dotenv import load_dotenv
import praw

# Load .env from this file’s directory
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

def get_reddit_instance():
    reddit = praw.Reddit(
    client_id="Vx6I4D9VqssYmwl9mu1xNw",
    client_secret="vndG_pN-UFAjmGLFdoX_-keafrtF8Q",
    user_agent="persona_extractor"
)

    reddit.read_only = True
    return reddit



