import os
from dotenv import load_dotenv

load_dotenv()  # load keys from .env

# LangSmith is automatically picked up via env variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"

