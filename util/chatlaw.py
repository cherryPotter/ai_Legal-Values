import requests
import json

def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """
    api_key = "YOUR_BAIDU_API_KEY"
    secret_key = "YOUR_BAIDU_SECRET_KEY"
        
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def chat(query):
        
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/chatlaw?access_token=" + get_access_token()
    
    payload = json.dumps({
            "messages": [{
                "role": "user",
                "content": query
            }],
            "temperature": 0.1,
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        rsp_json = json.loads(response.text)
        #print(rsp_json["result"])
        return rsp_json["result"]
    except:
        return ""
 