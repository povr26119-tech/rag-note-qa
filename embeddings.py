from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()


class BaseEmbeddings:
    def __init__(self, path: str, is_api: bool):
        self.path = path
        self.is_api = is_api

    def get_embedding(self, text: str, model: str):
        raise NotImplementedError


class SiliconFlowEmbedding(BaseEmbeddings):
    def __init__(self, path: str = '', is_api: bool = True):
        super().__init__(path, is_api)
        if self.is_api:
            self.client = OpenAI(
                api_key=os.getenv("SILICONFLOW_API_KEY"),
                base_url="https://api.siliconflow.cn/v1",
            )

    def get_embedding(self, text: str, model: str = "BAAI/bge-m3"):
        if self.is_api:
            return self.client.embeddings.create(input=[text], model=model).data[0].embedding
        else:
            raise NotImplementedError