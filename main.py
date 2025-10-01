import os
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain.prompts import ChatPromptTemplate
from pydantic import BaseModel
from dotenv import load_dotenv


#loading the env variables from .env file
load_dotenv()
#retrieve the api key from the .env file
api_key=os.getenv("DEEPSEEK_API_KEY")

# Create the FastAPI app object
app = FastAPI()

# Pydantic model to define the structure of a request
class TextInput(BaseModel):
    text: str

# A simple endpoint to check if the server is running
@app.get("/")
async def root():
    return {"message": "Server is running"}

# The main endpoint for our chatbot
@app.post("/chatbot")
async def chatbot(text: TextInput):
    # --- The AI logic will go here ---
    # 1. Initialize the LLM
    #llm = ChatOpenAI(openai_api_key=api_key) ##llm model initialization
    llm = ChatDeepSeek(model="deepseek-chat", api_key=api_key)
    # 2. Create the prompt template
    prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. Answer the following question: {user_query}") ##creating a prompt template for the llm input from the user
     # 3. Create the chain
    chain = prompt | llm

    # 4. Invoke the chain with the user's text
    response = chain.invoke({"user_query":text.text}) ##key_value pairs
    
    
    
    return {"response": response.content}