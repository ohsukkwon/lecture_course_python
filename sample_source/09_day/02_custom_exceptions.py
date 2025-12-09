"""
파일명: 02_custom_exceptions.py
설명: 사용자 정의 예외와 고급 예외 처리
Filename: 02_custom_exceptions.py
Description: Custom exceptions and advanced error handling
"""

print("="*70)
print("사용자 정의 예외와 고급 예외 처리")
print("Custom Exceptions and Advanced Error Handling")
print("="*70)
print()

# ===== 1. 기본 사용자 정의 예외 (Basic custom exception) =====
print("="*70)
print("1. 기본 사용자 정의 예외 (Basic Custom Exception)")
print("="*70)
print()

class CustomError(Exception):
    """기본 사용자 정의 예외"""
    pass

# 사용 예제 (Usage example)
def divide_custom(a, b):
    """사용자 정의 예외를 발생시키는 나눗셈"""
    if b == 0:
        raise CustomError("0으로 나눌 수 없습니다!")
    return a / b

try:
    result = divide_custom(10, 0)
except CustomError as e:
    print(f"❌ CustomError 발생: {e}")

print()

# ===== 2. 메시지를 가진 사용자 정의 예외 (Custom exception with message) =====
print("="*70)
print("2. 메시지를 가진 사용자 정의 예외")
print("="*70)
print()

class ValidationError(Exception):
    """검증 실패 예외"""
    def __init__(self, message, value=None):
        self.message = message
        self.value = value
        super().__init__(self.message)

    def __str__(self):
        if self.value is not None:
            return f"{self.message} (입력값: {self.value})"
        return self.message

# 사용 예제 (Usage example)
def validate_age(age):
    """나이 검증 함수"""
    if age < 0:
        raise ValidationError("나이는 음수일 수 없습니다", age)
    if age > 150:
        raise ValidationError("나이가 너무 큽니다", age)
    return True

try:
    validate_age(-5)
except ValidationError as e:
    print(f"❌ {e}")

try:
    validate_age(200)
except ValidationError as e:
    print(f"❌ {e}")

print()

# ===== 3. 예외 계층 구조 (Exception hierarchy) =====
print("="*70)
print("3. 예외 계층 구조 (Exception Hierarchy)")
print("="*70)
print()

class BankError(Exception):
    """은행 거래 관련 기본 예외"""
    pass

