import json, re

def parse_json_from_llm(text: str) -> dict:
    """
    - 3b
    - llm_prompts.py의 get_task_prompt에 의존적
    - text에서 'Now, process this user query:' 이후의 첫 번째 JSON 블록만 추출 후 파싱
    """
    match = re.search(r'```json\s*(\{.*?\})\s*```', text, re.DOTALL)
    if match:
        json_str = match.group(1)  # { ... } 부분만
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            print("[parser_Warning] JSON parse failed")
            return {}
    else:
        print("[parser_Warning] No JSON found before ```json")
        return {}
    
def llm1_output(text: str):
    # 결과값만
    # 'Now, process this user query:' 이후 문자열
    after_prompt = text.split("Now, process this user query:")[-1]
    print(f"\n\n###################\n[LLM(1)] output : \n{after_prompt}\n##################\n")
    
def parse_json_from_llm_7b(text: str) -> dict:
    """
    모델이 7b면 출력이 달라짐..
    """
    
    # 'Now, process this user query:' 이후 문자열
    try:
        after_prompt = text.split("Now, process this user query:")[-1]
    except IndexError:
        print("[parser_Warning] Prompt not found")
        return {}
    match = re.search(r'(\{.*?\})\s*```json', after_prompt, re.DOTALL)
    if match:
        json_str = match.group(1)  # { ... } 부분만
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            print("[parser_Warning] JSON parse failed")
            return {}
    else:
        print("[parser_Warning] No JSON found before ```json")
        return {}