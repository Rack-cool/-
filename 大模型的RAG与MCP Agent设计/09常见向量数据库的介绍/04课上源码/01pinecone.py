from sentence_transformers import SentenceTransformer

# 加载embedding模型
model = SentenceTransformer("models/AI-ModelScope/bge-large-zh-v1___5")

# 设置输入文本
texts = ["院子里有一只可爱的小猫", "厨房里有一只黑色的猫",  "大模型真简单"]

# 向量化, embeddings是一个2D的数组，形状(3, 1024)，3表示3句话，1024是每句话转成的向量
embeddings = model.encode(texts)
# print(embeddings.shape)

# 假设我们想查询："黑色的猫在哪？"
query_embedding = model.encode(["黑色的猫在哪？"])


from pinecone import Pinecone, ServerlessSpec
# 初始化Pinecone数据库
pc = Pinecone(api_key="pcsk_5jg1Re_Pmog8pbnb9ZCjAk3f2ver6BfcXYAqh5oqUd5shhkSxeVdAs52VgajqV6CLaGjGj")
index_name = "example"

# 创建数据库(创建时打开，其他时候注释)
# pc.create_index(
#     name=index_name,
#     dimension=1024, 
#     spec=ServerlessSpec(
#         cloud="aws",
#         region="us-east-1"
#     ),
#     metric="cosine"
# )

# # 向索引中插入向量（创建或者插入的时候打开，其他时候注释，查询的时候注释）
# index = pc.Index(index_name)
# index.upsert(
#     vectors=[
#         {"id": "vec1", "values": embeddings[0].tolist()},
#         {"id": "vec2", "values": embeddings[1].tolist()},
#         {"id": "vec3", "values": embeddings[2].tolist()},
#     ]
# )


# # 查询
# # 获取数据库的索引对象
# index = pc.Index(index_name)

# # 查询相似向量
# query_results = index.query(
#     top_k=3,   # 返回前几个最相关的
#     vector=query_embedding[0].tolist(),
#     include_values=False  # 包含返回向量的实际值
# )

# # 打印返回结果
# print(query_results)


# 删除example
pc.delete_index(index_name)

