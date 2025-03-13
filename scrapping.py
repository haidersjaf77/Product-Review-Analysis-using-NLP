import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from langdetect import detect
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_reviews(url):
    """
    Fetches and parses the HTML content of a webpage using the given URL.
    """
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    """
    Extracts reviewer names from the BeautifulSoup object.
    """
    Names = soup.findAll("span", {"class": "a-profile-name"})
    Reviewer = [Names[name].get_text() for name in range(2, len(Names))]

    """
    Extracts ratings from the BeautifulSoup object.
    """
    Rating = soup.findAll("i", {"class": "review-rating"})
    Reviews_rating = [Rating[review].get_text() for review in range(0, len(Rating))]

    """
    Extracts review texts from the BeautifulSoup object.
    """
    Reviews_Description = soup.findAll("span", {"class": "a-size-base reviewtext"})
    Reviews = []
    
    for review in range(0, len(Reviews_Description)):
        Reviews.append(Reviews_Description[review].get_text())
        Reviews[review] = re.sub(r'\s+', ' ', Reviews[review])
    
    data_length = min(len(Reviewer), len(Reviews_rating), len(Reviews))
    
    return Reviewer[:data_length], Reviews_rating[:data_length], Reviews[:data_length]

sneakers_url = {
    "Nike Sneakers": "your product URL",
    "Air Jordan Sneakers": "your product URL",
    "New Balance Sneakers": "your product URL",
    "Adidas Sneakers": "your product URL",
    "Reebok Sneakers": "your product URL",
    "Sannax Sneakers": "your product URL",
    "Caterpillar Sneakers": "your product URL",
    "Fila Sneakers": "your product URL",
    "Skechers Sneakers": "your product URL",
    "Asics Sneakers": "your product URL",
    "Lugz Sneakers": "your product URL",
    "Osiris Sneakers": "your product URL",
    "Puma Sneakers": "your product URL",
    "Converse Sneakers": "your product URL"
}

reviews = []

for product, url in sneakers_url.items():
    reviewer, rating, review = fetch_reviews(url)
    
    for b, rt, rv in zip(reviewer, rating, review):
        reviews.append({
            "Product": product,
            "Buyer": b,
            "Rating": rt,
            "Review": rv
        })

df = pd.DataFrame(reviews)
df.to_csv("sneakers_nlp.csv", index=False)
df
