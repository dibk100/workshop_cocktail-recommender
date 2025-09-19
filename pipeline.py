from langgraph.graph import StateGraph, START, END
from nodes.task_classifier import *
from nodes.retriever import *
from nodes.checking_hop import *
from nodes.generator import *
from core.schemas import PipelineState


def build_pipeline_graph() -> StateGraph:
    graph = StateGraph(PipelineState)
    
    # 노드 정의
    graph.add_node("Agent_TaskClassification", task_mapping_node)
    graph.add_node("Retriever", graph_query_node)
    graph.add_node("Checking_Hop", checking)
    graph.add_node("Generator", response_node)
    
    # 기본 플로우: 실선 연결
    graph.add_edge(START, "Agent_TaskClassification")
    graph.add_edge("Agent_TaskClassification", "Retriever")
    graph.add_edge("Retriever", "Checking_Hop")  # 실선
    graph.add_edge("Checking_Hop", "Generator")  # 실선
    
    # 조건부 분기:
    def checking_hop_condition(state: PipelineState) -> str:
        score = state.score if state.score is not None else 85
        return "score >= 80" if score >= 80 else "score < 80"
    
    graph.add_conditional_edges(
        "Checking_Hop",
        checking_hop_condition,
        {
            "score < 80": "Retriever",
            "score >= 80": "Generator"
        }
    )
    
    # 최종 출력
    graph.add_edge("Generator", END)
    
    return graph

def interface_cli():
    """
    CLI 기반 칵테일 추천 시스템 화면 ::::::: 수정해야함
    """
    print("\n=== 🍸 Cocktail Recommendation System 🍸 ===")
    print("Type your query to get a cocktail recommendation or type 'q' to quit.\n")


if __name__ == "__main__":
    interface_cli()