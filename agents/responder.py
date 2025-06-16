# agents/responder.py

from transformers import pipeline

# We'll use a text generation pipeline for friendly responses
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_response(user_query, summary):
    prompt = (
        f"The user asked: '{user_query}'\n"
        f"Based on this summarized medical information: '{summary}',\n"
        f"Compose a clear, helpful, and friendly medical assistant response."
    )

    result = generator(prompt, max_length=200)[0]["generated_text"]
    return result
