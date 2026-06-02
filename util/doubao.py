#encoding=utf-8

from openai import OpenAI


client = OpenAI(
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key
    api_key="YOUR_DOUBAO_API_KEY",
)


def chat(query, model_name):

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": query},
            ],
        temperature=0.0,
    )
    result = completion.choices[0].message.content
    
    return result

