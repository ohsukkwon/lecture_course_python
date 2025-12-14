# 7일차: 정렬 알고리즘 (Sorting Algorithms)

## 학습 목표
- 정렬 알고리즘의 개념과 필요성 이해
- 기본 정렬 알고리즘의 원리와 동작 방식 이해
- 버블 정렬, 선택 정렬, 삽입 정렬 구현
- 파이썬 내장 정렬 함수 활용
- 시간 복잡도의 기본 개념 이해

---

## 1. 정렬 알고리즘이란?

### 1.1 정렬의 정의
- 데이터를 특정 순서(오름차순 또는 내림차순)로 배열하는 것
- 데이터 검색과 처리를 효율적으로 만드는 기본 연산
- 실생활 및 프로그래밍에서 가장 많이 사용되는 알고리즘

### 1.2 정렬의 필요성
```python
# 정렬되지 않은 데이터
numbers = [64, 34, 25, 12, 22, 11, 90]
# 특정 값을 찾기 위해 모든 요소를 확인해야 함

# 정렬된 데이터
sorted_numbers = [11, 12, 22, 25, 34, 64, 90]
# 효율적인 검색 가능 (이진 탐색 등)
```

---

## 2. 버블 정렬 (Bubble Sort)

### 2.1 알고리즘 설명
- 인접한 두 원소를 비교하여 큰 값을 뒤로 보내는 방식
- 한 번의 순회마다 가장 큰 값이 맨 뒤로 이동
- 마치 거품(bubble)이 수면으로 올라오는 것처럼 동작

### 2.2 동작 원리
```
초기 배열: [64, 34, 25, 12, 22]

1회전:
[34, 64, 25, 12, 22] → 64와 34 비교 후 교환
[34, 25, 64, 12, 22] → 64와 25 비교 후 교환
[34, 25, 12, 64, 22] → 64와 12 비교 후 교환
[34, 25, 12, 22, 64] → 64와 22 비교 후 교환 (64는 제자리 확정)

2회전:
[25, 34, 12, 22, 64] → 34와 25 비교 후 교환
[25, 12, 34, 22, 64] → 34와 12 비교 후 교환
[25, 12, 22, 34, 64] → 34와 22 비교 후 교환 (34는 제자리 확정)

... (반복)
```

### 2.3 구현 코드
```python
def bubble_sort(arr):
    """버블 정렬 구현"""
    n = len(arr)

    # 전체 패스 반복
    for i in range(n):
        # 각 패스에서 인접한 요소 비교
        for j in range(0, n - i - 1):
            # 앞의 요소가 뒤의 요소보다 크면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# 테스트
numbers = [64, 34, 25, 12, 22, 11, 90]
print("정렬 전:", numbers)
bubble_sort(numbers)
print("정렬 후:", numbers)
```

### 2.4 최적화된 버블 정렬
```python
def bubble_sort_optimized(arr):
    """최적화된 버블 정렬 - 교환이 없으면 조기 종료"""
    n = len(arr)

    for i in range(n):
        swapped = False  # 교환 발생 여부 확인

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # 교환이 발생하지 않았다면 이미 정렬된 상태
        if not swapped:
            break

    return arr
```

---

## 3. 선택 정렬 (Selection Sort)

### 3.1 알고리즘 설명
- 남은 요소 중 최솟값을 찾아 현재 위치와 교환
- 매번 최솟값을 "선택"하여 앞으로 보내는 방식
- 교환 횟수가 버블 정렬보다 적음

### 3.2 동작 원리
```
초기 배열: [64, 25, 12, 22, 11]

1회전:
최솟값 11을 찾아 첫 번째와 교환
[11, 25, 12, 22, 64]

2회전:
남은 요소 중 최솟값 12를 찾아 두 번째와 교환
[11, 12, 25, 22, 64]

3회전:
남은 요소 중 최솟값 22를 찾아 세 번째와 교환
[11, 12, 22, 25, 64]

4회전:
남은 요소 중 최솟값 25는 이미 제자리
[11, 12, 22, 25, 64]
```

