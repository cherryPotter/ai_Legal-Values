from openai import OpenAI

client = OpenAI(
    api_key='YOUR_OPENAI_API_KEY')


def chat(p):
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            # model="gpt-3.5-turbo",
            temperature=0.0,
            messages=[
                #{"role": "system", "content": "你是一个中国的法律专家。"},
                {"role": "user", "content": p}
            ]
        )

        return completion.choices[0].message.content
    except:
        return "回答错误:{}"
