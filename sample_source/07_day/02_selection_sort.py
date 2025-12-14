"""
선택 정렬 (Selection Sort)
남은 요소 중 최솟값을 찾아 현재 위치와 교환하는 정렬 알고리즘
"""


def selection_sort(arr):
    """
    선택 정렬 구현

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
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


def selection_sort_visualized(arr):
    """
    정렬 과정을 시각화하는 선택 정렬

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
    n = len(arr)
    print(f"초기 배열: {arr}\n")

    for i in range(n):
        min_idx = i

        # 최솟값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # 교환
        if min_idx != i:
            print(f"{i+1}회전: 위치 {i}와 위치 {min_idx} 교환")
            print(f"  교환 전: {arr}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            print(f"  교환 후: {arr}")
        else:
            print(f"{i+1}회전: 위치 {i}는 이미 최솟값 (교환 없음)")
            print(f"  상태: {arr}")
        print()

    print(f"최종 배열: {arr}")
    return arr


def selection_sort_descending(arr):
    """
    내림차순 선택 정렬

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 내림차순으로 정렬된 리스트
    """
    n = len(arr)

    for i in range(n):
        max_idx = i  # 최댓값 위치로 변경

        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:  # 비교 조건 변경
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


# ===== 실행 예제 =====

if __name__ == "__main__":
    print("=" * 50)
    print("선택 정렬 (Selection Sort) 예제")
    print("=" * 50)

    # 예제 1: 기본 선택 정렬
    print("\n[예제 1] 기본 선택 정렬")
    numbers1 = [64, 25, 12, 22, 11]
    print(f"정렬 전: {numbers1}")
    selection_sort(numbers1)
    print(f"정렬 후: {numbers1}")

    # 예제 2: 정렬 과정 시각화
    print("\n[예제 2] 정렬 과정 시각화")
    numbers2 = [64, 25, 12, 22, 11]
    selection_sort_visualized(numbers2)

    # 예제 3: 내림차순 정렬
    print("\n[예제 3] 내림차순 정렬")
    numbers3 = [64, 25, 12, 22, 11]
    print(f"정렬 전: {numbers3}")
    selection_sort_descending(numbers3)
    print(f"내림차순 정렬 후: {numbers3}")

    # 예제 4: 문자열 정렬
    print("\n[예제 4] 문자열 리스트 정렬")
    fruits = ["orange", "apple", "banana", "cherry"]
    print(f"정렬 전: {fruits}")
    selection_sort(fruits)
    print(f"정렬 후: {fruits}")

    # 예제 5: 선택 정렬의 교환 횟수 확인
    print("\n[예제 5] 교환 횟수 확인")

    def selection_sort_count_swaps(arr):
        """교환 횟수를 세는 선택 정렬"""
        n = len(arr)
        swap_count = 0

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                swap_count += 1

        return arr, swap_count

    numbers5 = [64, 25, 12, 22, 11]
    print(f"정렬 전: {numbers5}")
    result, swaps = selection_sort_count_swaps(numbers5)
    print(f"정렬 후: {result}")
    print(f"총 교환 횟수: {swaps}회")
