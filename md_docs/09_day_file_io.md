# 9일차: 파일 입출력

## 학습 목표
- 파일 읽기/쓰기 기본
- with 문을 이용한 안전한 파일 처리
- CSV 파일 다루기
- JSON 파일 다루기
- 파일 경로 처리

---

## 1. 파일 기본 연산

### 1.1 파일 열기/닫기

```python
# 파일 열기
file = open("data.txt", "r")  # 읽기 모드
content = file.read()
file.close()  # 반드시 닫아야 함!

# with 문 사용 (권장) - 자동으로 닫힘
with open("data.txt", "r") as file:
    content = file.read()
# with 블록을 벗어나면 자동으로 close()
```

### 1.2 파일 모드

| 모드 | 설명 |
|------|------|
| 'r' | 읽기 (기본값) |
| 'w' | 쓰기 (기존 내용 삭제) |
| 'a' | 추가 (파일 끝에 추가) |
| 'r+' | 읽기/쓰기 |
| 'rb' | 이진 읽기 |
| 'wb' | 이진 쓰기 |

---

## 2. 파일 읽기

### 2.1 전체 읽기

```python
# read() - 전체 내용 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

### 2.2 한 줄씩 읽기

```python
# readline() - 한 줄씩 읽기
with open("data.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    while line:
        print(line.strip())  # strip()으로 줄바꿈 제거
        line = f.readline()

# readlines() - 모든 줄을 리스트로
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

# 가장 pythonic한 방법
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

---

## 3. 파일 쓰기

### 3.1 기본 쓰기

```python
# write() - 문자열 쓰기
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Python File I/O\n")

# writelines() - 리스트의 각 요소 쓰기
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

### 3.2 추가 모드

```python
# 'a' 모드 - 파일 끝에 추가
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("New log entry\n")
```

---

## 4. CSV 파일 처리

### 4.1 CSV 읽기

```python
import csv

# CSV 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # 리스트로 반환

# 딕셔너리로 읽기
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # 딕셔너리로 반환
        print(row["name"], row["age"])
```

### 4.2 CSV 쓰기

```python
import csv

# CSV 쓰기
data = [
    ["name", "age", "city"],
    ["Alice", "25", "Seoul"],
    ["Bob", "30", "Busan"]
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 딕셔너리로 쓰기
data = [
    {"name": "Alice", "age": 25, "city": "Seoul"},
    {"name": "Bob", "age": 30, "city": "Busan"}
]

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

---

## 5. JSON 파일 처리

### 5.1 JSON 읽기

```python
import json

# JSON 파일 읽기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)

# JSON 문자열 파싱
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)
print(data["name"])
```

### 5.2 JSON 쓰기

```python
import json

# Python 객체를 JSON으로
data = {
    "name": "Alice",
    "age": 25,
    "city": "Seoul",
    "hobbies": ["reading", "coding"]
}

# JSON 파일로 저장
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# JSON 문자열로 변환
json_string = json.dumps(data, indent=4, ensure_ascii=False)
print(json_string)
```

---

## 6. 파일 경로 처리

### 6.1 os.path 사용

```python
import os

# 경로 결합
path = os.path.join("folder", "subfolder", "file.txt")

# 경로 분리
dir_path, filename = os.path.split("/path/to/file.txt")

# 확장자 분리
name, ext = os.path.splitext("file.txt")

# 절대 경로
abs_path = os.path.abspath("file.txt")

# 파일 존재 확인
exists = os.path.exists("file.txt")
```

### 6.2 pathlib 사용 (Python 3.4+)

```python
from pathlib import Path

# Path 객체 생성
path = Path("folder") / "subfolder" / "file.txt"

# 파일 읽기
content = path.read_text(encoding="utf-8")

# 파일 쓰기
path.write_text("Hello", encoding="utf-8")

# 파일 존재 확인
if path.exists():
    print("File exists")

# 디렉토리 생성
path.parent.mkdir(parents=True, exist_ok=True)

# 파일 정보
print(path.name)        # 파일명
print(path.stem)        # 확장자 제외
print(path.suffix)      # 확장자
print(path.parent)      # 부모 디렉토리
```

---

## 7. 실전 예제

### 7.1 로그 파일 작성

```python
from datetime import datetime

def write_log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {message}\n"

    with open("app.log", "a", encoding="utf-8") as f:
        f.write(log_message)

write_log("Application started")
write_log("User logged in")
```

### 7.2 설정 파일 관리

```python
import json

# 설정 파일 읽기
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"default": "config"}

# 설정 파일 저장
def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

config = load_config()
config["new_setting"] = "value"
save_config(config)
```

---

## 실습 과제

### 과제 1: 일기장 프로그램
날짜별로 일기를 저장하고 조회하는 프로그램

### 과제 2: 학생 성적 관리
CSV 파일로 학생 성적 데이터 관리

### 과제 3: 할 일 관리 (TODO)
JSON으로 할 일 목록 저장/관리

### 과제 4: 로그 분석기
로그 파일을 읽어 통계 정보 출력

### 과제 5: 파일 정리 도구
특정 폴더의 파일을 확장자별로 정리

---

## 다음 시간 예고

10일차에는 **예외 처리 및 디버깅**을 학습합니다.
