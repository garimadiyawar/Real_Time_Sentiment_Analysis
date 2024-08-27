import matplotlib.pyplot as plt

def plot_sentiment_analysis(sentiment_counts):
    # Data preparation
    labels = sentiment_counts.keys()
    values = sentiment_counts.values()

    # Create the plot
    plt.figure(figsize=(12, 7))
    bars = plt.bar(labels, values, color=['#4CAF50', '#F44336', '#2196F3'])

    # Add labels and title
    plt.xlabel('Sentiment', fontsize=14)
    plt.ylabel('Number of Posts', fontsize=14)
    plt.title('Sentiment Analysis of Recent Reddit Posts', fontsize=16)
    
    # Add value labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom', ha='center', fontsize=12, color='black')

    # Add grid lines for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot
    plt.tight_layout()
    plt.show()
