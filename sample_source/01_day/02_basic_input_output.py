"""
파일명: 02_basic_input_output.py
설명: 기본 입출력 - input()과 print() 함수 활용
Filename: 02_basic_input_output.py
Description: Basic input/output - Using input() and print() functions
"""

# ===== 기본 입력 (Basic Input) =====

# 사용자 이름 입력받기 (Get user's name)
name = input("이름을 입력하세요 (Enter your name): ")
age = 20
print("안녕하세요,", name, "님!" , "나이:" , age)
print(f"Hello, {name}! 당신의 나이는 {age}")

print("\n" + "="*50 + "\n")

# ===== 다양한 출력 방법 (Various Output Methods) =====

# 방법 1: 콤마로 구분 (Method 1: Separate with comma)
print("이름:", name)
print("이름:", name, ", 나이:", age)

# 방법 2: 문자열 연결 (Method 2: String concatenation)
print("이름: " + name)
print("이름: " + name + ",나이: " + name)

# 방법 3: f-string (Python 3.6+) - 추천! (Recommended!)
print(f"이름: {name}")
print(f"이름: {name}, 나이:{age}")

# 방법 4: format() 메서드 (Method 4: format() method)
print("이름: {}".format(name))
print("이름: {}, 나이:{}".format(name,age))

# 방법 5: % 포맷팅 (Method 5: % formatting - Old style)
print("이름: %s" % name)
print("이름: %s, 나이:%d" % (name,age))

print("\n" + "="*50 + "\n")

# ===== 숫자 입력 (Number Input) =====

# 문자열을 정수로 변환 (Convert string to integer)
age = int(input("나이를 입력하세요 (Enter your age): "))
print(f"당신은 {age}살입니다. (You are {age} years old.)")
print(f"10년 후에는 {age + 10}살입니다. (In 10 years, you will be {age + 10} years old.)")

print("\n" + "="*50 + "\n")

# 문자열을 실수로 변환 (Convert string to float)
height = float(input("키를 입력하세요 (cm) [Enter your height (cm)]: "))
print(f"당신의 키는 {height}cm입니다. (Your height is {height}cm.)")
print(f"미터로는 {height/100}m입니다. (In meters: {height/100}m.)")

print("\n" + "="*50 + "\n")

# ===== 여러 입력 한 번에 받기 (Multiple Inputs at Once) =====

# 공백으로 구분된 입력 받기 (Get space-separated inputs)
print("두 개의 숫자를 입력하세요 (공백으로 구분)")
print("Enter two numbers (separated by space)")
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print(f"첫 번째 숫자: {num1}, 두 번째 숫자: {num2}")
print(f"First number: {num1}, Second number: {num2}")
print(f"합계: {num1 + num2}")
print(f"Sum: {num1 + num2}")

print("\n" + "="*50 + "\n")

# 더 간단한 방법 (Simpler way)
print("다시 두 개의 숫자를 입력하세요 (공백으로 구분)")
print("Enter two numbers again (separated by space)")
a, b = map(int, input().split())
print(f"곱셈 결과: {a} × {b} = {a * b}")
print(f"Multiplication result: {a} × {b} = {a * b}")

print("\n" + "="*50 + "\n")

# ===== 형식화된 출력 (Formatted Output) =====

# 소수점 자리 제한 (Limit decimal places)
pi = 3.141592653589793
print(f"파이(π) = {pi}")  # 전체 출력 (Full output)
print(f"파이(π) = {pi:.2f}")  # 소수점 2자리 (2 decimal places)
print(f"파이(π) = {pi:.4f}")  # 소수점 4자리 (4 decimal places)

print("\n" + "="*50 + "\n")

# 정렬 (Alignment)
print(f"{'이름':<10}{'나이':^10}{'직업':>10}")  # < 왼쪽, ^ 가운데, > 오른쪽
print(f"{'Name':<10}{'Age':^10}{'Job':>10}")  # < left, ^ center, > right
print(f"{'김철수':<10}{'25':^10}{'학생':>10}")
print(f"{'이영희':<10}{'30':^10}{'직장인':>10}")

print("\n" + "="*50 + "\n")

# 천 단위 구분자 (Thousands separator)
large_number = 1234567890
print(f"숫자: {large_number}")  # 1234567890
print(f"천 단위 구분: {large_number:,}")  # 1,234,567,890

print("\n" + "="*50 + "\n")

# 백분율 표시 (Percentage display)
percentage = 0.8567
print(f"비율: {percentage}")  # 0.8567
print(f"백분율: {percentage:.2%}")  # 85.67%
