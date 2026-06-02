# encoding=utf-8
from http import HTTPStatus
from dashscope import Generation
import dashscope
from openai import OpenAI

dashscope.api_key = "YOUR_DASHSCOPE_API_KEY"
client = OpenAI(
    api_key=dashscope.api_key,
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)


def chat(query):

    messages = [{'role': 'system',
                    'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': query}]
    response = dashscope.Generation.call(
        model="farui-plus",
        messages=messages,
        temperature=0.1,
        result_format='message',
    )
    
    if response.status_code == HTTPStatus.OK:
        rsp = response.output.choices[0]['message']['content']
        # logger.error(f"rsp:{rsp}")
        return rsp
    else:
        print(
            '[ERROR] Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
        return ""



