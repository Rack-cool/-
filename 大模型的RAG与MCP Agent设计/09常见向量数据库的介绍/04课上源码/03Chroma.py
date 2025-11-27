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

# 初始化Chroma
from chromadb import Client, PersistentClient

client = Client()

# 持久化
# client = PersistentClient(path="db")

# 创建集合，hnsw:图索引  space:距离度量空间  
collection = client.create_collection("example_collection", metadata={"hnsw:space": "cosine"})

# 插入向量
collection.add(
    ids=["vec0", "vec1", "vec2"],
    embeddings=embeddings
)

# 查询
results = collection.query(
    query_embeddings=query_embedding,
    n_results=3
)

print(f"最相似的句子索引: {results['ids']}")
print(f"对应的相似度/距离: {[1-d for d in results['distances'][0]]}")
