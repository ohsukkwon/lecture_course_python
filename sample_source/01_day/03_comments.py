"""
파일명: 03_comments.py
설명: 주석 작성 방법 - 코드 설명 및 문서화
Filename: 03_comments.py
Description: How to write comments - Code explanation and documentation
"""

# ===== 1. 한 줄 주석 (Single-line Comments) =====

# 이것은 한 줄 주석입니다 (This is a single-line comment)
print("Hello, World!")

# 주석은 코드 실행에 영향을 주지 않습니다 (Comments don't affect code execution)
# print("이 줄은 실행되지 않습니다")  # 주석 처리된 코드 (Commented out code)

# 코드 옆에도 주석을 달 수 있습니다 (You can add comments next to code)
x = 10  # 변수 x에 10을 할당 (Assign 10 to variable x)


# ===== 2. 여러 줄 주석 (Multi-line Comments) =====

"""
이것은 여러 줄 주석입니다.
작은따옴표 3개 또는 큰따옴표 3개를 사용합니다.

This is a multi-line comment.
Use three single quotes or three double quotes.

주요 용도 (Main uses):
1. 함수나 클래스의 docstring (Function or class docstring)
2. 긴 설명이 필요한 경우 (When long explanation is needed)
3. 임시로 여러 줄 코드를 비활성화할 때 (To temporarily disable multiple lines of code)
"""

'''
작은따옴표 3개로도 가능합니다.
Single quotes also work.
'''

# ===== 3. 주석 사용 예시 (Comment Usage Examples) =====

# 좋은 주석 예시 (Good comment examples)

# 섭씨를 화씨로 변환하는 함수 (Function to convert Celsius to Fahrenheit)
def celsius_to_fahrenheit(celsius):
    """
    섭씨 온도를 화씨 온도로 변환합니다.
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): 섭씨 온도 (Celsius temperature)

    Returns:
        float: 화씨 온도 (Fahrenheit temperature)
    """
    return (celsius * 9/5) + 32


# 나쁜 주석 예시 (Bad comment examples)

# x에 10을 할당 (Don't write obvious comments)
x = 10  # 이런 주석은 불필요합니다 (This comment is unnecessary)

# y를 증가 (Increase y)
y = 20  # 코드만 봐도 알 수 있는 내용 (Information obvious from code)


# ===== 4. 주석 작성 가이드라인 (Comment Guidelines) =====

# 1) 왜(Why)를 설명하세요, 무엇(What)이 아니라 (Explain WHY, not WHAT)

# 좋은 예 (Good example):
# 사용자 입력 검증을 위해 정규표현식 사용 (Use regex for input validation)
import re
pattern = r'^[a-zA-Z0-9]+$'

# 나쁜 예 (Bad example):
# 정규표현식 패턴 선언 (Declare regex pattern) - 코드만 봐도 명확함
# pattern = r'^[a-zA-Z0-9]+$'


# 2) 복잡한 로직에는 주석을 추가하세요 (Add comments to complex logic)

# 피보나치 수열의 n번째 항 계산 (Calculate nth term of Fibonacci sequence)
# 시간 복잡도 O(2^n)이므로 큰 n에 대해서는 비효율적 (Time complexity O(2^n), inefficient for large n)
def fibonacci(n):
    if n <= 1:
        return n
    # 재귀적으로 이전 두 항의 합 계산 (Recursively calculate sum of previous two terms)
    return fibonacci(n-1) + fibonacci(n-2)


# 3) TODO, FIXME, NOTE 등의 태그 사용 (Use tags like TODO, FIXME, NOTE)

# TODO: 에러 처리 추가 필요 (Need to add error handling)
def divide(a, b):
    return a / b

# FIXME: 0으로 나누기 오류 발생 가능 (Possible division by zero error)
result = divide(10, 0)

# NOTE: 이 함수는 Python 3.6 이상에서만 동작 (This function works only in Python 3.6+)
def format_string(name, age):
    return f"Name: {name}, Age: {age}"


# ===== 5. 임시로 코드 비활성화 (Temporarily Disable Code) =====

print("이 코드는 실행됩니다 (This code will run)")

# 디버깅 중 임시로 비활성화 (Temporarily disabled during debugging)
# print("이 코드는 실행되지 않습니다 (This code won't run)")
# x = 100
# y = 200

"""
여러 줄을 한 번에 비활성화할 수 있습니다.
Multiple lines can be disabled at once.

print("Line 1")
print("Line 2")
print("Line 3")
"""

print("이 코드는 다시 실행됩니다 (This code will run again)")


# ===== 6. Docstring 예시 (Docstring Examples) =====

def add(a, b):
    """
    두 숫자를 더합니다.
    Add two numbers.

    Parameters:
        a (int or float): 첫 번째 숫자 (First number)
        b (int or float): 두 번째 숫자 (Second number)

    Returns:
        int or float: 두 숫자의 합 (Sum of two numbers)

    Examples:
        >>> add(3, 5)
        8
        >>> add(2.5, 3.5)
        6.0
    """
    return a + b


class Calculator:
    """
    간단한 계산기 클래스
    Simple calculator class

    이 클래스는 기본적인 산술 연산을 제공합니다.
    This class provides basic arithmetic operations.

    Attributes:
        result (float): 마지막 계산 결과 (Last calculation result)
    """

    def __init__(self):
        """계산기 초기화 (Initialize calculator)"""
        self.result = 0

    def add(self, x, y):
        """덧셈 (Addition)"""
        self.result = x + y
        return self.result


# ===== 7. 주석 활용 팁 (Comment Tips) =====

# Tip 1: 주석은 코드를 이해하기 쉽게 만들지만, 과도한 주석은 오히려 방해가 됩니다
#        (Comments make code easier to understand, but excessive comments are counterproductive)

# Tip 2: 코드를 수정할 때는 관련 주석도 함께 업데이트하세요
#        (Update related comments when modifying code)

# Tip 3: 명확한 변수명과 함수명을 사용하면 주석이 덜 필요합니다
#        (Clear variable and function names reduce the need for comments)

# 좋은 예 (Good example):
user_age = 25  # 명확한 변수명 (Clear variable name)

# 나쁜 예 (Bad example):
# 사용자 나이 (User age) - 변수명만 봐도 알 수 있음
# ua = 25  # 모호한 변수명에 주석이 필요 (Unclear variable name needs comment)


print("\n주석 예제 실행 완료! (Comment examples completed!)")
