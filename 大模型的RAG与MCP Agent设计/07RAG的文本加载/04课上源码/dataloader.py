# """加载TXT"""
# from langchain_community.document_loaders import TextLoader
# txt_loader = TextLoader("test.txt", encoding="UTF-8")
# txt_data = txt_loader.load()
# print(txt_data)


# """加载CSV"""
# from langchain_community.document_loaders import CSVLoader
# csv_loader = CSVLoader(file_path="test.csv", encoding="UTF-8")
# csv_data = csv_loader.load()
# print(csv_data)


# """加载PDF"""
# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("test.pdf")
# pages = loader.load_and_split()  # 按页面分割 PDF
# print(pages)


# """加载markdown"""
# from langchain_community.document_loaders import UnstructuredMarkdownLoader
# loader = UnstructuredMarkdownLoader(file_path="test.md", mode="elements")
# data = loader.load()
# print(data)

# """加载JSON"""
# from langchain_community.document_loaders import JSONLoader
# loader = JSONLoader(file_path="test.json", jq_schema=".skills")
# data = loader.load()
# print(data)


"""加载HTML"""
from langchain_community.document_loaders import UnstructuredHTMLLoader
loader = UnstructuredHTMLLoader("test.html")
data = loader.load()
print(data)


from langchain_community.document_loaders import BSHTMLLoader
loader1 = BSHTMLLoader("test.html")
data1 = loader1.load()
print(data1)
