import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")

# Configure the Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name='gemini-2.0-flash')

def ask_gemini(prompt_text):
    response = model.generate_content(prompt_text)
    return response.text
