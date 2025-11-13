import torch
import time
# 导入transformers库中的AutoModelForCausalLM（用于因果语言模型）和AutoTokenizer（自动化的分词工具）。
from transformers import AutoModelForCausalLM, AutoTokenizer

# 检查是否有可用的CUDA设备（即NVIDIA GPU），如果有，则设置为使用GPU，否则使用CPU。
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
# 使用预训练模型Qwen2.5-7B的分词器实例化tokenizer对象。
tokenizer = AutoTokenizer.from_pretrained("models/Qwen/Qwen2___5-7B-Instruct")
# 实例化一个预训练的因果语言模型，并将其移动到指定的device上执行。
model = AutoModelForCausalLM.from_pretrained("models/Qwen/Qwen2___5-7B-Instruct", torch_dtype=torch.float16).to(device)
# 设置对话的提示词。
prompt = "讲下周幽王烽火戏诸侯的故事"
# 定义对话历史，包括系统信息（指示助手的角色）和用户输入的提示。
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
# 使用分词器将对话历史转换为适用于模型输入的格式，并添加生成提示。
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# 对输入文本进行分词处理，并转换为PyTorch张量格式，然后移动到指定的device上执行。
model_inputs = tokenizer([text], return_tensors="pt").to(device)

# 记录开始时间
start_time = time.time()

# 使用模型生成新的token序列，最大生成新的token数量为512。
generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=4096,
)
# 记录结束时间
end_time = time.time()

# 计算生成时间
generate_time = end_time - start_time

# 截取生成的token序列，去除原始输入的部分。
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

# 计算生成的token的数量
generate_token_num = sum(len(ids) for ids in generated_ids)
# 计算每秒生成的token数量
token_per_second = generate_token_num / generate_time

# 将生成的token序列解码回文本，并忽略特殊token。
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

# 输出生成的响应文本。
print(response)
# 输出每秒生成token数量的结果
print(f"tokens per second: {token_per_second}")
