"""
파일명: 01_class_basics.py
설명: 객체지향 프로그래밍 기초 - 클래스와 객체
Filename: 01_class_basics.py
Description: OOP basics - Classes and objects
"""

# ===== 1. 기본 클래스 정의 =====
print("="*60)
print("1. 기본 클래스 정의")
print("="*60)

class Person:
    def __init__(self, name, age):
        """생성자 - 객체 초기화"""
        self.name = name
        self.age = age

    def greet(self):
        """인사 메서드"""
        return f"안녕하세요, {self.name}입니다."

    def get_info(self):
        """정보 반환"""
        return f"{self.name} ({self.age}세)"

# 객체 생성
person1 = Person("김철수", 25)
person2 = Person("이영희", 30)

print(person1.greet())
print(person2.get_info())

print()

# ===== 2. 클래스 변수와 인스턴스 변수 =====
print("="*60)
print("2. 클래스 변수와 인스턴스 변수")
print("="*60)

class Employee:
    # 클래스 변수 (모든 인스턴스가 공유)
    company = "ABC Company"
    employee_count = 0

    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Employee.employee_count += 1

emp1 = Employee("철수")
emp2 = Employee("영희")

print(f"회사: {Employee.company}")
print(f"직원 수: {Employee.employee_count}")

print()

# ===== 3. 메서드 종류 =====
print("="*60)
print("3. 메서드 종류")
print("="*60)

class Math:
    @staticmethod
    def add(a, b):
        """정적 메서드 - self 불필요"""
        return a + b

    @classmethod
    def create_calculator(cls):
        """클래스 메서드"""
        return cls()

# 정적 메서드 호출
print(f"Math.add(5, 3) = {Math.add(5, 3)}")

print()

# ===== 4. 프라이빗 속성 =====
print("="*60)
print("4. 프라이빗 속성과 프로퍼티")
print("="*60)

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # 프라이빗 변수

    @property
    def balance(self):
        """잔액 조회 (읽기 전용)"""
        return self.__balance

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """출금"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

account = BankAccount("김철수", 10000)
print(f"소유자: {account.owner}")
print(f"잔액: {account.balance}원")

account.deposit(5000)
print(f"5000원 입금 후: {account.balance}원")

account.withdraw(3000)
print(f"3000원 출금 후: {account.balance}원")

print()

# ===== 5. 매직 메서드 =====
print("="*60)
print("5. 매직 메서드")
print("="*60)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """문자열 표현"""
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """+ 연산자 오버로딩"""
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2

print(f"p1: {p1}")
print(f"p2: {p2}")
print(f"p1 + p2: {p3}")

print()

# ===== 6. 실전 예제: 학생 클래스 =====
print("="*60)
print("6. 실전 예제: 학생 성적 관리")
print("="*60)

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        """성적 추가"""
        if 0 <= score <= 100:
            self.scores.append(score)
            return True
        return False

    def get_average(self):
        """평균 계산"""
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_grade(self):
        """학점 계산"""
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        return "F"

    def __str__(self):
        return f"{self.name} ({self.student_id}): 평균 {self.get_average():.1f}, 학점 {self.get_grade()}"

# 학생 생성 및 성적 추가
student = Student("김철수", "2024001")
student.add_score(85)
student.add_score(90)
student.add_score(88)

print(student)

print()
print("="*60)
print("클래스 기초 예제 완료!")
print("="*60)