class InsufficientFundsError(BankError):
    """잔액 부족 예외"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"잔액 부족: 현재 {balance:,}원, 요청 {amount:,}원"
        super().__init__(message)

class InvalidAccountError(BankError):
    """유효하지 않은 계좌 예외"""
    pass

class TransactionLimitError(BankError):
    """거래 한도 초과 예외"""
    def __init__(self, limit, amount):
        self.limit = limit
        self.amount = amount
        message = f"거래 한도 초과: 한도 {limit:,}원, 요청 {amount:,}원"
        super().__init__(message)

# 은행 계좌 클래스 (Bank account class)
class BankAccount:
    """은행 계좌"""
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self.daily_limit = 1000000  # 일일 한도: 100만원

    def withdraw(self, amount):
        """출금"""
        if amount > self.daily_limit:
            raise TransactionLimitError(self.daily_limit, amount)
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """입금"""
        if amount > self.daily_limit:
            raise TransactionLimitError(self.daily_limit, amount)
        self.balance += amount
        return self.balance

# 사용 예제 (Usage example)
print("💳 은행 계좌 테스트:")
account = BankAccount("123-456-789", 500000)

print(f"초기 잔액: {account.balance:,}원")

# 정상 출금 (Normal withdrawal)
try:
    new_balance = account.withdraw(100000)
    print(f"✓ 100,000원 출금 성공. 잔액: {new_balance:,}원")
except BankError as e:
    print(f"❌ {e}")

# 잔액 부족 (Insufficient funds)
try:
    account.withdraw(500000)
except InsufficientFundsError as e:
    print(f"❌ {e}")

# 거래 한도 초과 (Transaction limit exceeded)
try:
    account.withdraw(2000000)
except TransactionLimitError as e:
    print(f"❌ {e}")

print()

# ===== 4. 여러 예외 처리 (Handling multiple exceptions) =====
print("="*70)
print("4. 여러 예외 처리 (Handling Multiple Exceptions)")
print("="*70)
print()

def process_transaction(account, amount, transaction_type):
    """거래 처리 함수"""
    try:
        if transaction_type == "withdraw":
            new_balance = account.withdraw(amount)
            print(f"✓ 출금 성공: {amount:,}원. 잔액: {new_balance:,}원")
        elif transaction_type == "deposit":
            new_balance = account.deposit(amount)
            print(f"✓ 입금 성공: {amount:,}원. 잔액: {new_balance:,}원")
        else:
            print("❌ 알 수 없는 거래 유형")

    except InsufficientFundsError as e:
        print(f"❌ 잔액 부족: {e}")
    except TransactionLimitError as e:
        print(f"❌ 한도 초과: {e}")
    except BankError as e:
        print(f"❌ 은행 오류: {e}")
    except Exception as e:
        print(f"❌ 예상치 못한 오류: {e}")
    finally:
        print(f"   현재 잔액: {account.balance:,}원")

# 테스트 (Test)
account = BankAccount("123-456-789", 500000)
print("🏦 거래 테스트:")
process_transaction(account, 100000, "withdraw")
print()
process_transaction(account, 600000, "withdraw")
print()
process_transaction(account, 2000000, "deposit")

print()

# ===== 5. 예외 연쇄 (Exception chaining) =====
print("="*70)
print("5. 예외 연쇄 (Exception Chaining)")
print("="*70)
print()

class DataProcessError(Exception):
    """데이터 처리 오류"""
    pass

def load_data(filename):
    """데이터 로드 (시뮬레이션)"""
    raise FileNotFoundError(f"파일을 찾을 수 없습니다: {filename}")

def process_data(filename):
    """데이터 처리"""
    try:
        load_data(filename)
    except FileNotFoundError as e:
        # 원본 예외를 보존하면서 새 예외 발생
        # (Raise new exception while preserving original)
        raise DataProcessError("데이터 처리 중 오류 발생") from e

# 사용 (Usage)
try:
    process_data("data.txt")
except DataProcessError as e:
    print(f"❌ {e}")
    if e.__cause__:
        print(f"   원인: {e.__cause__}")

print()

# ===== 6. 컨텍스트 정보를 가진 예외 (Exception with context) =====
print("="*70)
print("6. 컨텍스트 정보를 가진 예외")
print("="*70)
print()

class APIError(Exception):
    """API 오류"""
    def __init__(self, message, status_code=None, response=None):
        self.message = message
        self.status_code = status_code
        self.response = response
        super().__init__(self.message)

    def __str__(self):
        error_msg = f"API Error: {self.message}"
        if self.status_code:
            error_msg += f" (Status: {self.status_code})"
        return error_msg

def call_api(endpoint):
    """API 호출 시뮬레이션"""
    # 시뮬레이션: 404 오류
    raise APIError(
        "리소스를 찾을 수 없습니다",
        status_code=404,
        response={"error": "Not Found"}
    )

# 사용 (Usage)
try:
    call_api("/users/123")
except APIError as e:
    print(f"❌ {e}")
    print(f"   상태 코드: {e.status_code}")
    print(f"   응답: {e.response}")

print()

# ===== 7. 재시도 메커니즘 (Retry mechanism) =====
print("="*70)
print("7. 재시도 메커니즘 (Retry Mechanism)")
print("="*70)
print()

import random
import time

class NetworkError(Exception):
    """네트워크 오류"""
    pass

def unreliable_operation():
    """불안정한 작업 시뮬레이션"""
    if random.random() < 0.7:  # 70% 실패 확률
        raise NetworkError("네트워크 연결 실패")
    return "성공!"

def retry_operation(max_retries=3, delay=1):
    """재시도 로직"""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"  시도 {attempt}/{max_retries}...")
            result = unreliable_operation()
            print(f"  ✓ {result}")
            return result
        except NetworkError as e:
            print(f"  ❌ {e}")
            if attempt < max_retries:
                print(f"  {delay}초 후 재시도...")
                time.sleep(delay)
            else:
                print(f"  최대 재시도 횟수 초과")
                raise

# 테스트 (Test)
print("🔄 재시도 메커니즘 테스트:")
try:
    retry_operation(max_retries=5, delay=0.5)
except NetworkError:
    print("  최종 실패")

print()

# ===== 8. 예외 로깅 (Exception logging) =====
print("="*70)
print("8. 예외 로깅 (Exception Logging)")
print("="*70)
print()

import traceback
from datetime import datetime

class ErrorLogger:
    """예외 로거"""
    def __init__(self):
        self.errors = []

    def log_error(self, error, context=None):
        """오류 로깅"""
        error_info = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'error_type': type(error).__name__,
            'error_message': str(error),
            'context': context or {},
            'traceback': traceback.format_exc()
        }
        self.errors.append(error_info)

    def print_log(self):
        """로그 출력"""
        print("\n📋 오류 로그:")
        for i, error in enumerate(self.errors, 1):
            print(f"\n[{i}] {error['timestamp']}")
            print(f"  유형: {error['error_type']}")
            print(f"  메시지: {error['error_message']}")
            if error['context']:
                print(f"  컨텍스트: {error['context']}")

# 사용 예제 (Usage example)
logger = ErrorLogger()

def risky_operation(value):
    """위험한 작업"""
    try:
        result = 100 / value
        return result
    except Exception as e:
        logger.log_error(e, context={'value': value, 'operation': 'division'})
        raise

# 테스트 (Test)
print("🔍 예외 로깅 테스트:")
try:
    risky_operation(0)
except:
    pass

try:
    risky_operation(10)
    print("✓ 정상 실행")
except:
    pass

logger.print_log()

print()

# ===== 9. 예외 변환 (Exception translation) =====
print("="*70)
print("9. 예외 변환 (Exception Translation)")
print("="*70)
print()

class UserFriendlyError(Exception):
    """사용자 친화적 오류 메시지"""
    pass

def translate_error(func):
    """예외를 사용자 친화적으로 변환하는 데코레이터"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            raise UserFriendlyError("입력값이 올바르지 않습니다")
        except KeyError:
            raise UserFriendlyError("필요한 정보가 누락되었습니다")
        except Exception as e:
            raise UserFriendlyError(f"처리 중 오류가 발생했습니다: {e}")
    return wrapper

