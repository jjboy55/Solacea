import os
from openai import OpenAI
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_LLM = OpenAI(api_key=OPENAI_KEY)
OPENAI_MODEL = "gpt-4o-mini"
LLAMA_OPENAI = OpenAI(model=OPENAI_MODEL, api_key=OPENAI_KEY)
EMBED_OPENAI = OpenAIEmbedding(api_key=OPENAI_KEY)
