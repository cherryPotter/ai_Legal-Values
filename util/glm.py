#encoding=utf-8
from zhipuai import ZhipuAI
import json

client = ZhipuAI(api_key="YOUR_ZHIPU_API_KEY")


def chat(query, model_name):
    print(f"model_name:{model_name}")
    response = client.chat.completions.create(
        model=model_name,
        temperature=0.0,
        messages=[
            {"role": "user", "content": query}
        ],
        response_format = {'type': 'json_object'},
    )
    rsp = response.choices[0].message.content
    return rsp