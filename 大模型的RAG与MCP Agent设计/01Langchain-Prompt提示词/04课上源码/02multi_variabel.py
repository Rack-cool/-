from langchain_core.prompts import PromptTemplate

# 多个变量
template = """
{data}{location}天气怎么样？
"""

prompt = PromptTemplate.from_template(template=template)
print(prompt.format(data="今天", location="北京"))

prompt = PromptTemplate(input_variables=["data", "location"], template=template)
print(prompt.format(data="明天", location="上海"))



