# 🍹 workshop_cocktail-recommender

## 🔍 프로젝트 목표
- 칵테일 추천시스템 개발
- Neo4j 기반 그래프 DB(GraphRAG) 구축
- LangGraph를 활용한 파이프라인 설계

## ⚙️ LangGraph 파이프라인 설계
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
<details>
<summary> WorkFlow : user </summary>

1. **사용자 입력**
   - 예: `"달콤하면서 상큼한 칵테일 추천해줘"`

2. **LLM(1) – 의도 해석 & Graph Query 생성**
   - 사용자 질의를 분석하여 속성 추출 (맛, 도수, 재료 등)
   - qwen2.5 모델을 사용하여 사용자 입력(텍스트 + 이미지)을 분석 → 태스크 분류(Recommend / Description / Classification) → GraphRAG에 쿼리 전달
   - GraphRAG 기반 **검색 쿼리 생성**
   - Retrieval 방식 고려:
     - 단순 속성 매칭 (MATCH)
     - 유사도 기반 추천 (embedding + vector search)

3. **GraphRAG – 후보 칵테일 검색**
   - Neo4j에서 속성 기반 칵테일 후보 검색
   - 후보 데이터를 JSON 등 구조화된 형태로 반환

4. **LLM(2) – 최종 추천 생성**
   - 후보 데이터 기반으로 **사용자 맞춤 자연어 추천** 생성
   - 필요 시 후보 순위화 또는 필터링 가능

5. **사용자에게 응답 전달**
   - 최종 추천 결과 출력

</details>

## 📁 Folder Structure
```
project_root/
│
├─ drafts/         # 파이프라인 초안 테스트
---------------------------------------------
├─ pipeline.py                  # LangGraph 파이프라인 정의 및 실행
├─ llm_task.py       # LLM(1) : 사용자 입력 기반 태스크 분류 + GraphRAG 호출
├─ llm_response.py    # LLM(2) : GraphRAG에서 받아온 후보 데이터를 기반으로 최종 추천/설명/분류 결과 생성
├─ graph_nodes.py               # Neo4j GraphRAG 연동 함수
├─ config.py                    # Neo4j URI, 계정, OpenAI/qwen2.5 API Key 등 환경 변수 관리
├─ utils.py                     # 공통 유틸 함수 정리
└─ requirements.txt
```