"""
파일명: 02_data_types.py
설명: 파이썬 기본 자료형 (숫자, 문자열, 불린, None)
Filename: 02_data_types.py
Description: Python basic data types (Numbers, Strings, Boolean, None)
"""

# ===== 1. 정수형 (Integer) =====

print("="*60)
print("1. 정수형 (Integer)")
print("="*60)

# 기본 정수 (Basic integers)
positive_num = 100
negative_num = -50
zero = 0

print(f"양수 (Positive): {positive_num}")
print(f"음수 (Negative): {negative_num}")
print(f"영 (Zero): {zero}")
print(f"타입 (Type): {type(positive_num)}")

# 매우 큰 정수 (Very large integers)
big_number = 123456789012345678901234567890
print(f"큰 수 (Big number): {big_number}")

# 다양한 진법 (Different number bases)
binary = 0b1010  # 2진수 (Binary) = 10
octal = 0o12  # 8진수 (Octal) = 10
decimal = 10  # 10진수 (Decimal) = 10
hexadecimal = 0xA  # 16진수 (Hexadecimal) = 10

print(f"\n진법 변환 (Base Conversion):")
print(f"2진수 (Binary) 0b1010 = {binary}")
print(f"8진수 (Octal) 0o12 = {octal}")
print(f"10진수 (Decimal) 10 = {decimal}")
print(f"16진수 (Hexadecimal) 0xA = {hexadecimal}")

# 진법 변환 함수 (Base conversion functions)
num = 255
print(f"\n{num}의 진법 변환:")
print(f"2진수 (Binary): {bin(num)}")  # 0b11111111
print(f"8진수 (Octal): {oct(num)}")  # 0o377
print(f"16진수 (Hexadecimal): {hex(num)}")  # 0xff

print()

# ===== 2. 실수형 (Float) =====

print("="*60)
print("2. 실수형 (Float)")
print("="*60)

# 기본 실수 (Basic floats)
pi = 3.14159
temperature = -15.5
percentage = 0.95

print(f"원주율 (Pi): {pi}")
print(f"온도 (Temperature): {temperature}°C")
print(f"비율 (Percentage): {percentage}")
print(f"타입 (Type): {type(pi)}")

# 과학적 표기법 (Scientific notation)
scientific1 = 3.14e2  # 3.14 × 10² = 314.0
scientific2 = 3.14e-2  # 3.14 × 10⁻² = 0.0314

print(f"\n과학적 표기법 (Scientific notation):")
print(f"3.14e2 = {scientific1}")
print(f"3.14e-2 = {scientific2}")

# 부동소수점 정밀도 문제 (Floating point precision issue)
print(f"\n부동소수점 문제 (Floating point issue):")
print(f"0.1 + 0.2 = {0.1 + 0.2}")  # 0.30000000000000004
print(f"0.1 + 0.2 == 0.3 → {0.1 + 0.2 == 0.3}")  # False

# 해결 방법 (Solution)
from decimal import Decimal
result = Decimal('0.1') + Decimal('0.2')
print(f"Decimal('0.1') + Decimal('0.2') = {result}")  # 0.3

# round() 함수 사용 (Using round() function)
print(f"round(0.1 + 0.2, 1) = {round(0.1 + 0.2, 1)}")  # 0.3

print()

# ===== 3. 복소수 (Complex) =====

print("="*60)
print("3. 복소수 (Complex)")
print("="*60)

# 복소수 생성 (Create complex numbers)
complex1 = 3 + 4j
complex2 = complex(3, 4)  # 동일한 결과 (Same result)

print(f"복소수 (Complex number): {complex1}")
print(f"타입 (Type): {type(complex1)}")

# 실수부와 허수부 (Real and imaginary parts)
print(f"실수부 (Real part): {complex1.real}")
print(f"허수부 (Imaginary part): {complex1.imag}")

# 복소수 연산 (Complex number operations)
complex3 = (1 + 2j) + (3 + 4j)
print(f"\n복소수 덧셈 (Addition): (1+2j) + (3+4j) = {complex3}")

# 절댓값 (Absolute value - Magnitude)
magnitude = abs(3 + 4j)
print(f"절댓값 (Magnitude): |3+4j| = {magnitude}")

# 켤레 복소수 (Complex conjugate)
conjugate = complex1.conjugate()
print(f"켤레 복소수 (Conjugate): {conjugate}")

print()

# ===== 4. 문자열 (String) =====

print("="*60)
print("4. 문자열 (String)")
print("="*60)

# 문자열 생성 (Create strings)
str1 = "Hello"
str2 = 'World'
str3 = """여러 줄
문자열
입니다"""
str4 = '''작은따옴표로도
여러 줄
가능합니다'''

print(f"문자열 1 (String 1): {str1}")
print(f"문자열 2 (String 2): {str2}")
print(f"타입 (Type): {type(str1)}")

