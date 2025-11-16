from langchain_core.prompts import PromptTemplate


# 定义一个包含单个变量的模板字符串
template = """
今天{location}天气怎么样？
"""

# 方式一：
# 使用PromptTemplate类从模板字符串中创建一个提示对象
prompt = PromptTemplate.from_template(template=template)
# format方法填入变量
print(prompt.format(location="北京"))

# 方式二：
# 创建PromptTemplate对象来显式的输入变量和模板字符串
prompt = PromptTemplate(input_variables=["location"], template=template)
print(prompt.format(location="上海"))

