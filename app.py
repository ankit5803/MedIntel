import streamlit as st
import os

from agents.retriever import build_vector_store, retrieve_relevant_docs
from agents.analyzer import analyze_chunks
from agents.responder import generate_response

st.set_page_config(page_title="🧠 MedIntel Assistant", layout="wide")
st.title("🩺 MedIntel: Your Medical AI Assistant")

# Sidebar
st.sidebar.header("📁 Dataset Selection")
data_dir = "data"
files = [f for f in os.listdir(data_dir) if f.endswith(".txt")]

selected_file = st.sidebar.selectbox("Choose a dataset", files)

query = st.text_input("Enter your medical query:", "")
submit = st.button("🔍 Search")

if submit and query:
    file_path = os.path.join(data_dir, selected_file)
    st.write(f"📂 Using data from: `{selected_file}`")

    with st.spinner("Analyzing..."):
        try:
            vectorstore = build_vector_store(file_path)
            chunks = retrieve_relevant_docs(query, vectorstore)

            st.subheader("📑 Top Relevant Info")
            for i, chunk in enumerate(chunks, 1):
                with st.expander(f"Chunk {i}"):
                    st.write(chunk)

            summary = analyze_chunks(chunks)

            st.subheader("📋 Final Summarized Answer")
            st.write(summary)

            st.subheader("💬 Assistant Response")
            response = generate_response(query, summary)
            st.write(response)

        except Exception as e:
            st.error(f"Error: {e}")
