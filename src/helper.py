import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
# Correct Import: Import the class directly
from langchain.chains import ConversationalRetrievalChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory

# --- API Key Loading (as previously discussed, verify this is working) ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    print("Google API Key loaded successfully.")
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
else:
    print("WARNING: Google API Key not found. Please check your .env file or set it manually.")
    # You might want to raise an error here if the key is mandatory for your app
    # raise ValueError("GOOGLE_API_KEY environment variable not set.")


def get_pdf_text(pdf_docs):
    """Extract text from a PDF file."""
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    return text

def get_chunks(text):
    """Split text into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(chunks):
    """Create a vector store from text chunks."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=GOOGLE_API_KEY # Explicitly pass the key for robustness
        )
        print("GoogleGenerativeAIEmbeddings initialized successfully.")
        vector_store = FAISS.from_texts(chunks, embedding=embeddings)
        print("Vector store created successfully.")
        return vector_store
    except Exception as e:
        print(f"Error initializing GoogleGenerativeAIEmbeddings or creating vector store: {e}")
        print("Please ensure your GOOGLE_API_KEY is correctly set and valid.")
        raise # Re-raise for full traceback

def get_conversational_chain(vector_store):
    """Create a conversational retrieval chain."""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Correct Usage: Call from_llm directly on the imported class
    conversational_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversational_chain

# Example usage (for testing)
if __name__ == "__main__":
    print("\n--- Starting demo ---")

    # Mock PDF text for testing the chain setup without actual PDFs
    sample_text = """
    LangChain is a framework designed to simplify the creation of applications using large language models (LLMs).
    It provides components for working with LLMs and a framework for orchestrating these components.
    Key features include:
    1. Chains: Combine LLMs with other components.
    2. Agents: Allow LLMs to interact with their environment.
    3. Memory: Persist state between calls of a chain/agent.
    4. Callbacks: Log and stream intermediate steps.

    LangChain supports various LLM providers, including OpenAI, Google, Anthropic, and many more.
    It's particularly useful for building applications like chatbots, summarization tools, and question-answering systems over documents.
    """

    print("Getting chunks from sample text...")
    chunks = get_chunks(sample_text)
    print(f"Number of chunks: {len(chunks)}")

    print("Creating vector store...")
    vector_store = get_vector_store(chunks)
    print("Vector store created.")

    print("Creating conversational chain...")
    chain = get_conversational_chain(vector_store)
    print("Conversational chain created.")

    # Simple interaction example
    print("\n--- Engaging in conversation ---")
    question1 = "What is LangChain?"
    print(f"User: {question1}")
    response1 = chain({"question": question1})
    print(f"AI: {response1['answer']}")

    question2 = "What are its key features?"
    print(f"User: {question2}")
    response2 = chain({"question": question2})
    print(f"AI: {response2['answer']}")