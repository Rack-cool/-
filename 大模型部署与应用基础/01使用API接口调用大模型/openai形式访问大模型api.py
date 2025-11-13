from openai import OpenAI

api_key = "sk-keluyynkrgpraneyqclrzkcaychsplskqduzljsfykkaqwba"   #API密钥
base_url = "https://api.siliconflow.cn/v1"     #API的基础URL
client = OpenAI(api_key= api_key,base_url=base_url)    #实例化openai


# # 发送请求到GPT模型，非流式输出
# response = client.chat.completions.create(         #调用聊天补全接口创建响应
#     model ="Qwen/Qwen2.5-7B-Instruct",            #选择模型
#     messages = [
#         {"role": "system","content": "你是一个卖萌的助手"},  #设置对话消息
#         {"role": "user","content": "讲一个笑话"}
#     ],
#     max_tokens = 150,        #设置最大输出token数
#     # stream决定（非）流式输出
#     stream = False
# )
#
# print(response)



# 发送请求到GPT模型，非流式输出
response = client.chat.completions.create(
    model ="Qwen/Qwen2.5-7B-Instruct",
    messages = [
        {"role": "system","content": "你是一个卖萌的助手"},
        {"role": "user","content": "讲一个笑话"}
    ],
    max_tokens = 150,
    # stream决定（非）流式输出
    stream = True
)

for chunk in response:
    print(chunk)

