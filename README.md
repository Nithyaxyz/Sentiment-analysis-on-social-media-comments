A Python-based sentiment analysis application that evaluates the polarity of social media comments using two popular NLP libraries — TextBlob and VADER.
The tool supports both file-based input and manual comment entry, classifying sentiment as Good, Bad, or Neutral.

🚀 Features
Dual Sentiment Analysis – Uses:
TextBlob for polarity scoring
VADER (Valence Aware Dictionary for Sentiment Reasoning) for fine-grained analysis
Multiple Input Modes:
File Upload – Reads multiple comments from a text file
Manual Input – Analyze custom comment entered by the user
Clear Output – Displays sentiment classification for each method side-by-side
Easy-to-Use CLI Interface

🛠️ Tech Stack
Language: Python 3.x
Libraries:
textblob
vaderSentiment

Project Structure
sentiment-analysis/
│── sentiment_analysis.py   # Main script
│── comments.txt             # Sample comments file
│── README.md
