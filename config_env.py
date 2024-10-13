import os

# Access environment variables
llm_endpoint = os.environ["AZURE_OPENAI_LLM_ENDPOINT"]
embedding_endpoint = os.environ["AZURE_OPENAI_EMBEDDING_ENDPOINT"]
azure_openai_version = os.environ['AZURE_OPENAI_VERSION']
api_key = os.environ['AZURE_OPENAI_API_KEY']


vector_store_name = os.getenv('VECTOR_STORE_NAME', 'VS-final')
low_temp_param = float(os.getenv('LOW_TEMP_PARAM', 0.3))
high_temp_param = float(os.getenv('HIGH_TEMP_PARAM', 0.7))


similarity_search_k= int(os.getenv('SIMILARITY_SEARCH_K', 5))
similarity_search_threshold = float(os.getenv('SIMILARITY_SEARCH_THRESHOLD', 0.65))
similarity_search_alpha = float(os.getenv('SIMILARITY_SEARCH_ALPHA', 0.7))