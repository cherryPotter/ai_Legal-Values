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


def call_with_messages(query, model_name):
    print(f"model_name:{model_name}")
    messages = [
        #{'role': 'system', 'content': '你是一个法律专家。'},
        {'role': 'user', 'content': query}]
    
    if model_name.startswith("qwq-plus") or model_name.startswith("qwq-32b") or model_name.startswith("qwen3"):
        full_content = ""
        try:
            responses = Generation.call(model_name,
                               messages=messages,
                               temperature=0.0,
                               stream=True,
                               enable_search=False,
                               result_format='message',
                               incremental_output=True)
        
        
            for response in responses:
                full_content += response.output.choices[0].message.content
            #print(response.output.choices[0].message.content)
        except:
            print("ERROR rsp")
            pass
            
        return full_content
    
    else:
        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=messages,
                temperature=0.0,
                #response_format={"type": "json_object"},
            )
            json_string = completion.choices[0].message.content
            return json_string
        except:
            print("ERROR rsp")
            return ""



def chat(query, model_name):
    return call_with_messages(query, model_name)

