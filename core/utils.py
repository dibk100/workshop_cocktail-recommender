import json, re

def parse_json_from_llm(text: str) -> dict:
    """
    생성형 결과는 정규화가 필요하지
    """
    try:
        json_str = re.search(r"\{.*\}", text, re.DOTALL).group()
        processed_result = json.loads(json_str)
    except Exception:
        # JSON 디코딩 실패 시 기본값
        processed_result = {"task": "C1", "confidence": 85, "reason": text}
    
    return processed_result
