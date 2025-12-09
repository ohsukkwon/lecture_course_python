"""
파일명: 03_practice_gugudan.py
설명: 실습 과제 - 구구단 출력 프로그램
Filename: 03_practice_gugudan.py
Description: Practice - Multiplication table (Gugudan) program
"""

print("="*60)
print("구구단 출력 프로그램 (Multiplication Table Program)")
print("="*60)
print()

# ===== 1. 특정 단 출력 (Print specific table) =====

print("="*60)
print("1. 2단 출력 (Print 2 times table)")
print("="*60)

dan = 2
for i in range(1, 10):
    print(f"{dan} × {i} = {dan * i}")

print()

# ===== 2. 전체 구구단 출력 (Print all tables) =====

print("="*60)
print("2. 전체 구구단 (2단 ~ 9단)")
print("="*60)

for dan in range(2, 10):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i:2d}")  # :2d로 정렬

print()

# ===== 3. 가로로 출력 (Print horizontally) =====

print("="*60)
print("3. 구구단 가로 출력")
print("="*60)

for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan}×{i}={dan*i:2d}", end="  ")
    print()

print()

# ===== 4. 표 형식으로 출력 (Print in table format) =====

print("="*60)
print("4. 구구단 표 형식")
print("="*60)

# 헤더 출력 (Print header)
print("    |", end="")
for dan in range(2, 10):
    print(f"  {dan}단 ", end="")
print()
print("-" * 60)

# 내용 출력 (Print content)
for i in range(1, 10):
    print(f" ×{i} |", end="")
    for dan in range(2, 10):
        result = dan * i
        print(f"  {result:2d}  ", end="")
    print()

print()

# ===== 5. 사용자 입력으로 특정 단 출력 (User input for specific table) =====

print("="*60)
print("5. 원하는 단 출력 (대화형 - 시뮬레이션)")
print("="*60)

# 실제 실행 시에는 아래 주석을 해제하세요 (Uncomment for actual execution)
# dan = int(input("원하는 단을 입력하세요 (2-9): "))

# 시뮬레이션 (Simulation)
dan = 7  # 예시로 7단 선택

if 2 <= dan <= 9:
    print(f"\n[{dan}단 출력]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")
else:
    print("2부터 9 사이의 숫자를 입력하세요!")

print()

# ===== 6. 역순 구구단 (Reverse multiplication table) =====

print("="*60)
print("6. 역순 구구단 (9단 → 2단)")
print("="*60)

for dan in range(9, 1, -1):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

print()

# ===== 7. 짝수 단만 출력 (Print only even tables) =====

print("="*60)
print("7. 짝수 단만 출력 (2, 4, 6, 8단)")
print("="*60)

for dan in range(2, 10, 2):  # 2씩 증가
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

print()

# ===== 8. 특정 결과값 찾기 (Find specific results) =====

print("="*60)
print("8. 결과가 24인 구구단 찾기")
print("="*60)

target = 24
print(f"결과가 {target}인 경우:")

for dan in range(2, 10):
    for i in range(1, 10):
        if dan * i == target:
            print(f"{dan} × {i} = {target}")

print()

# ===== 9. 구구단 퀴즈 (Multiplication quiz) =====

print("="*60)
print("9. 구구단 퀴즈 (시뮬레이션)")
print("="*60)

import random

dan = random.randint(2, 9)
num = random.randint(1, 9)
correct_answer = dan * num

print(f"문제: {dan} × {num} = ?")

# 시뮬레이션: 자동 답변 (Simulation: auto answer)
user_answer = correct_answer  # 예시로 정답 입력

if user_answer == correct_answer:
    print(f"정답! {dan} × {num} = {correct_answer}")
else:
    print(f"오답! 정답은 {correct_answer}입니다.")

print()

# ===== 10. 구구단 전체 메뉴 시스템 (Complete menu system) =====

print("="*60)
print("10. 구구단 메뉴 시스템 (Menu system)")
print("="*60)

def print_single_table(dan):
    """특정 단 출력"""
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i}")

def print_all_tables():
    """전체 구구단 출력"""
    for dan in range(2, 10):
        print_single_table(dan)
        print()

def print_range_tables(start, end):
    """범위 내 구구단 출력"""
    for dan in range(start, end + 1):
        print_single_table(dan)
        print()

# 메뉴 시뮬레이션 (Menu simulation)
print("\n=== 구구단 메뉴 ===")
print("1. 특정 단 출력")
print("2. 전체 구구단 (2-9단)")
print("3. 범위 지정 출력")
print("4. 종료")

# 시뮬레이션: 메뉴 2 선택 (Simulation: select menu 2)
choice = "2"

if choice == "1":
    dan = 5  # 예시
    print_single_table(dan)
elif choice == "2":
    print_all_tables()
elif choice == "3":
    start, end = 3, 5  # 예시
    print_range_tables(start, end)
elif choice == "4":
    print("종료합니다.")
else:
    print("잘못된 선택입니다.")

print()

# ===== 11. 보너스: 확장 구구단 (Extended tables) =====

print("="*60)
print("11. 보너스: 확장 구구단 (10단 ~ 15단)")
print("="*60)

for dan in range(10, 16):
    print(f"\n[{dan}단]")
    for i in range(1, 10):
        print(f"{dan} × {i} = {dan * i:3d}")

print()
print("="*60)
print("구구단 프로그램 완료! (Multiplication table completed!)")
print("="*60)
