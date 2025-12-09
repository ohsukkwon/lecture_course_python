"""
파일명: 03_practice_contact_book.py
설명: 실습 - 딕셔너리를 활용한 연락처 관리 프로그램
Filename: 03_practice_contact_book.py
Description: Practice - Contact book management using dictionaries
"""

print("="*70)
print("연락처 관리 프로그램 (Contact Book Management)")
print("="*70)
print()

# ===== 전역 변수: 연락처 데이터베이스 (Global variable: Contact database) =====
contacts = {}

# ===== 1. 연락처 추가 함수 (Add contact function) =====
def add_contact(name, phone, email="", memo=""):
    """
    새 연락처를 추가합니다 (Add new contact)

    Args:
        name: 이름 (Name)
        phone: 전화번호 (Phone number)
        email: 이메일 (Email, optional)
        memo: 메모 (Memo, optional)
    """
    if name in contacts:
        print(f"❌ '{name}'은(는) 이미 존재하는 연락처입니다.")
        return False

    contacts[name] = {
        "phone": phone,
        "email": email,
        "memo": memo
    }
    print(f"✓ '{name}' 연락처가 추가되었습니다.")
    return True


# ===== 2. 연락처 검색 함수 (Search contact function) =====
def search_contact(name):
    """
    연락처를 검색합니다 (Search for contact)

    Args:
        name: 검색할 이름 (Name to search)
    """
    if name not in contacts:
        print(f"❌ '{name}'을(를) 찾을 수 없습니다.")
        return None

    contact = contacts[name]
    print(f"\n{'='*50}")
    print(f"이름 (Name): {name}")
    print(f"전화번호 (Phone): {contact['phone']}")
    print(f"이메일 (Email): {contact['email'] or '없음'}")
    print(f"메모 (Memo): {contact['memo'] or '없음'}")
    print(f"{'='*50}")
    return contact


# ===== 3. 연락처 수정 함수 (Update contact function) =====
def update_contact(name, phone=None, email=None, memo=None):
    """
    연락처를 수정합니다 (Update contact)

    Args:
        name: 이름 (Name)
        phone: 새 전화번호 (New phone, optional)
        email: 새 이메일 (New email, optional)
        memo: 새 메모 (New memo, optional)
    """
    if name not in contacts:
        print(f"❌ '{name}'을(를) 찾을 수 없습니다.")
        return False

    # None이 아닌 값만 업데이트 (Update only non-None values)
    if phone is not None:
        contacts[name]["phone"] = phone
    if email is not None:
        contacts[name]["email"] = email
    if memo is not None:
        contacts[name]["memo"] = memo

    print(f"✓ '{name}' 연락처가 수정되었습니다.")
    return True


# ===== 4. 연락처 삭제 함수 (Delete contact function) =====
def delete_contact(name):
    """
    연락처를 삭제합니다 (Delete contact)

    Args:
        name: 삭제할 이름 (Name to delete)
    """
    if name not in contacts:
        print(f"❌ '{name}'을(를) 찾을 수 없습니다.")
        return False

    del contacts[name]
    print(f"✓ '{name}' 연락처가 삭제되었습니다.")
    return True


# ===== 5. 모든 연락처 출력 함수 (Print all contacts function) =====
def print_all_contacts():
    """
    모든 연락처를 출력합니다 (Print all contacts)
    """
    if not contacts:
        print("📭 저장된 연락처가 없습니다.")
        return

    print(f"\n{'='*70}")
    print(f"전체 연락처 목록 (Total: {len(contacts)}명)")
    print(f"{'='*70}")

    # 이름순 정렬 (Sort by name)
    for name in sorted(contacts.keys()):
        contact = contacts[name]
        print(f"\n👤 {name}")
        print(f"   📞 전화: {contact['phone']}")
        if contact['email']:
            print(f"   📧 이메일: {contact['email']}")
        if contact['memo']:
            print(f"   📝 메모: {contact['memo']}")

    print(f"\n{'='*70}")


# ===== 6. 이름으로 검색 함수 (Search by name pattern) =====
def search_by_pattern(pattern):
    """
    이름 패턴으로 검색합니다 (Search by name pattern)

    Args:
        pattern: 검색 패턴 (Search pattern)
    """
    results = {name: info for name, info in contacts.items()
               if pattern.lower() in name.lower()}

    if not results:
        print(f"❌ '{pattern}'을(를) 포함하는 연락처가 없습니다.")
        return

    print(f"\n검색 결과 ({len(results)}명):")
    for name in results:
        contact = results[name]
        print(f"  👤 {name}: {contact['phone']}")


# ===== 7. 전화번호로 검색 함수 (Search by phone) =====
def search_by_phone(phone_pattern):
    """
    전화번호로 검색합니다 (Search by phone number)

    Args:
        phone_pattern: 전화번호 패턴 (Phone pattern)
    """
    results = {name: info for name, info in contacts.items()
               if phone_pattern in info['phone']}

    if not results:
        print(f"❌ '{phone_pattern}'을(를) 포함하는 전화번호가 없습니다.")
        return

    print(f"\n검색 결과 ({len(results)}명):")
    for name in results:
        contact = results[name]
        print(f"  👤 {name}: {contact['phone']}")


