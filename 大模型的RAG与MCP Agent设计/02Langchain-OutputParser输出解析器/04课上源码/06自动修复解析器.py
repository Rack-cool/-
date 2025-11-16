from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
class Person(BaseModel):
    name: str = Field(description="姓名")
    age: int = Field(description="年龄")

# 顶一个格式不正确的输出（注意：这个代表大模型的输出结果）
misformatted = "{'name': 'John', 'age': 30}"
parser = PydanticOutputParser(pydantic_object=Person)
try:
    output = parser.parse(misformatted)
    print("output:", output)
except Exception as e:
    print(e)


from langchain.output_parsers import OutputFixingParser
new_parser = OutputFixingParser.from_llm(parser=parser, llm=chat_model)
output = new_parser.parse(misformatted)
print("output:", output)
