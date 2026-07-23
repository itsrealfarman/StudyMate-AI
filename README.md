# 🎓 StudyMate AI

An AI-powered PDF Study Assistant built using Retrieval-Augmented Generation (RAG).

Users can upload a PDF document and ask questions in natural language. The application retrieves the most relevant document sections using semantic search and generates accurate answers using OpenAI GPT.

---

## 🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text extraction & chunking
- 🧠 Semantic Search using FAISS
- 🤖 AI-generated answers using OpenAI GPT
- 💬 Conversational memory
- 📚 Source references
- 🎨 Clean Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- HuggingFace Embeddings
- OpenAI GPT-4o-mini
- PyPDF

---

## 📂 Project Structure

```
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env
│
├── utils/
│   ├── pdf_reader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   ├── search.py
│   ├── llm.py
│   └── qa_chain.py
│
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/itsrealfarman/StudyMate-AI.git
```

Go to the project

```bash
cd StudyMate-AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file

```env
OPENAI_API_KEY
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

---

## 📸 Demo

Upload any PDF and ask questions like:

- What is a Router?
- Explain OSI Layer.
- Summarize this document.
- What are the key points?

---

## 👨‍💻 Author

**Farman Ali**

Software Engineering Student

Generative AI Enthusiast

GitHub:
https://github.com/itsrealfarman

LinkedIn:
https://www.linkedin.com/in/farman-ali-78850b339

---

## ⭐ If you like this project, give it a Star!