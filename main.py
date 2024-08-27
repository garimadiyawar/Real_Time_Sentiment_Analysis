from sentiment_analysis import analyze_sentiment
from visualization import plot_sentiment_analysis
from data_collection import get_reddit_posts
from preprocessing import preprocess_text

def main():
    # Fetch Reddit posts
    posts = get_reddit_posts(subreddit='technology', limit=50, post_type='hot')

    # Preprocess and analyze posts
    sentiments = [analyze_sentiment(preprocess_text(post)) for post in posts]

    # Count sentiments
    sentiment_counts = {
        "POSITIVE": sentiments.count("POSITIVE"),
        "NEGATIVE": sentiments.count("NEGATIVE"),
        "NEUTRAL": sentiments.count("NEUTRAL"),
    }

    # Plot sentiment analysis
    plot_sentiment_analysis(sentiment_counts)

if __name__ == "__main__":
    main()
