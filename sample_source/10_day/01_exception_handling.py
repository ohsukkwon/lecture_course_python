"""
파일명: 01_exception_handling.py
설명: 예외 처리 기본
Filename: 01_exception_handling.py
Description: Exception handling basics
"""

# ===== 1. 기본 try-except =====
print("="*60)
print("1. 기본 try-except")
print("="*60)

try:
    number = int(input("숫자를 입력하세요 (예: 10): ") or "10")
    result = 100 / number
    print(f"결과: {result}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except ValueError:
    print("숫자를 입력하세요!")

print()

# ===== 2. 여러 예외 처리 =====
print("="*60)
print("2. 여러 예외 처리")
print("="*60)

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다"
    except TypeError:
        return "숫자만 입력하세요"

print(divide(10, 2))   # 정상
print(divide(10, 0))   # ZeroDivisionError
print(divide(10, "a")) # TypeError

print()

# ===== 3. try-except-else-finally =====
print("="*60)
print("3. try-except-else-finally")
print("="*60)

try:
    file = open("test.txt", "w")
    file.write("Hello")
except IOError:
    print("파일 오류")
else:
    print("파일 쓰기 성공")
finally:
    file.close()
    print("파일 닫기 (항상 실행)")

print()

# ===== 4. 예외 발생시키기 =====
print("="*60)
print("4. 예외 발생시키기 (raise)")
print("="*60)

def check_age(age):
    if age < 0:
        raise ValueError("나이는 0 이상이어야 합니다")
    if age > 150:
        raise ValueError("나이가 너무 많습니다")
    return f"나이: {age}"

try:
    print(check_age(25))   # 정상
    print(check_age(-5))   # ValueError
except ValueError as e:
    print(f"오류: {e}")

print()

# ===== 5. 사용자 정의 예외 =====
print("="*60)
print("5. 사용자 정의 예외")
print("="*60)

class InsufficientFundsError(Exception):
    """잔액 부족 예외"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"잔액 부족: 현재 {self.balance}원, 출금 요청 {amount}원"
            )
        self.balance -= amount
        return self.balance

account = BankAccount(10000)

try:
    account.withdraw(5000)
    print("5000원 출금 성공")
    account.withdraw(10000)  # 잔액 부족
except InsufficientFundsError as e:
    print(f"오류: {e}")

print()

# ===== 6. 실전 예제: 안전한 입력 =====
print("="*60)
print("6. 실전 예제: 안전한 정수 입력")
print("="*60)

def get_integer_input(prompt, min_value=None, max_value=None):
    """안전한 정수 입력 함수"""
    while True:
        try:
            value = int(input(prompt) or "25")  # 기본값 25

            if min_value is not None and value < min_value:
                print(f"{min_value} 이상을 입력하세요")
                return get_integer_input(prompt, min_value, max_value)

            if max_value is not None and value > max_value:
                print(f"{max_value} 이하를 입력하세요")
                return get_integer_input(prompt, min_value, max_value)

            return value
        except ValueError:
            print("정수를 입력하세요")
            return 25  # 기본값

age = get_integer_input("나이를 입력하세요 (0-150): ", 0, 150)
print(f"입력된 나이: {age}")

print()
print("="*60)
print("예외 처리 예제 완료!")
print("="*60)
