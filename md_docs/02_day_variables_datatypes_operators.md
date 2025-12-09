# 2일차: 기본 문법 - 변수, 자료형, 연산자

## 학습 목표
- 변수의 개념과 사용법 이해하기
- 파이썬의 기본 자료형 이해하기
- 형 변환(Type Casting) 활용하기
- 다양한 연산자 사용하기
- 문자열 포맷팅 마스터하기

---

## 1. 변수 (Variables)

### 1.1 변수란?
- 데이터를 저장하는 공간 (메모리에 값을 저장)
- 변수명으로 해당 값에 접근 가능
- 파이썬은 동적 타이핑 (변수 타입을 미리 선언할 필요 없음)

### 1.2 변수 선언과 할당

```python
# 변수 선언 및 할당
name = "Python"
age = 30
height = 175.5
is_student = True

# 여러 변수 동시 할당
x, y, z = 10, 20, 30

# 같은 값 여러 변수에 할당
a = b = c = 100
```

### 1.3 변수명 규칙

**✅ 가능한 경우:**
```python
name = "John"
user_name = "John"
userName = "John"  # 가능하지만 PEP 8 권장 스타일 아님
_name = "John"
name2 = "John"
```

**❌ 불가능한 경우:**
```python
2name = "John"  # 숫자로 시작 불가
user-name = "John"  # 하이픈 사용 불가
user name = "John"  # 공백 사용 불가
for = "John"  # 예약어 사용 불가
```

**예약어 (Keywords):**
```python
# 예약어 목록 확인
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', ...]
```

### 1.4 변수명 작성 스타일

| 스타일 | 예시 | 용도 |
|--------|------|------|
| snake_case | user_name, total_price | 변수, 함수 (파이썬 권장) |
| camelCase | userName, totalPrice | 일반적으로 사용하지 않음 |
| PascalCase | UserName, TotalPrice | 클래스명 |
| UPPER_CASE | MAX_SIZE, PI | 상수 |

---

## 2. 기본 자료형 (Data Types)

### 2.1 숫자형 (Numeric Types)

#### 정수형 (int)
```python
num1 = 10
num2 = -5
num3 = 0

# 큰 수도 제한 없이 표현 가능
big_number = 123456789012345678901234567890

# 다양한 진법
binary = 0b1010  # 2진수 (10)
octal = 0o12     # 8진수 (10)
hexa = 0xA       # 16진수 (10)
```

#### 실수형 (float)
```python
pi = 3.14
temperature = -15.5
scientific = 3.14e2  # 314.0 (과학적 표기법)

# 부동소수점 주의사항
print(0.1 + 0.2)  # 0.30000000000000004
```

#### 복소수 (complex)
```python
complex_num = 3 + 4j
print(complex_num.real)  # 3.0 (실수부)
print(complex_num.imag)  # 4.0 (허수부)
```

### 2.2 문자열 (String)

```python
# 문자열 생성
str1 = "Hello"
str2 = 'World'
str3 = """여러 줄
문자열"""
str4 = '''작은따옴표로도
여러 줄 가능'''

# 문자열 연결
greeting = str1 + " " + str2  # "Hello World"

# 문자열 반복
repeat = "Ha" * 3  # "HaHaHa"

# 문자열 인덱싱
text = "Python"
print(text[0])   # 'P' (첫 번째 문자)
print(text[-1])  # 'n' (마지막 문자)

# 문자열 슬라이싱
print(text[0:3])   # 'Pyt'
print(text[2:])    # 'thon'
print(text[:4])    # 'Pyth'
print(text[::2])   # 'Pto' (2칸씩 건너뛰기)
print(text[::-1])  # 'nohtyP' (역순)
```

### 2.3 불린 (Boolean)

```python
is_active = True
is_deleted = False

# 비교 연산 결과
result = 10 > 5  # True
result = 10 < 5  # False

# 논리 연산
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 불린 변환
print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False (빈 문자열)
print(bool("Hi"))   # True
print(bool([]))     # False (빈 리스트)
print(bool([1]))    # True
```

### 2.4 None 타입

```python
# None은 "값이 없음"을 나타냄
value = None

# None 체크
if value is None:
    print("값이 없습니다")

# None과 False는 다름
print(None == False)  # False
print(None is False)  # False
```

---

## 3. 형 변환 (Type Casting)

### 3.1 자동 형 변환 (Implicit)

```python
# int + float → float
result = 10 + 3.14  # 13.14 (float)
```

### 3.2 명시적 형 변환 (Explicit)

```python
# 문자열 → 정수
num = int("100")  # 100

# 문자열 → 실수
price = float("19.99")  # 19.99

# 숫자 → 문자열
text = str(100)  # "100"

# 정수 → 실수
decimal = float(10)  # 10.0

# 실수 → 정수 (소수점 버림)
integer = int(3.14)  # 3

# 불린 변환
bool("False")  # True (빈 문자열이 아니므로)
bool(0)        # False
bool("")       # False
```

### 3.3 형 변환 시 주의사항

```python
# 오류 발생 예시
# num = int("3.14")  # ValueError
# num = int("ABC")   # ValueError

# 올바른 방법
num = int(float("3.14"))  # 3
```

---

## 4. 연산자 (Operators)

### 4.1 산술 연산자

```python
a = 10
b = 3

print(a + b)   # 13 (덧셈)
print(a - b)   # 7 (뺄셈)
print(a * b)   # 30 (곱셈)
print(a / b)   # 3.333... (나눗셈)
print(a // b)  # 3 (몫)
print(a % b)   # 1 (나머지)
print(a ** b)  # 1000 (거듭제곱)
```

### 4.2 비교 연산자

