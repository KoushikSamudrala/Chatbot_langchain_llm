# Chatbot_langchain_llm
Simple chatbot created using langchain that can use LLM functionality built-in.
# FastAPI & LangChain LLM Chatbot

## Description

This project is an initial roadmap to build chatbots using modern day LLMs like ChatGPT or DeepSeek using API keys. The chatbot processes the user query to any LLM and gives us the response. This chatbot functionality can be integrated into any application easily, allowing the application to access the power of an LLM in making user interaction more intelligent.

## Features

- **FastAPI Backend:** A high-performance, asynchronous API to handle user requests.
- **LangChain Integration:** Uses LangChain for modular and easy interaction with different LLMs.
- **Dockerized Application:** Fully containerized with Docker for easy setup, deployment, and scalability.
- **Secure API Key Management:** Uses a `.env` file to keep secret API keys safe and out of the source code.

## Tech Stack

- **Backend:** Python, FastAPI
- **AI:** LangChain, Langchain-DeepSeek
- **Containerization:** Docker
- **Server:** Uvicorn

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd functional-chatbot
    ```

2.  **Create the environment file:**
    Create a file named `.env` in the root directory and add your API key:
    ```
    DEEPSEEK_API_KEY="sk-YourSecretKeyGoesHere"
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t chatbot-app .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run -p 8080:80 --env-file .env chatbot-app
    ```

## API Usage

Once the container is running, you can interact with the API at `http://localhost:8080/docs` or send a request using a tool like `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8080/chatbot' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Tell me a fun fact about the roman empire"
}'
