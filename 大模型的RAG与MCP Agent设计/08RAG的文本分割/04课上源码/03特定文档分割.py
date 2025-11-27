from langchain.text_splitter import MarkdownHeaderTextSplitter

text = """
# 第一章
在西天取经的几百年前，黑风山上。\n\n在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。在西天取经的几百年前，黑风山上。
# 第二章
测试。
"""

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
chunks = splitter.split_text(text)
print(chunks)
