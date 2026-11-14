from vector_store import search
from llm import answer

def ask(question: str, index, emb, k: int = 3):
    query_vec = emb.get_embedding(question, index["model"])
    results = search(query_vec, index, k=k)
    chunks = [item["chunk"] for item in results]
    reply = answer(question, chunks)

    return reply, results