from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

# 创建聊天模板，包含占位符topic
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("说出一句包含{topic}的诗句")

# 创建一个字符串输出解析器
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# 构造一个链，依次包含提示模板、语言模型，输出解析器
chain = prompt | chat_model | output_parser

print(chain.invoke({"topic": "花"}))
