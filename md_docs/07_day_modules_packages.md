# 7일차: 모듈과 패키지

## 학습 목표
- 모듈의 개념 이해
- 표준 라이브러리 활용
- 사용자 정의 모듈 작성
- 패키지 구조 이해
- pip를 이용한 외부 패키지 설치

---

## 1. 모듈 (Module)

### 1.1 모듈이란?
- 파이썬 코드를 담고 있는 파일 (.py)
- 함수, 클래스, 변수 등을 재사용 가능하게 구성
- 코드의 모듈화와 재사용성 향상

### 1.2 모듈 import

```python
# 전체 모듈 import
import math
print(math.pi)  # 3.141592...
print(math.sqrt(16))  # 4.0

# 특정 함수만 import
from math import pi, sqrt
print(pi)
print(sqrt(16))

# 모든 함수 import (비권장)
from math import *

# 별칭 사용
import math as m
print(m.pi)

from math import sqrt as square_root
print(square_root(16))
```

---

## 2. 표준 라이브러리

### 2.1 math 모듈

```python
import math

# 상수
print(math.pi)  # 원주율
print(math.e)   # 자연상수

# 기본 함수
print(math.ceil(3.7))   # 올림: 4
print(math.floor(3.7))  # 내림: 3
print(math.trunc(3.7))  # 버림: 3
print(math.sqrt(16))    # 제곱근: 4.0
print(math.pow(2, 3))   # 거듭제곱: 8.0

# 삼각함수
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# 로그
print(math.log(10))      # 자연로그
print(math.log10(100))   # 상용로그: 2.0
```

### 2.2 random 모듈

```python
import random

# 랜덤 정수
print(random.randint(1, 10))  # 1~10 사이의 정수

# 랜덤 실수
print(random.random())  # 0.0~1.0 사이
print(random.uniform(1.0, 10.0))  # 1.0~10.0 사이

# 랜덤 선택
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))  # 하나 선택
print(random.sample(colors, 2))  # 여러 개 선택

# 리스트 섞기
random.shuffle(colors)
print(colors)

# 시드 설정 (재현 가능한 랜덤)
random.seed(42)
print(random.randint(1, 100))
```

### 2.3 datetime 모듈

```python
from datetime import datetime, date, time, timedelta

# 현재 날짜와 시간
now = datetime.now()
print(now)

today = date.today()
print(today)

# 날짜 생성
birthday = date(1995, 3, 15)
print(birthday)

# 시간 생성
meeting_time = time(14, 30, 0)
print(meeting_time)

# 날짜 연산
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)

# 날짜 차이
age_days = (today - birthday).days
age_years = age_days // 365

# 포맷팅
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)  # 2024-01-15 14:30:00

# 파싱
date_string = "2024-01-15"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
```

### 2.4 os 모듈

```python
import os

# 현재 작업 디렉토리
print(os.getcwd())

# 디렉토리 변경
# os.chdir("/path/to/directory")

# 디렉토리 생성
# os.mkdir("new_folder")
# os.makedirs("parent/child/grandchild")

# 파일 및 디렉토리 목록
print(os.listdir("."))

# 경로 관련
print(os.path.exists("file.txt"))  # 파일 존재 여부
print(os.path.isfile("file.txt"))  # 파일인지 확인
print(os.path.isdir("folder"))     # 디렉토리인지 확인
print(os.path.join("folder", "file.txt"))  # 경로 결합

# 환경 변수
print(os.environ.get("HOME"))  # HOME 환경 변수
```

### 2.5 sys 모듈

```python
import sys

# Python 버전
print(sys.version)

# 명령줄 인자
print(sys.argv)  # 스크립트 실행 시 전달된 인자

# 모듈 검색 경로
print(sys.path)

# 프로그램 종료
# sys.exit(0)
```

---

## 3. 사용자 정의 모듈

### 3.1 모듈 작성

**calculator.py**
```python
"""
간단한 계산기 모듈
Simple calculator module
"""

def add(a, b):
    """두 수를 더합니다"""
    return a + b

def subtract(a, b):
    """두 수를 뺍니다"""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다"""
    return a * b

def divide(a, b):
    """두 수를 나눕니다"""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return a / b

# 모듈 레벨 변수
PI = 3.14159

if __name__ == "__main__":
    # 모듈을 직접 실행할 때만 실행되는 코드
    print("Calculator module test")
    print(f"2 + 3 = {add(2, 3)}")
```

### 3.2 모듈 사용

**main.py**
```python
# 같은 디렉토리의 모듈 import
import calculator

result = calculator.add(10, 5)
print(result)

# 또는
from calculator import add, subtract
result = add(10, 5)
```

---

## 4. 패키지 (Package)

### 4.1 패키지 구조

```
my_package/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
```

### 4.2 __init__.py

```python
# __init__.py
"""
My Package
패키지 초기화 파일
"""

# 패키지 버전
__version__ = "1.0.0"

# 패키지 임포트 시 자동으로 import할 모듈
from .module1 import function1
from .module2 import function2

# __all__ 정의 (from package import * 시 포함될 항목)
__all__ = ["function1", "function2"]
```

### 4.3 패키지 사용

```python
# 전체 패키지 import
import my_package

# 특정 모듈 import
from my_package import module1

# 특정 함수 import
from my_package.module1 import function1

# 서브패키지 import
from my_package.subpackage import module3
```

---

## 5. 외부 패키지 관리 (pip)

### 5.1 pip 기본 명령어

```bash
# 패키지 설치
pip install requests

# 특정 버전 설치
pip install requests==2.28.0

# 패키지 업그레이드
pip install --upgrade requests

# 패키지 제거
pip uninstall requests

# 설치된 패키지 목록
pip list

# 패키지 정보 확인
pip show requests

# requirements.txt 생성
pip freeze > requirements.txt

# requirements.txt로 설치
pip install -r requirements.txt
```

### 5.2 주요 외부 패키지

| 패키지 | 용도 |
|--------|------|
| requests | HTTP 요청 |
| numpy | 수치 계산 |
| pandas | 데이터 분석 |
| matplotlib | 데이터 시각화 |
| beautifulsoup4 | 웹 스크래핑 |
| flask | 웹 프레임워크 |
| django | 웹 프레임워크 |
| pytest | 테스트 |

---

## 실습 과제

### 과제 1: 유틸리티 모듈
자주 사용하는 함수들을 모아둔 유틸리티 모듈 작성

### 과제 2: 날짜 계산기
datetime 모듈을 이용한 날짜 계산 프로그램

### 과제 3: 파일 관리 도구
os 모듈을 이용한 파일/폴더 관리 프로그램

### 과제 4: 랜덤 게임
random 모듈을 이용한 간단한 게임

### 과제 5: 계산기 패키지
다양한 계산 기능을 가진 패키지 작성

---

## 다음 시간 예고

8일차에는 **파일 입출력**을 학습합니다.
