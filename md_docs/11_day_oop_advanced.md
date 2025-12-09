# 11일차: 객체지향 프로그래밍 II - 심화

## 학습 목표
- 상속(Inheritance) 이해 및 활용
- 메서드 오버라이딩
- super() 함수 사용
- 다형성(Polymorphism)
- 추상 클래스
- 다중 상속

---

## 1. 상속 (Inheritance)

### 1.1 상속의 개념
- 기존 클래스의 속성과 메서드를 물려받음
- 코드 재사용성 향상
- 계층적 클래스 구조 구현

### 1.2 기본 상속

```python
class Animal:
    """부모 클래스 (상위 클래스, 슈퍼 클래스)"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다")

class Dog(Animal):
    """자식 클래스 (하위 클래스, 서브 클래스)"""
    def bark(self):
        print(f"{self.name}이(가) 짖습니다: 멍멍!")

# 사용
dog = Dog("멍멍이")
dog.speak()  # 부모 클래스의 메서드
dog.bark()   # 자식 클래스의 메서드
```

---

## 2. 메서드 오버라이딩

### 2.1 메서드 재정의

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리를 냅니다"

class Dog(Animal):
    def speak(self):
        """메서드 오버라이딩"""
        return f"{self.name}: 멍멍!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 야옹!"

dog = Dog("멍멍이")
cat = Cat("야옹이")
print(dog.speak())  # 멍멍이: 멍멍!
print(cat.speak())  # 야옹이: 야옹!
```

---

## 3. super() 함수

### 3.1 부모 클래스 메서드 호출

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"이름: {self.name}, 나이: {self.age}"

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 부모 생성자 호출
        self.student_id = student_id

    def introduce(self):
        parent_intro = super().introduce()  # 부모 메서드 호출
        return f"{parent_intro}, 학번: {self.student_id}"

student = Student("김철수", 20, "2024001")
print(student.introduce())
```

### 3.2 super()의 고급 활용

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name} - {self.salary}원"

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} (팀: {self.team})"

manager = Manager("박부장", 5000000, "개발팀")
print(manager.get_info())
```

---

## 4. 다형성 (Polymorphism)

### 4.1 다형성의 개념
- 같은 인터페이스, 다른 구현
- 객체의 타입에 따라 다르게 동작

### 4.2 다형성 예제

```python
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# 다형성 활용
shapes = [
    Rectangle(10, 20),
    Circle(5),
    Rectangle(5, 5)
]

for shape in shapes:
    print(f"넓이: {shape.area():.2f}")
```

---

## 5. 추상 클래스 (Abstract Class)

### 5.1 ABC 모듈 사용

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    """추상 클래스"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        """추상 메서드 - 반드시 구현해야 함"""
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}: 멍멍!"

    def move(self):
        return f"{self.name}이(가) 걷습니다"

# animal = Animal("동물")  # TypeError: 추상 클래스는 인스턴스화 불가
dog = Dog("멍멍이")
print(dog.speak())
```

### 5.2 인터페이스 패턴

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """결제 방법 인터페이스"""

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"신용카드 {self.card_number}로 {amount}원 결제"

class BankTransfer(PaymentMethod):
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        return f"계좌 {self.account}에서 {amount}원 이체"

# 사용
payments = [
    CreditCard("1234-5678-9012-3456"),
    BankTransfer("123-456-789")
]

for payment in payments:
    print(payment.pay(10000))
```

---

## 6. 다중 상속 (Multiple Inheritance)

### 6.1 다중 상속 기본

```python
class Flyer:
    def fly(self):
        return "날아갑니다"

class Swimmer:
    def swim(self):
        return "수영합니다"

class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name

duck = Duck("오리")
print(duck.fly())   # Flyer로부터 상속
print(duck.swim())  # Swimmer로부터 상속
```

### 6.2 MRO (Method Resolution Order)

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

d = D()
print(d.method())  # B (MRO: D -> B -> C -> A)
print(D.mro())     # MRO 확인
```

---

## 7. 캡슐화 (Encapsulation)

### 7.1 정보 은닉

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private 변수

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    @property
    def balance(self):
        """잔액 조회 (읽기 전용)"""
        return self.__balance

account = BankAccount("김철수", 10000)
account.deposit(5000)
print(account.balance)  # OK
# account.__balance = 1000000  # 직접 접근 불가
```

---

## 8. 조합 vs 상속

### 8.1 조합 (Composition)

```python
class Engine:
    def start(self):
        return "엔진 시동"

    def stop(self):
        return "엔진 정지"

class Car:
    def __init__(self):
        self.engine = Engine()  # 조합

    def start(self):
        return self.engine.start()

    def stop(self):
        return self.engine.stop()

car = Car()
print(car.start())
```

### 8.2 상속 vs 조합 선택 가이드

- **상속**: "is-a" 관계 (Dog is an Animal)
- **조합**: "has-a" 관계 (Car has an Engine)

---

## 9. 디자인 패턴 예제

### 9.1 싱글톤 패턴

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True - 같은 인스턴스
```

### 9.2 팩토리 패턴

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "멍멍!"

class Cat(Animal):
    def speak(self):
        return "야옹!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")

# 사용
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")
print(dog.speak())
print(cat.speak())
```

---

## 실습 과제

### 과제 1: 도형 클래스 계층
Shape 추상 클래스와 다양한 도형 클래스

### 과제 2: 직원 관리 시스템
Employee 기본 클래스와 Manager, Engineer 등 파생 클래스

### 과제 3: 동물원 시뮬레이션
Animal 추상 클래스와 다양한 동물 클래스

### 과제 4: 결제 시스템
PaymentMethod 인터페이스와 다양한 결제 방법

### 과제 5: 게임 캐릭터 시스템
캐릭터 상속 계층과 스킬 시스템

---

## 다음 시간 예고

12일차에는 **실전 라이브러리 활용 및 최종 프로젝트**를 진행합니다.
