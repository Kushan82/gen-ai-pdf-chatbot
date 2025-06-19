# 📄 GenAI PDF Chatbot

An intelligent PDF chatbot powered by **Generative AI** and **LangChain** that allows you to upload a PDF and ask questions about its content. Built with **Streamlit**, it leverages embeddings and a language model (like OpenAI or Groq) to answer in real-time using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 📤 Upload any PDF document
- 🔍 Asks questions about the content using semantic search
- 🧠 Powered by LLMs (OpenAI, Groq)
- ⚙️ Built with Streamlit and LangChain
- 🧾 Easy to run locally

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/gen-ai-pdf-chatbot.git
cd gen-ai-pdf-chatbot-main

## 🗂️ Project Structure
gen-ai-pdf-chatbot-main/
├── app.py               # Main Streamlit app
├── template.py          # LLM and document QA logic
├── Chap2.pdf            # Sample input PDF
├── requirements.txt     # Python dependencies
├── setup.py             # Project metadata
├── LICENSE              # Open source license
└── README.md            # This file

---

## 🔧 Requirements

- Python 3.10+
- Pip / Pipenv
- OpenAI / Groq / Tavily API keys

---

## 📥 Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/gen-ai-pdf-chatbot.git
cd gen-ai-pdf-chatbot-main

**### 2. Install dependencies**
pip install -r requirements.txt

**###3. Add Environment Variables**
Create a .env file in the root directory:
GOOGLE_API_KEY="YOUR_GEMINI_KEY"

**###4. Run the app **
streamlit run app.py

🤖 How It Works
1.PDF is uploaded and split into text chunks.
2.Each chunk is embedded using a text embedding model.
3.A FAISS vector store is used to find the most relevant content.
4.The selected context is passed to a language model to generate an answer.

🔍 Tech Stack
  LangChain
  Streamlit
  OpenAI / Groq
  FAISS