# ===== 8. 통계 함수 (Statistics function) =====
def show_statistics():
    """
    연락처 통계를 보여줍니다 (Show contact statistics)
    """
    print(f"\n{'='*70}")
    print("📊 연락처 통계 (Contact Statistics)")
    print(f"{'='*70}")

    # 전체 연락처 수 (Total contacts)
    total = len(contacts)
    print(f"전체 연락처: {total}명")

    # 이메일이 있는 연락처 (Contacts with email)
    with_email = sum(1 for c in contacts.values() if c['email'])
    print(f"이메일 등록: {with_email}명 ({with_email/total*100:.1f}%)" if total > 0 else "이메일 등록: 0명")

    # 메모가 있는 연락처 (Contacts with memo)
    with_memo = sum(1 for c in contacts.values() if c['memo'])
    print(f"메모 등록: {with_memo}명 ({with_memo/total*100:.1f}%)" if total > 0 else "메모 등록: 0명")

    # 가장 긴 이름 (Longest name)
    if contacts:
        longest_name = max(contacts.keys(), key=len)
        print(f"가장 긴 이름: {longest_name} ({len(longest_name)}자)")

    print(f"{'='*70}")


# ===== 9. 그룹 관리 기능 (Group management) =====
contact_groups = {
    "가족": set(),
    "친구": set(),
    "직장": set(),
}

def add_to_group(name, group):
    """
    연락처를 그룹에 추가합니다 (Add contact to group)

    Args:
        name: 이름 (Name)
        group: 그룹명 (Group name)
    """
    if name not in contacts:
        print(f"❌ '{name}'을(를) 찾을 수 없습니다.")
        return False

    if group not in contact_groups:
        contact_groups[group] = set()

    contact_groups[group].add(name)
    print(f"✓ '{name}'을(를) '{group}' 그룹에 추가했습니다.")
    return True


def show_group(group):
    """
    특정 그룹의 연락처를 보여줍니다 (Show contacts in a group)

    Args:
        group: 그룹명 (Group name)
    """
    if group not in contact_groups:
        print(f"❌ '{group}' 그룹이 존재하지 않습니다.")
        return

    members = contact_groups[group]
    if not members:
        print(f"'{group}' 그룹에 멤버가 없습니다.")
        return

    print(f"\n{group} 그룹 ({len(members)}명):")
    for name in sorted(members):
        if name in contacts:
            print(f"  👤 {name}: {contacts[name]['phone']}")


def show_all_groups():
    """
    모든 그룹을 보여줍니다 (Show all groups)
    """
    print(f"\n{'='*70}")
    print("📁 그룹 목록 (Groups)")
    print(f"{'='*70}")

    for group, members in contact_groups.items():
        print(f"\n{group} ({len(members)}명)")
        if members:
            for name in sorted(members):
                if name in contacts:
                    print(f"  - {name}")


# ===== 10. 메인 프로그램 - 데모 모드 (Main program - Demo mode) =====
def run_demo():
    """
    데모 모드로 실행합니다 (Run in demo mode)
    """
    print("\n" + "="*70)
    print("📱 데모 모드 시작 (Demo Mode Start)")
    print("="*70)

    # 샘플 데이터 추가 (Add sample data)
    print("\n1️⃣ 연락처 추가 (Adding contacts)")
    print("-"*70)
    add_contact("김철수", "010-1234-5678", "kim@email.com", "대학 동창")
    add_contact("이영희", "010-2345-6789", "lee@email.com", "직장 동료")
    add_contact("박민수", "010-3456-7890", "", "헬스장 친구")
    add_contact("최지연", "010-4567-8901", "choi@email.com", "")
    add_contact("정수진", "010-5678-9012", "jung@email.com", "고등학교 친구")

    input("\n계속하려면 Enter를 누르세요...")

    # 전체 연락처 출력 (Print all contacts)
    print("\n2️⃣ 전체 연락처 보기 (View all contacts)")
    print("-"*70)
    print_all_contacts()

    input("\n계속하려면 Enter를 누르세요...")

    # 연락처 검색 (Search contact)
    print("\n3️⃣ 연락처 검색 (Search contact)")
    print("-"*70)
    search_contact("김철수")

    input("\n계속하려면 Enter를 누르세요...")

    # 이름 패턴 검색 (Search by name pattern)
    print("\n4️⃣ 이름으로 검색 (Search by name)")
    print("-"*70)
    search_by_pattern("이")

    input("\n계속하려면 Enter를 누르세요...")

    # 연락처 수정 (Update contact)
    print("\n5️⃣ 연락처 수정 (Update contact)")
    print("-"*70)
    print("이영희의 메모를 수정합니다...")
    update_contact("이영희", memo="팀장님")
    search_contact("이영희")

    input("\n계속하려면 Enter를 누르세요...")

    # 그룹 관리 (Group management)
    print("\n6️⃣ 그룹 관리 (Group management)")
    print("-"*70)
    add_to_group("김철수", "친구")
    add_to_group("박민수", "친구")
    add_to_group("이영희", "직장")
    add_to_group("최지연", "직장")
    add_to_group("정수진", "친구")

    show_all_groups()

    input("\n계속하려면 Enter를 누르세요...")

    # 특정 그룹 보기 (Show specific group)
    print("\n7️⃣ 특정 그룹 보기 (View specific group)")
    print("-"*70)
    show_group("친구")

    input("\n계속하려면 Enter를 누르세요...")

    # 통계 (Statistics)
    print("\n8️⃣ 통계 보기 (View statistics)")
    print("-"*70)
    show_statistics()

    input("\n계속하려면 Enter를 누르세요...")

    # 연락처 삭제 (Delete contact)
    print("\n9️⃣ 연락처 삭제 (Delete contact)")
    print("-"*70)
    print("박민수 연락처를 삭제합니다...")
    delete_contact("박민수")
    print_all_contacts()

    print("\n" + "="*70)
    print("✅ 데모 모드 완료 (Demo Mode Completed)")
    print("="*70)


