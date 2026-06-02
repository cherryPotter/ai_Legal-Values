# encoding=utf-8

import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_ANTHROPIC_API_KEY",
)

def chat(p, model_name):
    message = client.messages.create(
        model=model_name,
        max_tokens=1024,
        temperature=0.0,
        messages=[
            {"role": "user", "content": p}
        ]
    )
    ans = message.content
    return ans[0].text

