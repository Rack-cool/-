from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 加载TXT文档
text_loader = TextLoader("黑悟空.txt", encoding="UTF-8")
documents = text_loader.load()

# 定义递归字符分割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ".", ",", "，", "。", ""]
)


# 开始分割
splits_docs = text_splitter.split_documents(documents)
# print(splits_docs)
for i, chunk in enumerate(splits_docs):
    print(f"Chunk {i+1}: \n {chunk}\n")

