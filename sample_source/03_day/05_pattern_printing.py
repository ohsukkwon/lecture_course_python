"""
파일명: 05_pattern_printing.py
설명: 다양한 별 패턴 출력 연습 (중첩 반복문)
Filename: 05_pattern_printing.py
Description: Various star pattern printing practice (nested loops)
"""

print("="*70)
print("별 패턴 출력 연습 (Star Pattern Printing Practice)")
print("="*70)
print()

# ===== 1. 직사각형 (Rectangle) =====
print("="*70)
print("1. 직사각형 (Rectangle)")
print("="*70)

rows = 5
cols = 10

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()  # 줄바꿈 (Newline)

print()

# ===== 2. 직각삼각형 (Right Triangle) =====
print("="*70)
print("2. 직각삼각형 - 왼쪽 정렬 (Right Triangle - Left aligned)")
print("="*70)

for i in range(1, 6):  # 1부터 5까지
    for j in range(i):
        print("*", end="")
    print()

print()

# ===== 3. 역 직각삼각형 (Inverted Right Triangle) =====
print("="*70)
print("3. 역 직각삼각형 (Inverted Right Triangle)")
print("="*70)

for i in range(5, 0, -1):  # 5부터 1까지
    for j in range(i):
        print("*", end="")
    print()

print()

# ===== 4. 직각삼각형 - 오른쪽 정렬 (Right Triangle - Right aligned) =====
print("="*70)
print("4. 직각삼각형 - 오른쪽 정렬 (Right aligned)")
print("="*70)

n = 5
for i in range(1, n + 1):
    # 공백 출력 (Print spaces)
    for j in range(n - i):
        print(" ", end="")
    # 별 출력 (Print stars)
    for j in range(i):
        print("*", end="")
    print()

print()

# ===== 5. 피라미드 (Pyramid) =====
print("="*70)
print("5. 피라미드 (Pyramid)")
print("="*70)

n = 5
for i in range(1, n + 1):
    # 공백 출력 (Print spaces)
    for j in range(n - i):
        print(" ", end="")
    # 별 출력 (Print stars)
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print()

# ===== 6. 역 피라미드 (Inverted Pyramid) =====
print("="*70)
print("6. 역 피라미드 (Inverted Pyramid)")
print("="*70)

n = 5
for i in range(n, 0, -1):
    # 공백 출력 (Print spaces)
    for j in range(n - i):
        print(" ", end="")
    # 별 출력 (Print stars)
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print()

# ===== 7. 다이아몬드 (Diamond) =====
print("="*70)
print("7. 다이아몬드 (Diamond)")
print("="*70)

n = 5

# 위쪽 절반 (Upper half)
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 아래쪽 절반 (Lower half)
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

print()

# ===== 8. 속이 빈 사각형 (Hollow Rectangle) =====
print("="*70)
print("8. 속이 빈 사각형 (Hollow Rectangle)")
print("="*70)

rows = 5
cols = 10

for i in range(rows):
    for j in range(cols):
        # 테두리만 별 출력 (Print stars only on border)
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# ===== 9. 속이 빈 피라미드 (Hollow Pyramid) =====
print("="*70)
print("9. 속이 빈 피라미드 (Hollow Pyramid)")
print("="*70)

n = 7
for i in range(1, n + 1):
    # 공백 출력 (Print spaces)
    for j in range(n - i):
        print(" ", end="")

    # 별 출력 (Print stars)
    for j in range(2 * i - 1):
        # 첫 번째 줄, 마지막 줄, 또는 양 끝만 별 출력
        # Print stars only on first line, last line, or edges
        if i == n or j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print()

# ===== 10. 숫자 패턴 (Number Pattern) =====
print("="*70)
print("10. 숫자 패턴 (Number Pattern)")
print("="*70)

# 패턴 1: 증가하는 숫자
print("패턴 1: 증가하는 숫자")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# 패턴 2: 같은 숫자 반복
print("패턴 2: 같은 숫자 반복")
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

print()

# ===== 11. 알파벳 패턴 (Alphabet Pattern) =====
print("="*70)
print("11. 알파벳 패턴 (Alphabet Pattern)")
print("="*70)

for i in range(5):
    for j in range(i + 1):
        # A부터 시작하는 알파벳 출력 (Print alphabets starting from A)
        print(chr(65 + j), end=" ")  # 65 = 'A'
    print()

print()

# ===== 12. 체스판 패턴 (Chessboard Pattern) =====
print("="*70)
print("12. 체스판 패턴 (Chessboard Pattern)")
print("="*70)

size = 8
for i in range(size):
    for j in range(size):
        # 체스판처럼 교차 패턴 (Alternating pattern like chessboard)
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

print()

# ===== 13. 나비 모양 (Butterfly Pattern) =====
print("="*70)
print("13. 나비 모양 (Butterfly Pattern)")
print("="*70)

n = 5

# 위쪽 날개 (Upper wings)
for i in range(1, n + 1):
    # 왼쪽 별 (Left stars)
    for j in range(i):
        print("*", end="")
    # 가운데 공백 (Middle spaces)
    for j in range(2 * (n - i)):
        print(" ", end="")
    # 오른쪽 별 (Right stars)
    for j in range(i):
        print("*", end="")
    print()

# 아래쪽 날개 (Lower wings)
for i in range(n - 1, 0, -1):
    # 왼쪽 별 (Left stars)
    for j in range(i):
        print("*", end="")
    # 가운데 공백 (Middle spaces)
    for j in range(2 * (n - i)):
        print(" ", end="")
    # 오른쪽 별 (Right stars)
    for j in range(i):
        print("*", end="")
    print()

print()

# ===== 14. 파스칼 삼각형 숫자 (Pascal's Triangle Numbers) =====
print("="*70)
print("14. 파스칼 삼각형 (Pascal's Triangle)")
print("="*70)

n = 6
for i in range(n):
    # 공백 출력 (Print spaces)
    for j in range(n - i - 1):
        print(" ", end=" ")

    # 숫자 출력 (Print numbers)
    num = 1
    for j in range(i + 1):
        print(num, end="   ")
        # 다음 숫자 계산 (Calculate next number)
        num = num * (i - j) // (j + 1)
    print()

print()

print("="*70)
print("별 패턴 연습 완료! (Pattern practice completed!)")
print("="*70)
print()
print("💡 Tip: 이중 반복문의 원리")
print("   - 바깥 for문: 행(row) 제어")
print("   - 안쪽 for문: 열(column) 제어")
print("   - Outer for loop: controls rows")
print("   - Inner for loop: controls columns")
