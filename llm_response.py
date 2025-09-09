# LLM(2) : GraphRAG 결과 기반 최종 추천/설명/분류 생성
# qwen2.5 또는 OpenAI 모델로 교체 가능

def generate_response(cocktail_list: list, task: str) -> str:
    if task == "Recommend":
        return f"추천 칵테일: {', '.join(cocktail_list)}"
    elif task == "Description":
        return f"재료 정보: {', '.join(cocktail_list)}"
    elif task == "Classification":
        return f"이미지 기반 칵테일: {', '.join(cocktail_list)}"
    else:
        return f"결과: {', '.join(cocktail_list)}"
