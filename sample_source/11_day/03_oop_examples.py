"""
파일명: 03_oop_examples.py
설명: 다양한 객체지향 프로그래밍 예제 모음
Filename: 03_oop_examples.py
Description: Collection of various OOP examples
"""

print("="*70)
print("다양한 OOP 예제 모음 (Various OOP Examples)")
print("="*70)
print()

# ===== 1. 은행 계좌 클래스 (Bank Account class) =====
print("="*70)
print("1. 은행 계좌 클래스 (Bank Account Class)")
print("="*70)
print()

class BankAccount:
    """은행 계좌 클래스"""

    # 클래스 변수 (Class variable)
    bank_name = "파이썬 은행"
    interest_rate = 0.03  # 3% 이자율

    def __init__(self, account_number, owner, balance=0):
        # 인스턴스 변수 (Instance variables)
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance  # private 변수 (언더스코어 2개)

    def deposit(self, amount):
        """입금"""
        if amount > 0:
            self.__balance += amount
            return f"✓ {amount:,}원 입금 완료. 잔액: {self.__balance:,}원"
        return "❌ 입금액은 0보다 커야 합니다"

    def withdraw(self, amount):
        """출금"""
        if amount > self.__balance:
            return f"❌ 잔액 부족. 현재 잔액: {self.__balance:,}원"
        if amount > 0:
            self.__balance -= amount
            return f"✓ {amount:,}원 출금 완료. 잔액: {self.__balance:,}원"
        return "❌ 출금액은 0보다 커야 합니다"

    def get_balance(self):
        """잔액 조회"""
        return self.__balance

    def apply_interest(self):
        """이자 적용"""
        interest = self.__balance * self.interest_rate
        self.__balance += interest
        return f"✓ 이자 {interest:,.0f}원 적용. 잔액: {self.__balance:,}원"

    def __str__(self):
        return f"[{self.account_number}] {self.owner} - {self.__balance:,}원"

# 사용 예제 (Usage example)
print("💰 은행 계좌 예제:")

account = BankAccount("123-456-789", "홍길동", 1000000)
print(f"  계좌 생성: {account}")
print(f"  {account.deposit(500000)}")
print(f"  {account.withdraw(300000)}")
print(f"  {account.apply_interest()}")

print()

# ===== 2. 상품 재고 관리 클래스 (Product Inventory class) =====
print("="*70)
print("2. 상품 재고 관리 클래스 (Product Inventory Class)")
print("="*70)
print()

class Product:
    """상품 클래스"""

    def __init__(self, product_id, name, price, stock=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.sales_count = 0  # 판매 수량

    def restock(self, quantity):
        """재고 추가"""
        self.stock += quantity
        return f"✓ {self.name} {quantity}개 입고. 현재 재고: {self.stock}개"

    def sell(self, quantity):
        """판매"""
        if quantity > self.stock:
            return f"❌ 재고 부족. 현재 재고: {self.stock}개"
        self.stock -= quantity
        self.sales_count += quantity
        total_price = self.price * quantity
        return f"✓ {self.name} {quantity}개 판매. 금액: {total_price:,}원. 남은 재고: {self.stock}개"

    def get_total_sales(self):
        """총 판매 금액"""
        return self.price * self.sales_count

    def is_low_stock(self, threshold=10):
        """재고 부족 여부"""
        return self.stock < threshold

    def __str__(self):
        return f"[{self.product_id}] {self.name} - {self.price:,}원 (재고: {self.stock})"

# 사용 예제 (Usage example)
print("📦 상품 재고 관리 예제:")

product = Product("P001", "노트북", 1200000, stock=5)
print(f"  {product}")
print(f"  {product.sell(2)}")
print(f"  {product.restock(10)}")
print(f"  총 판매 금액: {product.get_total_sales():,}원")
print(f"  재고 부족: {'예' if product.is_low_stock() else '아니오'}")

print()

# ===== 3. 학생 성적 관리 클래스 (Student Grade Management) =====
print("="*70)
print("3. 학생 성적 관리 클래스 (Student Grade Management)")
print("="*70)
print()

class Student:
    """학생 클래스"""

    # 클래스 변수: 학생 수 카운터 (Class variable: student counter)
    student_count = 0

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}  # 과목별 성적
        Student.student_count += 1

    def add_grade(self, subject, score):
        """성적 추가"""
        if 0 <= score <= 100:
            self.grades[subject] = score
            return f"✓ {subject} 성적 등록: {score}점"
        return "❌ 성적은 0-100 사이여야 합니다"

    def get_average(self):
        """평균 계산"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_grade_letter(self):
        """등급 계산"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def get_rank_in_subject(self, subject, all_students):
        """특정 과목에서의 등수"""
        if subject not in self.grades:
            return None

        # 해당 과목 성적이 있는 학생들만 필터링
        students_with_grade = [s for s in all_students if subject in s.grades]
        # 성적 기준 내림차순 정렬
        sorted_students = sorted(students_with_grade,
                                 key=lambda s: s.grades[subject],
                                 reverse=True)

        for rank, student in enumerate(sorted_students, 1):
            if student.student_id == self.student_id:
                return rank
        return None

    def __str__(self):
        avg = self.get_average()
        grade = self.get_grade_letter()
        return f"{self.name} ({self.student_id}) - 평균: {avg:.1f}점 ({grade}등급)"

    @classmethod
    def get_total_students(cls):
        """전체 학생 수 반환 (클래스 메서드)"""
        return cls.student_count

