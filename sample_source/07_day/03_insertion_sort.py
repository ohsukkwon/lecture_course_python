"""
삽입 정렬 (Insertion Sort)
배열을 정렬된 부분과 미정렬 부분으로 나누어
미정렬 요소를 정렬된 부분의 적절한 위치에 삽입하는 알고리즘
"""


def insertion_sort(arr):
    """
    삽입 정렬 구현

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
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


def insertion_sort_visualized(arr):
    """
    정렬 과정을 시각화하는 삽입 정렬

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 정렬된 리스트
    """
    n = len(arr)
    print(f"초기 배열: {arr}\n")

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        print(f"{i}회전: key = {key}")
        print(f"  정렬된 부분: {arr[:i]}")
        print(f"  삽입할 요소: {key}")

        # key보다 큰 요소들을 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"  삽입 후: {arr}")
        print()

    print(f"최종 배열: {arr}")
    return arr


def insertion_sort_descending(arr):
    """
    내림차순 삽입 정렬

    Parameters:
        arr (list): 정렬할 리스트

    Returns:
        list: 내림차순으로 정렬된 리스트
    """
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # 비교 조건만 변경 (작은 값을 뒤로)
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ===== 실행 예제 =====

if __name__ == "__main__":
    print("=" * 50)
    print("삽입 정렬 (Insertion Sort) 예제")
    print("=" * 50)

    # 예제 1: 기본 삽입 정렬
    print("\n[예제 1] 기본 삽입 정렬")
    numbers1 = [12, 11, 13, 5, 6]
    print(f"정렬 전: {numbers1}")
    insertion_sort(numbers1)
    print(f"정렬 후: {numbers1}")

    # 예제 2: 정렬 과정 시각화
    print("\n[예제 2] 정렬 과정 시각화")
    numbers2 = [12, 11, 13, 5, 6]
    insertion_sort_visualized(numbers2)

    # 예제 3: 내림차순 정렬
    print("\n[예제 3] 내림차순 정렬")
    numbers3 = [12, 11, 13, 5, 6]
    print(f"정렬 전: {numbers3}")
    insertion_sort_descending(numbers3)
    print(f"내림차순 정렬 후: {numbers3}")

    # 예제 4: 거의 정렬된 배열 (삽입 정렬이 효율적)
    print("\n[예제 4] 거의 정렬된 배열")
    nearly_sorted = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]
    print(f"정렬 전: {nearly_sorted}")
    insertion_sort(nearly_sorted)
    print(f"정렬 후: {nearly_sorted}")
    print("→ 거의 정렬된 배열에서 삽입 정렬은 매우 효율적입니다!")

    # 예제 5: 문자열 정렬
    print("\n[예제 5] 문자열 리스트 정렬")
    words = ["python", "java", "cpp", "javascript", "go"]
    print(f"정렬 전: {words}")
    insertion_sort(words)
    print(f"정렬 후: {words}")

    # 예제 6: 삽입 정렬의 이동 횟수 확인
    print("\n[예제 6] 요소 이동 횟수 확인")

    def insertion_sort_count_moves(arr):
        """이동 횟수를 세는 삽입 정렬"""
        n = len(arr)
        move_count = 0

        for i in range(1, n):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                move_count += 1

            arr[j + 1] = key

        return arr, move_count

    numbers6 = [12, 11, 13, 5, 6]
    print(f"정렬 전: {numbers6}")
    result, moves = insertion_sort_count_moves(numbers6)
    print(f"정렬 후: {result}")
    print(f"총 이동 횟수: {moves}회")
