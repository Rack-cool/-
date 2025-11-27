from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(
    openai_api_key="EMPTY",
    base_url="http://127.0.0.1:10259/v1",
    model="Qwen2___5-7B-Instruct"
)

from langchain_community.document_loaders import TextLoader
loader = TextLoader("黑悟空.txt", encoding="utf-8")
docs = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter
# 块大小200字为一组，每组之间20字重叠
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
chunks = text_splitter.split_documents(docs)  # 分割成块

from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="models/AI-ModelScope/bge-large-zh-v1___5")

# 构建faiss向量存储
from langchain_community.vectorstores import FAISS
vs = FAISS.from_documents(chunks, embedding) # 将文本块转换为向量并且存储到FAISS

retriever = vs.as_retriever() #创建检索器用于从数据库中获取相关信息

from langchain.chains import RetrievalQA
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

system_msg = SystemMessagePromptTemplate.from_template(
    "根据以下已知的内容回答用户问题。\n  已知消息{context}"
)

huamn_msg = HumanMessagePromptTemplate.from_template(
    "用户问题：{question}"
)

chat_prompt = ChatPromptTemplate.from_messages([
    system_msg, huamn_msg
])

qa = RetrievalQA.from_chain_type(llm=chat_model, 
                                 chain_type="stuff", 
                                 retriever=retriever, 
                                 chain_type_kwargs={"prompt": chat_prompt})

user_question = "黑熊精自称为？"
related_docs = retriever.invoke(user_question)

# # 打印相关文档的内容
# for i, doc in enumerate(related_docs):
#     print(f"文档 {i+1}")
#     print(doc.page_content)
#     print("--" * 40)

print(qa.invoke(user_question))
