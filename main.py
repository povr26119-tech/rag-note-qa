from vector_store import load_index
from embeddings import SiliconFlowEmbedding
from rag import ask
from llm import NO_ANSWER

index = load_index("index.json")
emb = SiliconFlowEmbedding()

while True:
    question = input("问题：").strip()
    if question == "":
        continue
    if question == "exit":
        break

    try:
        reply, results = ask(question, index, emb)
    except Exception as e:
        print(f"出错了：{e}")
        continue

    print(reply)

    if NO_ANSWER not in reply:
        print("参考资料：")
        for item in results:
            print(f"  {item['cosine']:.3f}  {item['chunk'][:40].replace(chr(10), ' ')}")