# 사용 예제 (Usage example)
print("🎓 학생 성적 관리 예제:")

students = [
    Student("김철수", "2024001"),
    Student("이영희", "2024002"),
    Student("박민수", "2024003"),
]

# 성적 입력
students[0].add_grade("수학", 95)
students[0].add_grade("영어", 88)
students[0].add_grade("과학", 92)

students[1].add_grade("수학", 88)
students[1].add_grade("영어", 95)
students[1].add_grade("과학", 90)

students[2].add_grade("수학", 92)
students[2].add_grade("영어", 85)
students[2].add_grade("과학", 88)

# 결과 출력
for student in students:
    print(f"  {student}")

print(f"\n  전체 학생 수: {Student.get_total_students()}명")

# 수학 등수
print(f"\n  수학 등수:")
for student in students:
    rank = student.get_rank_in_subject("수학", students)
    score = student.grades.get("수학", 0)
    print(f"    {student.name}: {rank}등 ({score}점)")

print()

# ===== 4. 타이머 클래스 (Timer class) =====
print("="*70)
print("4. 타이머 클래스 (Timer Class)")
print("="*70)
print()

import time

class Timer:
    """타이머 클래스"""

    def __init__(self, name="타이머"):
        self.name = name
        self.start_time = None
        self.end_time = None

    def start(self):
        """타이머 시작"""
        self.start_time = time.time()
        print(f"⏰ {self.name} 시작")

    def stop(self):
        """타이머 종료"""
        if self.start_time is None:
            return "❌ 타이머가 시작되지 않았습니다"
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"⏰ {self.name} 종료: {elapsed:.4f}초")
        return elapsed

    def __enter__(self):
        """컨텍스트 매니저 시작"""
        self.start()
        return self

    def __exit__(self, *args):
        """컨텍스트 매니저 종료"""
        self.stop()

# 사용 예제 (Usage example)
print("⏰ 타이머 예제:")

# 방법 1: 일반 사용
timer = Timer("테스트1")
timer.start()
time.sleep(0.1)  # 0.1초 대기
timer.stop()

# 방법 2: with 문 사용
print("\nwith 문 사용:")
with Timer("테스트2"):
    time.sleep(0.1)

print()

# ===== 5. 캐시 클래스 (Cache class) =====
print("="*70)
print("5. 캐시 클래스 (Cache Class)")
print("="*70)
print()

