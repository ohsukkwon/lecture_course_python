"""
파일명: 01_variables.py
설명: 변수의 선언, 할당, 명명 규칙
Filename: 01_variables.py
Description: Variable declaration, assignment, and naming conventions
"""

# ===== 1. 기본 변수 선언 및 할당 (Basic Variable Declaration and Assignment) =====

# 단일 변수 선언 (Single variable declaration)
name = "김철수"  # 문자열 (String)
age = 25  # 정수 (Integer)
height = 175.5  # 실수 (Float)
is_student = True  # 불린 (Boolean)

print("=== 기본 변수 (Basic Variables) ===")
print(f"이름 (Name): {name}")
print(f"나이 (Age): {age}")
print(f"키 (Height): {height}cm")
print(f"학생 여부 (Is Student): {is_student}")
print()

# ===== 2. 여러 변수 동시 할당 (Multiple Variable Assignment) =====

# 방법 1: 각각 다른 값 할당 (Assign different values)
x, y, z = 10, 20, 30
print("=== 여러 변수 동시 할당 (Multiple Assignment) ===")
print(f"x = {x}, y = {y}, z = {z}")

# 방법 2: 같은 값 할당 (Assign same value)
a = b = c = 100
print(f"a = {a}, b = {b}, c = {c}")
print()

# ===== 3. 변수 타입 확인 (Check Variable Type) =====

print("=== 변수 타입 확인 (Type Checking) ===")
print(f"type(name) = {type(name)}")  # <class 'str'>
print(f"type(age) = {type(age)}")  # <class 'int'>
print(f"type(height) = {type(height)}")  # <class 'float'>
print(f"type(is_student) = {type(is_student)}")  # <class 'bool'>
print()

# ===== 4. 변수값 변경 (Change Variable Value) =====

print("=== 변수값 변경 (Value Change) ===")
score = 80
print(f"초기 점수 (Initial score): {score}")

score = 90  # 값 변경 (Change value)
print(f"변경된 점수 (Changed score): {score}")

score = score + 10  # 기존 값에서 연산 (Operation on existing value)
print(f"10점 추가 (Added 10 points): {score}")
print()

# ===== 5. 변수 교환 (Variable Swapping) =====

print("=== 변수 교환 (Variable Swapping) ===")
num1 = 10
num2 = 20
print(f"교환 전 (Before swap): num1 = {num1}, num2 = {num2}")

# Python의 간편한 교환 방법 (Python's easy swap method)
num1, num2 = num2, num1
print(f"교환 후 (After swap): num1 = {num1}, num2 = {num2}")
print()

# ===== 6. 변수명 작성 규칙 (Variable Naming Rules) =====

print("=== 변수명 작성 규칙 (Naming Rules) ===")

# ✅ 올바른 변수명 (Valid variable names)
user_name = "홍길동"  # snake_case (Python 권장)
userName = "이영희"  # camelCase (가능하지만 비권장)
_private_var = "비공개"  # 언더스코어로 시작 가능
name2 = "김영수"  # 숫자 포함 가능 (단, 시작은 불가)

print("올바른 변수명 예시 (Valid examples):")
print(f"user_name = {user_name}")
print(f"userName = {userName}")
print(f"_private_var = {_private_var}")
print(f"name2 = {name2}")
print()

# ❌ 잘못된 변수명 (Invalid variable names) - 주석 처리됨
# 2name = "오류"  # SyntaxError: 숫자로 시작 불가
# user-name = "오류"  # SyntaxError: 하이픈 사용 불가
# user name = "오류"  # SyntaxError: 공백 사용 불가
# for = "오류"  # SyntaxError: 예약어 사용 불가

# ===== 7. 예약어 확인 (Check Keywords) =====

print("=== 파이썬 예약어 (Python Keywords) ===")
import keyword

print(f"예약어 개수 (Number of keywords): {len(keyword.kwlist)}")
print("예약어 목록 (Keyword list):")
print(keyword.kwlist)
print()

# ===== 8. 변수명 스타일 (Variable Naming Styles) =====

print("=== 변수명 스타일 가이드 (Naming Style Guide) ===")

# 일반 변수 (Regular variables) - snake_case
user_age = 30
total_price = 50000
max_retry_count = 5

# 상수 (Constants) - UPPER_CASE
MAX_SIZE = 100
PI = 3.14159
DEFAULT_COLOR = "blue"

# 클래스명 (Class names) - PascalCase
class UserProfile:  # 클래스명은 PascalCase
    pass

class ShoppingCart:
    pass

print("일반 변수 (Regular variables): user_age, total_price")
print("상수 (Constants): MAX_SIZE, PI, DEFAULT_COLOR")
print("클래스 (Classes): UserProfile, ShoppingCart")
print()

# ===== 9. 의미 있는 변수명 사용 (Use Meaningful Names) =====

print("=== 의미 있는 변수명 사용 (Meaningful Names) ===")

# ❌ 나쁜 예 (Bad examples)
x = 25  # 무엇을 의미하는지 불명확 (Unclear meaning)
n = "John"  # 무엇을 의미하는지 불명확
t = 100000  # 무엇을 의미하는지 불명확

# ✅ 좋은 예 (Good examples)
student_age = 25  # 학생의 나이임을 명확히 알 수 있음 (Clearly student's age)
customer_name = "John"  # 고객 이름임을 명확히 알 수 있음 (Clearly customer's name)
total_amount = 100000  # 총액임을 명확히 알 수 있음 (Clearly total amount)

print(f"학생 나이 (Student age): {student_age}")
print(f"고객 이름 (Customer name): {customer_name}")
print(f"총액 (Total amount): {total_amount:,}원")
print()

# ===== 10. 변수 삭제 (Delete Variables) =====

print("=== 변수 삭제 (Delete Variables) ===")
temp_var = "임시 변수"
print(f"삭제 전 (Before deletion): temp_var = {temp_var}")

del temp_var  # 변수 삭제 (Delete variable)
print("변수 삭제 완료 (Variable deleted)")

# print(temp_var)  # NameError: name 'temp_var' is not defined
print()

# ===== 11. 전역 변수와 지역 변수 (Global and Local Variables) =====

print("=== 전역 변수와 지역 변수 (Global and Local Variables) ===")

global_var = "전역 변수 (Global)"  # 전역 변수 (Global variable)


def test_function():
    """함수 내부의 지역 변수 (Local variable inside function)"""
    local_var = "지역 변수 (Local)"  # 지역 변수 (Local variable)
    print(f"함수 내부 - global_var: {global_var}")
    print(f"함수 내부 - local_var: {local_var}")


test_function()
print(f"함수 외부 - global_var: {global_var}")
# print(local_var)  # NameError: local_var는 함수 외부에서 접근 불가

print()
print("="*60)
print("변수 학습 완료! (Variables learning completed!)")
print("="*60)
