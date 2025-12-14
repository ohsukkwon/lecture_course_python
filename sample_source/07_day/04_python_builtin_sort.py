"""
파이썬 내장 정렬 함수 활용
sorted() 함수와 list.sort() 메서드
"""


def main():
    print("=" * 50)
    print("파이썬 내장 정렬 함수 활용")
    print("=" * 50)

    # ===== sorted() 함수 =====
    print("\n[1] sorted() 함수 - 원본 유지")
    numbers = [64, 34, 25, 12, 22]
    sorted_numbers = sorted(numbers)
    print(f"원본: {numbers}")
    print(f"정렬: {sorted_numbers}")

    # 내림차순
    desc_numbers = sorted(numbers, reverse=True)
    print(f"내림차순: {desc_numbers}")

    # ===== list.sort() 메서드 =====
    print("\n[2] list.sort() 메서드 - 원본 수정")
    numbers2 = [64, 34, 25, 12, 22]
    print(f"정렬 전: {numbers2}")
    numbers2.sort()
    print(f"정렬 후: {numbers2}")

    # 내림차순
    numbers2.sort(reverse=True)
    print(f"내림차순: {numbers2}")

    # ===== 문자열 정렬 =====
    print("\n[3] 문자열 정렬")
    words = ["banana", "apple", "Cherry", "date"]

    # 기본 정렬 (대소문자 구분)
    print(f"기본 정렬: {sorted(words)}")

    # 대소문자 무시 정렬
    print(f"대소문자 무시: {sorted(words, key=str.lower)}")

    # 길이순 정렬
    print(f"길이순 정렬: {sorted(words, key=len)}")

    # ===== key 매개변수 활용 =====
    print("\n[4] key 매개변수 활용")

    # 튜플 정렬
    students = [("철수", 85), ("영희", 92), ("민수", 78), ("지영", 95)]

    # 이름순 정렬
    sorted_by_name = sorted(students, key=lambda x: x[0])
    print(f"이름순: {sorted_by_name}")

    # 점수순 정렬 (높은 점수부터)
    sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
    print(f"점수순: {sorted_by_score}")

    # ===== 딕셔너리 정렬 =====
    print("\n[5] 딕셔너리 정렬")
    scores = {"철수": 85, "영희": 92, "민수": 78, "지영": 95}

    # 키 기준 정렬
    sorted_by_key = sorted(scores.items())
    print(f"키 기준: {sorted_by_key}")

    # 값 기준 정렬 (높은 점수부터)
    sorted_by_value = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    print(f"값 기준: {sorted_by_value}")

    # 딕셔너리로 변환
    sorted_dict = dict(sorted_by_value)
    print(f"딕셔너리: {sorted_dict}")

    # ===== 다중 기준 정렬 =====
    print("\n[6] 다중 기준 정렬")
    data = [
        ("철수", 25, 85),
        ("영희", 23, 92),
        ("민수", 25, 78),
        ("지영", 23, 95),
    ]

    # 나이순, 같은 나이면 점수순 (높은 점수 우선)
    sorted_data = sorted(data, key=lambda x: (x[1], -x[2]))
    print("나이순 → 점수순 (높은 점수 우선):")
    for person in sorted_data:
        print(f"  {person[0]}: {person[1]}세, {person[2]}점")

    # ===== 객체 정렬 =====
    print("\n[7] 클래스 객체 정렬")

    class Student:
        def __init__(self, name, score):
            self.name = name
            self.score = score

        def __repr__(self):
            return f"Student('{self.name}', {self.score})"

    students_obj = [
        Student("철수", 85),
        Student("영희", 92),
        Student("민수", 78),
        Student("지영", 95),
    ]

    # 점수순 정렬
    sorted_students = sorted(students_obj, key=lambda s: s.score, reverse=True)
    print("점수순 정렬:")
    for student in sorted_students:
        print(f"  {student}")

    # ===== 특수한 정렬 =====
    print("\n[8] 특수한 정렬")

    # 절댓값 기준 정렬
    numbers3 = [-5, 2, -3, 8, -1, 4]
    sorted_abs = sorted(numbers3, key=abs)
    print(f"절댓값 기준: {sorted_abs}")

    # 리스트의 두 번째 요소 기준 정렬
    matrix = [[3, 4], [1, 2], [5, 1], [2, 3]]
    sorted_matrix = sorted(matrix, key=lambda x: x[1])
    print(f"두 번째 요소 기준: {sorted_matrix}")

    # 문자열의 특정 위치 문자 기준
    words2 = ["apple", "banana", "cherry", "date"]
    sorted_words = sorted(words2, key=lambda x: x[-1])  # 마지막 문자 기준
    print(f"마지막 문자 기준: {sorted_words}")

    # ===== 안정 정렬 (Stable Sort) =====
    print("\n[9] 안정 정렬 특성")
    data2 = [("A", 1), ("B", 2), ("C", 1), ("D", 2)]
    print(f"원본: {data2}")

    # 두 번째 요소로 정렬 (첫 번째 요소의 순서 유지)
    sorted_stable = sorted(data2, key=lambda x: x[1])
    print(f"두 번째 요소 기준 정렬: {sorted_stable}")
    print("→ 같은 값에 대해 원래 순서가 유지됨 (안정 정렬)")


if __name__ == "__main__":
    main()
