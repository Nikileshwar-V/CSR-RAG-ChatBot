from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_and_store_embeddings(cleaned_text):
    # Split large text into smaller chunks (important!)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # 500 characters per chunk
        chunk_overlap=100
    )
    docs = splitter.create_documents([cleaned_text])

    # Create embeddings (small model)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Store in FAISS vector database
    db = FAISS.from_documents(docs, embedding_model)
    return db
