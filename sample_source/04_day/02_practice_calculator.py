"""
파일명: 02_practice_calculator.py
설명: 실습 - 함수를 활용한 계산기 프로그램
Filename: 02_practice_calculator.py
Description: Practice - Calculator program using functions
"""

print("="*70)
print("함수 기반 계산기 프로그램 (Function-based Calculator)")
print("="*70)
print()

# ===== 1. 기본 계산 함수들 (Basic calculation functions) =====

def add(a, b):
    """
    두 수를 더합니다 (Add two numbers)
    Args:
        a: 첫 번째 숫자 (First number)
        b: 두 번째 숫자 (Second number)
    Returns:
        두 수의 합 (Sum of two numbers)
    """
    return a + b


def subtract(a, b):
    """두 수를 뺍니다 (Subtract two numbers)"""
    return a - b


def multiply(a, b):
    """두 수를 곱합니다 (Multiply two numbers)"""
    return a * b


def divide(a, b):
    """
    두 수를 나눕니다 (Divide two numbers)
    0으로 나누는 경우 None 반환 (Returns None if dividing by zero)
    """
    if b == 0:
        return None  # 0으로 나눌 수 없음
    return a / b


def power(a, b):
    """거듭제곱을 계산합니다 (Calculate power)"""
    return a ** b


def modulo(a, b):
    """나머지를 계산합니다 (Calculate modulo)"""
    if b == 0:
        return None
    return a % b


# ===== 2. 고급 계산 함수들 (Advanced calculation functions) =====

