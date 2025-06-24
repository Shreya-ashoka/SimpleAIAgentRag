# Simple AI Agent RAG for Pizza Restaurant Reviews

This project is a Retrieval-Augmented Generation (RAG) AI agent that answers questions about a pizza restaurant using real customer reviews.

## Features

- Uses LangChain and Ollama for LLM and embeddings.
- Retrieves the most relevant reviews from a vector database (Chroma).
- Answers user questions based on real customer feedback.

## Project Structure

- `main.py` — Main script for running the Q&A loop.
- `vector.py` — Handles review embeddings and vector database setup.
- `realistic_restaurant_reviews.csv` — CSV file with restaurant reviews.
- `chrome_langchain_db/` — Directory for the Chroma vector database.

## Setup

1. **Install dependencies**  
   Make sure you have Python 3.10+ and install required packages:
   ```powershell
   pip install langchain langchain_ollama langchain_chroma pandas
   ```

2. **Download Ollama and models**  
   - Install [Ollama](https://ollama.com/) and ensure it’s running.
   - Download the required models (`llama3.2` and `nomic-embed-text`).

3. **Prepare the data**  
   - Ensure `realistic_restaurant_reviews.csv` is present in the project directory.

## Usage

Run the main script:
```powershell
python main.py
```
- Enter your question about the pizza restaurant.
- The AI will retrieve relevant reviews and answer your question.
- Type `q` to quit.

## How it Works

- Loads reviews and creates embeddings.
- Stores/retrieves embeddings using Chroma.
- Uses a prompt template to instruct the LLM.
- Retrieves top 5 relevant reviews for each question and generates an answer.

## Notes

- The first run may take longer as it builds the vector database.
- Make sure Ollama is running before starting the script.

---

**Author:** Your Name  
**Date:** June 24, 2025
