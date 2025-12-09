"""
파일명: 02_custom_module_example.py
설명: 사용자 정의 모듈 생성 및 사용 예제
Filename: 02_custom_module_example.py
Description: Custom module creation and usage example
"""

print("="*70)
print("사용자 정의 모듈 예제 (Custom Module Example)")
print("="*70)
print()

# ===== 1. 수학 유틸리티 모듈 시뮬레이션 (Math utility module simulation) =====
print("="*70)
print("1. 수학 유틸리티 모듈 (Math Utility Module)")
print("="*70)
print()

# 실제로는 별도의 math_utils.py 파일로 만듭니다
# (In practice, create a separate math_utils.py file)
print("📄 math_utils.py 내용:")
print("-"*70)
print("""
def factorial(n):
    '''팩토리얼을 계산합니다'''
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    '''소수인지 판별합니다'''
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    '''n번째 피보나치 수를 반환합니다'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# 모듈 레벨 변수 (Module-level variable)
PI = 3.14159265359
E = 2.71828182846
""")
print("-"*70)
print()

# 함수 정의 (실제 구현) - Function definitions (actual implementation)
def factorial(n):
    """팩토리얼을 계산합니다 (Calculate factorial)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def is_prime(n):
    """소수인지 판별합니다 (Check if prime)"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """n번째 피보나치 수를 반환합니다 (Return nth Fibonacci number)"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

PI = 3.14159265359
E = 2.71828182846

# 사용 예제 (Usage example)
print("💻 사용 예제:")
print(f"5! = {factorial(5)}")
print(f"17은 소수인가? {is_prime(17)}")
print(f"10번째 피보나치 수: {fibonacci(10)}")
print(f"원주율 PI: {PI}")
print()

# ===== 2. 문자열 유틸리티 모듈 (String utility module) =====
print("="*70)
print("2. 문자열 유틸리티 모듈 (String Utility Module)")
print("="*70)
print()

print("📄 string_utils.py 내용:")
print("-"*70)
print("""
def reverse_string(s):
    '''문자열을 뒤집습니다'''
    return s[::-1]

def is_palindrome(s):
    '''회문인지 확인합니다'''
    s = s.lower().replace(' ', '')
    return s == s[::-1]

def count_words(text):
    '''단어 수를 셉니다'''
    return len(text.split())

def capitalize_words(text):
    '''각 단어의 첫 글자를 대문자로 만듭니다'''
    return ' '.join(word.capitalize() for word in text.split())
""")
print("-"*70)
print()

# 함수 정의 (Function definitions)
def reverse_string(s):
    """문자열을 뒤집습니다 (Reverse string)"""
    return s[::-1]

def is_palindrome(s):
    """회문인지 확인합니다 (Check if palindrome)"""
    s = s.lower().replace(' ', '')
    return s == s[::-1]

def count_words(text):
    """단어 수를 셉니다 (Count words)"""
    return len(text.split())

def capitalize_words(text):
    """각 단어의 첫 글자를 대문자로 만듭니다 (Capitalize each word)"""
    return ' '.join(word.capitalize() for word in text.split())

# 사용 예제 (Usage example)
print("💻 사용 예제:")
print(f"reverse_string('hello'): {reverse_string('hello')}")
print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")
print(f"is_palindrome('hello'): {is_palindrome('hello')}")
print(f"count_words('Hello Python World'): {count_words('Hello Python World')}")
print(f"capitalize_words('hello world'): {capitalize_words('hello world')}")
print()

# ===== 3. 날짜/시간 유틸리티 모듈 (Date/Time utility module) =====
print("="*70)
print("3. 날짜/시간 유틸리티 모듈 (Date/Time Utility Module)")
print("="*70)
print()

from datetime import datetime, timedelta

print("📄 datetime_utils.py 내용:")
print("-"*70)
print("""
from datetime import datetime, timedelta

def get_current_time():
    '''현재 시간을 반환합니다'''
    return datetime.now()

def format_datetime(dt, fmt='%Y-%m-%d %H:%M:%S'):
    '''날짜/시간을 원하는 형식으로 포맷합니다'''
    return dt.strftime(fmt)

def days_until(target_date):
    '''특정 날짜까지 남은 일수를 계산합니다'''
    now = datetime.now()
    diff = target_date - now
    return diff.days

def add_days(date, days):
    '''날짜에 일수를 더합니다'''
    return date + timedelta(days=days)
""")
print("-"*70)
print()

# 함수 정의 (Function definitions)
def get_current_time():
    """현재 시간을 반환합니다 (Get current time)"""
    return datetime.now()

