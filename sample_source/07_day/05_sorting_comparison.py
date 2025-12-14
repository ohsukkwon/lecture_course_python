"""
정렬 알고리즘 비교 및 성능 측정
다양한 정렬 알고리즘의 실행 시간 비교
"""

import time
import random


# ===== 정렬 알고리즘 구현 =====


def bubble_sort(arr):
    """버블 정렬"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    """선택 정렬"""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """삽입 정렬"""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def python_sort(arr):
    """파이썬 내장 정렬"""
    arr.sort()
    return arr


# ===== 성능 측정 함수 =====


def measure_time(sort_function, arr):
    """
    정렬 알고리즘의 실행 시간 측정

    Parameters:
        sort_function: 정렬 함수
        arr: 정렬할 배열

    Returns:
        float: 실행 시간 (초)
    """
    arr_copy = arr.copy()  # 원본 보존
    start_time = time.time()
    sort_function(arr_copy)
    end_time = time.time()
    return end_time - start_time


def compare_sorts(arr_size, array_type="random"):
    """
    여러 정렬 알고리즘의 성능 비교

    Parameters:
        arr_size: 배열 크기
        array_type: 배열 유형 ('random', 'sorted', 'reversed')
    """
    # 배열 생성
    if array_type == "random":
        arr = [random.randint(1, 1000) for _ in range(arr_size)]
    elif array_type == "sorted":
        arr = list(range(arr_size))
    elif array_type == "reversed":
        arr = list(range(arr_size, 0, -1))
    else:
        arr = [random.randint(1, 1000) for _ in range(arr_size)]

    print(f"\n{'=' * 60}")
    print(f"배열 크기: {arr_size}, 유형: {array_type.upper()}")
    print(f"{'=' * 60}")

    # 각 정렬 알고리즘 실행 및 시간 측정
    algorithms = [
        ("버블 정렬", bubble_sort),
        ("선택 정렬", selection_sort),
        ("삽입 정렬", insertion_sort),
        ("파이썬 내장", python_sort),
    ]

    results = []

    for name, func in algorithms:
        try:
            elapsed_time = measure_time(func, arr)
            results.append((name, elapsed_time))
            print(f"{name:15} : {elapsed_time:.6f}초")
        except Exception as e:
            print(f"{name:15} : 오류 발생 ({e})")

    # 가장 빠른 알고리즘 표시
    if results:
        fastest = min(results, key=lambda x: x[1])
        print(f"\n→ 가장 빠름: {fastest[0]} ({fastest[1]:.6f}초)")


# ===== 실행 예제 =====


def main():
    print("=" * 60)
    print("정렬 알고리즘 성능 비교")
    print("=" * 60)

    # 예제 1: 작은 배열 (랜덤)
    print("\n[예제 1] 작은 배열 (크기: 100)")
    compare_sorts(100, "random")

    # 예제 2: 중간 크기 배열 (랜덤)
    print("\n[예제 2] 중간 크기 배열 (크기: 1000)")
    compare_sorts(1000, "random")

    # 예제 3: 이미 정렬된 배열
    print("\n[예제 3] 이미 정렬된 배열 (크기: 1000)")
    compare_sorts(1000, "sorted")
    print("→ 삽입 정렬과 최적화된 버블 정렬이 효율적!")

    # 예제 4: 역순 배열
    print("\n[예제 4] 역순 배열 (크기: 1000)")
    compare_sorts(1000, "reversed")
    print("→ 최악의 경우 시나리오")

    # 예제 5: 시각적 비교 (작은 배열)
    print("\n" + "=" * 60)
    print("[예제 5] 시각적 정렬 비교")
    print("=" * 60)

    test_arr = [64, 34, 25, 12, 22, 11, 90, 88]
    print(f"원본 배열: {test_arr}\n")

    algorithms = [
        ("버블 정렬", bubble_sort),
        ("선택 정렬", selection_sort),
        ("삽입 정렬", insertion_sort),
    ]

    for name, func in algorithms:
        arr_copy = test_arr.copy()
        print(f"{name}:")
        print(f"  정렬 전: {arr_copy}")
        func(arr_copy)
        print(f"  정렬 후: {arr_copy}")
        print()

    # 예제 6: 알고리즘 특성 비교
    print("=" * 60)
    print("[예제 6] 알고리즘 특성 비교")
    print("=" * 60)

    print(
        """
┌──────────────┬──────────┬──────────┬──────────┬────────────┐
│ 알고리즘     │ 최선     │ 평균     │ 최악     │ 공간 복잡도│
├──────────────┼──────────┼──────────┼──────────┼────────────┤
│ 버블 정렬    │ O(n)     │ O(n²)    │ O(n²)    │ O(1)       │
│ 선택 정렬    │ O(n²)    │ O(n²)    │ O(n²)    │ O(1)       │
│ 삽입 정렬    │ O(n)     │ O(n²)    │ O(n²)    │ O(1)       │
│ 파이썬 내장  │ O(n)     │ O(nlogn) │ O(nlogn) │ O(n)       │
│ (Timsort)    │          │          │          │            │
└──────────────┴──────────┴──────────┴──────────┴────────────┘

[알고리즘 선택 가이드]
- 교육 목적: 버블/선택/삽입 정렬
- 거의 정렬된 데이터: 삽입 정렬
- 일반적인 경우: 파이썬 내장 정렬 (가장 효율적)
- 메모리 제약: 버블/선택/삽입 정렬 (제자리 정렬)
"""
    )


if __name__ == "__main__":
    main()
