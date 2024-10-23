import json
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the knowledge base (intents)
with open('knowledge.json', 'r') as file:
    data = json.load(file)

intents = data['intents']

# Preprocess and tokenize the patterns
nltk.download('punkt')

patterns = []  # User questions
tags = []      # Tags (categories)

for intent in intents:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

# Vectorize the text (convert patterns to a matrix of token counts)
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(patterns)  # Features (vectorized patterns)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X, tags)

# Function to get response based on predicted intent
def get_response(user_input):
    user_input_tfidf = vectorizer.transform([user_input])  # Vectorize user input
    predicted_tag = model.predict(user_input_tfidf)[0]     # Predict intent

    # Fetch the response for the predicted intent tag
    for intent in intents:
        if intent['tag'] == predicted_tag:
            return np.random.choice(intent['responses'])  # Return a random response
