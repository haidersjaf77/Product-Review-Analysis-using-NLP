# Handle missing values in the Buyer column
df['Buyer'] = df['Buyer'].replace(['', ' '], np.nan)
df['Buyer'].fillna('Amazon Customer', inplace=True)

# Extract numeric rating values
df['Rating'] = df['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Text preprocessing function
def preprocess_text(text):
    try:
        if detect(text) != "en":
            text = TextBlob(text).translate(to="en")
    except:
        pass

    text = re.sub(r"[^a-zA-Z\s]", "", str(text))  # Remove non-alphabetic characters
    tokens = word_tokenize(text.lower())  # Tokenization
    stop_words = set(stopwords.words("english"))  # Load stopwords
    tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
    
    return " ".join(tokens)

# Apply preprocessing to the Review column
df['Review'] = df['Review'].apply(preprocess_text)

df  # Display the DataFrame