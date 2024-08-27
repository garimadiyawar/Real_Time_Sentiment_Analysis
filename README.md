# Real-Time Sentiment Analysis Project

## Overview

This project performs real-time sentiment analysis on Reddit posts using Python. The sentiment of posts is analyzed and visualized to provide insights into public opinion on various topics. The analysis is performed using Natural Language Processing (NLP) techniques and the results are visualized using Matplotlib.

## Features

- Fetches posts from Reddit based on specified subreddits and post types.
- Preprocesses text data to prepare it for sentiment analysis.
- Analyzes sentiment using pre-trained NLP models.
- Visualizes sentiment distribution with clear and descriptive charts.

## Requirements

- Python 3.x
- `praw` for Reddit API access
- `spacy` for text preprocessing
- `transformers` for sentiment analysis
- `matplotlib` for visualization

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/real-time-sentiment-analysis.git
    cd real-time-sentiment-analysis
    ```

2. **Create a Virtual Environment (optional but recommended)**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    Create a `requirements.txt` file with the following content:

    ```text
    praw==7.7.0
    spacy==3.5.0
    transformers==4.29.2
    matplotlib==3.7.0
    ```

    Install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download SpaCy Model**

    Run the following command to download the SpaCy language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

## Configuration

Update `data_collection.py` with your Reddit API credentials:

```python
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='your_user_agent'
)
```

## Usage

1. **Run the Main Script**

    Execute the `main.py` script to fetch, process, analyze, and visualize Reddit posts:

    ```bash
    python main.py
    ```

2. **Adjust Parameters**

    Modify the parameters in `data_collection.py` to control the subreddit, limit, and post type. For example:

    ```python
    posts = get_reddit_posts(subreddit='technology', limit=50, post_type='hot')
    ```

## Project Structure

- `data_collection.py`: Contains functions to fetch posts from Reddit.
- `preprocessing.py`: Contains functions to preprocess text data.
- `sentiment_analysis.py`: Contains functions to analyze sentiment using NLP models.
- `visualization.py`: Contains functions to visualize sentiment analysis results.
- `main.py`: The main script that orchestrates data collection, processing, analysis, and visualization.

## Contributing

Feel free to open issues or submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

---
