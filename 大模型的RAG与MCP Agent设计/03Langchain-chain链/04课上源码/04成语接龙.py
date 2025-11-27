from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

# 创建聊天模板，包含占位符topic
from langchain.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("""
接下来的四字成语必须以上一个成语“{pre_cy}”的最后一个字为开头。
例如：上一个成语是“兴高采烈”，那么下一个成语应该是以“烈”开头的成语。
请给出成语“{pre_cy}”接下来的接龙成语：
""")

# 创建一个字符串输出解析器
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

# 构造一个链，依次包含提示模板、语言模型，输出解析器
chain = prompt | chat_model | output_parser

while True:
    cy = input("给出成语：")
    init_cy = cy
    print("AI回答：", chain.invoke({"pre_cy": init_cy}))







