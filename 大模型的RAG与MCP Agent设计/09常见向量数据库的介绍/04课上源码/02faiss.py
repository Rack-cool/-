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

# FAISS向量数据库
import faiss
import numpy as np

# 转换为numpy数组
embeddings = np.array(embeddings)

# 初始化FAISS索引
index = faiss.IndexFlatIP(1024)  # 使用内积进行检索, 把内积做了标准化，于是结果等于余弦相似度
# index = faiss.IndexFlatL2(1024)  # 使用L2距离检索

# 将向量添加到索引
index.add(embeddings)

# 保存索引到磁盘
# faiss.write_index(index, "db/faiss_index.index")

# 查询并检索，返回最相似的3个结果
D, I = index.search(query_embedding, k=3)

# 输出
print(f"最相似的句子索引：{I}")
print(f"对应的相似度/距离：{D}")

