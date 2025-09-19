from langgraph.graph import StateGraph, START, END
from nodes.task_classifier import *
from nodes.graph_nodes import graph_query_node
from nodes.llm_response import llm_response_node
from nodes.response_node import response_node
from core.schemas import PipelineState

def build_pipeline_graph() -> StateGraph:
    graph = StateGraph(PipelineState)
    
    graph.add_node("TASK_mapping", task_mapping_node)
    graph.add_node("Agent_TaskClassification", llm_task_node)
    graph.add_node("Retriver", graph_query_node)
    graph.add_node("Agent_CheckingHop", llm_response_node)
    graph.add_node("ResponseFormatter", response_node)
    
    # 기본 플로우
    graph.add_edge(START, "TASK_mapping")
    graph.add_edge("TASK_mapping", "Agent_TaskClassification")
    graph.add_edge("Agent_TaskClassification", "Retriver")
    
    # Retriever ↔ CheckingHop 루프
    graph.add_edge("Retriver", "Agent_CheckingHop")
    graph.add_edge("Agent_CheckingHop", "Retriver")   # 루프 추가
    
    # 결과 출력
    graph.add_edge("Retriver", "ResponseFormatter")
    graph.add_edge("ResponseFormatter", END)
    
    return graph


def interface_cli():
    """
    CLI 기반 칵테일 추천 시스템 화면 ::::::: 수정해야함
    """
    print("\n=== 🍸 Cocktail Recommendation System 🍸 ===")
    print("Type your query to get a cocktail recommendation or type 'q' to quit.\n")


if __name__ == "__main__":
    interface_cli()