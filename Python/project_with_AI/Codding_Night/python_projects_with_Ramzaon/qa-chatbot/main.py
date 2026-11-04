import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model=genai.GenerativeModel(model_name="gemini-2.0-flash")
@cl.on_chat_start
async def chat_start():
    await cl.send_message("Enter your question or type 'exit' to quit:").send()
@cl.on_message
async def handle_message(message:cl.Message):
    prompt=message.content
    response=model.generate_content(prompt)
    response_text=response.text if hasattr(response,"text") else ""
    await cl.send_message(f"Response: {response_text}").send()
    
        

