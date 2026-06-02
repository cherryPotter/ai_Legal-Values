#encoding=utf-8
import json
#import jieba
from collections import Counter
import os
import sys
import csv
import time
import re


def json2item(input_rsp):
    input_rsp = input_rsp.replace("`", "")
    input_rsp = input_rsp.replace("json", "")
    input_rsp = input_rsp.replace("\n", "")
    js = json.loads(input_rsp)
    return js['rating'], js["rating_reason"], js["preferred_value_selection"], js['preferred_value_selection_reason']
'''


def extract_code_blocks(text):
    """
    提取所有以 ``` 开头、``` 结尾的内容（不含首尾反引号）。
    返回一个列表，列表元素是各个匹配块之间的字符串。
    """
    pattern = re.compile(r"{(.*?)}", re.DOTALL)
    return pattern.findall(text)

def json2item(input_rsp):
    ret_list = extract_code_blocks(input_rsp)
    for i in ret_list:
        #input_rsp = input_rsp.replace("`", "")
        #input_rsp = input_rsp.replace("json", "")
        js_i = "{" + i + "}"
        js = json.loads(js_i)
        last_key, last_value = list(js.items())[-1]
        return js['rating'], js["rating_reason"], js["preferred_value_selection"], last_value
'''

def process_each_model(model_name, input_fn, out_fn):
    with open(out_fn, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        with open(input_fn, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # 跳过标题行

            for row in csv_reader:
                if len(row) != 6 or len(row[2]) == 0:
                    continue

                successful_attempts = 0
                failure_count = 0

                while successful_attempts < N:
                    question = ""
                    question = row[2] + '''\n reply in json format, e.g. {"rating": 3, "rating_reason": "xxx", "preferred_value_selection": "A", "preferred_value_selection_reason": "xxx"} Note: when answering preferred_value_selection the former choice is A, the latter is B.'''
                    question += "Note: The last is preferred_value_selection_reason."

                    #question += "Answer in Enligh. Answer only in JSON!!! dont add other explanation or prefix"
                    #print(question)

                    if out_fn.endswith("_cn.csv"):
                        question = row[2] + '''\n 请以 JSON 格式回复，例如：{"rating": 3, "rating_reason": "xxx", "preferred_value_selection": "A", "preferred_value_selection_reason": "xxx"} 注意：在回答 preferred_value_selection 时，前者选项为 A，后者选项为 B。'''
                        #question += "注意：最后一项是 preferred_value_selection_reason。"

                    rsp = chat(question, model_name)

                    if len(rsp) > 5:
                        try:
                            rsp_js_item = json2item(rsp)
                            print(f"q: {row[0]}\t{row[1]} [{successful_attempts}]\trsp:{rsp}")
                            print("-" * 36)
                            print(f"rsp_js_item: {rsp_js_item}\n")
                            print("=" * 36)

                            out_row = list(row) + list(rsp_js_item) + [rsp]
                            writer.writerow(out_row)
                            
                            successful_attempts += 1
                            failure_count = 0  # 成功后重置失败计数
                        except Exception as e:
                            failure_count += 1
                            print(f"[JSON解析失败] failure_count={failure_count} 错误：{e} 内容：\n{rsp}")
                            print("=" * 36)

                            if failure_count >= max_failures:
                                print(f"[跳过此问题] 因为JSON解析已连续失败 {max_failures} 次。\n")
                                print("=" * 36)
                                break  # 超过失败次数，跳过此问题
                    else:
                        print("[无效回应] 回复内容过短，重试。")


if __name__ == "__main__":
    global N, max_failures
    N = 10
    max_failures = 5

    input_fn = "question_v3.csv"
    #out_fn = "result.csv"
    input_model_name = sys.argv[1]
    lang = sys.argv[2]

    if lang == "cn":
        input_fn = "question_v3_cn.csv"
    
    #model_name_list = ["chatglm", "ernie-4.0", "ernie-3.5", "kimi", "doubao", "deepseek-r1", "qwen-max"]
    
    model_name_list = [input_model_name]
    print(f"model_name_list: {model_name_list}")

    for model_name in model_name_list:
        print(f"model_name:{model_name}")
        if model_name == "meta-llama-3-70b":
            from util.llama_3_70b import *
        elif model_name.startswith("glm"):
            from util.glm import *
        elif model_name.startswith("ernie"):
            from util.ernie import *
        elif model_name.startswith("kimi") or model_name.startswith("moonshot"):
            from util.kimi import *
        elif model_name.startswith("doubao"):
            from util.doubao import *
        elif model_name.startswith("deepseek-r1"):
            from util.deepseek_r1 import *
        elif model_name == "deepseek-v3":
            from util.deepseek_v3 import *
        elif model_name.startswith("qw"):
            from util.qwen import *
        elif model_name.startswith("claude") or model_name.startswith("grok") or model_name.startswith("o3") or model_name.startswith("o4"):
            from util.qianduoduo import *
        elif model_name.startswith("MiniMax"):
            from util.minimax import *

        elif model_name.startswith("gpt") or model_name.startswith("o1"):
            from util.chatgpt import *
        #elif model_name == "chatgpt_4_1":
        #    from util.chatgpt_4_1 import *
        elif model_name == "farui":
            from util.farui import *
        elif model_name.startswith("llama-4") or model_name.startswith("meta-llama"):
            #from util.llama_3_70b import *
            from util.ernie import *
        elif model_name.startswith("gemini"):
            from util.gemini import *
        
        if lang == "cn":
            process_each_model(model_name, input_fn, f"./result_v5/{model_name}_{lang}.csv")
        else:
            process_each_model(model_name, input_fn, f"./result_v5/{model_name}.csv")