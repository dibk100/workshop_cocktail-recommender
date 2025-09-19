from pydantic import BaseModel, Field
from typing import Any, Dict, Optional
from typing import List

class PipelineState(BaseModel):
    """
    LangGraph 파이프라인 전체 상태 정의 및 저장하는 공간.
    """
    # -------------------
    # 사용자 입력
    # -------------------
    user_query: Dict[str, Any]            # 예: {"text": "질문 내용", "image": <이미지 객체>}
    input_text: str = ""                  # 텍스트만 별도로 저장
    input_image: Optional[Any] = None    # 이미지 객체, 없을 수도 있음

    # -------------------
    # Retriever 전달용
    # -------------------
    embedding_model : str = ""
    task_type: str = ""                               # C1~C4 태스크 분류 결과
    input_text_to_image_text : str = ""                  # 텍스트+이미지 변환 텍스트
    
    # -------------------
    # Checking_Hop 노드 관련
    # -------------------
    score: Optional[float] = None         # LLM 응답 평가 점수
    search_results : Optional[List[Any]] = []
    
    # -------------------
    # Generator 결과
    # -------------------
    final_text: Optional[str] = None          # 최종 텍스트 response

    class Config:
        arbitrary_types_allowed = True        