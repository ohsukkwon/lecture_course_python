"""
버블 정렬 (Bubble Sort)
인접한 두 원소를 비교하여 큰 값을 뒤로 보내는 정렬 알고리즘
"""


def bubble_sort(arr):
    """
    버블 정렬 구현

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
    n = len(arr)

    # 전체 패스 반복
    for i in range(n):
        # 각 패스에서 인접한 요소 비교
        for j in range(0, n - i - 1):
            # 앞의 요소가 뒤의 요소보다 크면 교환
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def bubble_sort_optimized(arr):
    """
    최적화된 버블 정렬 - 교환이 없으면 조기 종료

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
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


def bubble_sort_visualized(arr):
    """
    정렬 과정을 시각화하는 버블 정렬

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
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


# ===== 실행 예제 =====

if __name__ == "__main__":
    print("=" * 50)
    print("버블 정렬 (Bubble Sort) 예제")
    print("=" * 50)

    # 예제 1: 기본 버블 정렬
    print("\n[예제 1] 기본 버블 정렬")
    numbers1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"정렬 전: {numbers1}")
    bubble_sort(numbers1.copy())
    print(f"정렬 후: {bubble_sort(numbers1)}")

    # 예제 2: 최적화된 버블 정렬
    print("\n[예제 2] 최적화된 버블 정렬")
    numbers2 = [1, 2, 3, 5, 4, 6]  # 거의 정렬된 배열
    print(f"정렬 전: {numbers2}")
    bubble_sort_optimized(numbers2)
    print(f"정렬 후: {numbers2}")

    # 예제 3: 정렬 과정 시각화
    print("\n[예제 3] 정렬 과정 시각화")
    numbers3 = [64, 34, 25, 12, 22]
    bubble_sort_visualized(numbers3)

    # 예제 4: 내림차순 정렬 (비교 조건 변경)
    print("\n[예제 4] 내림차순 정렬")

    def bubble_sort_descending(arr):
        """내림차순 버블 정렬"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] < arr[j + 1]:  # 비교 조건만 변경
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    numbers4 = [64, 34, 25, 12, 22]
    print(f"정렬 전: {numbers4}")
    bubble_sort_descending(numbers4)
    print(f"내림차순 정렬 후: {numbers4}")

    # 예제 5: 문자열 정렬
    print("\n[예제 5] 문자열 리스트 정렬")
    words = ["banana", "apple", "cherry", "date"]
    print(f"정렬 전: {words}")
    bubble_sort(words)
    print(f"정렬 후: {words}")
