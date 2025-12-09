"""
파일명: 04_operators.py
설명: 파이썬 연산자 (산술, 비교, 논리, 할당, 멤버십, 식별, 비트)
Filename: 04_operators.py
Description: Python operators (Arithmetic, Comparison, Logical, Assignment, Membership, Identity, Bitwise)
"""

# ===== 1. 산술 연산자 (Arithmetic Operators) =====

print("="*60)
print("1. 산술 연산자 (Arithmetic Operators)")
print("="*60)

a = 10
b = 3

print(f"a = {a}, b = {b}\n")

# 기본 산술 연산 (Basic arithmetic operations)
print(f"덧셈 (Addition): a + b = {a + b}")
print(f"뺄셈 (Subtraction): a - b = {a - b}")
print(f"곱셈 (Multiplication): a * b = {a * b}")
print(f"나눗셈 (Division): a / b = {a / b:.2f}")
print(f"정수 나눗셈/몫 (Floor Division): a // b = {a // b}")
print(f"나머지 (Modulo): a % b = {a % b}")
print(f"거듭제곱 (Exponentiation): a ** b = {a ** b}")

# 음수 연산 (Negative operations)
print(f"\n음수 (Negative): -a = {-a}")
print(f"양수 (Positive): +a = {+a}")

# 나눗셈 상세 설명 (Division detailed explanation)
print(f"\n나눗셈 상세 (Division details):")
print(f"10 / 3 = {10 / 3} (실수 결과)")
print(f"10 // 3 = {10 // 3} (정수 결과 - 내림)")
print(f"10 % 3 = {10 % 3} (나머지)")
print(f"검증 (Verification): {10 // 3} * {3} + {10 % 3} = {(10 // 3) * 3 + (10 % 3)}")

# 음수와의 연산 (Operations with negative numbers)
print(f"\n음수와의 연산 (Negative number operations):")
print(f"-10 // 3 = {-10 // 3}")  # -4 (음수 무한대 방향으로 내림)
print(f"-10 % 3 = {-10 % 3}")  # 2
print(f"10 // -3 = {10 // -3}")  # -4
print(f"10 % -3 = {10 % -3}")  # -2

print()

# ===== 2. 비교 연산자 (Comparison Operators) =====

print("="*60)
print("2. 비교 연산자 (Comparison Operators)")
print("="*60)

x = 10
y = 20
z = 10

print(f"x = {x}, y = {y}, z = {z}\n")

# 비교 연산 (Comparison operations)
print(f"같음 (Equal): x == y → {x == y}")
print(f"같음 (Equal): x == z → {x == z}")
print(f"다름 (Not equal): x != y → {x != y}")
print(f"큼 (Greater than): x > y → {x > y}")
print(f"작음 (Less than): x < y → {x < y}")
print(f"크거나 같음 (Greater or equal): x >= z → {x >= z}")
print(f"작거나 같음 (Less or equal): x <= y → {x <= y}")

# 문자열 비교 (String comparison)
print(f"\n문자열 비교 (String comparison):")
str1 = "apple"
str2 = "banana"
print(f"'{str1}' < '{str2}' → {str1 < str2} (사전 순서)")
print(f"'{str1}' == '{str1}' → {str1 == str1}")

# 연쇄 비교 (Chained comparison)
print(f"\n연쇄 비교 (Chained comparison):")
num = 15
print(f"10 < {num} < 20 → {10 < num < 20}")
print(f"10 < {num} > 12 → {10 < num > 12}")

print()

# ===== 3. 논리 연산자 (Logical Operators) =====

print("="*60)
print("3. 논리 연산자 (Logical Operators)")
print("="*60)

# and 연산자 (and operator) - 모두 True일 때만 True
print("and 연산자 (모두 True일 때만 True):")
print(f"True and True → {True and True}")
print(f"True and False → {True and False}")
print(f"False and False → {False and False}")

# or 연산자 (or operator) - 하나라도 True면 True
print(f"\nor 연산자 (하나라도 True면 True):")
print(f"True or False → {True or False}")
print(f"False or False → {False or False}")
print(f"True or True → {True or True}")

# not 연산자 (not operator) - 반대로 변환
print(f"\nnot 연산자 (반대로 변환):")
print(f"not True → {not True}")
print(f"not False → {not False}")

# 실제 활용 예시 (Practical examples)
print(f"\n실제 활용 (Practical usage):")
age = 25
has_license = True
is_experienced = False

can_drive = age >= 18 and has_license
print(f"나이 {age}세, 면허 {has_license} → 운전 가능: {can_drive}")

