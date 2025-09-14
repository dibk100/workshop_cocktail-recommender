from nodes.llm_task import llm_task_node
from nodes.graph_nodes import graph_query_node
from nodes.llm_response import llm_response_node
from nodes.response_node import response_node
from core.schemas import PipelineState

def run_pipeline(user_input: str) -> str:
    """
    전체 파이프라인 :
    user_input -> llm_task_node -> graph_query_node -> llm_response_node -> response_node
    """
    
    state = PipelineState(query=user_input)
    state = llm_task_node(state)
    state = graph_query_node(state)        # 현재는 더미 함수
    state = llm_response_node(state)
    state = response_node(state)           # 최종 응답 포맷팅
    return state.final_text

def interface_cli():
    """
    CLI 기반 칵테일 추천 시스템 화면
    """
    print("\n=== 🍸 Cocktail Recommendation System 🍸 ===")
    print("Type your query to get a cocktail recommendation or type 'q' to quit.\n")

    while True:
        user_query = input("Your query: ").strip()

        if user_query.lower() in ["q", "quit", "exit"]:
            print("Exiting the system.")
            break

        if not user_query:
            print("Please enter a valid query.\n")
            continue

        # 파이프라인 실행
        result = run_pipeline(user_query)

        if not result:
            print("Failed to generate response. Exiting.")
            break

        print("\n=== Final Recommendation ===")
        print(result)
        print("\n" + "-"*50)

if __name__ == "__main__":
    interface_cli()