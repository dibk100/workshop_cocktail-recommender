from core.schemas import PipelineState
from core.llm_model import QwenModel
from prompts.response_template import RESPONSE_PROMPT
from core.promptloader import PromptLoader

# 답변 모델
qwen_generator = QwenModel()

def response_node(state: PipelineState) -> PipelineState:
    """
    Generator 노드:
    - Checking_Hop에서 전달된 정보를 기반으로 최종 응답 생성

    """
    
    # Respones 프롬프트
    prompt = RESPONSE_PROMPT.format(
        query=state.user_query,                      # 질문
        task_type=state.task_type,            # 속성
        search_results=state.search_results        # 후보 결과
    )    

    # 답변생성기
    try:
        output = qwen_generator.generate(prompt)

    except Exception as e:
        print(f"Generator failed: {e}")
        output = "답변 생성 모델에서 오류"

    # PipelineState에 저장
    state.final_text = output.strip()

    return state