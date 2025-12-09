"""
파일명: 01_list_methods.py
설명: 리스트 메서드 및 활용
Filename: 01_list_methods.py
Description: List methods and usage
"""

# ===== 1. 리스트 생성 및 인덱싱 =====

print("="*60)
print("1. 리스트 생성 및 인덱싱")
print("="*60)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"리스트: {fruits}")
print(f"첫 번째: {fruits[0]}")
print(f"마지막: {fruits[-1]}")
print(f"슬라이싱 [1:4]: {fruits[1:4]}")

print()

# ===== 2. 리스트 메서드 - 추가 =====

print("="*60)
print("2. 리스트 요소 추가")
print("="*60)

numbers = [1, 2, 3]
print(f"초기: {numbers}")

numbers.append(4)  # 끝에 추가
print(f"append(4): {numbers}")

numbers.insert(0, 0)  # 특정 위치에 추가
print(f"insert(0, 0): {numbers}")

numbers.extend([5, 6, 7])  # 여러 요소 추가
print(f"extend([5,6,7]): {numbers}")

print()

# ===== 3. 리스트 메서드 - 삭제 =====

print("="*60)
print("3. 리스트 요소 삭제")
print("="*60)

colors = ["red", "blue", "green", "yellow", "blue"]
print(f"초기: {colors}")

colors.remove("blue")  # 값으로 삭제 (첫 번째만)
print(f"remove('blue'): {colors}")

popped = colors.pop()  # 마지막 요소 제거 및 반환
print(f"pop(): {popped}, 리스트: {colors}")

popped = colors.pop(0)  # 특정 인덱스 제거
print(f"pop(0): {popped}, 리스트: {colors}")

print()

# ===== 4. 리스트 정렬 =====

print("="*60)
print("4. 리스트 정렬")
print("="*60)

nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"원본: {nums}")

nums.sort()  # 오름차순 정렬 (원본 변경)
print(f"sort(): {nums}")

nums.sort(reverse=True)  # 내림차순
print(f"sort(reverse=True): {nums}")

nums = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(nums)  # 새 리스트 반환 (원본 유지)
print(f"sorted(): {sorted_nums}, 원본: {nums}")

print()

# ===== 5. 리스트 컴프리헨션 =====

print("="*60)
print("5. 리스트 컴프리헨션")
print("="*60)

# 기본
squares = [x**2 for x in range(10)]
print(f"제곱수: {squares}")

# 조건 포함
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수 제곱: {even_squares}")

# 문자열 처리
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"대문자: {upper_words}")

print()

# ===== 6. 실전 예제: 학생 성적 관리 =====

print("="*60)
print("6. 실전 예제: 학생 성적 관리")
print("="*60)

students = ["철수", "영희", "민수", "지영", "동현"]
scores = [85, 92, 78, 95, 88]

# 성적순 정렬 (학생 이름과 함께)
student_scores = list(zip(students, scores))
print(f"원본: {student_scores}")

sorted_students = sorted(student_scores, key=lambda x: x[1], reverse=True)
print(f"성적순: {sorted_students}")

# 평균 계산
average = sum(scores) / len(scores)
print(f"평균: {average:.2f}")

# 90점 이상
high_scorers = [name for name, score in student_scores if score >= 90]
print(f"90점 이상: {high_scorers}")

print()
print("="*60)
print("리스트 예제 완료!")
print("="*60)
