# agents/analyzer.py

from transformers import pipeline

# Initialize summarizer model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def analyze_chunks(chunks):
    """
    Summarizes the retrieved text chunks into a clean, final answer.
    """
    combined_text = " ".join(chunks)

    # Some models have a max token/character limit — keep it short
    if len(combined_text) > 1000:
        combined_text = combined_text[:1000]

    summary = summarizer(combined_text, max_length=150, min_length=40, do_sample=False)

    return summary[0]['summary_text']