eligible_for_discount = age < 18 or age >= 65
print(f"나이 {age}세 → 할인 대상: {eligible_for_discount}")

needs_training = not is_experienced
print(f"경험 {is_experienced} → 교육 필요: {needs_training}")

# 논리 연산자 우선순위 (Logical operator precedence)
print(f"\n논리 연산자 우선순위 (Precedence): not > and > or")
result = True or False and False  # True or (False and False)
print(f"True or False and False → {result}")
result = (True or False) and False  # 괄호 사용
print(f"(True or False) and False → {result}")

# 단축 평가 (Short-circuit evaluation)
print(f"\n단축 평가 (Short-circuit evaluation):")
print(f"False and <anything> → {False and print('실행되지 않음')}")
print(f"True or <anything> → {True or print('실행되지 않음')}")

print()

# ===== 4. 할당 연산자 (Assignment Operators) =====

print("="*60)
print("4. 할당 연산자 (Assignment Operators)")
print("="*60)

# 기본 할당 (Basic assignment)
value = 10
print(f"초기값 (Initial value): value = {value}")

# 복합 할당 연산자 (Compound assignment operators)
value += 5  # value = value + 5
print(f"value += 5 → {value}")

value -= 3  # value = value - 3
print(f"value -= 3 → {value}")

value *= 2  # value = value * 2
print(f"value *= 2 → {value}")

value /= 4  # value = value / 4
print(f"value /= 4 → {value}")

value //= 2  # value = value // 2
print(f"value //= 2 → {value}")

value %= 3  # value = value % 3
print(f"value %= 3 → {value}")

value **= 3  # value = value ** 3
print(f"value **= 3 → {value}")

# 여러 변수 할당 (Multiple assignment)
print(f"\n여러 변수 할당 (Multiple assignment):")
x, y, z = 1, 2, 3
print(f"x, y, z = 1, 2, 3 → x={x}, y={y}, z={z}")

# 같은 값 할당 (Same value assignment)
a = b = c = 100
print(f"a = b = c = 100 → a={a}, b={b}, c={c}")

