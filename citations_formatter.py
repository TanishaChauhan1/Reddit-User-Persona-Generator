from tqdm import tqdm

def collect_user_content(reddit, username, max_items=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for submission in tqdm(user.submissions.new(limit=max_items), desc="Fetching posts"):
        posts.append(f"Post Title: {submission.title}\nContent: {submission.selftext}\n")

    for comment in tqdm(user.comments.new(limit=max_items), desc="Fetching comments"):
        comments.append(f"Comment: {comment.body} (in r/{comment.subreddit})\n")

    return "\n".join(posts + comments)
