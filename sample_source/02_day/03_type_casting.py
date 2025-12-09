"""
파일명: 03_type_casting.py
설명: 형 변환 (Type Casting) - 자료형 간 변환
Filename: 03_type_casting.py
Description: Type Casting - Converting between data types
"""

# ===== 1. 정수 변환 (Integer Conversion) =====

print("="*60)
print("1. 정수 변환 (Integer Conversion - int())")
print("="*60)

# 문자열 → 정수 (String to Integer)
str_num = "100"
int_num = int(str_num)
print(f"문자열 '{str_num}' → 정수 {int_num}, 타입: {type(int_num)}")

# 실수 → 정수 (소수점 버림) (Float to Integer - floor)
float_num = 3.14
int_from_float = int(float_num)
print(f"실수 {float_num} → 정수 {int_from_float} (소수점 버림)")

float_num2 = 9.99
int_from_float2 = int(float_num2)
print(f"실수 {float_num2} → 정수 {int_from_float2} (소수점 버림)")

# 불린 → 정수 (Boolean to Integer)
bool_true = True
bool_false = False
print(f"불린 {bool_true} → 정수 {int(bool_true)}")  # True = 1
print(f"불린 {bool_false} → 정수 {int(bool_false)}")  # False = 0

# 진법 변환 (Base conversion)
binary_str = "1010"
int_from_binary = int(binary_str, 2)  # 2진수 문자열을 10진수로
print(f"2진수 문자열 '{binary_str}' → 10진수 {int_from_binary}")

hex_str = "FF"
int_from_hex = int(hex_str, 16)  # 16진수 문자열을 10진수로
print(f"16진수 문자열 '{hex_str}' → 10진수 {int_from_hex}")

print()

# ===== 2. 실수 변환 (Float Conversion) =====

print("="*60)
print("2. 실수 변환 (Float Conversion - float())")
print("="*60)

# 문자열 → 실수 (String to Float)
str_float = "3.14"
float_from_str = float(str_float)
print(f"문자열 '{str_float}' → 실수 {float_from_str}, 타입: {type(float_from_str)}")

# 정수 → 실수 (Integer to Float)
int_value = 10
float_from_int = float(int_value)
print(f"정수 {int_value} → 실수 {float_from_int}")

# 불린 → 실수 (Boolean to Float)
print(f"불린 {bool_true} → 실수 {float(bool_true)}")  # True = 1.0
print(f"불린 {bool_false} → 실수 {float(bool_false)}")  # False = 0.0

# 과학적 표기법 문자열 → 실수 (Scientific notation string to Float)
scientific_str = "1.5e3"
float_from_scientific = float(scientific_str)
print(f"과학적 표기법 '{scientific_str}' → 실수 {float_from_scientific}")

# 무한대와 NaN (Infinity and NaN)
positive_inf = float('inf')
negative_inf = float('-inf')
not_a_number = float('nan')
print(f"양의 무한대 (Positive infinity): {positive_inf}")
print(f"음의 무한대 (Negative infinity): {negative_inf}")
print(f"숫자 아님 (Not a Number): {not_a_number}")

print()

# ===== 3. 문자열 변환 (String Conversion) =====

print("="*60)
print("3. 문자열 변환 (String Conversion - str())")
print("="*60)

# 정수 → 문자열 (Integer to String)
number = 100
str_from_int = str(number)
print(f"정수 {number} → 문자열 '{str_from_int}', 타입: {type(str_from_int)}")

# 실수 → 문자열 (Float to String)
pi = 3.14159
str_from_float = str(pi)
print(f"실수 {pi} → 문자열 '{str_from_float}'")

# 불린 → 문자열 (Boolean to String)
str_from_bool = str(True)
print(f"불린 True → 문자열 '{str_from_bool}'")

# 리스트 → 문자열 (List to String)
my_list = [1, 2, 3]
str_from_list = str(my_list)
print(f"리스트 {my_list} → 문자열 '{str_from_list}'")

print()

# ===== 4. 불린 변환 (Boolean Conversion) =====

print("="*60)
print("4. 불린 변환 (Boolean Conversion - bool())")
print("="*60)

# 숫자 → 불린 (Number to Boolean)
print(f"bool(0) = {bool(0)}")  # False
print(f"bool(1) = {bool(1)}")  # True
print(f"bool(-1) = {bool(-1)}")  # True
print(f"bool(100) = {bool(100)}")  # True
print(f"bool(0.0) = {bool(0.0)}")  # False
print(f"bool(3.14) = {bool(3.14)}")  # True

# 문자열 → 불린 (String to Boolean)
print(f"\nbool('') = {bool('')}")  # False (빈 문자열)
print(f"bool('Hello') = {bool('Hello')}")  # True
print(f"bool('False') = {bool('False')}")  # True (문자열이 비어있지 않으므로)
print(f"bool('0') = {bool('0')}")  # True (문자열 '0'은 True)

# 컬렉션 → 불린 (Collection to Boolean)
print(f"\nbool([]) = {bool([])}")  # False (빈 리스트)
print(f"bool([1, 2]) = {bool([1, 2])}")  # True
print(f"bool({{}}) = {bool({})}")  # False (빈 딕셔너리)
print(f"bool({{'key': 'value'}}) = {bool({'key': 'value'})}")  # True

