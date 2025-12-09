"""
파일명: 02_set_operations.py
설명: 집합(Set) 완벽 가이드
Filename: 02_set_operations.py
Description: Complete guide to Set operations
"""

print("="*70)
print("집합(Set) 완벽 가이드 (Complete Set Guide)")
print("="*70)
print()

# ===== 1. 집합 생성 (Creating sets) =====
print("="*70)
print("1. 집합 생성 (Creating Sets)")
print("="*70)

# 중괄호로 생성 (Create with curly braces)
fruits = {"apple", "banana", "cherry"}
print(f"과일 집합: {fruits}")

# set() 함수로 생성 (Create with set() function)
numbers = set([1, 2, 3, 4, 5])
print(f"숫자 집합: {numbers}")

# 빈 집합 (Empty set)
empty_set = set()  # 주의: {}는 빈 딕셔너리입니다! (Note: {} is an empty dict!)
print(f"빈 집합: {empty_set}, 타입: {type(empty_set)}")

# 문자열로부터 집합 생성 (Create from string)
letters = set("hello")
print(f"문자 집합: {letters}")  # 중복 제거됨 (duplicates removed)

print()

# ===== 2. 집합의 특징 (Set characteristics) =====
print("="*70)
print("2. 집합의 특징 (Set Characteristics)")
print("="*70)

# 특징 1: 중복 불가 (No duplicates)
numbers = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"중복 제거: {numbers}")

# 특징 2: 순서 없음 (Unordered)
print(f"순서 없음: {fruits}")  # 매번 순서가 다를 수 있음

# 특징 3: 변경 가능 (Mutable)
fruits.add("orange")
print(f"추가 후: {fruits}")

# 특징 4: 인덱싱 불가 (No indexing)
# print(fruits[0])  # ❌ 오류 발생! (Error!)

print()

# ===== 3. 집합 기본 메서드 (Basic set methods) =====
print("="*70)
print("3. 집합 기본 메서드 (Basic Set Methods)")
print("="*70)

fruits = {"apple", "banana", "cherry"}

# add() - 원소 추가 (Add element)
fruits.add("orange")
print(f"add('orange'): {fruits}")

# remove() - 원소 제거 (Remove element, raises error if not found)
fruits.remove("banana")
print(f"remove('banana'): {fruits}")

# discard() - 원소 제거 (Remove element, no error if not found)
fruits.discard("grape")  # 없어도 오류 안남 (No error even if not exists)
print(f"discard('grape'): {fruits}")

# pop() - 임의의 원소 제거 및 반환 (Remove and return arbitrary element)
removed = fruits.pop()
print(f"pop(): {removed}, 남은 집합: {fruits}")

# clear() - 모든 원소 제거 (Remove all elements)
temp_set = {1, 2, 3}
temp_set.clear()
print(f"clear(): {temp_set}")

# copy() - 집합 복사 (Copy set)
fruits = {"apple", "banana", "cherry"}
fruits_copy = fruits.copy()
print(f"copy(): {fruits_copy}")

print()

# ===== 4. 집합 연산 - 합집합 (Union) =====
print("="*70)
print("4. 합집합 (Union)")
print("="*70)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# | 연산자 (| operator)
union1 = set1 | set2
print(f"{set1} | {set2}")
print(f"결과: {union1}")

# union() 메서드 (union() method)
union2 = set1.union(set2)
print(f"set1.union(set2): {union2}")

# 여러 집합의 합집합 (Union of multiple sets)
set3 = {8, 9, 10}
union3 = set1 | set2 | set3
print(f"set1 | set2 | set3: {union3}")

print()

# ===== 5. 집합 연산 - 교집합 (Intersection) =====
print("="*70)
print("5. 교집합 (Intersection)")
print("="*70)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# & 연산자 (& operator)
intersection1 = set1 & set2
print(f"{set1} & {set2}")
print(f"결과: {intersection1}")

# intersection() 메서드 (intersection() method)
intersection2 = set1.intersection(set2)
print(f"set1.intersection(set2): {intersection2}")

# 여러 집합의 교집합 (Intersection of multiple sets)
set3 = {4, 5, 9, 10}
intersection3 = set1 & set2 & set3
print(f"set1 & set2 & set3: {intersection3}")

print()

