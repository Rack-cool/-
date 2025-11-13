from openai import OpenAI

# API密钥，基础的URL
api_key = "EMPTY"
base_url = "http://127.0.0.1:10222/v1"

# 将上面定义的内容创建openai实例
client = OpenAI(api_key=api_key, base_url=base_url)

# 发送请求，流式输出
response = client.chat.completions.create(
    model="Qwen2___5-7B-Instruct",
    messages=[
        {"role": "system", "content": "你是一个有用的助手。"},
        {"role": "user", "content": "讲一个小红帽的故事。"}
    ],
    max_tokens=4096,
    temperature=0.5, 
    top_p=0.5,
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content)
