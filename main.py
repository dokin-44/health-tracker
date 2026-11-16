from datetime import date
import json
from pathlib import Path
from weekly_summary import show_weekly_summary

RECORDS_FILE = Path(__file__).with_name("records.json")
records = []


def load_records():
    if not RECORDS_FILE.exists():
        return []
    with RECORDS_FILE.open(encoding="utf-8") as file:
        saved_records = json.load(file)
    if not isinstance(saved_records, list) or any(
        not isinstance(record, dict)
        or not {"date", "exercise", "weight", "reps", "sets"} <= record.keys()
        for record in saved_records
    ):
        raise ValueError("저장된 운동 기록 형식이 올바르지 않습니다")
    return saved_records


def save_records(updated_records):
    temporary_file = RECORDS_FILE.with_suffix(".json.tmp")
    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(updated_records, file, ensure_ascii=False, indent=2)
    temporary_file.replace(RECORDS_FILE)


def add_record():
    exercise = input("종목: ")
    weight = float(input("무게(kg): "))
    reps = int(input("횟수: "))
    sets = int(input("세트: "))
    record = {
        "date": str(date.today()),
        "exercise": exercise,
        "weight": weight,
        "reps": reps,
        "sets": sets,
    }
    try:
        save_records(records + [record])
    except OSError as error:
        print(f"기록 저장 실패: {error}")
        return
    records.append(record)
    print("기록 완료")


def show_records():
    if not records:
        print("기록 없음")
        return
    dates = sorted({r["date"] for r in records}, reverse=True)
    print("기록이 있는 날짜:")
    for number, recorded_date in enumerate(dates, start=1):
        print(f"{number}. {recorded_date}")
    print("0. 돌아가기")
    try:
        choice = int(input("조회할 날짜 번호: ").strip())
        if choice == 0:
            return
        if not 1 <= choice <= len(dates):
            raise ValueError
    except ValueError:
        print("목록에 있는 번호를 입력해주세요")
        return
    selected_date = dates[choice - 1]
    selected_records = [r for r in records if r["date"] == selected_date]
    if not selected_records:
        print("해당 날짜의 기록 없음")
        return
    for r in selected_records:
        print(r["date"], r["exercise"], r["weight"], "kg",
              r["reps"], "회", r["sets"], "세트")


def main():
    try:
        records[:] = load_records()
    except (OSError, ValueError) as error:
        print(f"기록 불러오기 실패: {error}")
        return
        
def main():
    try:
        records[:] = load_records()
    except (OSError, ValueError) as error:
        print(f"기록 불러오기 실패: {error}")
        return

    while True:
        print("1. 기록 추가  2. 기록 보기  3. 주간 요약  0. 종료")
        choice = input("선택: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            show_weekly_summary(records)
        elif choice == "0":
            print("종료합니다")
            break
        else:
            print("잘못된 입력입니다")


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
