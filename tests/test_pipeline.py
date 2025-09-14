import sys
import os

# tests폴더에서 실행하며 발생한 이슈
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipeline import run_pipeline

"""
질문 3개 테스트하는 공간
"""

EXAMPLE_QUERIES  = [
    "This is a drink called a mojito. Can you recommend something similar?",
    "It's a drink called a Manhattan. Tell me the ingredients that go into it.",
    "Please tell me what kind of cocktail is shown in the given picture."
]

def print_menu():
    print("\n===== 칵테일 질문 선택 =====")
    for i, q in enumerate(EXAMPLE_QUERIES, start=1):
        print(f"{i}. {q}")
    print("0. 새로운 질문 입력")
    print("q. 종료")
    print("=================================")

def main():
    while True:
        print("\n=== TEST Interface🍸 Cocktail Recommendation System 🍸 ===\n")
        print_menu()
        choice = input("선택 (번호 또는 종료 'q'): ").strip()

        if choice.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        if choice == '0':
            user_query = input("질문을 입력하세요: ").strip()
        elif choice in ['1','2','3']:
            user_query = EXAMPLE_QUERIES[int(choice)-1]
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")
            continue

        try:
            response = run_pipeline(user_query)
            if not response:
                print("응답 생성 실패. 프로그램을 종료합니다.")
                break

            print("\n=== 최종 응답 ===")
            print(response)
            print("\n" + "-"*50 + "\n")

        except Exception as e:
            print(f"파이프라인 실행 중 오류 발생: {e}")
            break

if __name__ == "__main__":
    main()
