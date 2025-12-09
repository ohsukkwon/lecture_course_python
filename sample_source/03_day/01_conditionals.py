"""
파일명: 01_conditionals.py
설명: 조건문 (if-elif-else) 예제
Filename: 01_conditionals.py
Description: Conditional statements (if-elif-else) examples
"""

# ===== 1. 기본 if 문 (Basic if statement) =====

print("="*60)
print("1. 기본 if 문 (Basic if statement)")
print("="*60)

age = 20

if age >= 18:
    print("성인입니다 (Adult)")

print()

# ===== 2. if-else 문 (if-else statement) =====

print("="*60)
print("2. if-else 문 (if-else statement)")
print("="*60)

score = 75

if score >= 60:
    print("합격 (Pass)")
else:
    print("불합격 (Fail)")

print()

# ===== 3. if-elif-else 문 (if-elif-else statement) =====

print("="*60)
print("3. if-elif-else 문 (Grade system)")
print("="*60)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수: {score}, 학점: {grade}")

print()

# ===== 4. 중첩 if 문 (Nested if statement) =====

print("="*60)
print("4. 중첩 if 문 (Nested if)")
print("="*60)

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능합니다 (Can drive)")
    else:
        print("면허가 필요합니다 (License required)")
else:
    print("나이 미달입니다 (Age requirement not met)")

print()

# ===== 5. 조건 표현식 (Conditional expression / Ternary operator) =====

print("="*60)
print("5. 조건 표현식 (Conditional expression)")
print("="*60)

age = 20

# 삼항 연산자 (Ternary operator)
status = "성인" if age >= 18 else "미성년자"
print(f"나이: {age}, 상태: {status}")

# 일반 if-else와 동일 (Equivalent to regular if-else)
if age >= 18:
    status = "성인"
else:
    status = "미성년자"
print(f"일반 if-else: {status}")

print()

# ===== 6. 실전 예제: 계절 판별 (Season determination) =====

print("="*60)
print("6. 실전 예제: 계절 판별 (Season determination)")
print("="*60)

month = 7

if month in [3, 4, 5]:
    season = "봄 (Spring)"
elif month in [6, 7, 8]:
    season = "여름 (Summer)"
elif month in [9, 10, 11]:
    season = "가을 (Fall)"
elif month in [12, 1, 2]:
    season = "겨울 (Winter)"
else:
    season = "잘못된 월 (Invalid month)"

print(f"{month}월은 {season}입니다")

print()

# ===== 7. 실전 예제: BMI 판정 (BMI classification) =====

print("="*60)
print("7. 실전 예제: BMI 판정 (BMI classification)")
print("="*60)

height = 175  # cm
weight = 70   # kg

# BMI 계산 (Calculate BMI)
height_m = height / 100
bmi = weight / (height_m ** 2)

print(f"키: {height}cm, 몸무게: {weight}kg")
print(f"BMI: {bmi:.2f}")

# BMI 판정 (BMI classification)
if bmi < 18.5:
    category = "저체중 (Underweight)"
elif 18.5 <= bmi < 23.0:
    category = "정상 (Normal)"
elif 23.0 <= bmi < 25.0:
    category = "비만 전단계 (Pre-obese)"
else:
    category = "비만 (Obese)"

print(f"판정: {category}")

print()

# ===== 8. 실전 예제: 로그인 시스템 (Login system) =====

print("="*60)
print("8. 실전 예제: 로그인 시스템 (Login system)")
print("="*60)

# 미리 정의된 계정 (Predefined accounts)
correct_username = "admin"
correct_password = "password123"

# 사용자 입력 (시뮬레이션) (User input simulation)
username = "admin"
password = "password123"

print(f"입력된 사용자명: {username}")
print(f"입력된 비밀번호: {password}")

if username == correct_username:
    if password == correct_password:
        print("✅ 로그인 성공! (Login successful!)")
    else:
        print("❌ 비밀번호가 틀렸습니다 (Incorrect password)")
else:
    print("❌ 존재하지 않는 사용자입니다 (User not found)")

print()

# ===== 9. 실전 예제: 할인율 계산 (Discount calculation) =====

print("="*60)
print("9. 실전 예제: 할인율 계산 (Discount calculation)")
print("="*60)

price = 150000  # 원 (KRW)
is_member = True
is_vip = False

print(f"원가: {price:,}원")
print(f"회원 여부: {is_member}")
print(f"VIP 여부: {is_vip}")

# 할인율 결정 (Determine discount rate)
if is_vip:
    discount_rate = 0.20  # 20%
elif is_member:
    discount_rate = 0.10  # 10%
else:
    discount_rate = 0.0   # 0%

# 할인 금액 계산 (Calculate discount amount)
discount_amount = price * discount_rate
final_price = price - discount_amount

print(f"할인율: {discount_rate * 100:.0f}%")
print(f"할인 금액: {discount_amount:,}원")
print(f"최종 가격: {final_price:,}원")

print()

# ===== 10. 논리 연산자와 조건문 (Logical operators with conditionals) =====

print("="*60)
print("10. 논리 연산자와 조건문 (Logical operators)")
print("="*60)

age = 25
income = 3000000  # 월 소득 (Monthly income)

# and 연산자 (and operator)
if age >= 20 and income >= 2000000:
    print("대출 가능 (Loan eligible)")
else:
    print("대출 불가 (Loan not eligible)")

# or 연산자 (or operator)
if age < 18 or age >= 65:
    print("할인 대상 (Discount eligible)")
else:
    print("정상 가격 (Regular price)")

# not 연산자 (not operator)
is_banned = False
if not is_banned:
    print("서비스 이용 가능 (Service available)")
else:
    print("이용 제한 (Service restricted)")

print()
print("="*60)
print("조건문 예제 완료! (Conditionals examples completed!)")
print("="*60)
