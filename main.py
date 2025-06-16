import os
from dotenv import load_dotenv
load_dotenv()

from agents.retriever import build_vector_store, retrieve_relevant_docs
from agents.analyzer import analyze_chunks
from agents.responder import generate_response

def find_best_file(query, data_folder="data"):
    """
    Matches user query with known diseases and finds the corresponding file.
    """
    disease_keywords = {
        "lupus": "lupus.txt",
        "diabetes": "diabetes_mellitus.txt",
        "asthma": "asthma.txt",
        "eczema": "eczema.txt",
        "covid": "covid-19.txt",
        "covid-19": "covid-19.txt",
        "coronavirus": "covid-19.txt",
    }

    query_lower = query.lower()

    for keyword, file_name in disease_keywords.items():
        if keyword in query_lower:
            full_path = os.path.join(data_folder, file_name)
            if os.path.exists(full_path):
                return full_path

    return None


if __name__ == "__main__":
    query = input("Enter your medical query: ")

    file_path = find_best_file(query)
    if not file_path:
        print("❌ Could not find a relevant dataset for your query.")
        exit()

    print(f"\n📂 Using data from: {file_path}")

    vectorstore = build_vector_store(file_path)
    chunks = retrieve_relevant_docs(query, vectorstore)

    print("\n📑 Top Relevant Info:")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n{i}. {chunk}")

    summary = analyze_chunks(chunks)

    print("\n📋 Final Summarized Answer:")
    print(summary)

    print("\n💬 Assistant Response:")
    print(generate_response(query, summary))
