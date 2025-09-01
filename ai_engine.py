#AAH3 web_ui groq
import os
import requests

def get_groq_response(user_input):
    api_key = os.getenv("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192", 
        "messages": [
            {"role": "system", "content": "You are a professional summarizer. Your task is to convert any long text into clear, concise and brief bullet points focused on the main ideas. Be objective, and avoid casual tone."},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print("Groq Status Code:", response.status_code)
        print("Groq Raw Response:", response.text)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return "Groq API error: " + response.text

    except Exception as e:
        return f"Exception occurred: {e}"
