from datetime import date

records = []


def add_record():
    exercise = input("종목: ")
    weight = float(input("무게(kg): "))
    reps = int(input("횟수: "))
    sets = int(input("세트: "))
    records.append({
        "date": str(date.today()),
        "exercise": exercise,
        "weight": weight,
        "reps": reps,
        "sets": sets,
    })
    print("기록 완료")


def show_records():
    if not records:
        print("기록 없음")
        return
    for r in records:
        print(r["date"], r["exercise"], r["weight"], "kg",
              r["reps"], "회", r["sets"], "세트")


def main():
    while True:
        print("1. 기록 추가  2. 기록 보기  0. 종료")
        choice = input("선택: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "0":
            print("종료합니다")
            break
        else:
            print("잘못된 입력입니다")


main()
