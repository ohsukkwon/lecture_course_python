"""
파일명: 02_list_comprehension.py
설명: 리스트 컴프리헨션 완벽 가이드
Filename: 02_list_comprehension.py
Description: Complete guide to list comprehension
"""

print("="*70)
print("리스트 컴프리헨션 (List Comprehension)")
print("="*70)
print()

# ===== 1. 기본 리스트 컴프리헨션 =====
print("1. 기본 형식 (Basic format)")
print("-"*70)

# 일반 방법
squares_normal = []
for x in range(10):
    squares_normal.append(x**2)
print(f"일반 방법: {squares_normal}")

# 리스트 컴프리헨션
squares_comp = [x**2 for x in range(10)]
print(f"컴프리헨션: {squares_comp}")
print()

# ===== 2. 조건이 있는 리스트 컴프리헨션 =====
print("2. 조건 포함 (With condition)")
print("-"*70)

# 짝수만
evens = [x for x in range(20) if x % 2 == 0]
print(f"짝수: {evens}")

# 홀수만
odds = [x for x in range(20) if x % 2 != 0]
print(f"홀수: {odds}")

# 3의 배수
multiples_of_3 = [x for x in range(30) if x % 3 == 0]
print(f"3의 배수: {multiples_of_3}")
print()

# ===== 3. if-else가 있는 리스트 컴프리헨션 =====
print("3. if-else 포함 (With if-else)")
print("-"*70)

# 짝수는 제곱, 홀수는 음수
numbers = [x**2 if x % 2 == 0 else -x for x in range(10)]
print(f"결과: {numbers}")

# 양수는 그대로, 음수는 0으로
original = [-2, -1, 0, 1, 2, 3]
processed = [x if x >= 0 else 0 for x in original]
print(f"원본: {original}")
print(f"처리: {processed}")
print()

# ===== 4. 중첩 리스트 컴프리헨션 =====
print("4. 중첩 (Nested)")
print("-"*70)

# 2차원 리스트 생성
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("구구단 일부:")
for row in matrix:
    print(row)

# 2차원 리스트 평탄화
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"\n원본: {matrix}")
print(f"평탄화: {flattened}")
print()

# ===== 5. 문자열 처리 =====
print("5. 문자열 처리 (String processing)")
print("-"*70)

words = ["hello", "world", "python", "programming"]

# 대문자로 변환
upper_words = [word.upper() for word in words]
print(f"대문자: {upper_words}")

# 길이가 5 이상인 단어만
long_words = [word for word in words if len(word) >= 5]
print(f"긴 단어: {long_words}")

# 첫 글자만 추출
first_letters = [word[0] for word in words]
print(f"첫 글자: {first_letters}")
print()

# ===== 6. 실전 예제 =====
print("6. 실전 예제 (Practical examples)")
print("-"*70)

# 예제 1: 온도 변환 (섭씨 → 화씨)
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(f"섭씨: {celsius}")
print(f"화씨: {fahrenheit}")

# 예제 2: 숫자 필터링
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positives = [n for n in numbers if n > 0]
negatives = [n for n in numbers if n < 0]
print(f"\n숫자: {numbers}")
print(f"양수: {positives}")
print(f"음수: {negatives}")

# 예제 3: 중복 제거
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique = list(set(numbers))  # 또는 리스트 컴프리헨션과 조건
print(f"\n중복 있음: {numbers}")
print(f"중복 제거: {unique}")
print()

print("="*70)
print("리스트 컴프리헨션 완료!")
print("="*70)
