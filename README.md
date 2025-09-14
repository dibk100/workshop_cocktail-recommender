# 🍹 WORKSHOP : cocktail-recommender
- 칵테일 추천시스템 개발
- Neo4j 기반 그래프 DB(GraphRAG) 구축
- LangGraph를 활용한 파이프라인 설계

## 🚀 Getting Started
### 1. 가상환경 생성(권장) & 패키지 설치
```
/workshop_cocktail-recommender$ conda create -n workshop_311 python=3.11
/workshop_cocktail-recommender$ conda activate workshop_311
/workshop_cocktail-recommender(workshop_311)$ pip install -r requirements.txt
```
### 2. Test 파이프라인 실행
처음에 LLM모델 불러오느라 시간 걸림.
```
/workshop_cocktail-recommender(workshop_311)$ python tests/test_pipeline.py
```

<details> <summary> CODA out of memory </summary>
불필요한 파일, 오래된 캐시, 다운로드 파일 등을 삭제

```
# Hugging Face 캐시 정리
rm -rf ~/.cache/huggingface/hub
rm -rf ~/.cache/huggingface/transformers
```

실행중인 것 kill
```
# GPU모니터링
watch -n 1 nvidia-smi
```
</details>


## 📌 Notes & Issues (update.2025-09-15) 🧷
- neo4j 미연결
- LLM(1), LLM(2) : Qwen/Qwen2.5-VL-3B-Instruct
- 현재 llm_response.py와 graph_nodes.py는 더미 형태로 구현 
- llm(1) 프롬프트를 json형태로 출력하도록 함.

## 📁 Folder Structure
```
project_root/
│
├─ pipeline.py                # 메인 파이프라인 정의/실행 (LangGraph EntryPoint)
│
├─ nodes/                     
│   ├─ llm_task.py            # LLM(1): 사용자 입력 태스크 분류 + GraphRAG 호출
│   ├─ llm_response.py        # LLM(2): 최종 응답 생성 (현재는 더미)
│   ├─ graph_nodes.py         # Neo4j Graph Query 노드 (더미)
│   └─ response_node.py       # 최종 사용자 Response 포맷팅
│
├─ core/                      
│   ├─ config.py              # 환경 변수 및 설정
│   ├─ llm_model.py           # Hugging Face Qwen2.5-VL-7B-Instruct 
│   ├─ llm_prompts.py         # LLM 프롬프트 템플릿 작성 공간
│   ├─ utils.py               # 
│   └─ schemas.py             # Pydantic 기반 PipelineState 정의
│
├─ tests/                     # 단위/통합 테스트
│   ├─ test_graph_nodes.py
│   └─ test_pipeline.py       # 예시 질의 3개 테스트
│
├─ graph_viz/                     # 시각화
│   ├─ visualize_pipeline.ipynb
│   └─ mermaid_code.mmd       
│
└─ requirements.txt
```

## ⚙️ LangGraph 파이프라인 설계
![파이프라인 구조](graph_viz/mermaid_code_white.png)
<details> <summary> 구조 </summary>
flow

```
[User Input] 
      │
      ▼
 [LLM(1) Node] ──> 속성 추출 & Graph Query
      │
      ▼
 [Graph Query Node] ──> Neo4j에서 후보 칵테일 조회
      │
      ▼
 [LLM(2) Node] ──> 최종 추천 텍스트 생성
      │
      ▼
 [Response Node] ──> 사용자 출력
```
</details>