### 3.3 구현 코드
```python
def selection_sort(arr):
    """선택 정렬 구현"""
    n = len(arr)

    # 배열을 순회하며
    for i in range(n):
        # 현재 위치를 최솟값 위치로 가정
        min_idx = i

        # 나머지 요소 중 최솟값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 최솟값을 현재 위치와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# 테스트
numbers = [64, 25, 12, 22, 11]
print("정렬 전:", numbers)
selection_sort(numbers)
print("정렬 후:", numbers)
```

---

## 4. 삽입 정렬 (Insertion Sort)

### 4.1 알고리즘 설명
- 배열을 정렬된 부분과 정렬되지 않은 부분으로 나눔
- 정렬되지 않은 부분의 첫 요소를 정렬된 부분의 적절한 위치에 삽입
- 카드 게임에서 카드를 정렬하는 방식과 유사

### 4.2 동작 원리
```
초기 배열: [12, 11, 13, 5, 6]

1회전: [12] | 11, 13, 5, 6
11을 정렬된 부분에 삽입 → [11, 12] | 13, 5, 6

2회전: [11, 12] | 13, 5, 6
13을 정렬된 부분에 삽입 → [11, 12, 13] | 5, 6

3회전: [11, 12, 13] | 5, 6
5를 정렬된 부분에 삽입 → [5, 11, 12, 13] | 6

4회전: [5, 11, 12, 13] | 6
6을 정렬된 부분에 삽입 → [5, 6, 11, 12, 13]
```

### 4.3 구현 코드
```python
def insertion_sort(arr):
    """삽입 정렬 구현"""
    n = len(arr)

    # 두 번째 요소부터 시작 (첫 번째는 이미 정렬된 것으로 간주)
    for i in range(1, n):
        key = arr[i]  # 삽입할 요소
        j = i - 1

        # key보다 큰 요소들을 한 칸씩 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 적절한 위치에 삽입
        arr[j + 1] = key

    return arr

# 테스트
numbers = [12, 11, 13, 5, 6]
print("정렬 전:", numbers)
insertion_sort(numbers)
print("정렬 후:", numbers)
```

---

## 5. 파이썬 내장 정렬

### 5.1 sorted() 함수
```python
# 리스트 정렬 (원본 유지)
numbers = [64, 34, 25, 12, 22]
sorted_numbers = sorted(numbers)
print("원본:", numbers)        # [64, 34, 25, 12, 22]
print("정렬:", sorted_numbers)  # [12, 22, 25, 34, 64]

# 내림차순 정렬
desc_numbers = sorted(numbers, reverse=True)
print("내림차순:", desc_numbers)  # [64, 34, 25, 22, 12]
```

### 5.2 list.sort() 메서드
```python
# 리스트 자체를 정렬 (원본 수정)
numbers = [64, 34, 25, 12, 22]
numbers.sort()
print("정렬:", numbers)  # [12, 22, 25, 34, 64]

# 내림차순 정렬
numbers.sort(reverse=True)
print("내림차순:", numbers)  # [64, 34, 25, 22, 12]
```

### 5.3 key 매개변수 활용
```python
# 문자열 길이로 정렬
words = ["banana", "pie", "Washington", "book"]
sorted_words = sorted(words, key=len)
print(sorted_words)  # ['pie', 'book', 'banana', 'Washington']

# 튜플의 특정 요소로 정렬
students = [("철수", 85), ("영희", 92), ("민수", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_score)
# [('영희', 92), ('철수', 85), ('민수', 78)]

# 딕셔너리 정렬
scores = {"철수": 85, "영희": 92, "민수": 78}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(sorted_scores)
# [('영희', 92), ('철수', 85), ('민수', 78)]
```

---

## 6. 시간 복잡도 (Time Complexity) 기초

