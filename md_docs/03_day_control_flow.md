# 3일차: 제어문 - 조건문과 반복문

## 학습 목표
- 조건문(if-elif-else)을 사용한 프로그램 흐름 제어
- for 반복문으로 순회 작업 수행
- while 반복문으로 조건 기반 반복 수행
- break, continue, pass의 활용
- 중첩 반복문 이해 및 활용

---

## 1. 조건문 (Conditional Statements)

### 1.1 if 문

```python
age = 20

if age >= 18:
    print("성인입니다")  # 조건이 True일 때 실행
```

**중요**: 파이썬은 들여쓰기(indentation)로 코드 블록을 구분합니다!

### 1.2 if-else 문

```python
score = 85

if score >= 60:
    print("합격")
else:
    print("불합격")
```

### 1.3 if-elif-else 문

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"학점: {grade}")
```

### 1.4 중첩 if 문

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능")
    else:
        print("면허 필요")
else:
    print("나이 미달")
```

### 1.5 조건 표현식 (Conditional Expression)

```python
# 삼항 연산자 (Ternary operator)
age = 20
status = "성인" if age >= 18 else "미성년자"
print(status)

# 일반 if-else와 동일
if age >= 18:
    status = "성인"
else:
    status = "미성년자"
```

---

## 2. for 반복문 (for Loop)

### 2.1 기본 사용법

```python
# 리스트 순회
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 문자열 순회
for char in "Python":
    print(char)
```

### 2.2 range() 함수

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 역순
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

### 2.3 enumerate() 함수

```python
fruits = ["apple", "banana", "cherry"]

# 인덱스와 값 동시에 가져오기
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

### 2.4 zip() 함수

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# 여러 리스트 동시 순회
for name, age in zip(names, ages):
    print(f"{name}: {age}세")
```

---

## 3. while 반복문 (while Loop)

### 3.1 기본 사용법

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### 3.2 무한 루프

```python
# 무한 루프 (Ctrl+C로 중단)
# while True:
#     print("무한 반복")

# 실용적인 무한 루프
while True:
    user_input = input("종료하려면 'q' 입력: ")
    if user_input == 'q':
        break
    print(f"입력: {user_input}")
```

### 3.3 while-else

```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("반복 완료")  # 정상 종료 시 실행
```

---

## 4. 제어문 (Control Statements)

### 4.1 break

반복문을 즉시 종료

```python
for i in range(10):
    if i == 5:
        break  # 반복문 종료
    print(i)  # 0, 1, 2, 3, 4
```

### 4.2 continue

현재 반복을 건너뛰고 다음 반복으로

```python
for i in range(5):
    if i == 2:
        continue  # i=2일 때 아래 코드 건너뜀
    print(i)  # 0, 1, 3, 4
```

### 4.3 pass

아무것도 하지 않음 (자리 표시용)

```python
for i in range(5):
    if i == 2:
        pass  # 나중에 구현 예정
    print(i)  # 0, 1, 2, 3, 4
```

---

## 5. 중첩 반복문 (Nested Loops)

### 5.1 기본 중첩

```python
# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} × {j} = {i*j}")
    print()  # 단 구분
```

### 5.2 별 찍기 패턴

```python
# 직각삼각형
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 출력:
# *
# **
# ***
# ****
# *****
```

---

## 6. 리스트 컴프리헨션 (List Comprehension)

간결한 리스트 생성 방법

```python
# 일반 방법
squares = []
for i in range(10):
    squares.append(i ** 2)

# 리스트 컴프리헨션
squares = [i ** 2 for i in range(10)]

# 조건 포함
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]

# 중첩
matrix = [[i*j for j in range(3)] for i in range(3)]
```

---

## 7. 실전 패턴

### 7.1 메뉴 선택 루프

```python
while True:
    print("\n=== 메뉴 ===")
    print("1. 추가")
    print("2. 삭제")
    print("3. 종료")

    choice = input("선택: ")

    if choice == '1':
        print("추가 기능")
    elif choice == '2':
        print("삭제 기능")
    elif choice == '3':
        print("종료합니다")
        break
    else:
        print("잘못된 선택")
```

### 7.2 입력 검증

```python
while True:
    age = input("나이 입력: ")

    if age.isdigit():
        age = int(age)
        if 0 < age < 150:
            break
        else:
            print("올바른 나이를 입력하세요")
    else:
        print("숫자를 입력하세요")

print(f"입력된 나이: {age}")
```

---

## 실습 과제

### 과제 1: 성적 처리 프로그램
학생 5명의 점수를 입력받아 평균과 등급 출력

### 과제 2: 구구단 출력
사용자가 원하는 단의 구구단 출력

### 과제 3: 숫자 맞추기 게임
1~100 사이의 랜덤 숫자를 맞추는 게임 (힌트 제공)

### 과제 4: 별 패턴 출력
다양한 별 패턴 출력 (피라미드, 다이아몬드 등)

### 과제 5: 소수 찾기
1~100 사이의 모든 소수 찾아 출력

---

## 참고 자료

- 제어문: https://docs.python.org/ko/3/tutorial/controlflow.html
- 반복문: https://docs.python.org/ko/3/reference/compound_stmts.html

---

## 다음 시간 예고

4일차에는 **함수(Functions)**에 대해 학습합니다.
- 함수 정의 및 호출
- 매개변수와 인자
- 반환값
- 람다 함수
- 변수 스코프

**미리 준비**: 함수의 개념과 필요성 생각해보기