```python
x = 10
y = 20

print(x == y)  # False (같음)
print(x != y)  # True (다름)
print(x > y)   # False (큼)
print(x < y)   # True (작음)
print(x >= y)  # False (크거나 같음)
print(x <= y)  # True (작거나 같음)

# 문자열 비교
print("apple" < "banana")  # True (사전 순서)
```

### 4.3 논리 연산자

```python
# and: 모두 True일 때만 True
print(True and True)    # True
print(True and False)   # False

# or: 하나라도 True면 True
print(True or False)    # True
print(False or False)   # False

# not: 반대로 변환
print(not True)         # False
print(not False)        # True

# 실제 활용
age = 25
is_student = True
print(age >= 18 and is_student)  # True
```

### 4.4 할당 연산자

```python
x = 10

x += 5   # x = x + 5 → 15
x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x /= 4   # x = x / 4 → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 2   # x = x % 2 → 1.0
x **= 3  # x = x ** 3 → 1.0
```

### 4.5 멤버십 연산자

```python
# in: 포함 여부 확인
print("a" in "apple")      # True
print("x" in "apple")      # False
print(1 in [1, 2, 3])      # True

# not in: 미포함 여부 확인
print("x" not in "apple")  # True
```

### 4.6 식별 연산자

```python
# is: 동일한 객체인지 확인
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True (같은 객체)
print(a is c)      # False (다른 객체)
print(a == c)      # True (값은 같음)

# is not: 다른 객체인지 확인
print(a is not c)  # True
```

### 4.7 비트 연산자

```python
a = 5   # 0101
b = 3   # 0011

print(a & b)   # 1 (AND: 0001)
print(a | b)   # 7 (OR: 0111)
print(a ^ b)   # 6 (XOR: 0110)
print(~a)      # -6 (NOT)
print(a << 1)  # 10 (왼쪽 시프트: 1010)
print(a >> 1)  # 2 (오른쪽 시프트: 0010)
```

---

## 5. 문자열 포맷팅

### 5.1 % 포맷팅 (Old Style)

```python
name = "Python"
version = 3.12

print("Language: %s, Version: %.2f" % (name, version))
# Language: Python, Version: 3.12
```

### 5.2 format() 메서드

```python
print("Language: {}, Version: {}".format("Python", 3.12))
print("Language: {0}, Version: {1}".format("Python", 3.12))
print("Language: {lang}, Version: {ver}".format(lang="Python", ver=3.12))
```

### 5.3 f-string (Python 3.6+) ⭐ 추천

```python
name = "Python"
version = 3.12

# 기본 사용
print(f"Language: {name}, Version: {version}")

# 표현식 사용
print(f"10 + 20 = {10 + 20}")

# 포맷 지정
pi = 3.141592
print(f"Pi: {pi:.2f}")  # Pi: 3.14

# 정렬
print(f"{'Left':<10}|")   # 왼쪽 정렬
print(f"{'Center':^10}|")  # 가운데 정렬
print(f"{'Right':>10}|")   # 오른쪽 정렬
```

---

## 6. 주요 문자열 메서드

```python
text = "Hello, Python!"

# 대소문자 변환
print(text.upper())       # HELLO, PYTHON!
print(text.lower())       # hello, python!
print(text.capitalize())  # Hello, python!
print(text.title())       # Hello, Python!

# 공백 제거
text2 = "  Hello  "
print(text2.strip())      # "Hello"
print(text2.lstrip())     # "Hello  "
print(text2.rstrip())     # "  Hello"

# 문자열 검색
print(text.find("Python"))     # 7 (위치 반환)
print(text.find("Java"))       # -1 (없으면 -1)
print(text.index("Python"))    # 7
# print(text.index("Java"))    # ValueError

# 문자열 치환
print(text.replace("Python", "World"))  # Hello, World!

# 문자열 분리
print(text.split(","))   # ['Hello', ' Python!']

# 문자열 결합
words = ["Hello", "Python", "World"]
print("-".join(words))   # Hello-Python-World

# 문자열 확인
print(text.startswith("Hello"))  # True
print(text.endswith("!"))        # True
print("123".isdigit())           # True
print("abc".isalpha())           # True
print("abc123".isalnum())        # True
```

---

## 실습 과제

### 과제 1: 변수와 자료형 연습
다양한 자료형의 변수를 만들고 type() 함수로 타입 확인하기

### 과제 2: BMI 계산기
사용자의 키(cm)와 몸무게(kg)를 입력받아 BMI를 계산하는 프로그램

**BMI 공식**: BMI = 몸무게(kg) / (키(m) ** 2)

**BMI 판정 기준**:
- 18.5 미만: 저체중
- 18.5 ~ 22.9: 정상
- 23.0 ~ 24.9: 비만 전단계
- 25.0 이상: 비만

### 과제 3: 문자열 처리
사용자로부터 문장을 입력받아 다음을 출력:
1. 전체 길이
2. 대문자로 변환
3. 소문자로 변환
4. 단어 개수
5. 역순 출력

### 과제 4: 환율 계산기
- USD to KRW
- EUR to KRW
- JPY to KRW

**실행 예시:**
```
환율 계산기
1. 달러 → 원
2. 유로 → 원
3. 엔화 → 원
선택: 1
금액 입력: 100
결과: 100 USD = 132,500 KRW
```

---

## 참고 자료

- 파이썬 자료형: https://docs.python.org/ko/3/library/stdtypes.html
- 문자열 메서드: https://docs.python.org/ko/3/library/stdtypes.html#string-methods
- PEP 8 스타일 가이드: https://peps.python.org/pep-0008/

---

## 다음 시간 예고

3일차에는 **제어문 (조건문과 반복문)**에 대해 학습합니다.
- if-elif-else 조건문
- for 반복문
- while 반복문
- break, continue, pass

**미리 준비**: 순서도(Flowchart) 개념 알아보기
