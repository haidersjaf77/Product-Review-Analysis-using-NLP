# Distribution of Sentiments
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Sentiment', palette='viridis')
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Sentiment Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Sentiment_Score'], kde=True, bins=30, color='purple')
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

#Sentiment Score by Product
plt.figure(figsize=(10, 5))
sns.barplot(data=avg_sentiment, x='Product', y='Sentiment_Score',
palette='coolwarm')
plt.title('Average Sentiment Score by Product')
plt.xlabel('Product')
plt.ylabel('Average Sentiment Score')
plt.xticks(rotation=45)
plt.show()