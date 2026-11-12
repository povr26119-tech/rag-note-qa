from vector_store import load_index, search, MODEL
from embeddings import SiliconFlowEmbedding
from llm import answer

NO_ANSWER = "资料里没有相关内容"
index = load_index("index.json")
emb = SiliconFlowEmbedding()

while True:
    question = input("问题：").strip()
    if question == "":
        continue
    if question == "exit":
        break
    query_vec = emb.get_embedding(question, MODEL)
    results = search(query_vec, index, k=3)
    chunks = [item["chunk"] for item in results]
    try:
        reply = answer(question, chunks)
    except Exception as e:
        print(f"出错了：{e}")
        continue

    print(reply)
    if NO_ANSWER not in reply:
        print("参考资料：")
        for item in results:
            print(f"  {item['cosine']:.3f}  {item['chunk'][:40].replace(chr(10), ' ')}")
