from pydantic import BaseModel
from typing import Any, Dict, Optional

class PipelineState(BaseModel):
    """
    LangGraph 파이프라인 전체 상태 정의 및 저장하는 공간.
    """
    # -------------------
    # 사용자 입력
    # -------------------
    query: str

    # -------------------
    # LLM1 결과
    # -------------------
    task_type: Optional[str] = None           # Recommend / Description / Classification
    attributes: Optional[Dict[str, Any]] = {} # taste, alcohol_level, ingredients 등
    graph_query: Optional[str] = None         # Graph Query 준비 정보

    # -------------------
    # Graph Node 결과
    # -------------------
    graph_result: Optional[Any] = None        # 후보 칵테일 데이터 (Neo4j JSON, List 등)

    # -------------------
    # LLM2 결과
    # -------------------
    final_text: Optional[str] = None          # 최종 텍스트 response

    class Config:
        arbitrary_types_allowed = True        # graph_result 등 다양한 타입 허용