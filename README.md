# **CSR-RAG-ChatBot**

### **Context-Aware Document Q&A System for Corporate Social Responsibility Modules**

## **Overview**

CSR-RAG-ChatBot is an intelligent Retrieval-Augmented Generation (RAG) system designed to extract content from CSR (Corporate Social Responsibility) documents, preprocess them, embed them into a searchable vector store, and provide accurate, context-aware answers to user queries.

It uses **local embeddings**, **PDF text extraction**, and a lightweight **LLM-powered chatbot** to deliver fast and reliable answers.
The system is modular, easy to extend, and built for academic research, CSR documentation assistance, and enterprise knowledge management.

> **Note:** This project is intended for educational and research purposes. It does not enforce legal or policy interpretations of CSR compliance.

---

## **Features**

* 📄 **PDF Content Extraction** (CSR modules, guidelines, policies)
* 🧹 **Text Preprocessing** (cleaning, chunking, normalization)
* 🔍 **Vector Embedding & Storage** (local embedding model + FAISS/other)
* 🤖 **RAG-Powered Chatbot** for CSR-specific Q&A
* 🗂️ **Modular Architecture** (easy to upgrade and integrate)
* ⚡ **Fast Local Execution**
* 📁 **Temporary image support** for OCR-based extraction (optional)

---

## **Architecture**

The workflow follows a simple but powerful CSR knowledge processing pipeline:

1. **Document Extraction**
   Extract text, images, and structured information from PDFs.

2. **Preprocessing & Chunking**
   Clean and segment the raw text into high-quality chunks.

3. **Embedding & Vector Store Creation**
   Generate embeddings and store them in a searchable format.

4. **Query Handling & Retrieval**
   Retrieve the most relevant CSR sections.

5. **LLM-Based Response Generation**
   Provide contextual answers based on retrieved content.

---

## **Project Structure**

```
csr_rag_chatbot/
│
├── data/
│   ├── temp_images/          # Extracted images (optional, OCR)
│   └── CSR MODULES.pdf       # Source CSR document
│
├── modules/
│   ├── chatbot.py            # RAG chatbot logic
│   ├── embed_store.py        # Embedding + vector DB builder
│   ├── extract.py            # PDF extractor (text/images)
│   ├── preprocess.py         # Cleaning, splitting, formatting
│
├── main.py                   # Script to run chatbot
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## **Technology Stack**

* **Python 3.10+**
* **LangChain / FAISS / sentence-transformers (depending on your setup)**
* **PyPDF2 / pdfplumber** for PDF extraction
* **Local Embedding Models** (MiniLM, BGE, etc.)
* **Optional:** OCR support using Tesseract

---

## **Installation**

```bash
git clone https://github.com/Nikileshwar-V/CSR-RAG-ChatBot
cd CSR-RAG-ChatBot
python -m venv .venv
```

Activate virtual environment:

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/Mac**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## **Preparing the Vector Store**

Run embedding pipeline to extract, preprocess, and store document chunks:

```bash
python modules/embed_store.py
```

This step will:

* Extract text from **CSR MODULES.pdf**
* Clean & chunk content
* Generate embeddings
* Save vector database locally

---

## **Run the Chatbot**

Start the CSR query answering system:

```bash
python main.py
```

---

## **Example Output**

**User Question:**
*“What are the main components of a CSR framework?”*

**Retrieved Context:**
(Shows matching extracted section from CSR modules)

**Chatbot Response:**

> The CSR framework typically includes policy formulation, stakeholder analysis, sustainability planning, compliance mechanisms, and social impact evaluation. These components ensure structured implementation and monitoring of corporate responsibility programs.

---

## **Future Enhancements**

* GUI/Streamlit Interface
* Multi-document support
* PDF result citation mode
* Improved chunking for large PDFs
* Multilingual CSR document support
* Neo4j Knowledge Graph integration
* Browser-based query panel

---

## **Author**

**Nikileshwar V**
MCA – Research & Development
GitHub: [https://github.com/Nikileshwar-V](https://github.com/Nikileshwar-V)
LinkedIn: [https://linkedin.com/in/nikileshwar-v](https://linkedin.com/in/nikileshwar-v)

---

## **Disclaimer**

This project is intended for **research and educational purposes only**.
The chatbot does not replace expert CSR interpretation, legal advice, or policy judgment.

---
