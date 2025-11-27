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

"""创建数据库"""
# from pymilvus import connections, db
# conn = connections.connect(host="127.0.0.1", port=19530)
# database = db.create_database("sample_db")


"""创建collection集合"""
# from pymilvus import CollectionSchema, FieldSchema, DataType
# from pymilvus import connections, db, Collection

# # 链接到milvus服务
# conn = connections.connect(host="127.0.0.1", port=19530)
# # 使用一个名为sample_db数据库
# db.using_database("sample_db")

# # 定义主键的字段"id", 类型是INT64, is_primary设置主键, auto_id开启自动增长
# id = FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True)

# # 定义embedding字段
# embedding = FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1024)

# # 创建集合模式，包含id 和 embedding ，可供描述信息
# schema = CollectionSchema(
#     fields=[id, embedding], 
#     description="Test"
# )

# # 定义集合的名称为"example"
# collection_name = "example"
# collection = Collection(name=collection_name, schema=schema)

"""创建索引"""
# from pymilvus import connections, db, Collection, utility

# # 链接到milvus服务
# conn = connections.connect(host="127.0.0.1", port=19530)
# # 使用一个名为sample_db数据库
# db.using_database("sample_db")

# # 定义索引参数，度量类型：余弦相似度
# index_param = {"metric_type": "COSINE"}

# # 获取名为example的集合
# collection = Collection("example")

# # 在名为"embedding"的字段上创建索引，参数为index_param
# collection.create_index(
#     field_name="embedding",
#     index_params=index_param
# )

# # 获取创建 的进度
# utility.index_building_progress("example")


# """插入数据"""
# from pymilvus import connections, db, Collection

# # 链接到milvus服务
# conn = connections.connect(host="127.0.0.1", port=19530)
# # 使用一个名为sample_db数据库
# db.using_database("sample_db")

# # 获取名为example的集合
# collection = Collection("example")

# # 插入数据
# mr = collection.insert([embeddings])

# print(mr)

"""向量搜索"""
from pymilvus import connections, db, Collection

# 链接到milvus服务
conn = connections.connect(host="127.0.0.1", port=19530)
# 使用一个名为sample_db数据库
db.using_database("sample_db")

# 获取名为example的集合
collection = Collection("example")

# 将集合加载到内存中，以便进行搜索
collection.load()

# 定义搜索参数
search_param = {"metric_type": "COSINE"}

# 执行搜索
results = collection.search(
    data=query_embedding.tolist(),  # 查询的向量
    anns_field="embedding",  # 要查询的字段
    param=search_param,   # 搜索参数
    limit=3,   #  返回最多的结果数量
    expr=None  # 过滤表达式，None表示不过滤
)

print(results)
