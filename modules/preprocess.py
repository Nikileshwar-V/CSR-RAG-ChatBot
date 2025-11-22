import re
from nltk.corpus import stopwords

def clean_text(text):
    # Remove multiple spaces, newlines, and special symbols
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9.,:;!?()&%₹$-]+', ' ', text)

    # Remove page numbers or repeated “chapter/module” lines
    text = re.sub(r'\b(chapter|module|csr|page|section)\b\s*\d*', '', text, flags=re.IGNORECASE)

    # Remove stopwords (optional for less noise)
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in text.split() if word.lower() not in stop_words]

    cleaned = " ".join(filtered_words)
    return cleaned.strip()