def format_datetime(dt, fmt='%Y-%m-%d %H:%M:%S'):
    """날짜/시간을 원하는 형식으로 포맷합니다 (Format datetime)"""
    return dt.strftime(fmt)

def days_until(target_date):
    """특정 날짜까지 남은 일수를 계산합니다 (Calculate days until target)"""
    now = datetime.now()
    diff = target_date - now
    return diff.days

def add_days(date, days):
    """날짜에 일수를 더합니다 (Add days to date)"""
    return date + timedelta(days=days)

# 사용 예제 (Usage example)
print("💻 사용 예제:")
now = get_current_time()
print(f"현재 시간: {format_datetime(now)}")
print(f"날짜만: {format_datetime(now, '%Y-%m-%d')}")
print(f"시간만: {format_datetime(now, '%H:%M:%S')}")

future = add_days(now, 7)
print(f"7일 후: {format_datetime(future, '%Y-%m-%d')}")

new_year = datetime(2026, 1, 1)
print(f"2026년까지 남은 일수: {days_until(new_year)}일")
print()

# ===== 4. 검증(Validation) 유틸리티 모듈 (Validation utility module) =====
print("="*70)
print("4. 검증 유틸리티 모듈 (Validation Utility Module)")
print("="*70)
print()

import re

print("📄 validators.py 내용:")
print("-"*70)
print("""
import re

def is_valid_email(email):
    '''이메일 형식이 유효한지 확인합니다'''
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    '''전화번호 형식이 유효한지 확인합니다 (한국)'''
    pattern = r'^01[0-9]-\\d{3,4}-\\d{4}$'
    return bool(re.match(pattern, phone))

def is_strong_password(password):
    '''강력한 비밀번호인지 확인합니다'''
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

def is_valid_url(url):
    '''URL 형식이 유효한지 확인합니다'''
    pattern = r'^https?://[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'
    return bool(re.match(pattern, url))
""")
print("-"*70)
print()

# 함수 정의 (Function definitions)
def is_valid_email(email):
    """이메일 형식이 유효한지 확인합니다 (Check if valid email)"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    """전화번호 형식이 유효한지 확인합니다 (Check if valid phone - Korean)"""
    pattern = r'^01[0-9]-\d{3,4}-\d{4}$'
    return bool(re.match(pattern, phone))

def is_strong_password(password):
    """강력한 비밀번호인지 확인합니다 (Check if strong password)"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

def is_valid_url(url):
    """URL 형식이 유효한지 확인합니다 (Check if valid URL)"""
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return bool(re.match(pattern, url))

# 사용 예제 (Usage example)
print("💻 사용 예제:")
print(f"is_valid_email('test@example.com'): {is_valid_email('test@example.com')}")
print(f"is_valid_email('invalid-email'): {is_valid_email('invalid-email')}")
print(f"is_valid_phone('010-1234-5678'): {is_valid_phone('010-1234-5678')}")
print(f"is_valid_phone('1234567890'): {is_valid_phone('1234567890')}")
print(f"is_strong_password('Abc12345'): {is_strong_password('Abc12345')}")
print(f"is_strong_password('weak'): {is_strong_password('weak')}")
print(f"is_valid_url('https://example.com'): {is_valid_url('https://example.com')}")
print()

# ===== 5. 파일 유틸리티 모듈 (File utility module) =====
print("="*70)
print("5. 파일 유틸리티 모듈 (File Utility Module)")
print("="*70)
print()

import os

print("📄 file_utils.py 내용:")
print("-"*70)
print("""
import os

def get_file_extension(filename):
    '''파일 확장자를 반환합니다'''
    return os.path.splitext(filename)[1]

def get_file_size(filepath):
    '''파일 크기를 반환합니다 (바이트)'''
    return os.path.getsize(filepath) if os.path.exists(filepath) else 0

def format_file_size(size_bytes):
    '''파일 크기를 읽기 쉬운 형식으로 변환합니다'''
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

def list_files_by_extension(directory, extension):
    '''특정 확장자를 가진 파일 목록을 반환합니다'''
    return [f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
            and f.endswith(extension)]
""")
print("-"*70)
print()

# 함수 정의 (Function definitions)
def get_file_extension(filename):
    """파일 확장자를 반환합니다 (Get file extension)"""
    return os.path.splitext(filename)[1]

