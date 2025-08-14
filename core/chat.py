import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)
def query(text):
    try:
        # Clean up any special characters that might confuse the model
        cleaned_text = text.replace("*", "")
        
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(cleaned_text)
        return response.text
    except Exception as e:
        print(f"Error during API request: {e}")
        return None
