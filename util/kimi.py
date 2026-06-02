#encoding=utf-8
from openai import OpenAI
import time
import csv
 
MOONSHOT_API_KEY='YOUR_MOONSHOT_API_KEY'

client = OpenAI(
    api_key = MOONSHOT_API_KEY,
    base_url = "https://api.moonshot.cn/v1",
)


def chat(query, model_name):
    history = []
    history.extend([
        {"role": "user", "content": query}
    ])
    # print(f"before {query} history:\t{history}")

    result = ""
    completion = client.chat.completions.create(
        model=model_name,
        messages=history,
        temperature=0.0,
        max_tokens=1024 * 32,
    )

    message = completion.choices[0].message

    return message.content
