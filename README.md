# 🏥 MedIntel – AI-Powered Medical Query Assistant  

MedIntel is an AI-driven medical query assistant that retrieves, analyzes, and responds to user questions using curated medical datasets.  
It leverages **LangChain**, **FAISS**, and **Streamlit** to provide meaningful answers to medical queries with a user-friendly interface.  

⚠️ **Disclaimer**: MedIntel is for **educational purposes only**. It should **not** be used as a substitute for professional medical advice, diagnosis, or treatment.  

---

## ✨ Features  
- 🔍 **Retriever Agent** – Finds relevant information from disease datasets  
- 📊 **Analyzer Agent** – Processes and interprets retrieved data  
- 💬 **Responder Agent** – Generates a clear response for the user  
- 📂 **Dataset Loader** – Automatically fetches Wikipedia articles for common diseases  
- 🌐 **Streamlit UI** – Clean web interface for interacting with the system  
- 📦 **Vector Database** – Uses FAISS for fast semantic search  

---

## 🚀 Quick Start  

## Clone the Repository  
git clone https://github.com/ankit5803/MedIntel.git
cd MedIntel

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

pip install -r requirements.txt
python main.py
streamlit run app.py
🌍 Deploy on Streamlit Cloud

Want to share your app online?

Go to Streamlit Cloud

Sign in with GitHub

Click New App

Select:

Repository: ankit5803/MedIntel

Branch: master (or main)

Main file: app.py

Click Deploy 🎉

Your app will be live at:

https://<your-username>-medintel.streamlit.app

📁 Project Structure
MedIntel/
│── agents/
│   ├── analyzer.py      # Analyzes retrieved data
│   ├── responder.py     # Generates final answers
│   └── retriever.py     # Loads datasets & builds FAISS vector store
│
│── data/                # Medical datasets (Wikipedia fetched)
│   ├── asthma.txt
│   ├── covid-19.txt
│   ├── diabetes_mellitus.txt
│   └── eczema.txt
│
│── app.py               # Streamlit UI
│── main.py              # CLI entry point
│── fetch_articles.py    # Script to fetch & save datasets
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── .gitignore

🔮 Roadmap

 Expand dataset with more diseases

 Add support for live web retrieval (Wikipedia / Mayo Clinic API)

 Enhance UI with themes and charts

 Add multilingual support (Hindi, Bengali, etc.)

👨‍💻 Author

Ankit Barik
