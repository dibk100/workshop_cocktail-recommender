from core.schemas import PipelineState
import networkx as nx
import matplotlib.pyplot as plt

def graph_query_node(state: PipelineState) -> PipelineState:
    """
    Graph Query Node
    - 지금은 Neo4j 미연결 상태
    - 그대로 state 반환
    - state.graph_result에 시각화 가능 구조가 있다면 사용
    """
    # 나중에 Neo4j 붙이면 여기서 state.graph_result 채우기
    state.search_results = []
    return state
