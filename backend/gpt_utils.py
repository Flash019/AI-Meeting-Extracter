from groq import Groq
from dotenv import load_dotenv
import os 
load_dotenv()


client = Groq(api_key=os.getenv("Groq_API_KEY"))

def analyze_audio(transcript):
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "system", "content": "You are an expert audio analysis assistant."},
            {"role": "user", "content": f"""Here is an audio transcript:
{transcript}

Summarize the key points, list action items, decisions made, and generate a follow-up email."""}
        ]
    )
    return response.choices[0].message.content
    