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
        print("1. 기록 추가  2. 기록 보기  3. 종목별 조회  0. 종료")
        choice = input("선택: ")
        if choice == "1":
            add_record()
        elif choice == "2":
            show_records()
        elif choice == "3":
            show_by_exercise()
        elif choice == "0":
            print("종료합니다")
            break
        else:
            print("잘못된 입력입니다")



def show_by_exercise():
    name = input("종목: ")
    found = [r for r in records if r["exercise"] == name]
    if not found:
        print("기록 없음")
        return
    for r in found:
        print(r["date"], r["weight"], "kg",
              r["reps"], "회", r["sets"], "세트")
    best = max(found, key=lambda r: r["weight"])
    print("최고 기록:", best["weight"], "kg,", best["date"])
        
main()