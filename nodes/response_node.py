from core.schemas import PipelineState
from core import config

def response_node(state: PipelineState) -> PipelineState:
    """최종 응답 or 디버깅 정보"""
    debug_text = (
        f"[사용자 입력] {state.input_text}\n"
        f"[태스크 유형] {state.task_type}\n"
        f"[속성] {state.attributes}\n"
        f"[검색 쿼리] {state.graph_query}\n"
        f"[검색 결과] {state.graph_result}"
    )

    if config.DEBUG:
        # 디버그 모드: 내부 상태 확인용으로 출력
        state.final_text = debug_text
    else:
        # 운영 모드: LLM이 생성한 응답 유지
        state.final_text = state.final_text or "응답을 생성하지 못했습니다."

    return state