from openai import OpenAI
client = OpenAI(
    base_url='https://qianfan.baidubce.com/v2',
    api_key='YOUR_BAIDU_BCE_API_KEY'
)

def chat(query, model_name):
    print(f"model_name: {model_name}")
    response = client.chat.completions.create(
            model=model_name,
            temperature=0,
            messages=[
            {
                "role": "user",
                "content": query
            }
        ]
        )
    result = response.choices[0].message.content
    return result

#print(chat("hello"))