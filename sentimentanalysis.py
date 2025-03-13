sia = SentimentIntensityAnalyzer()
df['Sentiment_Score'] = df['Review'].apply(lambda x:
sia.polarity_scores(x)['compound'])
df['Sentiment'] = df['Sentiment_Score'].apply(lambda x: 'Positive' if x > 0.05
else ('Negative' if x < -0.05 else 'Neutral'))
df
