from llama_cpp import Llama
llm = Llama(model_path="./models/ELYZA-japanese-Llama-2-7b-instruct-q4_K_M.gguf")
output = llm("Q: Name the planets in the solar system? A: ", max_tokens=2000, stop=["\n"], echo=True)
print(output)
# {'id': 'cmpl-d14faf5b-2e9a-48b2-951f-28aad52838a2', 'object': 'text_completion', 'created': 1697438976, 'model': './models/ELYZA-japanese-Llama-2-7b-instruct-q4_K_M.gguf', 'choices': [{'text': 'Q: Name the planets in the solar system? A: 1.冥王星,2地球,3火星,4木星,5金星', 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}], 'usage': {'prompt_tokens': 15, 'completion_tokens': 24,ens': 39}}