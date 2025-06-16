from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEmbeddings


def build_vector_store(file_path):
    loader = TextLoader(file_path,encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    # Use a HuggingFace embedding model
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # small, fast, accurate

    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def retrieve_relevant_docs(query, vectorstore, k=3):
    results = vectorstore.similarity_search(query, k=k)
    return [doc.page_content for doc in results]
