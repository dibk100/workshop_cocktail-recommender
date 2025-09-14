from core.schemas import PipelineState
from core.llm_model import QwenModel            ## 모델 가져옴
from core.llm_prompts import get_task_prompt    ## 프롬프트 가져옴
from core.utils import parse_json_from_llm,llm1_output  # utils에서 json 출력 핸들링

# 모델 불러옴
qwen_model = QwenModel()

def llm_task_node(state: PipelineState) -> PipelineState:
    """
    - LLM(1) node: 사용자 질의 분석 → 태스크 분류 + 속성 추출
    - 출력 JSON을 파싱하여 PipelineState에 저장
    """

    user_query = state.input_text                        # 입력된 질문
    prompt = get_task_prompt(user_query)            # llm(1) 프롬프트 
    
    try:
        raw_output = qwen_model.generate(prompt,max_length=256)        # temperature=0.7,top_p=0.9 조절 가능?
        
        #### 확인용
        # print(f"\n#############\n[LLM(1)] output :\n{raw_output}\n#############\n\n")        # 프롬프트와 출력값 같이 확인
        llm1_output(raw_output)        ## LLM(1) 결과값만 출력
        ####
        
        parsed = parse_json_from_llm(raw_output)
        state.task_type = parsed.get("task_type", "Recommend")
        state.attributes = parsed.get("attributes", {})

    except Exception as e:
        print(f"[llm_task_node_Warning] JSON parse failed: {e}")
        # fallback 처리
        state.task_type = "Recommend"
        state.attributes = {}

    # Graph Query 준비 (임시)
    state.graph_query = "MATCH (c:Cocktail) RETURN c LIMIT 3"

    return state