# ===== 6. 집합 연산 - 차집합 (Difference) =====
print("="*70)
print("6. 차집합 (Difference)")
print("="*70)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# - 연산자 (- operator)
difference1 = set1 - set2
print(f"{set1} - {set2}")
print(f"결과 (set1에만 있는 원소): {difference1}")

# difference() 메서드 (difference() method)
difference2 = set2.difference(set1)
print(f"set2.difference(set1): {difference2}")
print(f"결과 (set2에만 있는 원소): {difference2}")

print()

# ===== 7. 집합 연산 - 대칭 차집합 (Symmetric Difference) =====
print("="*70)
print("7. 대칭 차집합 (Symmetric Difference)")
print("="*70)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# ^ 연산자 (^ operator)
sym_diff1 = set1 ^ set2
print(f"{set1} ^ {set2}")
print(f"결과 (둘 중 하나에만 있는 원소): {sym_diff1}")

# symmetric_difference() 메서드 (symmetric_difference() method)
sym_diff2 = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2): {sym_diff2}")

print()

# ===== 8. 부분집합과 상위집합 (Subset and Superset) =====
print("="*70)
print("8. 부분집합과 상위집합 (Subset & Superset)")
print("="*70)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# issubset() - 부분집합 확인 (Check if subset)
print(f"{set1}이(가) {set2}의 부분집합인가?")
print(f"set1.issubset(set2): {set1.issubset(set2)}")
print(f"set1 <= set2: {set1 <= set2}")

# issuperset() - 상위집합 확인 (Check if superset)
print(f"\n{set2}이(가) {set1}의 상위집합인가?")
print(f"set2.issuperset(set1): {set2.issuperset(set1)}")
print(f"set2 >= set1: {set2 >= set1}")

# 진부분집합 (Proper subset)
print(f"\n{set1}이(가) {set2}의 진부분집합인가?")
print(f"set1 < set2: {set1 < set2}")

print()

# ===== 9. 집합 비교 (Set comparison) =====
print("="*70)
print("9. 집합 비교 (Set Comparison)")
print("="*70)

set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {3, 2, 1}  # 순서 다름 (Different order)
set4 = {1, 2, 4}

# 같은지 확인 (Check equality)
print(f"{set1} == {set2}: {set1 == set2}")
print(f"{set1} == {set3}: {set1 == set3}")  # 순서 무관 (Order doesn't matter)
print(f"{set1} == {set4}: {set1 == set4}")

# 다른지 확인 (Check inequality)
print(f"{set1} != {set4}: {set1 != set4}")

# isdisjoint() - 교집합이 없는지 확인 (Check if no intersection)
set5 = {4, 5, 6}
print(f"\n{set1}과 {set5}가 서로소인가?")
print(f"set1.isdisjoint(set5): {set1.isdisjoint(set5)}")

print()

# ===== 10. 집합 수정 메서드 (In-place modification methods) =====
print("="*70)
print("10. 집합 수정 메서드 (In-place Modification)")
print("="*70)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# update() - 합집합으로 수정 (Update with union)
set1_copy = set1.copy()
set1_copy.update(set2)
print(f"update: {set1} + {set2} = {set1_copy}")

# intersection_update() - 교집합으로 수정 (Update with intersection)
set1_copy = set1.copy()
set1_copy.intersection_update(set2)
print(f"intersection_update: {set1} & {set2} = {set1_copy}")

# difference_update() - 차집합으로 수정 (Update with difference)
set1_copy = set1.copy()
set1_copy.difference_update(set2)
print(f"difference_update: {set1} - {set2} = {set1_copy}")

# symmetric_difference_update() - 대칭 차집합으로 수정
set1_copy = set1.copy()
set1_copy.symmetric_difference_update(set2)
print(f"symmetric_difference_update: {set1} ^ {set2} = {set1_copy}")

print()

# ===== 11. 실전 예제 - 중복 제거 (Remove duplicates) =====
print("="*70)
print("11. 실전 예제 - 중복 제거 (Practical: Remove Duplicates)")
print("="*70)

# 리스트의 중복 제거 (Remove duplicates from list)
numbers = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers))
print(f"원본: {numbers}")
print(f"중복 제거: {unique_numbers}")

# 문자열의 중복 문자 제거 (Remove duplicate characters)
text = "hello world"
unique_chars = set(text)
print(f"\n원본 문자열: '{text}'")
print(f"고유 문자: {unique_chars}")