### 6.1 시간 복잡도란?
- 알고리즘의 실행 시간을 입력 크기에 따라 표현
- Big-O 표기법으로 나타냄
- 알고리즘의 효율성을 비교하는 척도

### 6.2 정렬 알고리즘 비교

| 알고리즘 | 최선 | 평균 | 최악 | 공간 복잡도 |
|---------|------|------|------|------------|
| 버블 정렬 | O(n) | O(n²) | O(n²) | O(1) |
| 선택 정렬 | O(n²) | O(n²) | O(n²) | O(1) |
| 삽입 정렬 | O(n) | O(n²) | O(n²) | O(1) |
| 파이썬 내장(Timsort) | O(n) | O(n log n) | O(n log n) | O(n) |

### 6.3 언제 어떤 정렬을 사용할까?

```python
# 일반적인 경우: 파이썬 내장 정렬 사용 (가장 효율적)
numbers = [64, 34, 25, 12, 22]
numbers.sort()

# 교육용 또는 작은 데이터: 간단한 정렬 알고리즘
# 버블 정렬, 선택 정렬, 삽입 정렬

# 거의 정렬된 데이터: 삽입 정렬이 효율적
nearly_sorted = [1, 2, 3, 5, 4, 6, 7]
insertion_sort(nearly_sorted)
```

---

## 7. 정렬 알고리즘 시각화

### 7.1 정렬 과정 출력
```python
def bubble_sort_visualized(arr):
    """정렬 과정을 시각화하는 버블 정렬"""
    n = len(arr)
    print(f"초기 배열: {arr}")

    for i in range(n):
        print(f"\n--- {i+1}회전 ---")
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"교환: {arr}")

        if not swapped:
            print("더 이상 교환 없음 - 정렬 완료!")
            break

    print(f"\n최종 배열: {arr}")
    return arr

# 테스트
numbers = [64, 34, 25, 12, 22]
bubble_sort_visualized(numbers)
```

---

## 8. 실전 예제

### 8.1 학생 성적 정렬
```python
students = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 78},
    {"name": "지영", "score": 95}
]

# 성적순 정렬 (높은 순)
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

print("성적순 순위:")
for i, student in enumerate(sorted_students, 1):
    print(f"{i}위: {student['name']} - {student['score']}점")
```

### 8.2 다중 기준 정렬
```python
data = [
    ("철수", 25, 85),
    ("영희", 23, 92),
    ("민수", 25, 78),
    ("지영", 23, 95)
]

# 나이순, 같은 나이면 점수순 정렬
sorted_data = sorted(data, key=lambda x: (x[1], -x[2]))
print(sorted_data)
```

---

## 실습 과제

### 과제 1: 정렬 알고리즘 구현
세 가지 정렬 알고리즘(버블, 선택, 삽입)을 모두 구현하고 동일한 데이터로 테스트하기

### 과제 2: 역순 정렬
내림차순으로 정렬하는 함수 구현 (각 알고리즘별로)

### 과제 3: 문자열 정렬
문자열 리스트를 알파벳순으로 정렬하는 프로그램 작성

### 과제 4: 성적 관리 시스템
학생 이름과 성적을 입력받아 다양한 기준으로 정렬하는 프로그램

### 과제 5: 정렬 비교 프로그램
여러 정렬 알고리즘의 실행 시간을 비교하는 프로그램 작성 (time 모듈 활용)

---

## 추가 학습 자료

### 더 알아보기
- **고급 정렬 알고리즘**: 병합 정렬, 퀵 정렬, 힙 정렬
- **파이썬 Timsort**: 파이썬 내장 정렬의 원리
- **안정 정렬**: 같은 값의 상대적 순서 유지
- **정렬 알고리즘 시각화 도구**: visualgo.net

---

## 다음 시간 예고

8일차에는 **모듈과 패키지**를 학습합니다.
- 모듈의 개념 및 import
- 표준 라이브러리 활용
- 사용자 정의 모듈 만들기
- 패키지 구조 이해
