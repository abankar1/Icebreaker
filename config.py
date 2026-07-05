"""Configuration settings for the Icebreaker Bot."""

import os

# watsonx.ai settings (credentials come from environment variables, never committed to git)
WATSONX_URL = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
WATSONX_PROJECT_ID = os.getenv("WATSONX_PROJECT_ID", "")
WATSONX_APIKEY = os.getenv("WATSONX_APIKEY", "")

# Model settings
LLM_MODEL_ID = "ibm/granite-4-h-small"
EMBEDDING_MODEL_ID = "ibm/slate-125m-english-rtrvr-v2"

# ProxyCurl API settings
PROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY", "")

# Local mock profile data (bundled with the repo so the demo works offline)
MOCK_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "mock_profile.json")

# Query settings
SIMILARITY_TOP_K = 5
TEMPERATURE = 0.0
MAX_NEW_TOKENS = 500
MIN_NEW_TOKENS = 1
TOP_K = 50
TOP_P = 1

# Node settings
CHUNK_SIZE = 400

# LLM prompt templates
INITIAL_FACTS_TEMPLATE = """
You are an AI assistant that provides detailed answers based on the provided context.

Context information is below:

{context_str}

Based on the context provided, list 3 interesting facts about this person's career or education.

Answer in detail, using only the information provided in the context.
"""

USER_QUESTION_TEMPLATE = """
You are an AI assistant that provides detailed answers to questions based on the provided context.

Context information is below:

{context_str}

Question: {query_str}

Answer in full details, using only the information provided in the context. If the answer is not available in the context, say "I don't know. The information is not available on the LinkedIn page."
"""
