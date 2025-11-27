from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate


# 创建一个系统消息，用于定义机器人的角色
system_message = SystemMessagePromptTemplate.from_template("你是一个有用的助手,帮助用户学习编程。")
# 添加一些额外的需要存储的信息，比如时间戳
system_message.additional_kwargs = {
    "timestamp": "2024",
    "source": "system"
}

# 创建一个人类的消息，user消息
hunman_message = HumanMessagePromptTemplate.from_template("用户问：{user_question}")


# 创建一个AI消息
ai_message = AIMessagePromptTemplate.from_template("")


chat_message = ChatPromptTemplate.from_messages([
    system_message,
    hunman_message,
    ai_message
])

user_input = "怎么学习python？"
print(chat_message.format(user_question=user_input))


