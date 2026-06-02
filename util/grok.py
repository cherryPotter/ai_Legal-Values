#encoding=utf-8
import os
from openai import OpenAI


client = OpenAI(
  api_key="YOUR_XAI_API_KEY",
  base_url="https://api.x.ai/v1",
)


def chat(query):
    completion = client.chat.completions.create(
          model="grok-3-beta",
          messages=[
            {"role": "user", "content": query}
          ]
        )
    result = completion.choices[0].message
    
    return result

print(chat("hello"))