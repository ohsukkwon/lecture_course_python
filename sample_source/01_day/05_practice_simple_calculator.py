"""
파일명: 05_practice_simple_calculator.py
설명: 실습 과제 - 간단한 계산 프로그램
Filename: 05_practice_simple_calculator.py
Description: Practice assignment - Simple calculator program
"""

print("="*60)
print("간단한 계산기 프로그램 (Simple Calculator Program)")
print("="*60)
print()

# 두 개의 숫자 입력받기 (Get two numbers from user)
print("두 개의 숫자를 입력하세요 (Enter two numbers)")
print("-"*60)

# 첫 번째 숫자 입력 (Input first number)
num1 = float(input("첫 번째 숫자 (First number): "))

# 두 번째 숫자 입력 (Input second number)
num2 = float(input("두 번째 숫자 (Second number): "))

print()
print("="*60)
print("계산 결과 (Calculation Results)")
print("="*60)
print()

# ===== 사칙연산 수행 (Perform four basic operations) =====

# 덧셈 (Addition)
addition = num1 + num2
print(f"덧셈 (Addition): {num1} + {num2} = {addition}")

# 뺄셈 (Subtraction)
subtraction = num1 - num2
print(f"뺄셈 (Subtraction): {num1} - {num2} = {subtraction}")

# 곱셈 (Multiplication)
multiplication = num1 * num2
print(f"곱셈 (Multiplication): {num1} × {num2} = {multiplication}")

# 나눗셈 (Division)
if num2 != 0:
    division = num1 / num2
    print(f"나눗셈 (Division): {num1} ÷ {num2} = {division}")
    print(f"나눗셈 (소수점 2자리): {num1} ÷ {num2} = {division:.2f}")
else:
    print(f"나눗셈 (Division): {num1} ÷ {num2} = 오류! 0으로 나눌 수 없습니다.")
    print(f"                    Error! Cannot divide by zero.")

print()
print("-"*60)
print("추가 연산 (Additional Operations)")
print("-"*60)
print()

# 몫 (Quotient - Integer division)
if num2 != 0:
    quotient = num1 // num2
    print(f"몫 (Quotient): {num1} // {num2} = {quotient}")
else:
    print(f"몫 (Quotient): {num1} // {num2} = 오류! (Error!)")

# 나머지 (Remainder - Modulo)
if num2 != 0:
    remainder = num1 % num2
    print(f"나머지 (Remainder): {num1} % {num2} = {remainder}")
else:
    print(f"나머지 (Remainder): {num1} % {num2} = 오류! (Error!)")

# 거듭제곱 (Power)
power = num1 ** num2
print(f"거듭제곱 (Power): {num1} ** {num2} = {power}")

# 절댓값 (Absolute value)
abs_num1 = abs(num1)
abs_num2 = abs(num2)
print(f"절댓값 (Absolute): |{num1}| = {abs_num1}, |{num2}| = {abs_num2}")

print()
print("="*60)
print("상세 계산 결과 (Detailed Results)")
print("="*60)
print()

# 표 형식으로 출력 (Output in table format)
print(f"┌{'─'*58}┐")
print(f"│ {'연산 (Operation)':<25} │ {'결과 (Result)':>28} │")
print(f"├{'─'*58}┤")
print(f"│ {f'{num1} + {num2}':<25} │ {addition:>28.2f} │")
print(f"│ {f'{num1} - {num2}':<25} │ {subtraction:>28.2f} │")
print(f"│ {f'{num1} × {num2}':<25} │ {multiplication:>28.2f} │")

if num2 != 0:
    print(f"│ {f'{num1} ÷ {num2}':<25} │ {division:>28.2f} │")
    print(f"│ {f'{num1} // {num2} (몫)':<25} │ {quotient:>28.2f} │")
    print(f"│ {f'{num1} % {num2} (나머지)':<25} │ {remainder:>28.2f} │")
else:
    print(f"│ {f'{num1} ÷ {num2}':<25} │ {'N/A (0으로 나눌 수 없음)':>28} │")

print(f"│ {f'{num1} ** {num2} (거듭제곱)':<25} │ {power:>28.2f} │")
print(f"└{'─'*58}┘")

print()
print("="*60)
print("통계 정보 (Statistical Information)")
print("="*60)
print()

# 최댓값과 최솟값 (Maximum and minimum)
max_value = max(num1, num2)
min_value = min(num1, num2)
print(f"최댓값 (Maximum): {max_value}")
print(f"최솟값 (Minimum): {min_value}")

# 평균 (Average)
average = (num1 + num2) / 2
print(f"평균 (Average): {average:.2f}")

# 차이 (Difference)
difference = abs(num1 - num2)
print(f"두 수의 차이 (Difference): {difference:.2f}")

# 비율 (Ratio)
if num2 != 0:
    ratio = num1 / num2
    print(f"비율 (Ratio): {num1} : {num2} = 1 : {ratio:.2f}")
    print(f"백분율 (Percentage): {num1}은(는) {num2}의 {(num1/num2)*100:.2f}%")

print()
print("="*60)
print("프로그램 종료 (Program ended)")
print("="*60)

# ===== 향상된 버전 추가 (Enhanced version) =====
print("\n\n")
print("="*60)
print("대화형 계산기 (Interactive Calculator)")
print("="*60)
print()
print("연산을 선택하세요 (Choose an operation):")
print("1. 덧셈 (Addition)")
print("2. 뺄셈 (Subtraction)")
print("3. 곱셈 (Multiplication)")
print("4. 나눗셈 (Division)")
print("5. 모든 연산 (All operations)")
print()

choice = input("선택 (1-5): ")

if choice in ['1', '2', '3', '4', '5']:
    a = float(input("\n첫 번째 숫자 (First number): "))
    b = float(input("두 번째 숫자 (Second number): "))
    print()
    print("-"*60)

    if choice == '1':
        print(f"결과 (Result): {a} + {b} = {a + b}")
    elif choice == '2':
        print(f"결과 (Result): {a} - {b} = {a - b}")
    elif choice == '3':
        print(f"결과 (Result): {a} × {b} = {a * b}")
    elif choice == '4':
        if b != 0:
            print(f"결과 (Result): {a} ÷ {b} = {a / b:.2f}")
        else:
            print("오류: 0으로 나눌 수 없습니다! (Error: Cannot divide by zero!)")
    elif choice == '5':
        print(f"덧셈 (Addition): {a} + {b} = {a + b}")
        print(f"뺄셈 (Subtraction): {a} - {b} = {a - b}")
        print(f"곱셈 (Multiplication): {a} × {b} = {a * b}")
        if b != 0:
            print(f"나눗셈 (Division): {a} ÷ {b} = {a / b:.2f}")
        else:
            print(f"나눗셈 (Division): 오류! (Error!)")

    print("-"*60)
else:
    print("잘못된 선택입니다! (Invalid choice!)")

print("\n계산기 프로그램을 종료합니다. (Calculator program ended.)")
