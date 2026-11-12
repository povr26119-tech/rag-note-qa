from utils import load_chunks
from embeddings import SiliconFlowEmbedding
from vector_store import build_index, save_index

chunks = load_chunks("data/tinyrag_readme.md")
index = build_index(chunks, SiliconFlowEmbedding())
save_index(index, "index.json")