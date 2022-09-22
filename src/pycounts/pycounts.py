from collections import Counter
from string import punctuation

def load_text(input_file):
    with open(input_file, "r") as file:
        text = file.read()
    return text

def clean_text(text):
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")

def count_words(input_file):
    text = load_text(input_file)
    text= clean_text(text)
    words = text.split()
    return Counter(words)