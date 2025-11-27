from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)


from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

# 定义输出模型
class EventDetails(BaseModel):
    event_name: str = Field(description="时间名称")
    date: str = Field(description="日期")

parser = PydanticOutputParser(pydantic_object=EventDetails)
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
# print("format_cinstrutions:", parser.get_format_instructions())
formatted_prompt = prompt.format(query="北京奥运会是什么时候开幕的？")
response = chat_model.invoke(formatted_prompt).content
print(response)
output = parser.parse(response)
print("output:", output)
