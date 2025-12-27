"""
파일명: 03_tuple_basics.py
설명: 튜플 기초 - 불변 자료구조의 이해와 활용
Filename: 03_tuple_basics.py
Description: Tuple basics - Understanding and using immutable data structures
"""

print("="*70)
print("튜플(Tuple) 기초 (Tuple Basics)")
print("="*70)
print()

# ===== 1. 튜플 생성 (Creating Tuples) =====
print("1. 튜플 생성 (Creating Tuples)")
print("-"*70)

# 빈 튜플 (Empty tuple)
empty_tuple = ()
empty_tuple2 = tuple()
print(f"빈 튜플: {empty_tuple}, 타입: {type(empty_tuple)}")

# 요소가 있는 튜플 (Tuple with elements)
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "Hello", 3.14, True)
print(f"\n숫자 튜플: {numbers}")
print(f"과일 튜플: {fruits}")
print(f"혼합 튜플: {mixed}")

# 단일 요소 튜플 - 쉼표 필수! (Single element tuple - comma required!)
single = (1,)  # 튜플 (Tuple)
not_tuple = (1)  # 정수 (Integer)
print(f"\n단일 요소 튜플: {single}, 타입: {type(single)}")
print(f"괄호만 사용: {not_tuple}, 타입: {type(not_tuple)}")

# 괄호 생략 가능 (Parentheses optional)
coordinates = 10, 20, 30
print(f"괄호 생략: {coordinates}, 타입: {type(coordinates)}")

print()
print("="*70)
print()

# ===== 2. 튜플의 불변성 (Tuple Immutability) =====
print("2. 튜플의 불변성 (Tuple Immutability)")
print("-"*70)

my_tuple = (1, 2, 3, 4, 5)
print(f"원본 튜플: {my_tuple}")

# 튜플은 변경할 수 없습니다 (Tuples are immutable)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"\n❌ 오류 발생: {e}")
    print("   튜플의 요소는 수정할 수 없습니다!")
    print("   (Tuple elements cannot be modified!)")

# 리스트와 비교 (Comparison with list)
my_list = [1, 2, 3, 4, 5]
print(f"\n리스트: {my_list}")
my_list[0] = 10
print(f"수정 후 리스트: {my_list} ✓")

print()
print("="*70)
print()

# ===== 3. 튜플 인덱싱과 슬라이싱 (Tuple Indexing and Slicing) =====
print("3. 튜플 인덱싱과 슬라이싱 (Tuple Indexing and Slicing)")
print("-"*70)

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"과일 튜플: {fruits}")

# 인덱싱 (Indexing)
print(f"\n첫 번째 요소 [0]: {fruits[0]}")
print(f"세 번째 요소 [2]: {fruits[2]}")
print(f"마지막 요소 [-1]: {fruits[-1]}")
print(f"뒤에서 두 번째 [-2]: {fruits[-2]}")

# 슬라이싱 (Slicing)
print(f"\n처음부터 3개 [:3]: {fruits[:3]}")
print(f"2번째부터 끝까지 [2:]: {fruits[2:]}")
print(f"2번째부터 4번째까지 [1:4]: {fruits[1:4]}")
print(f"2칸씩 건너뛰기 [::2]: {fruits[::2]}")
print(f"역순 [::-1]: {fruits[::-1]}")

print()
print("="*70)
print()

# ===== 4. 튜플 메서드 (Tuple Methods) =====
print("4. 튜플 메서드 (Tuple Methods)")
print("-"*70)

numbers = (1, 2, 3, 2, 2, 4, 5, 2)
print(f"숫자 튜플: {numbers}")

# count() - 특정 값의 개수 세기 (Count occurrences)
count_2 = numbers.count(2)
print(f"\n2의 개수: {count_2}개")

# index() - 특정 값의 인덱스 찾기 (Find index)
index_4 = numbers.index(4)
print(f"4의 인덱스: {index_4}")

# 첫 번째 2의 인덱스 (Index of first 2)
first_2 = numbers.index(2)
print(f"첫 번째 2의 인덱스: {first_2}")

print()
print("="*70)
print()

