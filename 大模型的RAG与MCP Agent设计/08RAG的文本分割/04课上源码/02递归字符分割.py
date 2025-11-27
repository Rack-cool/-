# from langchain.text_splitter import RecursiveCharacterTextSplitter

# text = "在西天取经的几百年前黑风山上有一只黑熊精占山为王，自称黑风大王。"
# splitter = RecursiveCharacterTextSplitter(chunk_size=15, chunk_overlap=3)
# chunks = splitter.split_text(text)
# print(chunks)


"""对中文优化"""
from langchain.text_splitter import RecursiveCharacterTextSplitter

text = "在西天取经的几百年前黑风山上有一只黑熊精占山为王，这里只是为了占位没什么用，自称黑风大王。"
splitter = RecursiveCharacterTextSplitter(chunk_size=15, chunk_overlap=3, separators=[
    "\n\n", "\n", " ", ".", ",", "，", "。", ""])
chunks = splitter.split_text(text)
print(chunks)