print()

# ===== 12. 실전 예제 - 멤버십 테스트 (Membership test) =====
print("="*70)
print("12. 실전 예제 - 멤버십 테스트 (Practical: Membership Test)")
print("="*70)

# 빠른 검색을 위해 집합 사용 (Use set for fast lookup)
allowed_users = {"alice", "bob", "charlie", "david"}

# O(1) 시간 복잡도 (O(1) time complexity)
user = "alice"
if user in allowed_users:
    print(f"✓ {user}는 허용된 사용자입니다.")

user = "eve"
if user not in allowed_users:
    print(f"✗ {user}는 허용되지 않은 사용자입니다.")

print()

# ===== 13. 실전 예제 - 공통 요소 찾기 (Find common elements) =====
print("="*70)
print("13. 실전 예제 - 공통 요소 찾기 (Find Common Elements)")
print("="*70)

# 여러 학생이 수강하는 과목 (Courses taken by students)
student1_courses = {"Math", "Physics", "Chemistry", "English"}
student2_courses = {"Math", "Biology", "English", "History"}
student3_courses = {"Math", "Physics", "English", "Art"}

# 모든 학생이 공통으로 듣는 과목 (Courses all students take)
common_courses = student1_courses & student2_courses & student3_courses
print("모든 학생이 공통으로 듣는 과목:")
print(common_courses)

# 적어도 한 학생이 듣는 모든 과목 (All courses taken by at least one student)
all_courses = student1_courses | student2_courses | student3_courses
print("\n개설된 모든 과목:")
print(all_courses)

# 한 명만 듣는 과목 (Courses taken by only one student)
unique_to_student1 = student1_courses - student2_courses - student3_courses
print(f"\n학생1만 듣는 과목: {unique_to_student1}")

print()

# ===== 14. 실전 예제 - 태그 시스템 (Tag system) =====
print("="*70)
print("14. 실전 예제 - 태그 시스템 (Tag System)")
print("="*70)

# 블로그 포스트의 태그 (Blog post tags)
post1_tags = {"python", "programming", "tutorial", "beginner"}
post2_tags = {"python", "data-science", "pandas", "tutorial"}
post3_tags = {"javascript", "web", "frontend", "tutorial"}

# python 태그가 있는 포스트 찾기 (Find posts with python tag)
print("'python' 태그가 있는 포스트:")
if "python" in post1_tags:
    print("  - Post 1")
if "python" in post2_tags:
    print("  - Post 2")

# 공통 태그 찾기 (Find common tags)
common_tags = post1_tags & post2_tags & post3_tags
print(f"\n모든 포스트의 공통 태그: {common_tags}")

# 관련 포스트 찾기 (Find related posts)
related_tags = post1_tags & post2_tags
print(f"\nPost 1과 Post 2의 관련 태그: {related_tags}")

print()

# ===== 15. frozenset - 불변 집합 (Immutable set) =====
print("="*70)
print("15. frozenset - 불변 집합 (Immutable Set)")
print("="*70)

# frozenset 생성 (Create frozenset)
frozen = frozenset([1, 2, 3, 4, 5])
print(f"frozenset: {frozen}")

# 수정 불가 (Cannot modify)
# frozen.add(6)  # ❌ 오류 발생! (Error!)

# 딕셔너리의 키로 사용 가능 (Can be used as dict key)
set_dict = {
    frozenset([1, 2]): "첫 번째",
    frozenset([3, 4]): "두 번째"
}
print(f"frozenset을 키로 사용: {set_dict}")

# 집합의 원소로 사용 가능 (Can be element of set)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"집합의 집합: {set_of_sets}")

print()

print("="*70)
print("집합(Set) 완벽 가이드 완료!")
print("="*70)
print()
print("💡 집합 사용 시기:")
print("   1. 중복을 제거해야 할 때")
print("   2. 빠른 멤버십 테스트가 필요할 때 (O(1) 시간)")
print("   3. 수학적 집합 연산이 필요할 때")
print("   4. 순서가 중요하지 않을 때")
print()
print("💡 When to use sets:")
print("   1. When you need to remove duplicates")
print("   2. When you need fast membership testing (O(1) time)")
print("   3. When you need mathematical set operations")
print("   4. When order doesn't matter")
