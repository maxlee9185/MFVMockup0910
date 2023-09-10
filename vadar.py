# Install the VADER sentiment analysis library if not already installed
# You can use pip for installation:
# pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create a SentimentIntensityAnalyzer instance
analyzer = SentimentIntensityAnalyzer()

# Input your sentence here
sentence = "I love this product! It's amazing."

# Get sentiment scores
sentiment_scores = analyzer.polarity_scores(sentence)

# Extract the compound sentiment score
compound_score = sentiment_scores['compound']

# Determine the sentiment based on the compound score
if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the results
print("Sentiment:", sentiment)
print("Compound Score:", compound_score)
