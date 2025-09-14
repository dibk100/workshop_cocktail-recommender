from langgraph.graph import StateGraph, START, END
from nodes.llm_task import llm_task_node
from nodes.graph_nodes import graph_query_node
from nodes.llm_response import llm_response_node
from nodes.response_node import response_node
from core.schemas import PipelineState

def build_pipeline_graph() -> StateGraph:
    """
    LangGraph 기반 파이프라인 구축
    user_input -> llm_task_node -> graph_query_node -> llm_response_node -> response_node
    """
    graph = StateGraph(PipelineState)
    graph.add_node("LLM1", llm_task_node)
    graph.add_node("GraphQuery", graph_query_node)
    graph.add_node("LLM2", llm_response_node)
    graph.add_node("ResponseFormatter", response_node)
    
    graph.add_edge(START, "LLM1")
    graph.add_edge("LLM1", "GraphQuery")
    graph.add_edge("GraphQuery", "LLM2")
    graph.add_edge("LLM2", "ResponseFormatter")
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