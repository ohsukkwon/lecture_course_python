"""
파일명: 01_functions_basic.py
설명: 함수 기본 - 정의, 호출, 매개변수, 반환값
Filename: 01_functions_basic.py
Description: Function basics - definition, calling, parameters, return values
"""

# ===== 1. 기본 함수 정의 및 호출 (Basic function definition and call) =====

print("="*60)
print("1. 기본 함수 정의 및 호출")
print("="*60)

def greet():
    """간단한 인사 함수 (Simple greeting function)"""
    print("안녕하세요! (Hello!)")

# 함수 호출 (Function call)
greet()
greet()

print()

# ===== 2. 매개변수가 있는 함수 (Function with parameters) =====

print("="*60)
print("2. 매개변수가 있는 함수")
print("="*60)

def greet_person(name):
    """이름을 받아 인사하는 함수"""
    print(f"안녕하세요, {name}님!")

greet_person("철수")
greet_person("영희")

print()

# ===== 3. 여러 매개변수 (Multiple parameters) =====

print("="*60)
print("3. 여러 매개변수")
print("="*60)

def introduce(name, age, city):
    """여러 정보를 받아 소개하는 함수"""
    print(f"이름: {name}, 나이: {age}세, 거주지: {city}")

introduce("김철수", 25, "서울")
introduce("이영희", 30, "부산")

print()

# ===== 4. 반환값 (Return value) =====

print("="*60)
print("4. 반환값 (Return value)")
print("="*60)

def add(a, b):
    """두 수를 더하여 반환 (Add two numbers and return)"""
    return a + b

result = add(10, 20)
print(f"10 + 20 = {result}")

result = add(5, 7)
print(f"5 + 7 = {result}")

print()

# ===== 5. 여러 값 반환 (Return multiple values) =====

print("="*60)
print("5. 여러 값 반환")
print("="*60)

def calculate(a, b):
    """사칙연산 결과를 모두 반환"""
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b if b != 0 else None
    return add_result, sub_result, mul_result, div_result

add, sub, mul, div = calculate(20, 5)
print(f"덧셈: {add}, 뺄셈: {sub}, 곱셈: {mul}, 나눗셈: {div}")

print()

# ===== 6. 기본값 매개변수 (Default parameters) =====

print("="*60)
print("6. 기본값 매개변수")
print("="*60)

def greet_with_message(name, message="안녕하세요"):
    """기본 메시지가 있는 인사 함수"""
    print(f"{message}, {name}님!")

greet_with_message("철수")  # 기본값 사용
greet_with_message("영희", "좋은 아침입니다")  # 기본값 덮어쓰기

print()

# ===== 7. 키워드 인자 (Keyword arguments) =====

print("="*60)
print("7. 키워드 인자")
print("="*60)

def create_profile(name, age, city, job):
    """프로필 생성 함수"""
    return f"{name} ({age}세) - {city}, {job}"

# 위치 인자
profile1 = create_profile("철수", 25, "서울", "개발자")
print(profile1)

# 키워드 인자 (순서 무관)
profile2 = create_profile(job="디자이너", city="부산", name="영희", age=28)
print(profile2)

# 혼합 사용
profile3 = create_profile("민수", 30, job="교사", city="인천")
print(profile3)

print()

# ===== 8. 가변 인자 (*args) =====

print("="*60)
print("8. 가변 인자 (*args)")
print("="*60)

def sum_all(*numbers):
    """모든 숫자의 합계를 반환"""
    total = sum(numbers)
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")
print(f"sum_all(10, 20) = {sum_all(10, 20)}")

print()

# ===== 9. 가변 키워드 인자 (**kwargs) =====

print("="*60)
print("9. 가변 키워드 인자 (**kwargs)")
print("="*60)

def print_info(**info):
    """모든 정보를 출력"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("학생 정보:")
print_info(name="철수", age=20, major="컴퓨터공학")

print("\n직원 정보:")
print_info(name="영희", department="개발팀", position="팀장", years=5)

print()

# ===== 10. 변수 스코프 (Variable scope) =====

print("="*60)
print("10. 변수 스코프")
print("="*60)

global_var = "전역 변수 (Global)"

def test_scope():
    local_var = "지역 변수 (Local)"
    print(f"함수 내부 - global_var: {global_var}")
    print(f"함수 내부 - local_var: {local_var}")

test_scope()
print(f"함수 외부 - global_var: {global_var}")
# print(local_var)  # NameError: 지역 변수는 함수 외부에서 접근 불가

print()

# ===== 11. global 키워드 (global keyword) =====

print("="*60)
print("11. global 키워드")
print("="*60)

counter = 0

def increment():
    global counter  # 전역 변수 수정
    counter += 1
    print(f"Counter: {counter}")

increment()
increment()
increment()
print(f"최종 counter: {counter}")

print()

# ===== 12. 람다 함수 (Lambda functions) =====

print("="*60)
print("12. 람다 함수")
print("="*60)

# 일반 함수
def square(x):
    return x ** 2

# 람다 함수
square_lambda = lambda x: x ** 2

print(f"square(5) = {square(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")

# 람다 함수 활용 - map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"제곱: {squared}")

# 람다 함수 활용 - filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"짝수: {evens}")

print()

# ===== 13. 실전 예제: 온도 변환 함수 (Temperature conversion) =====

print("="*60)
print("13. 실전 예제: 온도 변환")
print("="*60)

def celsius_to_fahrenheit(celsius):
    """섭씨를 화씨로 변환"""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """화씨를 섭씨로 변환"""
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")

print()

# ===== 14. 실전 예제: 소수 판별 함수 (Prime number check) =====

print("="*60)
print("14. 실전 예제: 소수 판별")
print("="*60)

def is_prime(n):
    """소수 판별 함수"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 테스트
test_numbers = [2, 3, 4, 5, 10, 17, 20, 23]
for num in test_numbers:
    result = "소수" if is_prime(num) else "소수 아님"
    print(f"{num}: {result}")

print()

# ===== 15. 실전 예제: 팩토리얼 (Factorial - recursive) =====

print("="*60)
print("15. 실전 예제: 재귀 함수 - 팩토리얼")
print("="*60)

def factorial(n):
    """팩토리얼 계산 (재귀)"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

for i in range(6):
    print(f"{i}! = {factorial(i)}")

print()
print("="*60)
print("함수 기본 예제 완료! (Function basics completed!)")
print("="*60)
