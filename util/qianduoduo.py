from openai import OpenAI
#import openai

client = OpenAI(
    api_key='YOUR_QIANDUODUO_API_KEY',
    base_url="https://api2.aigcbest.top/v1")


def chat(p, model_name):
    print(f"qianduoduo:{model_name}")
    completion = client.chat.completions.create(
        model=model_name,
        temperature=0.0,
        messages=[
            {"role": "user", "content": p}
        ]
    )

    return completion.choices[0].message.content
