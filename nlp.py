import nltk # type: ignore
from nltk.tokenize import word_tokenize # type: ignore

nltk.download('punkt')

def preprocess_query(query):
    tokens = word_tokenize(query.lower())
    return " ".join(tokens)
