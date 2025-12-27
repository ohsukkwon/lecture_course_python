"""
Pandas 기초
Series, DataFrame, 데이터 읽기/쓰기, 데이터 탐색
"""

import pandas as pd
import numpy as np


def main():
    print("=" * 60)
    print("Pandas 기초 예제")
    print("=" * 60)

    # ===== 1. Series 생성 =====
    print("\n[1] Series 생성")
    print("-" * 60)

    # 기본 Series
    s = pd.Series([10, 20, 30, 40, 50])
    print("기본 Series:")
    print(s)

    # 인덱스가 있는 Series
    s_named = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
    print("\n인덱스가 있는 Series:")
    print(s_named)
    print(f"\ns_named['a'] = {s_named['a']}")

    # 딕셔너리로 Series 생성
    s_dict = pd.Series({'apple': 100, 'banana': 200, 'cherry': 300})
    print("\n딕셔너리로 생성한 Series:")
    print(s_dict)

    # ===== 2. DataFrame 생성 =====
    print("\n[2] DataFrame 생성")
    print("-" * 60)

    # 딕셔너리로 생성
    data = {
        'name': ['철수', '영희', '민수', '지영'],
        'age': [25, 23, 27, 24],
        'score': [85, 92, 78, 95]
    }
    df = pd.DataFrame(data)
    print("기본 DataFrame:")
    print(df)

    # 리스트로 생성
    data_list = [
        ['철수', 25, 85],
        ['영희', 23, 92],
        ['민수', 27, 78]
    ]
    df_list = pd.DataFrame(data_list, columns=['name', 'age', 'score'])
    print("\n리스트로 생성한 DataFrame:")
    print(df_list)

    # ===== 3. 데이터 탐색 =====
    print("\n[3] 데이터 탐색")
    print("-" * 60)

    # 샘플 데이터 생성
    df = pd.DataFrame({
        'name': ['철수', '영희', '민수', '지영', '수현', '민지'],
        'age': [25, 23, 27, 24, 26, 22],
        'city': ['서울', '부산', '서울', '대구', '인천', '부산'],
        'score': [85, 92, 78, 95, 88, 82]
    })

    print("전체 데이터:")
    print(df)

    print("\n처음 3행:")
    print(df.head(3))

    print("\n마지막 2행:")
    print(df.tail(2))

    print("\n데이터 정보:")
    print(df.info())

    print("\n통계 요약:")
    print(df.describe())

    print(f"\nshape: {df.shape}")
    print(f"columns: {df.columns.tolist()}")
    print(f"index: {df.index.tolist()}")

    # ===== 4. 열 선택 =====
    print("\n[4] 열 선택")
    print("-" * 60)

    print("이름 열 (Series):")
    print(df['name'])
    print(f"타입: {type(df['name'])}")

    print("\n이름과 나이 열 (DataFrame):")
    print(df[['name', 'age']])

    # ===== 5. 행 선택 =====
    print("\n[5] 행 선택")
    print("-" * 60)

    print("첫 번째 행 (loc):")
    print(df.loc[0])

    print("\n첫 번째 행 (iloc):")
    print(df.iloc[0])

    print("\n0~2행:")
    print(df.loc[0:2])

    print("\n특정 위치의 값:")
    print(f"df.loc[0, 'name'] = {df.loc[0, 'name']}")
    print(f"df.iloc[0, 0] = {df.iloc[0, 0]}")

    # ===== 6. 데이터 필터링 =====
    print("\n[6] 데이터 필터링")
    print("-" * 60)

    print("나이가 25 이상인 사람:")
    print(df[df['age'] >= 25])

    print("\n점수가 85 이상인 사람:")
    print(df[df['score'] >= 85])

    print("\n서울에 사는 사람:")
    print(df[df['city'] == '서울'])

    print("\n나이가 24 이상이고 점수가 85 이상인 사람:")
    print(df[(df['age'] >= 24) & (df['score'] >= 85)])

    # ===== 7. 데이터 정렬 =====
    print("\n[7] 데이터 정렬")
    print("-" * 60)

    print("나이 오름차순:")
    print(df.sort_values('age'))

    print("\n점수 내림차순:")
    print(df.sort_values('score', ascending=False))

    print("\n도시, 나이 순으로 정렬:")
    print(df.sort_values(['city', 'age']))

    # ===== 8. 새 열 추가 및 수정 =====
    print("\n[8] 새 열 추가 및 수정")
    print("-" * 60)

    # 새 열 추가
    df_copy = df.copy()
    df_copy['grade'] = ['B', 'A', 'C', 'A', 'B', 'B']
    df_copy['passed'] = df_copy['score'] >= 80

    print("새 열 추가 후:")
    print(df_copy)

    # 열 수정
    df_copy['score'] = df_copy['score'] + 5
    print("\n점수 +5 후:")
    print(df_copy[['name', 'score']])

    # ===== 9. 집계 및 그룹화 =====
    print("\n[9] 집계 및 그룹화")
    print("-" * 60)

    print(f"평균 나이: {df['age'].mean():.2f}")
    print(f"평균 점수: {df['score'].mean():.2f}")
    print(f"최고 점수: {df['score'].max()}")
    print(f"최저 점수: {df['score'].min()}")

    print("\n도시별 평균 점수:")
    print(df.groupby('city')['score'].mean())

    print("\n도시별 통계:")
    print(df.groupby('city')['score'].agg(['mean', 'max', 'min', 'count']))

    # ===== 10. 결측치 처리 =====
    print("\n[10] 결측치 처리")
    print("-" * 60)

    # 결측치가 있는 데이터 생성
    df_na = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, 7, 8],
        'C': [9, 10, 11, 12]
    })

    print("결측치가 있는 데이터:")
    print(df_na)

    print("\n결측치 확인:")
    print(df_na.isnull())

    print("\n각 열의 결측치 개수:")
    print(df_na.isnull().sum())

    print("\n결측치가 있는 행 삭제:")
    print(df_na.dropna())

    print("\n결측치를 0으로 채움:")
    print(df_na.fillna(0))

    print("\n결측치를 평균값으로 채움:")
    df_filled = df_na.copy()
    df_filled['A'] = df_filled['A'].fillna(df_filled['A'].mean())
    df_filled['B'] = df_filled['B'].fillna(df_filled['B'].mean())
    print(df_filled)

    # ===== 11. 실전 예제: 학생 관리 시스템 =====
    print("\n[11] 실전 예제: 학생 관리 시스템")
    print("-" * 60)

    # 학생 데이터
    students = pd.DataFrame({
        'student_id': ['S001', 'S002', 'S003', 'S004', 'S005'],
        'name': ['김철수', '이영희', '박민수', '최지영', '정수현'],
        'math': [85, 92, 78, 95, 88],
        'english': [90, 88, 85, 92, 86],
        'science': [88, 90, 80, 93, 91]
    })

    print("학생 성적 데이터:")
    print(students)

    # 총점 및 평균 계산
    students['total'] = students[['math', 'english', 'science']].sum(axis=1)
    students['average'] = students[['math', 'english', 'science']].mean(axis=1)

    # 등수 매기기
    students['rank'] = students['total'].rank(ascending=False, method='min')

    print("\n총점 및 평균 추가:")
    print(students)

    # 상위 3명
    top3 = students.nlargest(3, 'total')
    print("\n상위 3명:")
    print(top3[['name', 'total', 'average', 'rank']])

    # 과목별 평균
    subject_avg = students[['math', 'english', 'science']].mean()
    print("\n과목별 평균:")
    print(subject_avg)

    # 수학 점수가 85 이상인 학생
    math_high = students[students['math'] >= 85]
    print("\n수학 점수 85 이상:")
    print(math_high[['name', 'math']])

    # 평균이 90 이상인 학생
    high_achievers = students[students['average'] >= 90]
    print("\n평균 90 이상 (우수 학생):")
    print(high_achievers[['name', 'average']])


if __name__ == "__main__":
    main()
