from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from enum import Enum
class Color(Enum):
    RED = "red"
    BLUE = "blue"
    YELLOW = "yellow"


from langchain.output_parsers import EnumOutputParser
from langchain_core.prompts import PromptTemplate

parser = EnumOutputParser(enum=Color)
prompt = PromptTemplate(
    template="回答用户查询，请直接输出颜色名称，如 'red', 'blue', 'yellow'。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
print("format_instructions:", parser.get_format_instructions())
formatted_prompt = prompt.format(query="香蕉是什么颜色的？")

response = chat_model.invoke(formatted_prompt).content
print(response)
output = parser.parse(response)
print("output:", output)