class Cache:
    """간단한 캐시 클래스"""

    def __init__(self, max_size=100):
        self.max_size = max_size
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def get(self, key):
        """캐시에서 값 가져오기"""
        if key in self.cache:
            self.hits += 1
            return self.cache[key]
        else:
            self.misses += 1
            return None

    def set(self, key, value):
        """캐시에 값 저장"""
        if len(self.cache) >= self.max_size:
            # 가장 오래된 항목 제거 (간단한 구현)
            self.cache.pop(next(iter(self.cache)))

        self.cache[key] = value

    def get_hit_rate(self):
        """캐시 적중률"""
        total = self.hits + self.misses
        if total == 0:
            return 0
        return (self.hits / total) * 100

    def clear(self):
        """캐시 초기화"""
        self.cache.clear()
        self.hits = 0
        self.misses = 0

    def __len__(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

# 사용 예제 (Usage example)
print("💾 캐시 예제:")

cache = Cache(max_size=3)

# 데이터 저장
cache.set("user_1", {"name": "홍길동", "age": 25})
cache.set("user_2", {"name": "김철수", "age": 30})
cache.set("user_3", {"name": "이영희", "age": 28})

print(f"  캐시 크기: {len(cache)}")

# 데이터 조회
user = cache.get("user_1")
print(f"  user_1 조회: {user} ({'Hit' if user else 'Miss'})")

user = cache.get("user_4")
print(f"  user_4 조회: {user} ({'Hit' if user else 'Miss'})")

print(f"  캐시 적중률: {cache.get_hit_rate():.1f}%")

print()

# ===== 6. 체인 연산 클래스 (Method Chaining) =====
print("="*70)
print("6. 체인 연산 클래스 (Method Chaining)")
print("="*70)
print()

class Calculator:
    """체인 연산을 지원하는 계산기"""

    def __init__(self, value=0):
        self.value = value

    def add(self, n):
        """더하기"""
        self.value += n
        return self  # self를 반환하여 체이닝 가능

    def subtract(self, n):
        """빼기"""
        self.value -= n
        return self

    def multiply(self, n):
        """곱하기"""
        self.value *= n
        return self

    def divide(self, n):
        """나누기"""
        if n != 0:
            self.value /= n
        return self

    def result(self):
        """결과 반환"""
        return self.value

    def __str__(self):
        return f"Calculator(value={self.value})"

# 사용 예제 (Usage example)
print("🔢 체인 연산 예제:")

calc = Calculator(10)
result = calc.add(5).multiply(2).subtract(10).divide(2).result()
print(f"  (10 + 5) × 2 - 10 ÷ 2 = {result}")

print()

# ===== 7. 싱글톤 패턴 (Singleton Pattern) =====
print("="*70)
print("7. 싱글톤 패턴 (Singleton Pattern)")
print("="*70)
print()

class DatabaseConnection:
    """싱글톤 패턴을 사용한 데이터베이스 연결 클래스"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = f"DB 연결 #{id(cls._instance)}"
        return cls._instance

    def query(self, sql):
        """쿼리 실행"""
        return f"[{self.connection}] 실행: {sql}"

# 사용 예제 (Usage example)
print("🔗 싱글톤 패턴 예제:")

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"  db1 연결: {db1.connection}")
print(f"  db2 연결: {db2.connection}")
print(f"  같은 인스턴스인가? {db1 is db2}")

print()

print("="*70)
print("다양한 OOP 예제 완료!")
print("="*70)
print()
print("💡 객체지향 프로그래밍 디자인 패턴:")
print("   1. 캡슐화: private 변수로 데이터 보호")
print("   2. 클래스 메서드: @classmethod 데코레이터")
print("   3. 정적 메서드: @staticmethod 데코레이터")
print("   4. 프로퍼티: @property 데코레이터")
print("   5. 컨텍스트 매니저: __enter__, __exit__")
print("   6. 매직 메서드: __str__, __len__, __contains__ 등")
print("   7. 메서드 체이닝: self 반환")
print("   8. 싱글톤: __new__ 메서드 활용")
print()
print("💡 OOP Design Patterns:")
print("   1. Encapsulation: Protect data with private variables")
print("   2. Class methods: @classmethod decorator")
print("   3. Static methods: @staticmethod decorator")
print("   4. Properties: @property decorator")
print("   5. Context managers: __enter__, __exit__")
print("   6. Magic methods: __str__, __len__, __contains__, etc.")
print("   7. Method chaining: Return self")
print("   8. Singleton: Use __new__ method")
