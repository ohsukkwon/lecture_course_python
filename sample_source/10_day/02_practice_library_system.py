"""
파일명: 02_practice_library_system.py
설명: 실습 - 도서관 관리 시스템 (객체지향 프로그래밍)
Filename: 02_practice_library_system.py
Description: Practice - Library management system using OOP
"""

from datetime import datetime, timedelta

print("="*70)
print("도서관 관리 시스템 (Library Management System)")
print("="*70)
print()

# ===== 1. Book 클래스 (Book class) =====
class Book:
    """도서 클래스"""

    def __init__(self, book_id, title, author, isbn, category="일반"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.is_borrowed = False
        self.borrower = None
        self.due_date = None

    def borrow(self, member_name):
        """도서 대출"""
        if self.is_borrowed:
            return False, f"'{self.title}'은(는) 이미 대출 중입니다"

        self.is_borrowed = True
        self.borrower = member_name
        self.due_date = datetime.now() + timedelta(days=14)  # 2주 대출
        return True, f"'{self.title}' 대출 성공. 반납일: {self.due_date.strftime('%Y-%m-%d')}"

    def return_book(self):
        """도서 반납"""
        if not self.is_borrowed:
            return False, f"'{self.title}'은(는) 대출 중이 아닙니다"

        borrower_name = self.borrower
        self.is_borrowed = False
        self.borrower = None
        self.due_date = None
        return True, f"'{self.title}' 반납 완료 (대출자: {borrower_name})"

    def is_overdue(self):
        """연체 여부 확인"""
        if not self.is_borrowed:
            return False
        return datetime.now() > self.due_date

    def get_info(self):
        """도서 정보 반환"""
        status = "대출 가능" if not self.is_borrowed else f"대출 중 ({self.borrower})"
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'category': self.category,
            'status': status
        }

    def __str__(self):
        status = "📗" if not self.is_borrowed else "📕"
        return f"{status} [{self.book_id}] {self.title} - {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"


# ===== 2. Member 클래스 (Member class) =====
class Member:
    """회원 클래스"""

    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []  # 대출한 도서 목록
        self.borrow_history = []  # 대출 이력

    def can_borrow(self, max_books=3):
        """대출 가능 여부 확인"""
        return len(self.borrowed_books) < max_books

    def borrow_book(self, book):
        """도서 대출"""
        if not self.can_borrow():
            return False, f"{self.name}님은 최대 대출 권수(3권)를 초과했습니다"

        success, message = book.borrow(self.name)
        if success:
            self.borrowed_books.append(book)
            self.borrow_history.append({
                'book': book.title,
                'borrow_date': datetime.now(),
                'action': 'borrow'
            })

        return success, message

    def return_book(self, book):
        """도서 반납"""
        if book not in self.borrowed_books:
            return False, f"{self.name}님이 대출한 도서가 아닙니다"

        success, message = book.return_book()
        if success:
            self.borrowed_books.remove(book)
            self.borrow_history.append({
                'book': book.title,
                'return_date': datetime.now(),
                'action': 'return'
            })

        return success, message

    def get_borrowed_books(self):
        """대출 중인 도서 목록"""
        return self.borrowed_books

    def get_overdue_books(self):
        """연체 도서 목록"""
        return [book for book in self.borrowed_books if book.is_overdue()]

    def __str__(self):
        return f"👤 {self.name} (ID: {self.member_id}) - 대출: {len(self.borrowed_books)}권"


