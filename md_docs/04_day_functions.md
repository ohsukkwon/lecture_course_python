# 4일차: 함수 (Functions)

## 학습 목표
- 함수의 개념과 필요성 이해
- 함수 정의 및 호출 방법 익히기
- 다양한 매개변수 유형 활용
- 반환값(return) 이해 및 활용
- 변수 스코프(scope) 이해
- 람다 함수 사용법

---

## 1. 함수란?

### 1.1 함수의 정의
- 특정 작업을 수행하는 코드 블록
- 재사용 가능한 코드 단위
- 코드의 가독성과 유지보수성 향상

### 1.2 함수의 필요성
```python
# 함수 없이 (중복 코드)
print("안녕하세요, 철수님!")
print("안녕하세요, 영희님!")
print("안녕하세요, 민수님!")

# 함수 사용 (재사용)
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("철수")
greet("영희")
greet("민수")
```

---

## 2. 함수 정의와 호출

### 2.1 기본 문법

```python
def function_name():
    """독스트링 (Docstring)"""
    # 함수 본문
    pass

# 함수 호출
function_name()
```

### 2.2 간단한 함수 예제

```python
def say_hello():
    """인사 메시지 출력"""
    print("Hello, World!")

say_hello()  # 함수 호출
```

---

## 3. 매개변수와 인자

### 3.1 위치 인자 (Positional Arguments)

```python
def add(a, b):
    return a + b

result = add(3, 5)  # a=3, b=5
print(result)  # 8
```

### 3.2 키워드 인자 (Keyword Arguments)

```python
def introduce(name, age, city):
    print(f"{name}, {age}세, {city} 거주")

introduce(name="철수", age=25, city="서울")
introduce(age=30, name="영희", city="부산")  # 순서 무관
```

### 3.3 기본값 매개변수 (Default Parameters)

```python
def greet(name, message="안녕하세요"):
    print(f"{message}, {name}님!")

greet("철수")  # 기본값 사용
greet("영희", "좋은 아침입니다")  # 기본값 덮어쓰기
```

### 3.4 가변 인자 (*args, **kwargs)

```python
# *args: 위치 인자를 튜플로 받음
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))  # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs: 키워드 인자를 딕셔너리로 받음
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="철수", age=25, city="서울")
```

---

## 4. 반환값 (Return Value)

### 4.1 기본 반환

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8
```

### 4.2 여러 값 반환

```python
def calculate(a, b):
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    return add_result, sub_result, mul_result

add, sub, mul = calculate(10, 5)
print(add, sub, mul)  # 15 5 50
```

### 4.3 조건부 반환

```python
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# 더 간결하게
def is_even(number):
    return number % 2 == 0
```

---

## 5. 변수 스코프 (Variable Scope)

### 5.1 지역 변수 (Local Variable)

```python
def my_function():
    local_var = 10  # 지역 변수
    print(local_var)

my_function()
# print(local_var)  # NameError
```

### 5.2 전역 변수 (Global Variable)

```python
global_var = 100  # 전역 변수

def print_global():
    print(global_var)  # 전역 변수 읽기 가능

print_global()  # 100
```

### 5.3 global 키워드

```python
count = 0

def increment():
    global count  # 전역 변수 수정
    count += 1

increment()
print(count)  # 1
```

---

## 6. 람다 함수 (Lambda Functions)

### 6.1 기본 문법

```python
# 일반 함수
def square(x):
    return x ** 2

# 람다 함수
square = lambda x: x ** 2

print(square(5))  # 25
```

### 6.2 람다 함수 활용

```python
# map()과 함께
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter()와 함께
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# sorted()와 함께
students = [("철수", 85), ("영희", 92), ("민수", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
```

---

## 7. 재귀 함수 (Recursive Functions)

```python
def factorial(n):
    """팩토리얼 계산"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """피보나치 수열"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(7))  # 13
```

---

## 실습 과제

### 과제 1: 계산기 함수
사칙연산(+, -, ×, ÷) 함수 작성

### 과제 2: 온도 변환기
섭씨 ↔ 화씨 변환 함수

### 과제 3: 리스트 처리 함수
최댓값, 최솟값, 평균을 반환하는 함수

### 과제 4: 문자열 처리 함수
회문(palindrome) 판별 함수

### 과제 5: 소수 판별 함수
주어진 숫자가 소수인지 판별

---

## 다음 시간 예고

5일차에는 **자료구조 I - 리스트와 튜플**을 학습합니다.