# ===== 5. 튜플 패킹과 언패킹 (Tuple Packing and Unpacking) =====
print("5. 튜플 패킹과 언패킹 (Tuple Packing and Unpacking)")
print("-"*70)

# 패킹 (Packing) - 여러 값을 하나의 튜플로
point = (10, 20)
print(f"패킹된 좌표: {point}")

person = "김철수", 25, "서울"  # 괄호 생략 가능
print(f"패킹된 정보: {person}")

# 언패킹 (Unpacking) - 튜플을 여러 변수로
x, y = point
print(f"\n언패킹: x = {x}, y = {y}")

name, age, city = person
print(f"언패킹: 이름 = {name}, 나이 = {age}, 도시 = {city}")

# 스왑 (Swap) - 두 변수 값 교환
a, b = 10, 20
print(f"\n교환 전: a = {a}, b = {b}")
a, b = b, a  # 튜플 언패킹을 이용한 스왑
print(f"교환 후: a = {a}, b = {b}")

# 확장 언패킹 (Extended unpacking) - *를 사용
first, *middle, last = (1, 2, 3, 4, 5, 6)
print(f"\nfirst = {first}, middle = {middle}, last = {last}")

print()
print("="*70)
print()

# ===== 6. 여러 값 반환 (Returning Multiple Values) =====
print("6. 함수에서 여러 값 반환 (Returning Multiple Values from Function)")
print("-"*70)

def get_user_info():
    """사용자 정보를 튜플로 반환 (Return user info as tuple)"""
    name = "이영희"
    age = 28
    city = "부산"
    return name, age, city  # 튜플로 반환 (Return as tuple)

def calculate_stats(numbers):
    """통계 정보를 튜플로 반환 (Return statistics as tuple)"""
    total = sum(numbers)
    avg = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, avg, minimum, maximum

# 여러 값 받기 (Receive multiple values)
user_name, user_age, user_city = get_user_info()
print(f"이름: {user_name}, 나이: {user_age}, 도시: {user_city}")

numbers = [85, 92, 78, 95, 88]
total, avg, min_val, max_val = calculate_stats(numbers)
print(f"\n통계: 합계={total}, 평균={avg:.1f}, 최소={min_val}, 최대={max_val}")

print()
print("="*70)
print()

# ===== 7. 튜플의 활용 (Using Tuples) =====
print("7. 튜플의 활용 사례 (Use Cases for Tuples)")
print("-"*70)

# 1) 좌표 표현 (Coordinates)
point_2d = (10, 20)
point_3d = (10, 20, 30)
print(f"2D 좌표: {point_2d}")
print(f"3D 좌표: {point_3d}")

# 2) RGB 색상 (RGB colors)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
print(f"\nRGB 빨강: {red}")
print(f"RGB 초록: {green}")
print(f"RGB 파랑: {blue}")

# 3) 날짜와 시간 (Date and time)
date = (2024, 1, 15)
time = (14, 30, 0)
print(f"\n날짜 (YYYY, MM, DD): {date}")
print(f"시간 (HH, MM, SS): {time}")

# 4) 딕셔너리의 키로 사용 (As dictionary keys)
locations = {
    (0, 0): "원점 (Origin)",
    (10, 20): "A 지점 (Point A)",
    (30, 40): "B 지점 (Point B)"
}
print(f"\n위치 정보:")
for coord, name in locations.items():
    print(f"  {coord}: {name}")

# 리스트는 딕셔너리 키로 사용 불가 (Lists cannot be dictionary keys)
try:
    invalid_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"\n❌ 리스트를 키로 사용 시: {e}")

print()
print("="*70)
print()

# ===== 8. 튜플 vs 리스트 비교 (Tuple vs List Comparison) =====
print("8. 튜플 vs 리스트 비교 (Tuple vs List Comparison)")
print("-"*70)

