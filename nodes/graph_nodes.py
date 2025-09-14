from core.schemas import PipelineState

def graph_query_node(state: PipelineState) -> PipelineState:
    """
    Graph Query Node
    - 지금은 Neo4j 미연결 상태
    - 그대로 state 반환
    """
    # 나중에 Neo4j 붙이면 여기서 state.graph_result 채우기
    return state
