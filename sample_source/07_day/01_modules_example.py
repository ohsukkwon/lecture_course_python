"""
파일명: 01_modules_example.py
설명: 모듈 활용 예제 (math, random, datetime)
Filename: 01_modules_example.py
Description: Module usage examples
"""

# ===== 1. math 모듈 =====
print("="*60)
print("1. math 모듈")
print("="*60)

import math

print(f"원주율 π: {math.pi}")
print(f"자연상수 e: {math.e}")
print(f"sqrt(16): {math.sqrt(16)}")
print(f"pow(2, 3): {math.pow(2, 3)}")
print(f"ceil(3.2): {math.ceil(3.2)}")
print(f"floor(3.8): {math.floor(3.8)}")

print()

# ===== 2. random 모듈 =====
print("="*60)
print("2. random 모듈")
print("="*60)

import random

print(f"랜덤 정수 (1-10): {random.randint(1, 10)}")
print(f"랜덤 실수 (0-1): {random.random()}")

colors = ["red", "blue", "green", "yellow"]
print(f"랜덤 선택: {random.choice(colors)}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"섞기: {numbers}")

print()

# ===== 3. datetime 모듈 =====
print("="*60)
print("3. datetime 모듈")
print("="*60)

from datetime import datetime, timedelta

now = datetime.now()
print(f"현재 시간: {now}")
print(f"포맷팅: {now.strftime('%Y-%m-%d %H:%M:%S')}")

tomorrow = now + timedelta(days=1)
print(f"내일: {tomorrow.strftime('%Y-%m-%d')}")

birthday = datetime(1995, 3, 15)
age_days = (now - birthday).days
print(f"태어난 지 {age_days}일")

print()

# ===== 4. 실전 예제: 주사위 게임 =====
print("="*60)
print("4. 실전 예제: 주사위 게임")
print("="*60)

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
total = dice1 + dice2

print(f"주사위 1: {dice1}")
print(f"주사위 2: {dice2}")
print(f"합계: {total}")

if total == 7:
    print("행운의 7!")
elif total >= 10:
    print("큰 수!")
else:
    print("도전!")

print()
print("="*60)
print("모듈 예제 완료!")
print("="*60)
