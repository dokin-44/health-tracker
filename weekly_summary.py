
from datetime import date, timedelta


def summarize_week(records, reference_date=None):
    """이번 주 운동 기록을 요약한다."""

    if reference_date is None:
        reference_date = date.today()
    elif isinstance(reference_date, str):
        reference_date = date.fromisoformat(reference_date)

    # 이번 주 월요일과 일요일 계산
    week_start = reference_date - timedelta(
        days=reference_date.weekday()
    )
    week_end = week_start + timedelta(days=6)

    workout_dates = set()
    total_sets = 0
    total_reps = 0
    exercises = {}

    for record in records:
        try:
            record_date = date.fromisoformat(record["date"])

            if not (week_start <= record_date <= week_end):
                continue

            exercise = record["exercise"]
            sets = int(record["sets"])
            reps = int(record["reps"])

            if sets < 0 or reps < 0:
                continue

            workout_dates.add(record_date)
            total_sets += sets
            total_reps += sets * reps

            if exercise not in exercises:
                exercises[exercise] = {
                    "sets": 0,
                    "reps": 0
                }

            exercises[exercise]["sets"] += sets
            exercises[exercise]["reps"] += sets * reps

        except (KeyError, ValueError, TypeError):
            continue

    return {
        "week_start": week_start.isoformat(),
        "week_end": week_end.isoformat(),
        "workout_days": len(workout_dates),
        "total_sets": total_sets,
        "total_reps": total_reps,
        "exercises": exercises
    }


def show_weekly_summary(records):
    """주간 운동 요약을 화면에 출력한다."""

    summary = summarize_week(records)

    print("\n===== 주간 운동 요약 =====")
    print(
        f"기간: {summary['week_start']} ~ "
        f"{summary['week_end']}"
    )
    print(f"운동한 날짜: {summary['workout_days']}일")
    print(f"총 운동 세트: {summary['total_sets']}세트")
    print(f"총 반복 횟수: {summary['total_reps']}회")

    if not summary["exercises"]:
        print("\n이번 주 운동 기록이 없습니다.")
        return

    print("\n[종목별 운동 기록]")

    for exercise, data in summary["exercises"].items():
        print(
            f"{exercise}: {data['sets']}세트 / "
            f"{data['reps']}회"
        )
