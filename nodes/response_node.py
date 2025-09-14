from core.schemas import PipelineState

def response_node(state: PipelineState) -> PipelineState:
    """사용자 입력 + 현재 상태 출력"""
    state.final_text = (
        f"[사용자 입력] {state.query}\n"
        f"[태스크 유형] {state.task_type}\n"
        f"[속성] {state.attributes}\n"
        f"[검색 쿼리] {state.graph_query}\n"
        f"[검색 결과] {state.graph_result}"
    )
    return state