def factorial(n):
    """
    팩토리얼을 계산합니다 (Calculate factorial)
    n! = n × (n-1) × (n-2) × ... × 1
    """
    if n < 0:
        return None  # 음수는 팩토리얼 불가
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """소수인지 판별합니다 (Check if prime number)"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """최대공약수를 계산합니다 (Calculate GCD - Greatest Common Divisor)"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """최소공배수를 계산합니다 (Calculate LCM - Least Common Multiple)"""
    return abs(a * b) // gcd(a, b)


# ===== 3. 메뉴 표시 함수 (Menu display function) =====

def show_menu():
    """계산기 메뉴를 표시합니다 (Display calculator menu)"""
    print("\n" + "="*70)
    print("계산기 메뉴 (Calculator Menu)")
    print("="*70)
    print("1. 덧셈 (Addition)")
    print("2. 뺄셈 (Subtraction)")
    print("3. 곱셈 (Multiplication)")
    print("4. 나눗셈 (Division)")
    print("5. 거듭제곱 (Power)")
    print("6. 나머지 (Modulo)")
    print("7. 팩토리얼 (Factorial)")
    print("8. 소수 판별 (Prime Check)")
    print("9. 최대공약수 (GCD)")
    print("10. 최소공배수 (LCM)")
    print("0. 종료 (Exit)")
    print("="*70)


# ===== 4. 계산 실행 함수 (Calculation execution function) =====

def calculate(choice, num1, num2=None):
    """
    선택에 따라 계산을 수행합니다 (Perform calculation based on choice)
    """
    if choice == "1":
        result = add(num1, num2)
        return f"{num1} + {num2} = {result}"

    elif choice == "2":
        result = subtract(num1, num2)
        return f"{num1} - {num2} = {result}"

    elif choice == "3":
        result = multiply(num1, num2)
        return f"{num1} × {num2} = {result}"

    elif choice == "4":
        result = divide(num1, num2)
        if result is None:
            return "❌ 0으로 나눌 수 없습니다 (Cannot divide by zero)"
        return f"{num1} ÷ {num2} = {result:.4f}"

    elif choice == "5":
        result = power(num1, num2)
        return f"{num1} ^ {num2} = {result}"

    elif choice == "6":
        result = modulo(num1, num2)
        if result is None:
            return "❌ 0으로 나눌 수 없습니다"
        return f"{num1} % {num2} = {result}"

    elif choice == "7":
        result = factorial(int(num1))
        if result is None:
            return "❌ 음수는 팩토리얼을 계산할 수 없습니다"
        return f"{int(num1)}! = {result}"

    elif choice == "8":
        result = is_prime(int(num1))
        status = "소수입니다 (Prime)" if result else "소수가 아닙니다 (Not prime)"
        return f"{int(num1)}은(는) {status}"

    elif choice == "9":
        result = gcd(int(num1), int(num2))
        return f"GCD({int(num1)}, {int(num2)}) = {result}"

    elif choice == "10":
        result = lcm(int(num1), int(num2))
        return f"LCM({int(num1)}, {int(num2)}) = {result}"

    else:
        return "❌ 잘못된 선택입니다 (Invalid choice)"


# ===== 5. 메인 프로그램 (Main program) =====

def main():
    """메인 함수 (Main function)"""
    print("계산기 프로그램을 시작합니다! (Starting calculator program!)")

    # 데모 모드 (Demo mode)
    demo_calculations = [
        ("1", 10, 5),   # 덧셈
        ("2", 20, 8),   # 뺄셈
        ("3", 6, 7),    # 곱셈
        ("4", 15, 3),   # 나눗셈
        ("5", 2, 10),   # 거듭제곱
        ("7", 5, None), # 팩토리얼
        ("8", 17, None),# 소수 판별
        ("9", 48, 18),  # 최대공약수
    ]

    for choice, num1, num2 in demo_calculations:
        show_menu()
        print(f"\n선택: {choice}")

        # 숫자 입력 시뮬레이션
        if choice in ["1", "2", "3", "4", "5", "6", "9", "10"]:
            print(f"첫 번째 숫자: {num1}")
            print(f"두 번째 숫자: {num2}")
        else:
            print(f"숫자: {num1}")

        # 계산 수행
        result = calculate(choice, num1, num2)
        print(f"\n결과 (Result): {result}")

        input("\n계속하려면 Enter를 누르세요... (Press Enter to continue...)\n")

    # 종료
    show_menu()
    print("\n선택: 0")
    print("계산기를 종료합니다 (Closing calculator)")


# ===== 6. 실전 예제 모음 (Practical examples) =====

def run_examples():
    """다양한 계산 예제를 실행합니다 (Run various calculation examples)"""
    print("\n" + "="*70)
    print("실전 예제 모음 (Practical Examples)")
    print("="*70)

    # 예제 1: 기본 사칙연산
    print("\n1. 기본 사칙연산 (Basic operations)")
    print(f"   10 + 5 = {add(10, 5)}")
    print(f"   10 - 5 = {subtract(10, 5)}")
    print(f"   10 × 5 = {multiply(10, 5)}")
    print(f"   10 ÷ 5 = {divide(10, 5)}")

    # 예제 2: 팩토리얼
    print("\n2. 팩토리얼 (Factorial)")
    for i in range(1, 6):
        print(f"   {i}! = {factorial(i)}")

    # 예제 3: 소수 찾기
    print("\n3. 1부터 20까지의 소수 (Primes from 1 to 20)")
    primes = [i for i in range(1, 21) if is_prime(i)]
    print(f"   {primes}")

    # 예제 4: 최대공약수와 최소공배수
    print("\n4. GCD & LCM")
    pairs = [(12, 18), (24, 36), (15, 25)]
    for a, b in pairs:
        print(f"   GCD({a}, {b}) = {gcd(a, b)}, LCM({a}, {b}) = {lcm(a, b)}")

    # 예제 5: 거듭제곱
    print("\n5. 거듭제곱 (Power)")
    for i in range(1, 6):
        print(f"   2^{i} = {power(2, i)}")


# ===== 실행 (Execution) =====

if __name__ == "__main__":
    # 예제 실행
    run_examples()

    print("\n" + "="*70)
    print("💡 Tip: 함수를 사용하면")
    print("   - 코드 재사용이 쉬워집니다 (Code reuse becomes easier)")
    print("   - 코드가 더 읽기 쉬워집니다 (Code becomes more readable)")
    print("   - 유지보수가 편리합니다 (Maintenance is easier)")
    print("="*70)

    # 메인 프로그램 실행 (데모 모드)
    print("\n데모 모드로 실행하시겠습니까? (y/n): ", end="")
    # 실제로는 input() 사용, 여기서는 자동 진행
    # response = input().lower()
    response = "n"  # 자동으로 n 선택

    if response == "y":
        main()

    print("\n프로그램 종료 (Program ended)")
