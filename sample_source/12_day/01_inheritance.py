"""
파일명: 01_inheritance.py
설명: 객체지향 프로그래밍 심화 - 상속과 다형성
Filename: 01_inheritance.py
Description: OOP advanced - Inheritance and polymorphism
"""

# ===== 1. 기본 상속 =====
print("="*60)
print("1. 기본 상속 (Inheritance)")
print("="*60)

class Animal:
    """부모 클래스"""
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "소리를 냅니다"

    def info(self):
        return f"이름: {self.name}"

class Dog(Animal):
    """자식 클래스"""
    def speak(self):
        """메서드 오버라이딩"""
        return f"{self.name}: 멍멍!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 야옹!"

# 객체 생성 및 사용
dog = Dog("멍멍이")
cat = Cat("야옹이")

print(dog.info())   # 부모 클래스 메서드
print(dog.speak())  # 오버라이딩된 메서드
print(cat.speak())

print()

# ===== 2. super() 함수 =====
print("="*60)
print("2. super() 함수")
print("="*60)

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

print()

# ===== 3. 다형성 (Polymorphism) =====
print("="*60)
print("3. 다형성 (Polymorphism)")
print("="*60)

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# 다형성 활용
shapes = [
    Rectangle(10, 20),
    Circle(5),
    Rectangle(5, 5)
]

print("도형들의 넓이:")
for i, shape in enumerate(shapes, 1):
    print(f"{i}. {shape.__class__.__name__}: {shape.area():.2f}")

print()

# ===== 4. 추상 클래스 =====
print("="*60)
print("4. 추상 클래스")
print("="*60)

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    """결제 방법 추상 클래스"""

    @abstractmethod
    def pay(self, amount):
        """추상 메서드 - 반드시 구현해야 함"""
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        return f"신용카드 {self.card_number[-4:]}로 {amount:,}원 결제"

class BankTransfer(PaymentMethod):
    def __init__(self, account):
        self.account = account

    def pay(self, amount):
        return f"계좌 {self.account}에서 {amount:,}원 이체"

# 사용
payments = [
    CreditCard("1234-5678-9012-3456"),
    BankTransfer("123-456-789")
]

for payment in payments:
    print(payment.pay(50000))

print()

# ===== 5. 실전 예제: RPG 게임 캐릭터 =====
print("="*60)
print("5. 실전 예제: RPG 게임 캐릭터")
print("="*60)

class Character:
    """캐릭터 기본 클래스"""
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_target(self, target):
        """공격"""
        target.hp -= self.attack
        return f"{self.name}이(가) {target.name}을(를) 공격! (데미지: {self.attack})"

    def is_alive(self):
        """생존 여부"""
        return self.hp > 0

    def __str__(self):
        return f"{self.name} (HP: {self.hp}, 공격력: {self.attack})"

class Warrior(Character):
    """전사 클래스"""
    def __init__(self, name):
        super().__init__(name, hp=150, attack=30)

    def special_attack(self, target):
        """특수 공격"""
        damage = self.attack * 2
        target.hp -= damage
        return f"{self.name}의 강타! (데미지: {damage})"

class Mage(Character):
    """마법사 클래스"""
    def __init__(self, name):
        super().__init__(name, hp=100, attack=40)

    def special_attack(self, target):
        """마법 공격"""
        damage = self.attack * 1.5
        target.hp -= damage
        return f"{self.name}의 파이어볼! (데미지: {int(damage)})"

# 전투 시뮬레이션
warrior = Warrior("전사")
mage = Mage("마법사")

print(warrior)
print(mage)
print()

print(warrior.attack_target(mage))
print(mage)
print()

print(mage.special_attack(warrior))
print(warrior)

print()
print("="*60)
print("상속과 다형성 예제 완료!")
print("="*60)