print("┌" + "─"*68 + "┐")
print(f"│ {'특징 (Feature)':<20} │ {'튜플 (Tuple)':<20} │ {'리스트 (List)':<20} │")
print("├" + "─"*68 + "┤")
print(f"│ {'가변성 (Mutability)':<20} │ {'불변 (Immutable)':<20} │ {'가변 (Mutable)':<20} │")
print(f"│ {'표기법 (Notation)':<20} │ {'(1, 2, 3)':<20} │ {'[1, 2, 3]':<20} │")
print(f"│ {'속도 (Speed)':<20} │ {'빠름 (Fast)':<20} │ {'느림 (Slower)':<20} │")
print(f"│ {'메모리 (Memory)':<20} │ {'적음 (Less)':<20} │ {'많음 (More)':<20} │")
print(f"│ {'메서드 (Methods)':<20} │ {'2개 (count,index)':<20} │ {'많음 (Many)':<20} │")
print(f"│ {'딕셔너리 키':<20} │ {'가능 (Possible)':<20} │ {'불가 (Impossible)':<20} │")
print("└" + "─"*68 + "┘")

print("\n언제 사용하나요? (When to use?)")
print("• 튜플: 데이터가 변경되지 않아야 할 때, 딕셔너리 키로 사용")
print("  (Tuple: When data shouldn't change, or as dictionary keys)")
print("• 리스트: 데이터를 자주 수정해야 할 때")
print("  (List: When data needs frequent modifications)")

print()
print("="*70)
print()

# ===== 9. 튜플 연산 (Tuple Operations) =====
print("9. 튜플 연산 (Tuple Operations)")
print("-"*70)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# 연결 (Concatenation)
combined = tuple1 + tuple2
print(f"연결: {tuple1} + {tuple2} = {combined}")

# 반복 (Repetition)
repeated = tuple1 * 3
print(f"반복: {tuple1} * 3 = {repeated}")

# 멤버십 (Membership)
print(f"\n2 in {tuple1}: {2 in tuple1}")
print(f"10 in {tuple1}: {10 in tuple1}")

# 길이 (Length)
print(f"\n튜플 길이: {len(tuple1)}")

# 최댓값, 최솟값, 합계 (Max, min, sum)
numbers = (10, 5, 8, 15, 3, 12)
print(f"\n숫자 튜플: {numbers}")
print(f"최댓값: {max(numbers)}")
print(f"최솟값: {min(numbers)}")
print(f"합계: {sum(numbers)}")

print()
print("="*70)
print()

# ===== 10. 실전 예제: 학생 정보 관리 (Practical Example: Student Info) =====
print("10. 실전 예제: 학생 정보 관리 (Practical Example: Student Info)")
print("-"*70)

# 학생 정보를 튜플로 저장 (불변 정보)
# Store student info as tuples (immutable data)
student1 = ("김철수", 20241001, "컴퓨터공학", 2024)
student2 = ("이영희", 20241002, "경영학", 2024)
student3 = ("박민수", 20241003, "전자공학", 2024)

# 학생 목록 (리스트 안에 튜플)
# Student list (tuples inside a list)
students = [student1, student2, student3]

print("학생 정보 목록:")
print("="*70)
for student in students:
    name, student_id, major, year = student
    print(f"이름: {name:<10} | 학번: {student_id} | 전공: {major:<15} | 학년: {year}")

# 특정 학생 검색 (Search for specific student)
search_id = 20241002
print(f"\n학번 {search_id} 검색:")
for student in students:
    if student[1] == search_id:
        print(f"찾음: {student[0]}, 전공: {student[2]}")
        break

print()
print("="*70)
print()

# ===== 11. 네임드 튜플 소개 (Named Tuple Introduction) =====
print("11. 네임드 튜플 소개 (Named Tuple Introduction)")
print("-"*70)

from collections import namedtuple

# 네임드 튜플 정의 (Define named tuple)
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# 생성 (Create)
p1 = Point(10, 20)
person1 = Person("김철수", 25, "서울")

# 접근 (Access)
print(f"좌표: x={p1.x}, y={p1.y}")
print(f"사람: 이름={person1.name}, 나이={person1.age}, 도시={person1.city}")

# 인덱스로도 접근 가능 (Also accessible by index)
print(f"\n인덱스 접근: {p1[0]}, {p1[1]}")
print(f"이름 접근: {person1.name}")

print()
print("="*70)
print("\n튜플 학습 완료! (Tuple learning completed!)")
print("="*70)
