from typing import List, Dict
from praw.models import Redditor
from praw import Reddit
from tqdm import tqdm

def collect_user_content(reddit: Reddit, username: str, max_items: int = 50) -> List[Dict]:
    user: Redditor = reddit.redditor(username)
    content_blocks = []

    # Get latest submissions (posts)
    print("🔍 Fetching submissions...")
    try:
        for submission in tqdm(user.submissions.new(limit=max_items), desc="Fetching posts"):
            content_blocks.append({
                "type": "post",
                "title": submission.title,
                "body": submission.selftext,
                "permalink": f"https://www.reddit.com{submission.permalink}",
                "subreddit": submission.subreddit.display_name
            })
    except Exception as e:
        print(f"⚠️ Error fetching posts: {e}")

    # Get latest comments
    print("💬 Fetching comments...")
    try:
        for comment in tqdm(user.comments.new(limit=max_items), desc="Fetching comments"):
            content_blocks.append({
                "type": "comment",
                "body": comment.body,
                "permalink": f"https://www.reddit.com{comment.permalink}",
                "subreddit": comment.subreddit.display_name
            })
    except Exception as e:
        print(f"⚠️ Error fetching comments: {e}")

    return content_blocks