# 문자열 연산 (String operations)
print(f"\n문자열 연결 (Concatenation): {str1} + ' ' + {str2} = '{str1 + ' ' + str2}'")
print(f"문자열 반복 (Repetition): 'Ha' * 3 = '{'Ha' * 3}'")

# 문자열 인덱싱 (String indexing)
text = "Python"
print(f"\n문자열 인덱싱 (Indexing): text = '{text}'")
print(f"text[0] = '{text[0]}'  (첫 번째 문자)")
print(f"text[-1] = '{text[-1]}'  (마지막 문자)")
print(f"text[2] = '{text[2]}'  (세 번째 문자)")

# 문자열 슬라이싱 (String slicing)
print(f"\n문자열 슬라이싱 (Slicing):")
print(f"text[0:3] = '{text[0:3]}'  (0부터 2까지)")
print(f"text[2:] = '{text[2:]}'  (2부터 끝까지)")
print(f"text[:4] = '{text[:4]}'  (처음부터 3까지)")
print(f"text[::2] = '{text[::2]}'  (2칸씩 건너뛰기)")
print(f"text[::-1] = '{text[::-1]}'  (역순)")

# 문자열 길이 (String length)
print(f"\n문자열 길이 (Length): len('{text}') = {len(text)}")

# 이스케이프 문자 (Escape characters)
print(f"\n이스케이프 문자 (Escape characters):")
print("줄바꿈 (Newline): 첫 줄\\n두 번째 줄")
print("첫 줄\n두 번째 줄")
print("탭 (Tab): 이름\\t나이")
print("이름\t나이")

print()

# ===== 5. 불린 (Boolean) =====

print("="*60)
print("5. 불린 (Boolean)")
print("="*60)

# 불린 값 (Boolean values)
is_active = True
is_deleted = False

print(f"활성화 (Active): {is_active}")
print(f"삭제됨 (Deleted): {is_deleted}")
print(f"타입 (Type): {type(is_active)}")

# 비교 연산의 결과 (Comparison results)
print(f"\n비교 연산 (Comparison):")
print(f"10 > 5 = {10 > 5}")
print(f"10 < 5 = {10 < 5}")
print(f"10 == 10 = {10 == 10}")

# 논리 연산 (Logical operations)
print(f"\n논리 연산 (Logical operations):")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# 불린 변환 (Boolean conversion)
print(f"\n불린 변환 (Boolean conversion):")
print(f"bool(1) = {bool(1)}")  # True
print(f"bool(0) = {bool(0)}")  # False
print(f"bool('Hello') = {bool('Hello')}")  # True
print(f"bool('') = {bool('')}")  # False (빈 문자열)
print(f"bool([1, 2]) = {bool([1, 2])}")  # True
print(f"bool([]) = {bool([])}")  # False (빈 리스트)

# False로 간주되는 값들 (Falsy values)
print(f"\nFalse로 간주되는 값들 (Falsy values):")
falsy_values = [None, False, 0, 0.0, '', [], {}, ()]
for value in falsy_values:
    print(f"bool({repr(value)}) = {bool(value)}")

print()

# ===== 6. None 타입 (None Type) =====

print("="*60)
print("6. None 타입 (None Type)")
print("="*60)

# None은 "값이 없음"을 나타냄 (None represents "no value")
empty_value = None
print(f"값 (Value): {empty_value}")
print(f"타입 (Type): {type(empty_value)}")

# None 체크 (Check for None)
print(f"\nNone 체크 (None check):")
print(f"empty_value is None → {empty_value is None}")
print(f"empty_value == None → {empty_value == None}")

# None과 False의 차이 (Difference between None and False)
print(f"\nNone과 False의 차이 (Difference):")
print(f"None == False → {None == False}")  # False
print(f"None is False → {None is False}")  # False
print(f"bool(None) → {bool(None)}")  # False (but None is not False)

# 함수에서 아무것도 반환하지 않으면 None 반환 (Function returns None if no return)
def no_return():
    pass


result = no_return()
print(f"\n반환값이 없는 함수 (Function with no return): {result}")

print()

# ===== 7. 자료형 확인 및 변환 (Type Checking and Conversion) =====

print("="*60)
print("7. 자료형 확인 및 변환 (Type Checking and Conversion)")
print("="*60)

# isinstance() 함수로 타입 확인 (Check type with isinstance())
value = 100
print(f"isinstance({value}, int) = {isinstance(value, int)}")
print(f"isinstance({value}, float) = {isinstance(value, float)}")
print(f"isinstance({value}, str) = {isinstance(value, str)}")

# 여러 타입 중 하나인지 확인 (Check if one of multiple types)
print(f"isinstance({value}, (int, float)) = {isinstance(value, (int, float))}")

print()
print("="*60)
print("자료형 학습 완료! (Data types learning completed!)")
print("="*60)
