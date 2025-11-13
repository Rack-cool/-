import requests     #用于发送HTTP请求
import json
# 设置请求的地址
url = "https://api.siliconflow.cn/v1/chat/completions"     #设置API的完整端点url

# 定义请求数据
data = {
    "model": "Qwen/Qwen2.5-7B-Instruct",     #指定模型
    "messages": [              #对话消息列表
        {
            "role": "system",
            "content": "你是一个卖萌的助手"
        },
        {
            "role": "user",
            "content": "讲一个笑话"
        }
    ],
    "max_tokens":150,
    # 流式输出
    "stream":True
}

#设置请求头
headers = {
    # api密钥
    "Authorization": "Bearer sk-keluyynkrgpraneyqclrzkcaychsplskqduzljsfykkaqwba",
    #指定请求数据为json格式
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)
# 非流式输出
# print(response.text)



# 流式输出用for循环
if response.status_code == 200:
    for chunk in response.iter_content(chunk_size=None):
        print(chunk.decode("utf-8"))
else:
    print(f"请求失败，状态码: {response.status_code}")
    print(response.text)
