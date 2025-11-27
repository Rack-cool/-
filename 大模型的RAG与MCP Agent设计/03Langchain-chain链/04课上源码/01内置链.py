from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
# 创建一个系统消息，定义机器人角色
system_msg = SystemMessagePromptTemplate.from_template(
    "你是一个有用的机器人。"
)
# 创建一个人类消息
human_msg = HumanMessagePromptTemplate.from_template(
    "{user_question}"
)
# 将模板结合成一个完整的聊天提示
chat_prompt = ChatPromptTemplate.from_messages([
    system_msg,
    human_msg
])

from langchain.chains.llm import LLMChain

# # 在旧版本中
# # 创建一个LLMChain
# llm_chain = LLMChain(llm=chat_model, prompt=chat_prompt, verbose=True)
# # 测试
# response = llm_chain("你好")
# print(response)

# 新版本
# runnableSequence 链
chain = chat_prompt | chat_model
response = chain.invoke({"user_question": "你好"}).content
print(response)







