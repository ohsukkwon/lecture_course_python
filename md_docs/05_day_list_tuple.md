# 5일차: 자료구조 I - 리스트와 튜플

## 학습 목표
- 리스트의 생성과 접근 방법
- 리스트 메서드 활용
- 리스트 컴프리헨션 마스터
- 튜플의 특징과 활용
- 리스트 vs 튜플 비교

---

## 1. 리스트 (List)

### 1.1 리스트 생성

```python
# 빈 리스트
empty_list = []
empty_list = list()

# 요소가 있는 리스트
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "Hello", 3.14, True]

# 중첩 리스트 (2차원)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### 1.2 리스트 인덱싱과 슬라이싱

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# 인덱싱
print(fruits[0])   # apple
print(fruits[-1])  # elderberry

# 슬라이싱
print(fruits[1:4])   # ['banana', 'cherry', 'date']
print(fruits[:3])    # ['apple', 'banana', 'cherry']
print(fruits[2:])    # ['cherry', 'date', 'elderberry']
print(fruits[::2])   # ['apple', 'cherry', 'elderberry']
print(fruits[::-1])  # 역순
```

### 1.3 리스트 메서드

```python
fruits = ["apple", "banana"]

# 추가
fruits.append("cherry")  # 끝에 추가
fruits.insert(1, "grape")  # 특정 위치에 추가
fruits.extend(["mango", "orange"])  # 여러 요소 추가

# 삭제
fruits.remove("banana")  # 값으로 삭제
popped = fruits.pop()  # 마지막 요소 제거 및 반환
popped = fruits.pop(0)  # 특정 인덱스 제거
fruits.clear()  # 모든 요소 제거

# 검색
fruits = ["apple", "banana", "cherry"]
index = fruits.index("banana")  # 인덱스 찾기
count = fruits.count("apple")  # 개수 세기

# 정렬
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()  # 오름차순 정렬
numbers.sort(reverse=True)  # 내림차순 정렬
numbers.reverse()  # 역순 정렬

# 복사
original = [1, 2, 3]
shallow_copy = original.copy()
```

### 1.4 리스트 연산

```python
# 연결
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# 반복
repeated = [0] * 5  # [0, 0, 0, 0, 0]

# 멤버십
print(1 in list1)  # True
print(10 in list1)  # False

# 길이
print(len(list1))  # 3
```

### 1.5 리스트 컴프리헨션

```python
# 기본
squares = [x**2 for x in range(10)]

# 조건 포함
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# if-else 포함
numbers = [x if x % 2 == 0 else -x for x in range(10)]

# 중첩 리스트 컴프리헨션
matrix = [[i*j for j in range(3)] for i in range(3)]

# 문자열 처리
words = ["Hello", "World", "Python"]
upper_words = [word.upper() for word in words]
```

---

## 2. 튜플 (Tuple)

### 2.1 튜플 생성

```python
# 빈 튜플
empty_tuple = ()
empty_tuple = tuple()

# 요소가 있는 튜플
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")

# 단일 요소 튜플 (쉼표 필수!)
single = (1,)  # 튜플
not_tuple = (1)  # 정수

# 괄호 생략 가능
coordinates = 10, 20
```

### 2.2 튜플 특징

```python
# 불변성 (Immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 패킹과 언패킹
# 패킹
point = (10, 20)

# 언패킹
x, y = point
print(x, y)  # 10 20

# 여러 변수 할당
a, b, c = 1, 2, 3
```

### 2.3 튜플 메서드

```python
my_tuple = (1, 2, 3, 2, 2, 4)

# count() - 개수 세기
count = my_tuple.count(2)  # 3

# index() - 인덱스 찾기
index = my_tuple.index(3)  # 2
```

### 2.4 튜플 활용

```python
# 함수에서 여러 값 반환
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# 스왑 (값 교환)
a, b = 10, 20
a, b = b, a  # 10과 20 교환

# 딕셔너리 키로 사용 (리스트는 불가)
locations = {
    (0, 0): "원점",
    (10, 20): "A지점",
    (30, 40): "B지점"
}
```

---

## 3. 리스트 vs 튜플

| 특징 | 리스트 (List) | 튜플 (Tuple) |
|------|---------------|--------------|
| 가변성 | 변경 가능 (Mutable) | 변경 불가 (Immutable) |
| 표기법 | `[1, 2, 3]` | `(1, 2, 3)` |
| 속도 | 느림 | 빠름 |
| 메모리 | 많이 사용 | 적게 사용 |
| 용도 | 변경 가능한 데이터 | 변경 불가한 데이터 |
| 메서드 | 많음 | 적음 |
| 딕셔너리 키 | 불가 | 가능 |

---

## 4. 고급 리스트 기법

### 4.1 다차원 리스트

```python
# 2차원 리스트
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 접근
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# 순회
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

### 4.2 리스트 정렬

```python
# sorted() - 새 리스트 반환
numbers = [3, 1, 4, 1, 5]
sorted_numbers = sorted(numbers)

# 역순 정렬
sorted_numbers = sorted(numbers, reverse=True)

# 키 함수 사용
words = ["apple", "pie", "zoo", "car"]
sorted_words = sorted(words, key=len)  # 길이순 정렬

# 복잡한 정렬
students = [
    ("철수", 85, 20),
    ("영희", 92, 19),
    ("민수", 78, 21)
]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
```

---

## 실습 과제

### 과제 1: 리스트 통계
리스트의 합계, 평균, 최댓값, 최솟값 계산

### 과제 2: 리스트 중복 제거
중복된 요소 제거 프로그램

### 과제 3: 2차원 리스트 연산
행렬 덧셈, 전치 행렬 구하기

### 과제 4: 성적 관리 프로그램
학생 이름과 점수를 리스트로 관리

### 과제 5: 리스트 병합
두 정렬된 리스트를 하나의 정렬된 리스트로 병합

---

## 다음 시간 예고

6일차에는 **자료구조 II - 딕셔너리와 집합**을 학습합니다.
