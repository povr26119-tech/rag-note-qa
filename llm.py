from openai import OpenAI
from dotenv import load_dotenv
import os

NO_ANSWER = "资料里没有相关内容"

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
SYSTEM_PROMPT = {"role": "system",
                 "content": "请用纯文本回答。不要使用任何 Markdown 格式，包括加粗（两个星号）、标题、列表符号和代码块。"}


def chat(question: str) -> str:
    user_message = {"role": "user", "content": question}

    try:
        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[SYSTEM_PROMPT] + [user_message],
        )

    except Exception:
        raise

    reply = response.choices[0].message.content
    return reply


def answer(question: str, chunks: list[str]) -> str:
    parts = []
    for i, chunk in enumerate(chunks, 1):
        parts.append(f"【资料{i}】\n{chunk}")
    context = "\n\n".join(parts)

    prompt = f"""请只根据下面的资料回答问题。
如果资料里没有相关内容，请直接回答：{NO_ANSWER}。不要使用资料以外的知识。

{context}

问题：{question}"""
    return chat(prompt)