import streamlit as st
from rag import ask
from llm import NO_ANSWER
from vector_store import load_index
from embeddings import SiliconFlowEmbedding

@st.cache_resource
def get_resources():
    index = load_index("index.json")
    emb = SiliconFlowEmbedding()
    return index, emb

index, emb = get_resources()

st.title("笔记问答机器人")
question = st.chat_input("请输入你的问题")

if question:
    with st.chat_message("user"):
        st.write(question)
    with st.chat_message("assistant"):
        try:
            with st.spinner("思考中....."):
                reply, results = ask(question, index, emb)
        except Exception as e:
            st.error(f"出错了:{e}")
            st.stop()
        st.write(reply)
        if NO_ANSWER not in reply:
            with st.expander("参考资料"):
                for item in results:
                    st.write(f"{item['cosine']:.3f} {item['chunk'][:60]}")