# ===== 3. Library 클래스 (Library class) =====
class Library:
    """도서관 클래스"""

    def __init__(self, name):
        self.name = name
        self.books = []  # 도서 목록
        self.members = []  # 회원 목록

    def add_book(self, book):
        """도서 추가"""
        self.books.append(book)
        return f"✓ 도서 추가: {book.title}"

    def add_member(self, member):
        """회원 추가"""
        self.members.append(member)
        return f"✓ 회원 추가: {member.name}"

    def find_book_by_id(self, book_id):
        """ID로 도서 찾기"""
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def find_member_by_id(self, member_id):
        """ID로 회원 찾기"""
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def search_books(self, keyword):
        """도서 검색 (제목 또는 저자)"""
        results = [book for book in self.books
                   if keyword.lower() in book.title.lower()
                   or keyword.lower() in book.author.lower()]
        return results

    def get_available_books(self):
        """대출 가능한 도서 목록"""
        return [book for book in self.books if not book.is_borrowed]

    def get_borrowed_books(self):
        """대출 중인 도서 목록"""
        return [book for book in self.books if book.is_borrowed]

    def get_overdue_books(self):
        """연체 도서 목록"""
        return [book for book in self.books if book.is_overdue()]

    def get_statistics(self):
        """통계 정보"""
        total_books = len(self.books)
        available_books = len(self.get_available_books())
        borrowed_books = len(self.get_borrowed_books())
        overdue_books = len(self.get_overdue_books())

        return {
            'total_books': total_books,
            'available_books': available_books,
            'borrowed_books': borrowed_books,
            'overdue_books': overdue_books,
            'total_members': len(self.members)
        }

    def print_catalog(self):
        """도서 목록 출력"""
        print(f"\n{'='*70}")
        print(f"📚 {self.name} 도서 목록 (총 {len(self.books)}권)")
        print(f"{'='*70}")

        if not self.books:
            print("도서가 없습니다.")
            return

        for book in self.books:
            print(f"  {book}")

        print(f"{'='*70}")

    def print_members(self):
        """회원 목록 출력"""
        print(f"\n{'='*70}")
        print(f"👥 {self.name} 회원 목록 (총 {len(self.members)}명)")
        print(f"{'='*70}")

        if not self.members:
            print("회원이 없습니다.")
            return

        for member in self.members:
            print(f"  {member}")

        print(f"{'='*70}")


# ===== 데모 실행 (Demo execution) =====
def run_demo():
    """데모 모드로 실행"""
    print("\n" + "="*70)
    print("📚 도서관 관리 시스템 데모")
    print("="*70)

    # 도서관 생성 (Create library)
    library = Library("중앙 도서관")

    # 도서 추가 (Add books)
    print("\n1️⃣ 도서 추가하기")
    print("-"*70)

    books = [
        Book("B001", "파이썬 입문", "김코딩", "978-1-234567-01-0", "프로그래밍"),
        Book("B002", "데이터 과학 기초", "이데이터", "978-1-234567-02-0", "데이터 과학"),
        Book("B003", "웹 개발 완벽 가이드", "박웹", "978-1-234567-03-0", "웹 개발"),
        Book("B004", "알고리즘 정복", "최알고", "978-1-234567-04-0", "알고리즘"),
        Book("B005", "파이썬 고급", "김코딩", "978-1-234567-05-0", "프로그래밍"),
    ]

    for book in books:
        print(f"  {library.add_book(book)}")

    input("\n계속하려면 Enter를 누르세요...")

    # 회원 추가 (Add members)
    print("\n2️⃣ 회원 추가하기")
    print("-"*70)

    members = [
        Member("M001", "홍길동", "hong@example.com", "010-1234-5678"),
        Member("M002", "김철수", "kim@example.com", "010-2345-6789"),
        Member("M003", "이영희", "lee@example.com", "010-3456-7890"),
    ]

    for member in members:
        print(f"  {library.add_member(member)}")

    input("\n계속하려면 Enter를 누르세요...")

    # 도서 목록 보기 (View books)
    print("\n3️⃣ 도서 목록 보기")
    print("-"*70)
    library.print_catalog()

    input("\n계속하려면 Enter를 누르세요...")

    # 도서 대출 (Borrow books)
    print("\n4️⃣ 도서 대출하기")
    print("-"*70)

    # 홍길동이 2권 대출
    member1 = library.find_member_by_id("M001")
    book1 = library.find_book_by_id("B001")
    book2 = library.find_book_by_id("B002")

    success, message = member1.borrow_book(book1)
    print(f"  {message}")

    success, message = member1.borrow_book(book2)
    print(f"  {message}")

    # 김철수가 1권 대출
    member2 = library.find_member_by_id("M002")
    book3 = library.find_book_by_id("B003")

    success, message = member2.borrow_book(book3)
    print(f"  {message}")

    input("\n계속하려면 Enter를 누르세요...")

    # 대출 후 도서 목록 (Books after borrowing)
    print("\n5️⃣ 대출 후 도서 목록")
    print("-"*70)
    library.print_catalog()

    input("\n계속하려면 Enter를 누르세요...")

    # 회원별 대출 현황 (Member borrowing status)
    print("\n6️⃣ 회원별 대출 현황")
    print("-"*70)
    library.print_members()

    print(f"\n{member1.name}님이 대출한 도서:")
    for book in member1.get_borrowed_books():
        print(f"  - {book.title} (반납일: {book.due_date.strftime('%Y-%m-%d')})")

    input("\n계속하려면 Enter를 누르세요...")

    # 도서 검색 (Search books)
    print("\n7️⃣ 도서 검색 (키워드: '파이썬')")
    print("-"*70)

    results = library.search_books("파이썬")
    print(f"검색 결과: {len(results)}권")
    for book in results:
        print(f"  {book}")

    input("\n계속하려면 Enter를 누르세요...")

    # 도서 반납 (Return books)
    print("\n8️⃣ 도서 반납하기")
    print("-"*70)

    success, message = member1.return_book(book1)
    print(f"  {message}")

    input("\n계속하려면 Enter를 누르세요...")

    # 통계 (Statistics)
    print("\n9️⃣ 도서관 통계")
    print("-"*70)

    stats = library.get_statistics()
    print(f"  총 도서 수: {stats['total_books']}권")
    print(f"  대출 가능: {stats['available_books']}권")
    print(f"  대출 중: {stats['borrowed_books']}권")
    print(f"  연체: {stats['overdue_books']}권")
    print(f"  총 회원 수: {stats['total_members']}명")

    print("\n" + "="*70)
    print("✅ 데모 완료")
    print("="*70)


