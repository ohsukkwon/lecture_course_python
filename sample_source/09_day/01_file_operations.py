"""
파일명: 01_file_operations.py
설명: 파일 입출력 기본
Filename: 01_file_operations.py
Description: File I/O basics
"""

import os

# ===== 1. 파일 쓰기 =====
print("="*60)
print("1. 파일 쓰기")
print("="*60)

# 파일 쓰기
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요\n")
    f.write("파이썬 파일 입출력\n")
    f.write("Hello Python File I/O\n")

print("sample.txt 파일 생성 완료")

# ===== 2. 파일 읽기 =====
print("\n" + "="*60)
print("2. 파일 읽기")
print("="*60)

with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# ===== 3. 한 줄씩 읽기 =====
print("="*60)
print("3. 한 줄씩 읽기")
print("="*60)

with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# ===== 4. 파일 추가 =====
print("\n" + "="*60)
print("4. 파일에 내용 추가")
print("="*60)

with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("추가된 내용\n")
    f.write("Appended content\n")

print("내용 추가 완료")

# 다시 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())

# ===== 5. CSV 파일 =====
print("="*60)
print("5. CSV 파일")
print("="*60)

import csv

# CSV 쓰기
students = [
    ["이름", "나이", "점수"],
    ["철수", "20", "85"],
    ["영희", "21", "92"],
    ["민수", "22", "78"]
]

with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)

print("students.csv 생성 완료")

# CSV 읽기
with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(", ".join(row))

# ===== 6. JSON 파일 =====
print("\n" + "="*60)
print("6. JSON 파일")
print("="*60)

import json

data = {
    "name": "김철수",
    "age": 25,
    "hobbies": ["독서", "코딩", "운동"],
    "scores": {"math": 90, "english": 85}
}

# JSON 쓰기
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("data.json 생성 완료")

# JSON 읽기
with open("data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(json.dumps(loaded_data, indent=2, ensure_ascii=False))

# 파일 정리
print("\n생성된 파일들을 확인하세요:")
print("- sample.txt")
print("- students.csv")
print("- data.json")

print("\n" + "="*60)
print("파일 입출력 예제 완료!")
print("="*60)