def format_file_size(size_bytes):
    """파일 크기를 읽기 쉬운 형식으로 변환합니다 (Format file size)"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"

# 사용 예제 (Usage example)
print("💻 사용 예제:")
print(f"get_file_extension('document.pdf'): {get_file_extension('document.pdf')}")
print(f"get_file_extension('image.jpg'): {get_file_extension('image.jpg')}")
print(f"format_file_size(1024): {format_file_size(1024)}")
print(f"format_file_size(1048576): {format_file_size(1048576)}")
print(f"format_file_size(1073741824): {format_file_size(1073741824)}")
print()

# ===== 6. 모듈 import 방법 정리 (Module import methods summary) =====
print("="*70)
print("6. 모듈 import 방법 정리 (Module Import Methods)")
print("="*70)
print()

print("방법 1: 전체 모듈 import (Import entire module)")
print("  import math_utils")
print("  result = math_utils.factorial(5)")
print()

print("방법 2: 특정 함수만 import (Import specific functions)")
print("  from math_utils import factorial, is_prime")
print("  result = factorial(5)")
print()

print("방법 3: 별칭(alias) 사용 (Use alias)")
print("  import math_utils as mu")
print("  result = mu.factorial(5)")
print()

print("방법 4: 모든 것 import (Import everything - 권장하지 않음)")
print("  from math_utils import *")
print("  result = factorial(5)")
print("  ⚠️ 주의: 이름 충돌 가능성이 있어 권장하지 않습니다")
print()

# ===== 7. __name__ == "__main__" 패턴 (Module main pattern) =====
print("="*70)
print("7. 모듈 메인 패턴 (__name__ == '__main__')")
print("="*70)
print()

print("📄 모듈에서 사용하는 일반적인 패턴:")
print("-"*70)
print("""
# my_module.py

def my_function():
    return "Hello from function"

def main():
    '''모듈이 직접 실행될 때만 실행됩니다'''
    print("모듈이 직접 실행되었습니다")
    print(my_function())

if __name__ == "__main__":
    main()
""")
print("-"*70)
print()

print("💡 설명:")
print("  - 모듈이 import될 때: main()은 실행되지 않음")
print("  - 모듈이 직접 실행될 때: main()이 실행됨")
print("  - 이 패턴으로 테스트 코드를 모듈 안에 포함시킬 수 있습니다")
print()

# ===== 8. 실전 예제 - 종합 활용 (Comprehensive practical example) =====
print("="*70)
print("8. 실전 예제 - 유틸리티 함수 종합 활용")
print("="*70)
print()

def process_user_data(name, email, phone, password):
    """
    사용자 데이터를 검증하고 처리합니다
    (Validate and process user data)
    """
    print(f"\n👤 사용자 등록 처리: {name}")
    print("-" * 50)

    # 이메일 검증 (Validate email)
    if is_valid_email(email):
        print(f"✓ 이메일: {email} (유효)")
    else:
        print(f"✗ 이메일: {email} (유효하지 않음)")

    # 전화번호 검증 (Validate phone)
    if is_valid_phone(phone):
        print(f"✓ 전화번호: {phone} (유효)")
    else:
        print(f"✗ 전화번호: {phone} (유효하지 않음)")

    # 비밀번호 검증 (Validate password)
    if is_strong_password(password):
        print(f"✓ 비밀번호: {'*' * len(password)} (강력함)")
    else:
        print(f"✗ 비밀번호: {'*' * len(password)} (약함)")

    # 이름 처리 (Process name)
    formatted_name = capitalize_words(name)
    print(f"✓ 이름 포맷: {formatted_name}")

    # 등록 시간 (Registration time)
    now = get_current_time()
    print(f"✓ 등록 시간: {format_datetime(now)}")

# 테스트 (Test)
process_user_data(
    "kim chul soo",
    "kim@example.com",
    "010-1234-5678",
    "MyPass123"
)

process_user_data(
    "lee young hee",
    "invalid-email",
    "1234567890",
    "weak"
)

print()
print("="*70)
print("사용자 정의 모듈 예제 완료!")
print("="*70)
print()
print("💡 모듈 작성 팁:")
print("   1. 관련된 함수들을 하나의 모듈로 그룹화하세요")
print("   2. 명확한 함수명과 docstring을 작성하세요")
print("   3. __name__ == '__main__' 패턴을 사용하여 테스트 코드를 포함하세요")
print("   4. 모듈은 재사용 가능하고 독립적이어야 합니다")
print()
print("💡 Module Writing Tips:")
print("   1. Group related functions into one module")
print("   2. Write clear function names and docstrings")
print("   3. Use __name__ == '__main__' pattern for test code")
print("   4. Modules should be reusable and independent")
