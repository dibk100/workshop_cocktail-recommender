import os
from dotenv import load_dotenv
load_dotenv()

# ========================================
# Hugging Face Qwen2.5-VL 모델 설정
# ========================================
HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "Qwen/Qwen2.5-VL-3B-Instruct")
HF_DEVICE = os.getenv("HF_DEVICE", "cuda")  # "cuda" 또는 "cpu"
HF_TORCH_DTYPE = os.getenv("HF_TORCH_DTYPE", "float16")

# ========================================
# Neo4j DB 설정 (GraphRAG)
# ========================================
# 환경변수 확인
# NEO4J_URI = os.getenv("NEO4J_URI")
# NEO4J_USER = os.getenv("NEO4J_USER") 
# NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

# ========================================
# 기타 설정
# ========================================
MAX_GENERATION_LENGTH = int(os.getenv("MAX_GENERATION_LENGTH", 256))
