import json
from embeddings import SiliconFlowEmbedding
import numpy as np

MODEL = "BAAI/bge-m3"


def build_index(chunks, emb, model=MODEL):
    vectors = []
    for i, chunk in enumerate(chunks):
        vectors.append(emb.get_embedding(chunk, model))
        print(f"{i + 1}/{len(chunks)}")
    return {"model": model, "chunks": chunks, "vectors": vectors}


def save_index(index, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)


def load_index(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search(query_vec, index, k=3):
    score_chunks = []

    for chunk, vec in zip(index["chunks"], index["vectors"]):
        score_chunks.append({"chunk": chunk, "cosine": cosine(query_vec, vec)})

    return sorted(score_chunks, reverse=True, key=lambda x: x["cosine"])[:k]
