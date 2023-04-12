import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
import json

# Check that NLTK and its dependencies are installed
try:
    nltk.data.find('punkt')
    nltk.data.find('stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')

# Define a function to tokenize text into words
def tokenize_text(text):
    # Check that text is a string
    if not isinstance(text, str):
        raise TypeError('Input text must be a string')
    # Split text into sentences
    sentences = sent_tokenize(text)
    # Create an empty dictionary to store words and their sentences
    word_dict = {}
    # Loop over each sentence
    for i, sentence in enumerate(sentences):
        # Tokenize sentence into words
        words = word_tokenize(sentence)
        # Filter out stop words and unwanted words
        filtered_words = [word for word in words if word.lower() not in stopwords.words('english') and not re.match('^[\W_]+$', word)]
        # Group words into phrases and expressions
        # (not implemented yet)
        # Add words and their sentence to the word_dict
        for word in filtered_words:
            if word in word_dict:
                word_dict[word].append(i)
            else:
                word_dict[word] = [i]
    # Convert word_dict to JSON and return it
    return json.dumps(word_dict)

# Example usage
text = "This is a sample text. It contains some words and some punctuation!"
print(tokenize_text(text))
