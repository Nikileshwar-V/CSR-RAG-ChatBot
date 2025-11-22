from modules.extract import extract_pdf_data
from modules.preprocess import clean_text
from modules.embed_store import create_and_store_embeddings
from modules.chatbot import get_chat_response

pdf_path = "data/CSR MODULES.pdf"

print("\n Starting CSR Chatbot...")
print(" Extracting data...")
raw_text = extract_pdf_data(pdf_path)

print(" Cleaning text...")
cleaned_text = clean_text(raw_text)

print(" Creating embeddings and storing...")
db = create_and_store_embeddings(cleaned_text)

print("\n Chatbot ready! Ask questions about the CSR Report (text + images).")

while True:
    query = input("\n You: ")
    if query.lower() == "exit":
        break
    response = get_chat_response(db, query)
    print(" Chatbot:", response)
