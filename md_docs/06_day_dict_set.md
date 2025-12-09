# 6일차: 자료구조 II - 딕셔너리와 집합

## 학습 목표
- 딕셔너리(Dictionary)의 개념과 활용
- 딕셔너리 메서드 마스터
- 집합(Set)의 특징과 연산
- 자료구조 선택 가이드

---

## 1. 딕셔너리 (Dictionary)

### 1.1 딕셔너리 생성

```python
# 빈 딕셔너리
empty_dict = {}
empty_dict = dict()

# 키-값 쌍으로 생성
student = {
    "name": "김철수",
    "age": 25,
    "grade": "A"
}

# dict() 함수 사용
student = dict(name="김철수", age=25, grade="A")

# 리스트로부터 생성
pairs = [("name", "김철수"), ("age", 25)]
student = dict(pairs)
```

### 1.2 딕셔너리 접근과 수정

```python
student = {"name": "김철수", "age": 25, "grade": "A"}

# 접근
print(student["name"])  # 김철수
print(student.get("age"))  # 25
print(student.get("address", "정보 없음"))  # 기본값

# 수정
student["age"] = 26
student["address"] = "서울"  # 새 키 추가

# 삭제
del student["grade"]
age = student.pop("age")  # 제거하면서 값 반환
student.clear()  # 모든 항목 제거
```

### 1.3 딕셔너리 메서드

```python
student = {"name": "김철수", "age": 25, "grade": "A"}

# keys(), values(), items()
keys = student.keys()  # dict_keys(['name', 'age', 'grade'])
values = student.values()  # dict_values(['김철수', 25, 'A'])
items = student.items()  # dict_items([('name', '김철수'), ...])

# update() - 딕셔너리 병합
student.update({"address": "서울", "phone": "010-1234-5678"})

# setdefault() - 키가 없을 때만 추가
student.setdefault("email", "default@email.com")
```

### 1.4 딕셔너리 순회

```python
student = {"name": "김철수", "age": 25, "grade": "A"}

# 키 순회
for key in student:
    print(key)

# 값 순회
for value in student.values():
    print(value)

# 키-값 쌍 순회
for key, value in student.items():
    print(f"{key}: {value}")
```

### 1.5 딕셔너리 컴프리헨션

```python
# 기본
squares = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 조건 포함
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# 두 리스트로부터 생성
keys = ["name", "age", "city"]
values = ["철수", 25, "서울"]
person = {k: v for k, v in zip(keys, values)}

# 변환
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

### 1.6 중첩 딕셔너리

```python
# 딕셔너리 안의 딕셔너리
students = {
    "student1": {"name": "김철수", "age": 25, "grade": "A"},
    "student2": {"name": "이영희", "age": 24, "grade": "B"},
    "student3": {"name": "박민수", "age": 26, "grade": "A"}
}

# 접근
print(students["student1"]["name"])  # 김철수

# 순회
for student_id, info in students.items():
    print(f"{student_id}: {info['name']}, {info['age']}세")
```

---

## 2. 집합 (Set)

### 2.1 집합 생성

```python
# 빈 집합
empty_set = set()  # {}는 빈 딕셔너리!

# 요소가 있는 집합
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# 리스트로부터 생성 (중복 자동 제거)
numbers_list = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers_list)  # {1, 2, 3, 4}

# 문자열로부터 생성
letters = set("hello")  # {'h', 'e', 'l', 'o'}
```

### 2.2 집합 연산

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 합집합 (Union)
union1 = set1 | set2  # {1, 2, 3, 4, 5, 6, 7, 8}
union2 = set1.union(set2)

# 교집합 (Intersection)
intersection1 = set1 & set2  # {4, 5}
intersection2 = set1.intersection(set2)

# 차집합 (Difference)
difference1 = set1 - set2  # {1, 2, 3}
difference2 = set1.difference(set2)

# 대칭 차집합 (Symmetric Difference)
sym_diff1 = set1 ^ set2  # {1, 2, 3, 6, 7, 8}
sym_diff2 = set1.symmetric_difference(set2)
```

### 2.3 집합 메서드

```python
fruits = {"apple", "banana"}

# 추가
fruits.add("cherry")

# 여러 요소 추가
fruits.update(["mango", "orange"])
fruits.update(["grape"], {"kiwi"})

# 제거
fruits.remove("banana")  # 없으면 KeyError
fruits.discard("melon")  # 없어도 에러 없음
fruit = fruits.pop()  # 임의의 요소 제거 및 반환
fruits.clear()  # 모든 요소 제거
```

### 2.4 집합 관계 확인

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 6}

# 부분집합 (Subset)
print(set1.issubset(set2))  # True
print(set1 <= set2)  # True

# 상위집합 (Superset)
print(set2.issuperset(set1))  # True
print(set2 >= set1)  # True

# 서로소 (Disjoint) - 교집합이 없음
print(set1.isdisjoint(set3))  # True
```

### 2.5 집합 컴프리헨션

```python
# 기본
squares = {x**2 for x in range(10)}

# 조건 포함
even_squares = {x**2 for x in range(10) if x % 2 == 0}

# 문자열 처리
words = ["Hello", "World", "hello", "WORLD"]
unique_lower = {word.lower() for word in words}
# {'hello', 'world'}
```

---

## 3. 자료구조 비교 및 선택

| 특징 | 리스트 | 튜플 | 딕셔너리 | 집합 |
|------|--------|------|----------|------|
| 표기법 | `[1, 2]` | `(1, 2)` | `{"a": 1}` | `{1, 2}` |
| 순서 | O | O | X (3.7+부터 O) | X |
| 중복 | O | O | 키는 X, 값은 O | X |
| 변경 | O | X | O | O |
| 인덱싱 | O | O | X | X |
| 용도 | 순서 있는 데이터 | 불변 데이터 | 키-값 쌍 | 고유한 값 |

---

## 4. 실전 활용 예제

### 4.1 단어 빈도수 계산

```python
text = "hello world hello python world"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# 또는 딕셔너리 컴프리헨션
from collections import Counter
word_count = Counter(words)
```

### 4.2 학생 성적 관리

```python
students = {
    "김철수": {"국어": 85, "영어": 90, "수학": 88},
    "이영희": {"국어": 92, "영어": 88, "수학": 95},
    "박민수": {"국어": 78, "영어": 85, "수학": 82}
}

# 평균 계산
for name, scores in students.items():
    average = sum(scores.values()) / len(scores)
    print(f"{name}: {average:.1f}점")
```

### 4.3 중복 제거 및 정렬

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 집합으로 중복 제거 후 정렬
unique_sorted = sorted(set(numbers))
print(unique_sorted)  # [1, 2, 3, 4, 5, 6, 9]
```

---

## 실습 과제

### 과제 1: 전화번호부
이름과 전화번호를 딕셔너리로 관리하는 프로그램

### 과제 2: 단어 카운터
텍스트에서 각 단어의 빈도수 계산

### 과제 3: 학생 성적 관리
여러 과목의 성적을 관리하고 통계 계산

### 과제 4: 집합 연산 계산기
두 집합의 합집합, 교집합, 차집합 계산

### 과제 5: 중복 제거 프로그램
리스트에서 중복된 요소를 제거하고 정렬

---

## 다음 시간 예고

7일차에는 **모듈과 패키지**를 학습합니다.
