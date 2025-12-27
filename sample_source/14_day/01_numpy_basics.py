"""
NumPy 기초
배열 생성, 연산, 인덱싱, 통계 함수
"""

import numpy as np


def main():
    print("=" * 60)
    print("NumPy 기초 예제")
    print("=" * 60)

    # ===== 1. 배열 생성 =====
    print("\n[1] 배열 생성")
    print("-" * 60)

    # 1차원 배열
    arr1 = np.array([1, 2, 3, 4, 5])
    print(f"1차원 배열: {arr1}")
    print(f"타입: {type(arr1)}")
    print(f"shape: {arr1.shape}")
    print(f"차원: {arr1.ndim}")

    # 2차원 배열
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\n2차원 배열:\n{arr2}")
    print(f"shape: {arr2.shape}")
    print(f"차원: {arr2.ndim}")

    # 특수 배열
    zeros = np.zeros((3, 3))
    ones = np.ones((2, 4))
    eye = np.eye(3)  # 단위 행렬
    arange = np.arange(0, 10, 2)
    linspace = np.linspace(0, 1, 5)

    print(f"\n0으로 채운 배열 (3x3):\n{zeros}")
    print(f"\n1로 채운 배열 (2x4):\n{ones}")
    print(f"\n단위 행렬 (3x3):\n{eye}")
    print(f"\narange(0, 10, 2): {arange}")
    print(f"linspace(0, 1, 5): {linspace}")

    # ===== 2. 랜덤 배열 =====
    print("\n[2] 랜덤 배열")
    print("-" * 60)

    # 시드 설정 (재현 가능한 랜덤)
    np.random.seed(42)

    random_uniform = np.random.rand(3, 3)  # 0~1 균등 분포
    random_normal = np.random.randn(3, 3)  # 표준 정규 분포
    random_int = np.random.randint(1, 100, size=10)  # 정수 난수

    print(f"균등 분포 (0~1):\n{random_uniform}\n")
    print(f"정규 분포:\n{random_normal}\n")
    print(f"정수 난수 (1~99): {random_int}")

    # ===== 3. 배열 연산 =====
    print("\n[3] 배열 연산")
    print("-" * 60)

    arr = np.array([1, 2, 3, 4, 5])

    print(f"원본 배열: {arr}")
    print(f"arr + 10 = {arr + 10}")
    print(f"arr * 2 = {arr * 2}")
    print(f"arr ** 2 = {arr ** 2}")
    print(f"arr / 2 = {arr / 2}")

    # 배열 간 연산
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])

    print(f"\narr1 = {arr1}")
    print(f"arr2 = {arr2}")
    print(f"arr1 + arr2 = {arr1 + arr2}")
    print(f"arr1 * arr2 = {arr1 * arr2}")
    print(f"arr1 - arr2 = {arr1 - arr2}")

    # ===== 4. 통계 함수 =====
    print("\n[4] 통계 함수")
    print("-" * 60)

    data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    print(f"데이터: {data}")
    print(f"\n합계: {np.sum(data)}")
    print(f"평균: {np.mean(data)}")
    print(f"중앙값: {np.median(data)}")
    print(f"표준편차: {np.std(data):.2f}")
    print(f"분산: {np.var(data):.2f}")
    print(f"최솟값: {np.min(data)}")
    print(f"최댓값: {np.max(data)}")
    print(f"최솟값 인덱스: {np.argmin(data)}")
    print(f"최댓값 인덱스: {np.argmax(data)}")

    # 2차원 배열의 축별 통계
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(f"\n2차원 배열:\n{arr2d}")
    print(f"전체 합계: {np.sum(arr2d)}")
    print(f"열별 합계 (axis=0): {np.sum(arr2d, axis=0)}")
    print(f"행별 합계 (axis=1): {np.sum(arr2d, axis=1)}")

    # ===== 5. 인덱싱과 슬라이싱 =====
    print("\n[5] 인덱싱과 슬라이싱")
    print("-" * 60)

    arr = np.array([10, 20, 30, 40, 50])

    print(f"배열: {arr}")
    print(f"arr[0] = {arr[0]}")
    print(f"arr[-1] = {arr[-1]}")
    print(f"arr[1:4] = {arr[1:4]}")
    print(f"arr[::2] = {arr[::2]}")

    # 2차원 배열 인덱싱
    arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(f"\n2차원 배열:\n{arr2d}")
    print(f"arr2d[0, 0] = {arr2d[0, 0]}")
    print(f"arr2d[1, 2] = {arr2d[1, 2]}")
    print(f"arr2d[:, 0] = {arr2d[:, 0]} (첫 번째 열)")
    print(f"arr2d[0, :] = {arr2d[0, :]} (첫 번째 행)")
    print(f"arr2d[0:2, 1:3] =\n{arr2d[0:2, 1:3]}")

    # ===== 6. 조건 인덱싱 =====
    print("\n[6] 조건 인덱싱 (Boolean Indexing)")
    print("-" * 60)

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"배열: {arr}")
    print(f"3보다 큰 값: {arr[arr > 3]}")
    print(f"짝수: {arr[arr % 2 == 0]}")
    print(f"5보다 크고 8보다 작은 값: {arr[(arr > 5) & (arr < 8)]}")

    # ===== 7. 배열 형태 변경 =====
    print("\n[7] 배열 형태 변경")
    print("-" * 60)

    arr = np.arange(12)
    print(f"원본: {arr}")

    reshaped = arr.reshape(3, 4)
    print(f"reshape(3, 4):\n{reshaped}")

    reshaped2 = arr.reshape(4, 3)
    print(f"\nreshape(4, 3):\n{reshaped2}")

    flattened = reshaped.flatten()
    print(f"\nflatten(): {flattened}")

    # ===== 8. 실전 예제: 학생 성적 분석 =====
    print("\n[8] 실전 예제: 학생 성적 분석")
    print("-" * 60)

    # 5명 학생의 3과목 성적 (행: 학생, 열: 과목)
    scores = np.array([
        [85, 90, 88],  # 학생 1
        [92, 88, 90],  # 학생 2
        [78, 85, 80],  # 학생 3
        [95, 92, 93],  # 학생 4
        [88, 86, 91]   # 학생 5
    ])

    print("학생별 성적 (수학, 영어, 과학):")
    print(scores)

    # 학생별 평균
    student_avg = np.mean(scores, axis=1)
    print(f"\n학생별 평균: {student_avg}")

    # 과목별 평균
    subject_avg = np.mean(scores, axis=0)
    print(f"과목별 평균: {subject_avg}")

    # 전체 평균
    total_avg = np.mean(scores)
    print(f"전체 평균: {total_avg:.2f}")

    # 최고 점수를 받은 학생과 과목
    max_idx = np.unravel_index(np.argmax(scores), scores.shape)
    print(f"\n최고 점수: {np.max(scores)}점")
    print(f"학생 {max_idx[0] + 1}의 과목 {max_idx[1] + 1}")

    # 80점 이상인 점수 개수
    high_scores = scores[scores >= 80]
    print(f"\n80점 이상 개수: {len(high_scores)}개")


if __name__ == "__main__":
    main()
