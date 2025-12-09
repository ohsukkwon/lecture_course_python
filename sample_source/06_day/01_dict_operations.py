"""
파일명: 01_dict_operations.py
설명: 딕셔너리 기본 연산 및 활용
Filename: 01_dict_operations.py
Description: Dictionary operations and usage
"""

# ===== 1. 딕셔너리 생성 및 접근 =====
print("="*60)
print("1. 딕셔너리 생성 및 접근")
print("="*60)

student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학",
    "gpa": 3.8
}

print(f"학생 정보: {student}")
print(f"이름: {student['name']}")
print(f"나이: {student.get('age')}")
print(f"주소: {student.get('address', '정보 없음')}")  # 기본값

print()

# ===== 2. 딕셔너리 수정 및 추가 =====
print("="*60)
print("2. 딕셔너리 수정 및 추가")
print("="*60)

student["age"] = 21  # 수정
student["phone"] = "010-1234-5678"  # 추가
print(f"수정 후: {student}")

# update()로 여러 항목 추가/수정
student.update({"grade": "3학년", "club": "코딩동아리"})
print(f"update 후: {student}")

print()

# ===== 3. 딕셔너리 메서드 =====
print("="*60)
print("3. 딕셔너리 메서드")
print("="*60)

print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

print()

# ===== 4. 딕셔너리 순회 =====
print("="*60)
print("4. 딕셔너리 순회")
print("="*60)

for key, value in student.items():
    print(f"{key}: {value}")

print()

# ===== 5. 실전 예제: 단어 빈도수 =====
print("="*60)
print("5. 실전 예제: 단어 빈도수")
print("="*60)

text = "hello world hello python world world"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"단어 빈도: {word_count}")

# 가장 많이 나온 단어
most_common = max(word_count.items(), key=lambda x: x[1])
print(f"가장 많은 단어: {most_common[0]} ({most_common[1]}번)")

print()
print("="*60)
print("딕셔너리 예제 완료!")
print("="*60)
