# 10일차: 객체지향 프로그래밍 I - 기초

## 학습 목표
- 객체지향 프로그래밍(OOP) 개념 이해
- 클래스와 객체의 차이
- 생성자와 소멸자 활용
- 인스턴스 변수와 메서드
- 클래스 변수와 메서드
- 정적 메서드

---

## 1. 객체지향 프로그래밍이란?

### 1.1 OOP의 정의
- 객체(Object)를 중심으로 프로그래밍
- 데이터와 기능을 하나로 묶음
- 코드 재사용성과 유지보수성 향상

### 1.2 주요 개념
- **클래스 (Class)**: 객체를 만들기 위한 설계도
- **객체 (Object)**: 클래스로부터 생성된 실체
- **인스턴스 (Instance)**: 특정 클래스의 객체

---

## 2. 클래스와 객체

### 2.1 클래스 정의

```python
class Person:
    """사람을 나타내는 클래스"""
    pass

# 객체 생성
person1 = Person()
person2 = Person()

print(type(person1))  # <class '__main__.Person'>
```

### 2.2 속성과 메서드

```python
class Person:
    """사람 클래스"""

    def __init__(self, name, age):
        """생성자 - 객체 초기화"""
        self.name = name  # 인스턴스 변수
        self.age = age

    def greet(self):
        """인사 메서드"""
        print(f"안녕하세요, {self.name}입니다.")

    def get_info(self):
        """정보 반환 메서드"""
        return f"{self.name} ({self.age}세)"

# 객체 생성 및 사용
person1 = Person("김철수", 25)
person1.greet()  # 안녕하세요, 김철수입니다.
print(person1.get_info())  # 김철수 (25세)
```

---

## 3. 생성자와 소멸자

### 3.1 생성자 (__init__)

```python
class Rectangle:
    def __init__(self, width, height):
        """생성자 - 객체 초기화"""
        print("Rectangle 객체 생성")
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산"""
        return self.width * self.height

rect = Rectangle(10, 20)
print(rect.area())  # 200
```

### 3.2 소멸자 (__del__)

```python
class Resource:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} 생성")

    def __del__(self):
        """소멸자 - 객체 삭제 시 호출"""
        print(f"{self.name} 삭제")

resource = Resource("MyResource")
del resource  # 명시적 삭제
```

---

## 4. 인스턴스 변수와 메서드

### 4.1 인스턴스 변수

```python
class Student:
    def __init__(self, name, student_id):
        # 인스턴스 변수 - 각 객체마다 고유
        self.name = name
        self.student_id = student_id
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

student1 = Student("철수", "2024001")
student2 = Student("영희", "2024002")

student1.add_score(85)
student1.add_score(90)
print(f"{student1.name}의 평균: {student1.get_average()}")
```

### 4.2 인스턴스 메서드

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """출금"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        """잔액 조회"""
        return self.balance

account = BankAccount("김철수", 10000)
account.deposit(5000)
account.withdraw(3000)
print(account.get_balance())  # 12000
```

---

## 5. 클래스 변수와 메서드

### 5.1 클래스 변수

```python
class Employee:
    # 클래스 변수 - 모든 인스턴스가 공유
    company = "ABC Company"
    employee_count = 0

    def __init__(self, name):
        self.name = name  # 인스턴스 변수
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        """클래스 메서드"""
        return cls.employee_count

emp1 = Employee("철수")
emp2 = Employee("영희")
print(Employee.employee_count)  # 2
print(Employee.get_employee_count())  # 2
```

### 5.2 클래스 메서드 (@classmethod)

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        """문자열로부터 Date 객체 생성"""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

# 일반 생성
date1 = Date(2024, 1, 15)

# 클래스 메서드 사용
date2 = Date.from_string("2024-01-15")
print(date2)  # 2024-01-15
```

---

## 6. 정적 메서드 (@staticmethod)

```python
class Math:
    @staticmethod
    def add(a, b):
        """정적 메서드 - self나 cls 불필요"""
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# 클래스 이름으로 직접 호출
print(Math.add(5, 3))  # 8
print(Math.multiply(4, 7))  # 28

# 인스턴스로도 호출 가능 (비권장)
math = Math()
print(math.add(2, 3))  # 5
```

---

## 7. 프라이빗 속성과 메서드

### 7.1 네이밍 컨벤션

```python
class Person:
    def __init__(self, name, age):
        self.name = name          # 공개 (public)
        self._age = age           # 보호 (protected) - 관습적
        self.__ssn = "123456"     # 비공개 (private) - 이름 맹글링

    def get_age(self):
        """getter 메서드"""
        return self._age

    def set_age(self, age):
        """setter 메서드"""
        if age > 0:
            self._age = age

    def __private_method(self):
        """비공개 메서드"""
        print("Private method")

person = Person("철수", 25)
print(person.name)      # OK
print(person._age)      # 가능하지만 비권장
# print(person.__ssn)   # AttributeError
```

### 7.2 프로퍼티 (@property)

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """getter"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """setter"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("반지름은 양수여야 합니다")

    @property
    def area(self):
        """읽기 전용 속성"""
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.radius)  # 5 (getter 호출)
circle.radius = 10    # setter 호출
print(circle.area)    # 314.0 (계산된 속성)
```

---

## 8. 매직 메서드 (Special Methods)

### 8.1 문자열 표현

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """사용자 친화적 문자열"""
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """개발자용 문자열"""
        return f"Book('{self.title}', '{self.author}')"

book = Book("Python 101", "John Doe")
print(str(book))   # Python 101 by John Doe
print(repr(book))  # Book('Python 101', 'John Doe')
```

### 8.2 연산자 오버로딩

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """+ 연산자"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """- 연산자"""
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
print(v3)  # Vector(3, 7)
```

---

## 실습 과제

### 과제 1: 학생 클래스
학생의 정보와 성적을 관리하는 클래스

### 과제 2: 은행 계좌 클래스
입금, 출금, 잔액 조회 기능

### 과제 3: 도서 관리 시스템
Book 클래스와 Library 클래스

### 과제 4: 게임 캐릭터 클래스
RPG 게임의 캐릭터 클래스

### 과제 5: 시간 클래스
시간 표현 및 연산 클래스

---

## 다음 시간 예고

11일차에는 **객체지향 프로그래밍 II - 심화**를 학습합니다.
