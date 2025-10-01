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


## Architecture

This application follows a simple, containerized microservice architecture.

┌───────────────────┐         ┌──────────────────────────────────────────────────┐
│                   │         │             Docker Container (on Port 8080)      │
│      User          ───────► │  FastAPI 🛎️ ───► LangChain 🔗 ───► LLM API 🧠  │
│                   │◄─────── ┤                                                  │
└───────────────────┘         └──────────────────────────────────────────────────┘

1.  A **User** sends a query to the FastAPI endpoint.
2.  **FastAPI** receives the request and passes it to the LangChain logic.
3.  **LangChain** formats the prompt and sends it to the external **LLM API** (e.g., DeepSeek).
4.  The response is sent back through the chain and returned to the user.

   
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

## API Usage

Once the container is running, you can interact with the API at `http://localhost:8080/docs` or send a request using a tool like `curl`.

**Example Request:**
```bash
curl -X 'POST' \
  'http://localhost:8080/chatbot' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Tell me a fun fact about the roman empire"
}'
 ```
## Example Response
```bash
{
  "response": "A fun fact about the Roman Empire is that they had a form of central heating called a hypocaust, where hot air from a furnace would circulate under floors and through walls to heat rooms and public baths!"
}
 ```
