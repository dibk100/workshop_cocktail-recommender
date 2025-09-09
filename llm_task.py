# LLM(1) : 사용자 입력 기반 태스크 분류 + GraphRAG 호출
# qwen2.5 또는 OpenAI 모델로 교체 가능

def classify_task(user_input: dict) -> dict:
    """
    입력: {"text": "...", "image_path": "..."}  # image_path 선택적
    반환: {"task": "Recommend", "attributes": {...}}
    """
    text = user_input.get("text", "").lower()

    if "recommend" in text:
        task = "Recommend"
        attributes = {"example_drink": "mojito"}
    elif "ingredients" in text:
        task = "Description"
        attributes = {"drink": "Manhattan"}
    elif "picture" in text or user_input.get("image_path"):
        task = "Classification"
        attributes = {"image_path": user_input.get("image_path")}
    else:
        task = "Recommend"
        attributes = {}

    return {"task": task, "attributes": attributes}
