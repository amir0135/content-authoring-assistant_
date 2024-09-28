import os
import asyncio
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import logging

# Load environment variables
# Updated to load .env from the config directory
load_dotenv(dotenv_path="config/.env")

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.ERROR)

# Handle exceptions globally and log errors
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logging.error(f"Exception occurred: {exc}")
    return {"detail": "Internal Server Error"}

# Define request model
class TextGenerationRequest(BaseModel):
    prompt: str
    max_tokens: int = 100
    temperature: float = 0.7
    top_p: float = 0.9
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    domain: str = "general"
    audience: str = "general"
    tone: str = "neutral"
    keywords: str = ""

# Define the /generate-text/ endpoint
@app.post("/generate-text/")
async def generate_text(request: TextGenerationRequest):
    try:
        # Build the full prompt
        full_prompt = (
            f"Generate content for the domain '{request.domain}', "
            f"targeted at an audience of '{request.audience}', "
            f"with a tone of voice that is '{request.tone}'. "
            f"Here are some keywords: {request.keywords}. "
            f"Prompt: {request.prompt}"
        )

        # Call OpenAI's API for text generation
        response = await asyncio.to_thread(
            openai.ChatCompletion.create,  # Fixed API method path
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": full_prompt}],
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            frequency_penalty=request.frequency_penalty,
            presence_penalty=request.presence_penalty,
        )
        
        # Extract and convert the generated text to UTF-16
        generated_text = response.choices[0].message["content"]
        utf16_text = generated_text.encode('utf-16')

        # Return the generated text as UTF-16
        return {"generated_text": utf16_text.decode('utf-16')}
    
    except Exception as e:
        logging.error(f"Error during text generation: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")