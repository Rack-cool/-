from langchain_openai import ChatOpenAI


chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from pydantic import BaseModel, Field
class Action(BaseModel):
    action: str = Field(description="要采取的操作")
    action_input: str = Field(description="输入的操作")

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
parser = PydanticOutputParser(pydantic_object=Action)
prompt = PromptTemplate(
    template="回答用户查询。\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    # 获取解析器的提示词
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
prompt_value = prompt.format_prompt(query="黑悟空是谁？")

bad_response = '{"action":"search"}'

# 修复解析器
from langchain.output_parsers import OutputFixingParser
fix_parser = OutputFixingParser.from_llm(parser=parser, llm=chat_model, max_retries=1)
try:
    fix_result = fix_parser.parse(bad_response)
    print(fix_result)
except Exception as e:
    print("修复解析器发生错误：", e)

# 重试解析器
from langchain.output_parsers import RetryWithErrorOutputParser
retry_parser = RetryWithErrorOutputParser.from_llm(parser=parser, llm=chat_model, max_retries=1)
try:
    retry_result = retry_parser.parse_with_prompt(bad_response, prompt_value)
    print(retry_result)
except Exception as e:
    print(e)
