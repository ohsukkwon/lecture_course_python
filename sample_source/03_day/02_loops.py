"""
파일명: 02_loops.py
설명: 반복문 (for, while) 및 제어문 (break, continue, pass)
Filename: 02_loops.py
Description: Loops (for, while) and control statements (break, continue, pass)
"""

# ===== 1. for 반복문 - 리스트 순회 (for loop - iterate list) =====

print("="*60)
print("1. for 반복문 - 리스트 순회 (for loop - list)")
print("="*60)

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"과일: {fruit}")

print()

# ===== 2. for 반복문 - range() 함수 (for loop - range function) =====

print("="*60)
print("2. for 반복문 - range() 함수")
print("="*60)

# range(stop)
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("\nrange(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 역순 (Reverse)
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# ===== 3. for 반복문 - enumerate() (for loop - enumerate) =====

print("="*60)
print("3. enumerate() - 인덱스와 값 동시 사용")
print("="*60)

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# 시작 인덱스 지정 (Start index)
print("\n시작 인덱스 1부터:")
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

print()

# ===== 4. for 반복문 - zip() (for loop - zip) =====

print("="*60)
print("4. zip() - 여러 리스트 동시 순회")
print("="*60)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Seoul", "Busan", "Incheon"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}세) - {city}")

print()

# ===== 5. while 반복문 (while loop) =====

print("="*60)
print("5. while 반복문 (while loop)")
print("="*60)

count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

print()

# ===== 6. while 무한 루프 with break (Infinite loop with break) =====

print("="*60)
print("6. while 무한 루프 with break")
print("="*60)

count = 0
while True:
    print(f"반복 {count}")
    count += 1

    if count >= 3:
        print("break로 종료!")
        break

print()

# ===== 7. break 문 (break statement) =====

print("="*60)
print("7. break - 반복문 즉시 종료")
print("="*60)

for i in range(10):
    if i == 5:
        print(f"i가 {i}일 때 break")
        break
    print(i, end=" ")
print("\n")

# ===== 8. continue 문 (continue statement) =====

print("="*60)
print("8. continue - 현재 반복 건너뛰기")
print("="*60)

for i in range(10):
    if i % 2 == 0:  # 짝수일 때 건너뛰기 (Skip even numbers)
        continue
    print(i, end=" ")  # 홀수만 출력 (Only print odd numbers)
print("\n")

# ===== 9. pass 문 (pass statement) =====

print("="*60)
print("9. pass - 아무것도 하지 않음")
print("="*60)

for i in range(5):
    if i == 2:
        pass  # 나중에 구현 예정 (To be implemented later)
    print(i, end=" ")
print("\n")

# ===== 10. 중첩 반복문 (Nested loops) =====

print("="*60)
print("10. 중첩 반복문 - 구구단 2단")
print("="*60)

dan = 2
for i in range(1, 10):
    result = dan * i
    print(f"{dan} × {i} = {result}")

print()

# ===== 11. 중첩 반복문 - 별 찍기 (Nested loops - star pattern) =====

print("="*60)
print("11. 중첩 반복문 - 별 찍기")
print("="*60)

# 직각삼각형 (Right triangle)
print("직각삼각형:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print()

# 역직각삼각형 (Inverted right triangle)
print("역직각삼각형:")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# ===== 12. 리스트 컴프리헨션 (List comprehension) =====

print("="*60)
print("12. 리스트 컴프리헨션 (List comprehension)")
print("="*60)

# 기본 (Basic)
squares = [x**2 for x in range(10)]
print(f"제곱수: {squares}")

# 조건 포함 (With condition)
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"짝수의 제곱: {even_squares}")

# if-else 포함 (With if-else)
numbers = [x if x % 2 == 0 else -x for x in range(10)]
print(f"짝수는 그대로, 홀수는 음수: {numbers}")

print()

# ===== 13. 실전 예제: 합계 계산 (Sum calculation) =====

print("="*60)
print("13. 실전 예제: 1부터 100까지의 합")
print("="*60)

# 방법 1: for 문
total = 0
for i in range(1, 101):
    total += i
print(f"for 문: {total}")

# 방법 2: sum() 함수
total = sum(range(1, 101))
print(f"sum() 함수: {total}")

print()

# ===== 14. 실전 예제: 소수 찾기 (Find prime numbers) =====

print("="*60)
print("14. 실전 예제: 2부터 30까지의 소수")
print("="*60)

primes = []
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(f"소수: {primes}")

print()

# ===== 15. 실전 예제: 팩토리얼 계산 (Factorial calculation) =====

print("="*60)
print("15. 실전 예제: 팩토리얼 계산")
print("="*60)

n = 5
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

print()

# ===== 16. 실전 예제: 숫자 맞추기 게임 (Number guessing game) =====

print("="*60)
print("16. 실전 예제: 숫자 맞추기 게임 (시뮬레이션)")
print("="*60)

import random

# 정답 설정 (Set answer)
answer = random.randint(1, 100)
attempts = 0
max_attempts = 10

print(f"1부터 100 사이의 숫자를 맞춰보세요! (최대 {max_attempts}번)")

# 시뮬레이션: 자동으로 맞추기 (Simulation: auto-guess)
low = 1
high = 100

while attempts < max_attempts:
    attempts += 1
    guess = (low + high) // 2  # 이진 탐색 (Binary search)

    print(f"\n시도 {attempts}: {guess}")

    if guess == answer:
        print(f"🎉 정답! {attempts}번 만에 맞췄습니다!")
        break
    elif guess < answer:
        print("더 큰 수입니다 (Higher)")
        low = guess + 1
    else:
        print("더 작은 수입니다 (Lower)")
        high = guess - 1
else:
    print(f"\n😢 실패! 정답은 {answer}였습니다.")

print()
print("="*60)
print("반복문 예제 완료! (Loops examples completed!)")
print("="*60)
