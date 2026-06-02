#encoding=utf-8
import requests
import json
import time
import csv



def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    api_key="YOUR_BAIDU_API_KEY"
    secret_key="YOUR_BAIDU_SECRET_KEY"

    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_3_70b?access_token=" + get_access_token()


def chat(query, model_name="meta-llama-3-70b"):
    history = {"messages": [], "temperature": 0.0}
    history["messages"].extend([{
            "role": "user",
            "content": query
        }])

    payload = json.dumps(history)
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    resp_str = ""
    try:
        resp_str = (json.loads(response.text))['result']
    except:
        print(f"response error:\t{response}")

    return resp_str

#print(chat("hello. Answer in Enligh."))