# 값 교환 (Value swapping)
num1, num2 = 10, 20
print(f"\n교환 전 (Before swap): num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"교환 후 (After swap): num1={num1}, num2={num2}")

print()

# ===== 5. 멤버십 연산자 (Membership Operators) =====

print("="*60)
print("5. 멤버십 연산자 (Membership Operators)")
print("="*60)

# in 연산자 (in operator)
fruits = ["apple", "banana", "cherry"]
text = "Hello, World!"
numbers = (1, 2, 3, 4, 5)

print(f"리스트 (List): {fruits}")
print(f"'apple' in fruits → {'apple' in fruits}")
print(f"'grape' in fruits → {'grape' in fruits}")

print(f"\n문자열 (String): '{text}'")
print(f"'World' in text → {'World' in text}")
print(f"'Python' in text → {'Python' in text}")

# not in 연산자 (not in operator)
print(f"\n튜플 (Tuple): {numbers}")
print(f"6 not in numbers → {6 not in numbers}")
print(f"3 not in numbers → {3 not in numbers}")

# 딕셔너리에서 키 확인 (Check key in dictionary)
person = {"name": "John", "age": 30}
print(f"\n딕셔너리 (Dictionary): {person}")
print(f"'name' in person → {'name' in person}")
print(f"'address' in person → {'address' in person}")

print()

# ===== 6. 식별 연산자 (Identity Operators) =====

print("="*60)
print("6. 식별 연산자 (Identity Operators)")
print("="*60)

# is 연산자 (is operator) - 동일한 객체인지 확인
list1 = [1, 2, 3]
list2 = list1  # 같은 객체를 참조 (Reference to same object)
list3 = [1, 2, 3]  # 새로운 객체 (New object)

print(f"list1 = {list1}")
print(f"list2 = list1  (같은 객체 참조)")
print(f"list3 = {list3} (새로운 객체)")

print(f"\nlist1 is list2 → {list1 is list2} (같은 객체)")
print(f"list1 is list3 → {list1 is list3} (다른 객체)")
print(f"list1 == list3 → {list1 == list3} (값은 같음)")

# id() 함수로 객체 주소 확인 (Check object address with id())
print(f"\n객체 주소 (Object addresses):")
print(f"id(list1) = {id(list1)}")
print(f"id(list2) = {id(list2)}")
print(f"id(list3) = {id(list3)}")

# None 체크 (None check)
value1 = None
value2 = 0

print(f"\nvalue1 = {value1}, value2 = {value2}")
print(f"value1 is None → {value1 is None}")
print(f"value2 is None → {value2 is None}")
print(f"value1 == None → {value1 == None} (비권장)")

print()

# ===== 7. 비트 연산자 (Bitwise Operators) =====

print("="*60)
print("7. 비트 연산자 (Bitwise Operators)")
print("="*60)

a = 5   # 0101 in binary
b = 3   # 0011 in binary

print(f"a = {a} (이진수: {bin(a)})")
print(f"b = {b} (이진수: {bin(b)})")
print()

# AND 연산 (AND operation)
and_result = a & b  # 0101 & 0011 = 0001 (1)
print(f"AND: a & b = {and_result} (이진수: {bin(and_result)})")

# OR 연산 (OR operation)
or_result = a | b  # 0101 | 0011 = 0111 (7)
print(f"OR:  a | b = {or_result} (이진수: {bin(or_result)})")

# XOR 연산 (XOR operation)
xor_result = a ^ b  # 0101 ^ 0011 = 0110 (6)
print(f"XOR: a ^ b = {xor_result} (이진수: {bin(xor_result)})")

# NOT 연산 (NOT operation)
not_result = ~a  # ~0101 = ...11111010 (-6 in two's complement)
print(f"NOT: ~a = {not_result} (이진수: {bin(not_result)})")

# 왼쪽 시프트 (Left shift)
left_shift = a << 1  # 0101 << 1 = 1010 (10)
print(f"Left Shift:  a << 1 = {left_shift} (이진수: {bin(left_shift)})")

# 오른쪽 시프트 (Right shift)
right_shift = a >> 1  # 0101 >> 1 = 0010 (2)
print(f"Right Shift: a >> 1 = {right_shift} (이진수: {bin(right_shift)})")

# 비트 연산 실전 활용 (Practical bitwise operations)
print(f"\n실전 활용 (Practical usage):")
# 짝수/홀수 판별 (Check even/odd)
num = 7
is_odd = (num & 1) == 1
print(f"{num}은(는) 홀수: {is_odd}")

# 2의 거듭제곱 확인 (Check if power of 2)
num = 16
is_power_of_2 = (num & (num - 1)) == 0 and num != 0
print(f"{num}은(는) 2의 거듭제곱: {is_power_of_2}")

print()

# ===== 8. 연산자 우선순위 (Operator Precedence) =====

print("="*60)
print("8. 연산자 우선순위 (Operator Precedence)")
print("="*60)

# 연산자 우선순위 예시 (Operator precedence examples)
result1 = 10 + 5 * 2  # 곱셈 먼저
print(f"10 + 5 * 2 = {result1} (곱셈 먼저)")

result2 = (10 + 5) * 2  # 괄호 먼저
print(f"(10 + 5) * 2 = {result2} (괄호 먼저)")

result3 = 2 ** 3 ** 2  # 거듭제곱은 오른쪽부터
print(f"2 ** 3 ** 2 = {result3} (2^(3^2) = 2^9 = 512)")

result4 = 10 > 5 and 20 < 30
print(f"10 > 5 and 20 < 30 = {result4}")

# 복잡한 표현식 (Complex expression)
result5 = 5 + 3 * 2 > 10 and not False or 5 < 3
print(f"5 + 3 * 2 > 10 and not False or 5 < 3 = {result5}")
print("  → (5 + 6) > 10 and True or False")
print("  → 11 > 10 and True or False")
print("  → True and True or False")
print("  → True or False")
print("  → True")

print()
print("="*60)
print("연산자 학습 완료! (Operators learning completed!)")
print("="*60)

# ===== 연산자 우선순위 표 (Operator Precedence Table) =====

print("\n연산자 우선순위 (높음 → 낮음):")
print("1. ()                    괄호")
print("2. **                    거듭제곱")
print("3. +x, -x, ~x            단항 연산자")
print("4. *, /, //, %           곱셈, 나눗셈")
print("5. +, -                  덧셈, 뺄셈")
print("6. <<, >>                비트 시프트")
print("7. &                     비트 AND")
print("8. ^                     비트 XOR")
print("9. |                     비트 OR")
print("10. ==, !=, <, <=, >, >= 비교 연산자")
print("11. is, is not           식별 연산자")
print("12. in, not in           멤버십 연산자")
print("13. not                  논리 NOT")
print("14. and                  논리 AND")
print("15. or                   논리 OR")
