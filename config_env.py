import os

# Access environment variables
llm_endpoint = os.environ["AZURE_OPENAI_LLM_ENDPOINT"]
embedding_endpoint = os.environ["AZURE_OPENAI_EMBEDDING_ENDPOINT"]
azure_openai_version = os.environ['AZURE_OPENAI_VERSION']
api_key = os.environ['AZURE_OPENAI_API_KEY']