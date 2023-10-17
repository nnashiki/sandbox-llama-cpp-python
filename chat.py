from llama_cpp import Llama
llm = Llama(model_path="./models/ELYZA-japanese-Llama-2-7b-instruct-q4_K_M.gguf")

# Chat形式の生成
output = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a helpful programing assistant."},
        {
            "role": "user",
            "content": "Q. Pythonでフィナボッチ数列を返す関数を実装してください。",
        },
    ],
    temperature=0.1,
    max_tokens=512,
)

print("=== OUTPUT (Create Chat Completion) ===")
print(output["choices"][0]["message"]["content"])
print("=== END ===")
