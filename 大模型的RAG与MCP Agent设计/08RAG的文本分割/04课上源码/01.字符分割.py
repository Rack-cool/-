from langchain.text_splitter import CharacterTextSplitter


text = "在西天取经的几百年前黑风山上有一只黑熊精占山为王，自称黑风大王。"
splitter = CharacterTextSplitter(chunk_size=15, chunk_overlap=2, separator="")
chunks = splitter.split_text(text)
print(chunks)
