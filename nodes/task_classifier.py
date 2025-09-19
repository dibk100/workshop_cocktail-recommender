from core.schemas import PipelineState
from core.llm_model import QwenModel            ## 모델 가져옴
from core.promptloader import PromptLoader
from core.utils import parse_json_from_llm
import json

# 모델 정의
qwen_vl = QwenModel()             # task classifier용
qwen_vl_imageTotext = QwenModel() # 이미지→텍스트 변환용

# PromptLoader 초기화
prompt_loader = PromptLoader(prompts_dir="./prompts")

def task_mapping_node(state: PipelineState) -> PipelineState:
    """
    1. 사용자 입력(user_query)을 state에 저장
    2. Qwen-VL로 task_type 분류 및 embedding 모델 지정
    3. 이미지 → 텍스트 변환 후 input_text와 결합
    """
    # -----------------------------
    # 1. 사용자 입력 저장
    # -----------------------------
    user_query = state.user_query
    state.input_text = user_query.get("text", "")
    state.input_image = user_query.get("image", None)

    # -----------------------------
    # 2. Task Classifier 실행
    # -----------------------------
    classifier_prompt = prompt_loader.get_task_classifier_prompt()

    prompt_text = f"{classifier_prompt['system_prompt']}\n\n{classifier_prompt['user_prompt']}\n\nUser Input: {state.input_text}"
    processed_result_text = qwen_vl.generate(prompt_text, max_length=classifier_prompt.get("max_tokens", 200))
    print("pre : ",processed_result_text)
    processed_result = parse_json_from_llm(processed_result_text)
    print("llm1 : ",processed_result)

    state.task_type = processed_result.get("task", "c1")
    # -----------------------------
    # 2-2. task_type에 맞는 embedding 모델 지정
    # -----------------------------
    emb_config = prompt_loader.get_embedding_model_config(state.task_type)
    state.embedding_model = emb_config.get("embedding_model", "text-embedding-3-small")

    # -----------------------------
    # 3. 이미지 → 텍스트 변환 후 input_text와 결합
    # -----------------------------
    if state.input_image is not None:
        image_prompt = prompt_loader.get_image_to_text_prompt()
        image_prompt_text = f"{image_prompt['system_prompt']}\n\n{image_prompt['user_prompt']}"
        image_description = qwen_vl_imageTotext.generate(image_prompt_text, max_length=image_prompt.get("max_tokens", 1000))
        # 기존 input_text와 결합
        state.input_text_to_image_text  = f"{state.input_text} {image_description}"
    else:
        state.input_text_to_image_text  = state.input_text

    return state