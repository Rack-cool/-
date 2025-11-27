from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10260/v1",
    model="Qwen2___5-7B-Instruct"
)

from langchain_core.prompts import PromptTemplate
template = """
你是一个与人类对话的机器人。
{chat_history}

Human:{human_input}
Chatbot:
"""

prompt = PromptTemplate(input_variables=["chat_history", "human_input"], template=template)

from langchain.memory import ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history")

from langchain.chains import LLMChain

llm_chain = LLMChain(llm=chat_model, prompt=prompt, verbose=True, memory=memory)

print(llm_chain.predict(human_input="可以介绍一下北京吗？"))
print(llm_chain.predict(human_input="我刚刚问了什么？"))









