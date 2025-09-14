from core.schemas import PipelineState
from core.llm_model import QwenModel
from core.llm_prompts import RESPONSE_PROMPT

# LLM2 Qwen 모델 인스턴스
qwen_model_2 = QwenModel()

def llm_response_node(state: PipelineState) -> PipelineState:
    """
    LLM(2) node: Graph 후보 데이터 + 속성 기반 최종 추천/설명 생성
    """
    # Graph 후보 결과가 없을 경우, 더미 처리
    graph_results_str = getattr(state, "graph_result", "[No search results available]")

    # Respones 프롬프트
    prompt = RESPONSE_PROMPT.format(
        query=state.input_text,                      # 질문
        attributes=state.attributes,            # 속성
        search_results=graph_results_str        # 후보 결과
    )

    # LLM(2)에 실행
    output = qwen_model_2.generate(prompt)
    #### 확인용
    print(f"\n#############\n[LLM(2)] output : {output}\n#############\n\n")
    ####

    # 결과값 저장
    state.final_text = output

    return state
