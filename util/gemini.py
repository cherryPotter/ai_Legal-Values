#encoding=utf-8
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def chat(query, model_name):
    response = client.chat.completions.create(
        model=model_name,
        n=1,
        temperature=0.0,
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )

    return response.choices[0].message.content
