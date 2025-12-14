# 9일차: 예외 처리 및 디버깅

## 학습 목표
- 예외(Exception)의 개념 이해
- try-except-else-finally 구문 활용
- 예외 발생시키기 (raise)
- 사용자 정의 예외 작성
- 디버깅 기법 익히기

---

## 1. 예외란?

### 1.1 예외의 정의
- 프로그램 실행 중 발생하는 오류
- 문법 오류(Syntax Error)와 다름
- 적절히 처리하지 않으면 프로그램 종료

### 1.2 주요 내장 예외

| 예외 | 설명 |
|------|------|
| ZeroDivisionError | 0으로 나누기 |
| ValueError | 부적절한 값 |
| TypeError | 부적절한 타입 |
| IndexError | 인덱스 범위 초과 |
| KeyError | 딕셔너리 키 없음 |
| FileNotFoundError | 파일 없음 |
| AttributeError | 속성 없음 |
| NameError | 이름 없음 |
| ImportError | import 실패 |

---

## 2. try-except 문

### 2.1 기본 구조

```python
try:
    # 예외가 발생할 수 있는 코드
    result = 10 / 0
except:
    # 예외 처리
    print("오류 발생!")
```

### 2.2 특정 예외 처리

```python
try:
    number = int(input("숫자 입력: "))
    result = 100 / number
except ValueError:
    print("숫자를 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
```

### 2.3 여러 예외 동시 처리

```python
try:
    # 코드
    pass
except (ValueError, TypeError):
    print("ValueError 또는 TypeError 발생")
```

### 2.4 예외 객체 활용

```python
try:
    number = int(input("숫자 입력: "))
    result = 100 / number
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
```

---

## 3. else와 finally

### 3.1 else 절

```python
try:
    number = int(input("숫자 입력: "))
except ValueError:
    print("숫자가 아닙니다")
else:
    # 예외가 발생하지 않았을 때 실행
    print(f"입력한 숫자: {number}")
```

### 3.2 finally 절

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("파일이 없습니다")
else:
    print("파일 읽기 성공")
finally:
    # 예외 발생 여부와 관계없이 항상 실행
    file.close()
    print("파일 닫기")
```

### 3.3 전체 구조

```python
try:
    # 예외가 발생할 수 있는 코드
    pass
except 예외타입1:
    # 예외타입1 처리
    pass
except 예외타입2:
    # 예외타입2 처리
    pass
else:
    # 예외가 발생하지 않았을 때
    pass
finally:
    # 항상 실행
    pass
```

---

## 4. 예외 발생시키기

### 4.1 raise 문

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b는 0이 될 수 없습니다")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"오류: {e}")
```

### 4.2 예외 재발생

```python
try:
    number = int(input("숫자 입력: "))
except ValueError:
    print("숫자 입력 오류")
    raise  # 예외를 다시 발생시킴
```

---

## 5. 사용자 정의 예외

### 5.1 기본 정의

```python
class MyException(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise MyException("양수만 허용됩니다")
    return number

try:
    check_positive(-5)
except MyException as e:
    print(f"오류: {e}")
```

### 5.2 고급 사용자 정의 예외

```python
class InvalidAgeError(Exception):
    """나이 검증 예외"""

    def __init__(self, age, message="나이가 유효하지 않습니다"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} (입력값: {self.age})"

def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    return True

try:
    validate_age(-5)
except InvalidAgeError as e:
    print(e)
```

---

## 6. 디버깅 기법

### 6.1 print() 디버깅

```python
def calculate_average(numbers):
    print(f"Debug: numbers = {numbers}")  # 디버그 출력
    total = sum(numbers)
    print(f"Debug: total = {total}")
    count = len(numbers)
    print(f"Debug: count = {count}")
    return total / count
```

### 6.2 assert 문

```python
def divide(a, b):
    assert b != 0, "b는 0이 될 수 없습니다"
    return a / b

# 디버그 모드에서만 작동 (python -O로 실행하면 무시됨)
```

### 6.3 logging 모듈

```python
import logging

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(a, b):
    logging.debug(f"calculate 함수 호출: a={a}, b={b}")
    result = a + b
    logging.info(f"계산 결과: {result}")
    return result

result = calculate(10, 20)
```

### 6.4 로깅 레벨

```python
import logging

logging.debug("디버그 메시지")      # DEBUG
logging.info("정보 메시지")        # INFO
logging.warning("경고 메시지")     # WARNING
logging.error("오류 메시지")       # ERROR
logging.critical("심각한 오류")    # CRITICAL
```

---

## 7. 예외 처리 모범 사례

### 7.1 구체적인 예외 처리

```python
# ❌ 나쁜 예
try:
    # 코드
    pass
except:
    pass  # 모든 예외를 무시

# ✅ 좋은 예
try:
    # 코드
    pass
except ValueError:
    # 특정 예외 처리
    pass
```

### 7.2 예외 정보 기록

```python
import logging

try:
    # 코드
    result = 10 / 0
except Exception as e:
    logging.error(f"오류 발생: {e}", exc_info=True)
    # exc_info=True: 전체 스택 트레이스 기록
```

### 7.3 리소스 정리

```python
# ✅ with 문 사용 (권장)
with open("file.txt", "r") as f:
    content = f.read()
# 자동으로 닫힘

# 또는 try-finally
f = None
try:
    f = open("file.txt", "r")
    content = f.read()
finally:
    if f:
        f.close()
```

---

## 8. 실전 예제

### 8.1 안전한 사용자 입력

```python
def get_integer_input(prompt, min_value=None, max_value=None):
    """안전한 정수 입력"""
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"{min_value} 이상을 입력하세요")
                continue

            if max_value is not None and value > max_value:
                print(f"{max_value} 이하를 입력하세요")
                continue

            return value

        except ValueError:
            print("정수를 입력하세요")

age = get_integer_input("나이 입력: ", min_value=0, max_value=150)
```

### 8.2 파일 처리 with 예외 처리

```python
def read_config(filename):
    """설정 파일 읽기"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"설정 파일 없음: {filename}, 기본값 사용")
        return {"default": True}
    except json.JSONDecodeError as e:
        logging.error(f"JSON 파싱 오류: {e}")
        raise
```

---

## 실습 과제

### 과제 1: 계산기 with 예외 처리
다양한 예외를 처리하는 계산기

### 과제 2: 파일 읽기 프로그램
존재하지 않는 파일 등 예외 처리

### 과제 3: 사용자 입력 검증
나이, 전화번호 등 입력 검증 프로그램

### 과제 4: 로그 시스템
logging 모듈을 활용한 로그 시스템

### 과제 5: 사용자 정의 예외
은행 계좌 시스템의 사용자 정의 예외

---

## 다음 시간 예고

10일차에는 **객체지향 프로그래밍 I - 기초**를 학습합니다.