# None → 불린 (None to Boolean)
print(f"\nbool(None) = {bool(None)}")  # False

print()

# ===== 5. 형 변환 시 주의사항 (Type Casting Cautions) =====

print("="*60)
print("5. 형 변환 시 주의사항 (Type Casting Cautions)")
print("="*60)

# ❌ 잘못된 형 변환 예시 (Invalid type casting examples)
print("❌ 오류 발생 예시 (Error cases):")

# 실수 문자열을 직접 정수로 변환 불가 (Cannot convert float string directly to int)
try:
    invalid_int = int("3.14")
except ValueError as e:
    print(f"int('3.14') → ValueError: {e}")

# 올바른 방법: 먼저 float으로 변환 후 int로 변환 (Correct way)
correct_int = int(float("3.14"))
print(f"✅ int(float('3.14')) = {correct_int}")

# 숫자가 아닌 문자열을 숫자로 변환 불가 (Cannot convert non-numeric string)
try:
    invalid_num = int("ABC")
except ValueError as e:
    print(f"int('ABC') → ValueError: {e}")

# 숫자가 아닌 문자열을 float로 변환 불가 (Cannot convert non-numeric string to float)
try:
    invalid_float = float("Hello")
except ValueError as e:
    print(f"float('Hello') → ValueError: {e}")

print()

# ===== 6. 자동 형 변환 (Implicit Type Conversion) =====

print("="*60)
print("6. 자동 형 변환 (Implicit Type Conversion)")
print("="*60)

# 정수 + 실수 → 실수 (Integer + Float → Float)
int_val = 10
float_val = 3.14
result = int_val + float_val
print(f"정수 {int_val} + 실수 {float_val} = {result} (타입: {type(result).__name__})")

# 정수 × 실수 → 실수 (Integer × Float → Float)
result2 = int_val * float_val
print(f"정수 {int_val} × 실수 {float_val} = {result2} (타입: {type(result2).__name__})")

# 불린은 정수로 자동 변환됨 (Boolean is automatically converted to integer)
bool_val = True
result3 = bool_val + 5
print(f"불린 {bool_val} + 정수 5 = {result3} (True는 1로 변환)")

result4 = False + 10
print(f"불린 False + 정수 10 = {result4} (False는 0으로 변환)")

print()

# ===== 7. 실전 예제 (Practical Examples) =====

print("="*60)
print("7. 실전 예제 (Practical Examples)")
print("="*60)

# 예제 1: 사용자 입력 처리 (User input processing)
print("예제 1: 사용자 입력 처리")
# 실제 실행 시 주석 해제 (Uncomment for actual execution)
# user_age = input("나이를 입력하세요: ")
# age_int = int(user_age)  # 문자열을 정수로 변환
# print(f"당신은 {age_int}살입니다.")

# 예제 2: 가격 계산 (Price calculation)
print("\n예제 2: 가격 계산")
price_str = "19.99"
quantity = 3
price_float = float(price_str)  # 문자열을 실수로 변환
total = price_float * quantity
print(f"단가: ${price_str}, 수량: {quantity}")
print(f"총액: ${total:.2f}")

# 예제 3: 데이터 검증 (Data validation)
print("\n예제 3: 데이터 검증")
input_data = "123"
if input_data.isdigit():
    number = int(input_data)
    print(f"'{input_data}'는 유효한 숫자입니다: {number}")
else:
    print(f"'{input_data}'는 유효한 숫자가 아닙니다")

# 예제 4: 퍼센트 계산 (Percentage calculation)
print("\n예제 4: 퍼센트 계산")
score = 85
max_score = 100
percentage = (score / max_score) * 100
percentage_str = f"{percentage:.1f}%"
print(f"점수: {score}/{max_score} = {percentage_str}")

# 예제 5: 안전한 형 변환 (Safe type conversion)
print("\n예제 5: 안전한 형 변환")


def safe_int_convert(value, default=0):
    """
    안전하게 정수로 변환하는 함수
    Safely convert to integer
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


test_values = ["123", "45.67", "abc", None, ""]
for val in test_values:
    result = safe_int_convert(val, default=-1)
    print(f"safe_int_convert({repr(val)}) = {result}")

print()

# ===== 8. 형 변환 정리표 (Type Conversion Summary) =====

print("="*60)
print("8. 형 변환 정리표 (Type Conversion Summary)")
print("="*60)

# 형 변환 예시 표 (Type conversion examples table)
conversions = [
    ("int('100')", int('100')),
    ("int(3.14)", int(3.14)),
    ("int(True)", int(True)),
    ("float('3.14')", float('3.14')),
    ("float(10)", float(10)),
    ("str(100)", str(100)),
    ("str(3.14)", str(3.14)),
    ("bool(1)", bool(1)),
    ("bool(0)", bool(0)),
    ("bool('')", bool('')),
]

print(f"{'변환 (Conversion)':<20} {'결과 (Result)':<15} {'타입 (Type)':<15}")
print("-" * 50)
for expr, result in conversions:
    print(f"{expr:<20} {str(result):<15} {type(result).__name__:<15}")

print()
print("="*60)
print("형 변환 학습 완료! (Type casting learning completed!)")
print("="*60)
