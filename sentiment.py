pip install textblob vaderSentiment
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Function to analyze sentiment using TextBlob
def analyze_sentiment_textblob(comment):
    blob = TextBlob(comment)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Good"
    elif polarity < 0:
        return "Bad"
    else:
        return "Neutral"

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(comment):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(comment)
    if sentiment_score['compound'] >= 0.05:
        return "Good"
    elif sentiment_score['compound'] <= -0.05:
        return "Bad"
    else:
        return "Neutral"

# Function to analyze sentiment of a file
def analyze_sentiment_from_file(file_path):
    with open(file_path, 'r') as file:
        comments = file.readlines()
        for i, comment in enumerate(comments, 1):
            print(f"Comment {i}: {comment.strip()}")
            print(f"Sentiment (TextBlob): {analyze_sentiment_textblob(comment.strip())}")
            print(f"Sentiment (VADER): {analyze_sentiment_vader(comment.strip())}")
            print("-" * 50)

# Function to analyze sentiment of a manually entered comment
def analyze_sentiment_manually():
    comment = input("Enter the comment: ")
    print(f"Sentiment (TextBlob): {analyze_sentiment_textblob(comment)}")
    print(f"Sentiment (VADER): {analyze_sentiment_vader(comment)}")

# Main function to allow user to choose file upload or manual input
def main():
    choice = input("Do you want to analyze sentiment from a file or manually input a comment? (file/manual): ").strip().lower()
    if choice == "file":
        file_path = input("Enter the file path containing comments: ").strip()
        analyze_sentiment_from_file(file_path)
    elif choice == "manual":
        analyze_sentiment_manually()
    else:
        print("Invalid choice. Please enter 'file' or 'manual'.")

if __name__ == "__main__":
    main()