# ===== 고급 기능 예제 (Advanced features) =====
print("="*70)
print("📚 고급 기능 - 도서 카테고리별 통계")
print("="*70)
print()

class LibraryAdvanced(Library):
    """고급 기능이 추가된 도서관 클래스"""

    def get_books_by_category(self, category):
        """카테고리별 도서 목록"""
        return [book for book in self.books if book.category == category]

    def get_category_statistics(self):
        """카테고리별 통계"""
        from collections import Counter
        categories = [book.category for book in self.books]
        return Counter(categories)

    def get_most_popular_author(self):
        """가장 많은 도서를 보유한 저자"""
        from collections import Counter
        authors = [book.author for book in self.books]
        counter = Counter(authors)
        if counter:
            return counter.most_common(1)[0]
        return None, 0

# 예제 (Example)
library_adv = LibraryAdvanced("고급 도서관")

# 도서 추가
books = [
    Book("B001", "파이썬 기초", "김코딩", "978-1-234567-01-0", "프로그래밍"),
    Book("B002", "파이썬 고급", "김코딩", "978-1-234567-02-0", "프로그래밍"),
    Book("B003", "자바 입문", "이자바", "978-1-234567-03-0", "프로그래밍"),
    Book("B004", "데이터베이스", "박디비", "978-1-234567-04-0", "데이터베이스"),
    Book("B005", "네트워크", "최네트", "978-1-234567-05-0", "네트워크"),
]

for book in books:
    library_adv.add_book(book)

# 카테고리별 통계
print("📊 카테고리별 통계:")
cat_stats = library_adv.get_category_statistics()
for category, count in cat_stats.items():
    print(f"  {category}: {count}권")

# 가장 인기 있는 저자
author, count = library_adv.get_most_popular_author()
print(f"\n👨\u200d💻 가장 많은 도서를 보유한 저자: {author} ({count}권)")

print()

# ===== 메인 실행 (Main execution) =====
if __name__ == "__main__":
    print("="*70)
    print("파이썬 10일차 - 도서관 관리 시스템")
    print("Python Day 10 - Library Management System")
    print("="*70)
    print("\n이 프로그램은 다음 개념을 포함합니다:")
    print("✓ 클래스와 객체 (Classes and objects)")
    print("✓ 생성자와 속성 (Constructor and attributes)")
    print("✓ 메서드 (Methods)")
    print("✓ 클래스 간 관계 (Relationships between classes)")
    print("✓ 캡슐화 (Encapsulation)")
    print("✓ 매직 메서드 (__str__, __repr__)")
    print()

    # 데모 실행
    run_demo()

    print("\n" + "="*70)
    print("💡 객체지향 프로그래밍 핵심 개념:")
    print("   1. 클래스: 객체의 설계도")
    print("   2. 객체: 클래스의 인스턴스")
    print("   3. 속성: 객체의 데이터")
    print("   4. 메서드: 객체의 동작")
    print("   5. 캡슐화: 데이터와 메서드를 하나로 묶기")
    print("="*70)
    print("\n프로그램 종료 (Program ended)")
