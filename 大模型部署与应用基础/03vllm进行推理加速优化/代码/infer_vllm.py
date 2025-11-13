from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
import time


# 实例化一个分词对象
tokenizer = AutoTokenizer.from_pretrained("models/Qwen/Qwen2___5-7B-Instruct", trust_remote_code=True)

# 定义文本输出的参数
sp = SamplingParams(temperature=0.5, top_p=0.5, repetition_penalty=1.05, max_tokens=4096)

# 实例化大模型
llm = LLM(model="models/Qwen/Qwen2___5-7B-Instruct", trust_remote_code=True)

prompt = "请讲一下周幽王烽火戏诸侯的故事。"
# 定义messages
messages = [
    {"role": "system", "content": "你是一个有用的助手。"},
    {"role": "user", "content": prompt}
    ]

# 使用分词器进行应用对话模板
text = tokenizer.apply_chat_template(
    messages, 
    tokenize=False,
    add_generation_prompt=True
)

# 记录开始时间
start_time = time.time()

outputs = llm.generate([text], sampling_params=sp)

# 记录结束时间
end_time = time.time()
# 计算生成时间
generate_time = end_time - start_time

for output in outputs:
    print(output.outputs[0].text)

# 计算每秒生成tokens的数量
generate_text= output.outputs[0].text
generate_tokens_num = len(tokenizer.tokenize(generate_text))
tokens_per_second = generate_tokens_num / generate_time

print(f"tokens per second: {tokens_per_second}")