# ===== 11. 실전 활용 예제 (Practical examples) =====
def show_practical_examples():
    """
    딕셔너리의 실전 활용 예제를 보여줍니다
    (Show practical dictionary usage examples)
    """
    print("\n" + "="*70)
    print("📚 딕셔너리 실전 활용 예제 (Practical Dictionary Examples)")
    print("="*70)

    # 예제 1: 빈도수 계산 (Frequency count)
    print("\n예제 1: 문자 빈도수 계산 (Character frequency count)")
    text = "hello world"
    freq = {}
    for char in text:
        if char != ' ':  # 공백 제외
            freq[char] = freq.get(char, 0) + 1

    print(f"텍스트: '{text}'")
    print("빈도수:", freq)

    # 예제 2: 데이터 그룹화 (Data grouping)
    print("\n예제 2: 학생 성적 데이터 그룹화 (Group student grades)")
    students = [
        {"name": "철수", "grade": "A"},
        {"name": "영희", "grade": "B"},
        {"name": "민수", "grade": "A"},
        {"name": "지연", "grade": "C"},
        {"name": "수진", "grade": "B"},
    ]

    grade_groups = {}
    for student in students:
        grade = student["grade"]
        if grade not in grade_groups:
            grade_groups[grade] = []
        grade_groups[grade].append(student["name"])

    print("성적별 학생 그룹:")
    for grade, names in sorted(grade_groups.items()):
        print(f"  {grade}등급: {', '.join(names)}")

    # 예제 3: 딕셔너리 컴프리헨션 (Dictionary comprehension)
    print("\n예제 3: 딕셔너리 컴프리헨션 (Dictionary comprehension)")
    numbers = [1, 2, 3, 4, 5]
    squares = {n: n**2 for n in numbers}
    print(f"숫자: {numbers}")
    print(f"제곱: {squares}")

    # 예제 4: 중첩 딕셔너리 (Nested dictionary)
    print("\n예제 4: 중첩 딕셔너리 - 학생 정보 (Nested dict - Student info)")
    students_info = {
        "2024001": {
            "name": "김철수",
            "age": 20,
            "scores": {"math": 95, "english": 88, "science": 92}
        },
        "2024002": {
            "name": "이영희",
            "age": 21,
            "scores": {"math": 88, "english": 95, "science": 90}
        }
    }

    for student_id, info in students_info.items():
        print(f"\n학번: {student_id}")
        print(f"  이름: {info['name']}, 나이: {info['age']}")
        print(f"  성적: {info['scores']}")
        avg_score = sum(info['scores'].values()) / len(info['scores'])
        print(f"  평균: {avg_score:.1f}")


# ===== 메인 실행 (Main execution) =====
if __name__ == "__main__":
    print("="*70)
    print("파이썬 6일차 - 연락처 관리 프로그램")
    print("Python Day 6 - Contact Book Management")
    print("="*70)
    print("\n이 프로그램은 다음 개념을 포함합니다:")
    print("✓ 딕셔너리 CRUD 연산 (Dictionary CRUD operations)")
    print("✓ 딕셔너리 컴프리헨션 (Dictionary comprehension)")
    print("✓ 집합(Set)을 사용한 그룹 관리 (Group management with sets)")
    print("✓ 중첩 딕셔너리 (Nested dictionaries)")
    print("✓ 함수와 딕셔너리의 조합 (Functions with dictionaries)")
    print()

    # 데모 모드 실행 (Run demo mode)
    run_demo()

    # 실전 예제 보기 (Show practical examples)
    show_practical_examples()

    print("\n" + "="*70)
    print("💡 학습 포인트:")
    print("   1. 딕셔너리는 키-값 쌍으로 데이터를 저장합니다")
    print("   2. 딕셔너리는 O(1) 시간에 검색이 가능합니다")
    print("   3. 집합(Set)은 중복을 허용하지 않고 빠른 멤버십 테스트를 제공합니다")
    print("   4. 딕셔너리 컴프리헨션으로 간결한 코드 작성이 가능합니다")
    print("="*70)
    print("\n프로그램 종료 (Program ended)")
