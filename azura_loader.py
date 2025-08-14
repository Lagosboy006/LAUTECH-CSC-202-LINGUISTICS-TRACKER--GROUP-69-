import os
import string

def load_texts_from_folder(folder_path):
    """
    Loads and cleans all .txt files in a given folder.
    Returns a list of cleaned text contents.
    """
    cleaned_texts = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                raw_text = file.read()
                cleaned = clean_text(raw_text)
                cleaned_texts.append(cleaned)
    
    return cleaned_texts

def clean_text(text):
    """
    Lowercases text, removes punctuation and extra spaces.
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join(text.split())  # Remove extra whitespace
    return text
