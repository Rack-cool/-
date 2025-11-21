from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

# 实例化：逗号分隔的列表解析器
parser = CommaSeparatedListOutputParser()
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

print("format_instructions: ", parser.get_format_instructions())
formatted_prompt = prompt.format(query="列出五种水果。")

print("formatted_prompt:", formatted_prompt)

# 生成响应
response = chat_model.invoke(formatted_prompt).content
print(response)

# 解析响应
output = parser.parse(response)
print("output:", output)