# Semantic Sentiment Analysis of Amazon Product Reviews 🛍️

This project leverages **Natural Language Processing (NLP)** techniques to analyze customer reviews of sneaker brands from Amazon. The goal is to extract meaningful insights about customer sentiment to support data-driven product and marketing decisions.

---

## 📌 Table of Contents

* [Introduction](#introduction)
* [Data Collection](#data-collection)
* [Preprocessing & Feature Extraction](#preprocessing--feature-extraction)
* [Sentiment Analysis](#sentiment-analysis)
* [Evaluation & Visualization](#evaluation--visualization)
* [Insights](#insights)
* [Technologies Used](#technologies-used)

---

## 📖 Introduction

Understanding customer sentiment is essential for product development and brand strategy. This project analyzes Amazon sneaker reviews to classify sentiments and identify the best-performing brands based on customer feedback.

---

## 🔍 Data Collection

* **Platform**: [Amazon](https://www.amazon.com/)
* **Method**: Web scraping using `requests` and `BeautifulSoup`
* **Fields Collected**:

  * `Product` (sneaker brand)
  * `Buyer` (reviewer's name or alias)
  * `Rating` (e.g., 4.0 out of 5)
  * `Review` (written feedback)

A total of **1035 reviews** across multiple sneaker brands were collected and stored in a structured CSV file.

---

## 🧹 Preprocessing & Feature Extraction

* Missing buyer names replaced with "Amazon Customer"
* Ratings extracted and converted to numeric
* Text preprocessing included:

  * Language detection and translation (via `TextBlob`)
  * Removing punctuation and non-alphabetic characters
  * Tokenization and stopword removal (using `nltk`)

---

## 💬 Sentiment Analysis

* Used **NLTK's SentimentIntensityAnalyzer** for scoring each review.
* Sentiment categories:

  * **Positive**: score > 0.05
  * **Neutral**: -0.05 ≤ score ≤ 0.05
  * **Negative**: score < -0.05

---

## 📊 Evaluation & Visualization

Visualizations were generated using `matplotlib` and `seaborn`:

* **Sentiment Distribution**: Majority of reviews were positive
* **Sentiment Score Histogram**: Showed skew toward high sentiment scores
* **Average Sentiment by Product**: Compared brands on average customer sentiment

---

## 📈 Insights

* **Top performer**: *Puma* had the highest average sentiment score
* **Others**: Adidas and Nike followed closely, while Sannax, Caterpillar, and Skechers showed weaker customer sentiment
* **Recommendation**: Brands with low sentiment should review feedback to improve customer satisfaction

---

## 🛠️ Technologies Used

* Python
* `requests`, `BeautifulSoup` – Web scraping
* `pandas`, `numpy` – Data processing
* `nltk`, `TextBlob` – NLP and sentiment analysis
* `matplotlib`, `seaborn` – Visualization
