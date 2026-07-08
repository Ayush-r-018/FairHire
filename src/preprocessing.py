"""
FairHire
Text Preprocessing Module
"""

import re
import string

import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    """
    Clean textual data for NLP and Machine Learning.

    Steps:
    1. Lowercase conversion
    2. Remove URLs
    3. Remove email addresses
    4. Remove phone numbers
    5. Remove punctuation
    6. Remove extra whitespace
    7. Remove stopwords
    8. Lemmatization
    """

    if not isinstance(text, str):
        return ""

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # Remove phone numbers
    text = re.sub(r"\d{10,}", "", text)

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    # Tokenize
    words = text.split()

    # Remove stopwords and lemmatize
    cleaned_words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(cleaned_words)