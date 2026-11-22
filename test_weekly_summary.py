
from datetime import date
from weekly_summary import summarize_week

# 테스트용 운동 기록
test_records = [
    {
        "date": "2026-11-16",
        "exercise": "벤치프레스",
        "weight": 40,
        "reps": 10,
        "sets": 3
    },
    {
        "date": "2026-11-17",
        "exercise": "벤치프레스",
        "weight": 40,
        "reps": 8,
        "sets": 3
    },
    {
        "date": "2026-11-18",
        "exercise": "스쿼트",
        "weight": 50,
        "reps": 12,
        "sets": 4
    },
    {
        # 이번 주가 아니므로 집계에서 제외되어야 함
        "date": "2026-11-10",
        "exercise": "데드리프트",
        "weight": 60,
        "reps": 5,
        "sets": 2
    }
]

# 기준 날짜를 2026년 11월 18일로 설정
result = summarize_week(
    test_records,
    reference_date=date(2026, 11, 18)
)

# 결과 출력
print("===== 주간 요약 테스트 =====")
print("기간:", result["week_start"], "~", result["week_end"])
print("운동한 날짜:", result["workout_days"], "일")
print("총 세트:", result["total_sets"], "세트")
print("총 반복 횟수:", result["total_reps"], "회")

print("\n[종목별 기록]")
for exercise, data in result["exercises"].items():
    print(exercise, data["sets"], "세트 /", data["reps"], "회")

# 예상 결과 검증
assert result["workout_days"] == 3
assert result["total_sets"] == 10
assert result["total_reps"] == 102
assert result["exercises"]["벤치프레스"]["sets"] == 6
assert result["exercises"]["벤치프레스"]["reps"] == 54
assert result["exercises"]["스쿼트"]["sets"] == 4
assert result["exercises"]["스쿼트"]["reps"] == 48

print("\n모든 테스트 통과!")
