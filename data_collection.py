import praw

def get_reddit_posts(subreddit='all', limit=100, post_type='hot'):
    # Initialize Reddit API client
    reddit = praw.Reddit(
        client_id='enter_client_id',
        client_secret='enter_client_secret',
        user_agent='my_reddit_app'
    )

    # Initialize an empty list to hold posts
    posts = []

    # Fetch posts from the specified subreddit and post type
    if post_type == 'hot':
        for submission in reddit.subreddit(subreddit).hot(limit=limit):
            posts.append(submission.title + ' ' + submission.selftext)
    elif post_type == 'new':
        for submission in reddit.subreddit(subreddit).new(limit=limit):
            posts.append(submission.title + ' ' + submission.selftext)
    elif post_type == 'top':
        for submission in reddit.subreddit(subreddit).top(limit=limit):
            posts.append(submission.title + ' ' + submission.selftext)
    else:
        raise ValueError("Invalid post_type. Choose 'hot', 'new', or 'top'.")

    return posts