@translate_error
def process_user_input(data):
    """사용자 입력 처리"""
    # 의도적으로 오류 발생
    required_key = data['name']  # KeyError 발생 가능
    age = int(data['age'])  # ValueError 발생 가능
    return f"{required_key}, {age}세"

# 테스트 (Test)
print("🔄 예외 변환 테스트:")

try:
    result = process_user_input({'age': '25'})  # 'name' 누락
except UserFriendlyError as e:
    print(f"❌ {e}")

try:
    result = process_user_input({'name': '김철수', 'age': 'invalid'})  # 잘못된 나이
except UserFriendlyError as e:
    print(f"❌ {e}")

print()

# ===== 10. 예외 억제 (Exception suppression) =====
print("="*70)
print("10. 예외 억제 (Exception Suppression)")
print("="*70)
print()

from contextlib import suppress

# 예외를 무시하고 계속 진행 (Ignore exceptions and continue)
print("📦 파일 삭제 시뮬레이션:")

files_to_delete = ['file1.txt', 'file2.txt', 'file3.txt']

for filename in files_to_delete:
    with suppress(FileNotFoundError):
        # 파일이 없어도 오류 없이 계속 진행
        # (Continue even if file doesn't exist)
        print(f"  {filename} 삭제 시도...")
        raise FileNotFoundError(f"파일 없음: {filename}")

print("  ✓ 모든 작업 완료 (오류 무시)")

print()

print("="*70)
print("사용자 정의 예외 완료!")
print("="*70)
print()
print("💡 예외 처리 모범 사례:")
print("   1. 구체적인 예외를 먼저 처리하고 일반적인 예외는 나중에")
print("   2. 예외 메시지에 충분한 컨텍스트 정보 포함")
print("   3. 예외를 무시하지 말고 적절히 처리하거나 로깅")
print("   4. 사용자 정의 예외로 의미 있는 오류 전달")
print("   5. finally 블록으로 리소스 정리 보장")
print()
print("💡 Exception Handling Best Practices:")
print("   1. Handle specific exceptions first, general ones later")
print("   2. Include sufficient context in exception messages")
print("   3. Don't ignore exceptions - handle or log them properly")
print("   4. Use custom exceptions for meaningful error communication")
print("   5. Use finally blocks to ensure resource cleanup")
