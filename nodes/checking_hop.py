from core.schemas import PipelineState

def checking(state: PipelineState) -> PipelineState:
    """
    테스트용 Checking_Hop 노드:
    - 임의로 score를 설정하여 분기 로직 테스트 가능
    """
    # 점수가 아직 없으면 기본값 지정
    if state.score is None:
        # TODO: 실제 모델/평가 로직으로 score 계산/ 룰 베이스로 하기
        state.score = 85  # 테스트용 임의 점수
    
    # print(f"계산된 score: {state.score}")

    return state
