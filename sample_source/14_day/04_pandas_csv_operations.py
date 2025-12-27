"""
Pandas CSV 파일 처리
CSV 읽기/쓰기, 데이터 전처리, 분석
"""

import pandas as pd
import numpy as np
import os


def create_sample_csv():
    """샘플 CSV 파일 생성"""
    print("\n[샘플 CSV 파일 생성]")

    # 학생 데이터
    students_data = {
        'student_id': ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008'],
        'name': ['김철수', '이영희', '박민수', '최지영', '정수현', '강민지', '윤서준', '임하은'],
        'age': [20, 19, 21, 20, 22, 19, 21, 20],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'major': ['컴퓨터', '경영', '컴퓨터', '경영', '디자인', '컴퓨터', '디자인', '경영'],
        'math': [85, 92, 78, 95, 70, 88, 82, 90],
        'english': [90, 88, 85, 92, 75, 86, 89, 94],
        'science': [88, 90, 80, 93, 72, 91, 85, 89]
    }

    df = pd.DataFrame(students_data)
    df.to_csv('students.csv', index=False, encoding='utf-8-sig')
    print("✓ students.csv 파일이 생성되었습니다.")

    # 판매 데이터
    sales_data = {
        'date': pd.date_range('2024-01-01', periods=30, freq='D'),
        'product': np.random.choice(['A', 'B', 'C'], 30),
        'sales': np.random.randint(50, 200, 30),
        'revenue': np.random.randint(500000, 2000000, 30)
    }

    df_sales = pd.DataFrame(sales_data)
    df_sales.to_csv('sales.csv', index=False, encoding='utf-8-sig')
    print("✓ sales.csv 파일이 생성되었습니다.")

    return df, df_sales


def read_csv_examples():
    """CSV 읽기 예제"""
    print("\n[1] CSV 파일 읽기")
    print("-" * 60)

    # 기본 읽기
    df = pd.read_csv('students.csv', encoding='utf-8-sig')
    print("전체 데이터:")
    print(df)

    print("\n데이터 정보:")
    print(df.info())

    # 특정 열만 읽기
    df_selected = pd.read_csv('students.csv', usecols=['name', 'age', 'major'])
    print("\n특정 열만 읽기:")
    print(df_selected)

    # 조건에 맞는 행만 읽기 (nrows)
    df_limited = pd.read_csv('students.csv', nrows=3)
    print("\n처음 3행만 읽기:")
    print(df_limited)

    return df


def data_exploration(df):
    """데이터 탐색"""
    print("\n[2] 데이터 탐색")
    print("-" * 60)

    print("기본 통계:")
    print(df.describe())

    print("\n각 열의 데이터 타입:")
    print(df.dtypes)

    print("\n결측치 확인:")
    print(df.isnull().sum())

    print("\n전공별 학생 수:")
    print(df['major'].value_counts())

    print("\n성별 분포:")
    print(df['gender'].value_counts())


def data_filtering(df):
    """데이터 필터링"""
    print("\n[3] 데이터 필터링")
    print("-" * 60)

    # 수학 점수 85점 이상
    high_math = df[df['math'] >= 85]
    print("수학 점수 85점 이상:")
    print(high_math[['name', 'math']])

    # 컴퓨터 전공 학생
    cs_students = df[df['major'] == '컴퓨터']
    print("\n컴퓨터 전공 학생:")
    print(cs_students[['name', 'major']])

    # 나이가 20세이고 수학 점수가 80점 이상
    filtered = df[(df['age'] == 20) & (df['math'] >= 80)]
    print("\n나이 20세 & 수학 80점 이상:")
    print(filtered[['name', 'age', 'math']])

    # 영어 또는 과학이 90점 이상
    high_scores = df[(df['english'] >= 90) | (df['science'] >= 90)]
    print("\n영어 또는 과학 90점 이상:")
    print(high_scores[['name', 'english', 'science']])


def data_aggregation(df):
    """데이터 집계"""
    print("\n[4] 데이터 집계 및 그룹화")
    print("-" * 60)

    # 전공별 평균 점수
    print("전공별 수학 평균:")
    print(df.groupby('major')['math'].mean())

    print("\n전공별 모든 과목 평균:")
    print(df.groupby('major')[['math', 'english', 'science']].mean())

    print("\n전공별 통계:")
    print(df.groupby('major')['math'].agg(['mean', 'max', 'min', 'count']))

    # 성별, 전공별 평균
    print("\n성별, 전공별 수학 평균:")
    print(df.groupby(['gender', 'major'])['math'].mean())


def data_transformation(df):
    """데이터 변환"""
    print("\n[5] 데이터 변환")
    print("-" * 60)

    df_copy = df.copy()

    # 총점 및 평균 계산
    df_copy['total'] = df_copy[['math', 'english', 'science']].sum(axis=1)
    df_copy['average'] = df_copy[['math', 'english', 'science']].mean(axis=1)

    # 등급 부여
    def get_grade(avg):
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        else:
            return 'D'

    df_copy['grade'] = df_copy['average'].apply(get_grade)

    # 등수
    df_copy['rank'] = df_copy['total'].rank(ascending=False, method='min')

    print("변환된 데이터:")
    print(df_copy[['name', 'total', 'average', 'grade', 'rank']])

    return df_copy


def data_sorting(df):
    """데이터 정렬"""
    print("\n[6] 데이터 정렬")
    print("-" * 60)

    # 수학 점수 내림차순
    print("수학 점수 내림차순:")
    print(df.sort_values('math', ascending=False)[['name', 'math']].head())

    # 전공, 나이 순으로 정렬
    print("\n전공, 나이 순 정렬:")
    print(df.sort_values(['major', 'age'])[['name', 'major', 'age']])


def save_csv_examples(df):
    """CSV 저장 예제"""
    print("\n[7] CSV 파일 저장")
    print("-" * 60)

    # 변환된 데이터 생성
    df_result = df.copy()
    df_result['total'] = df_result[['math', 'english', 'science']].sum(axis=1)
    df_result['average'] = df_result[['math', 'english', 'science']].mean(axis=1)

    # CSV 저장
    df_result.to_csv('students_result.csv', index=False, encoding='utf-8-sig')
    print("✓ students_result.csv 파일이 저장되었습니다.")

    # 특정 열만 저장
    df_result[['name', 'total', 'average']].to_csv(
        'students_summary.csv',
        index=False,
        encoding='utf-8-sig'
    )
    print("✓ students_summary.csv 파일이 저장되었습니다.")

    # 조건에 맞는 데이터만 저장
    high_achievers = df_result[df_result['average'] >= 85]
    high_achievers.to_csv(
        'high_achievers.csv',
        index=False,
        encoding='utf-8-sig'
    )
    print("✓ high_achievers.csv 파일이 저장되었습니다.")


def sales_analysis():
    """판매 데이터 분석"""
    print("\n[8] 판매 데이터 분석")
    print("-" * 60)

    # 데이터 읽기
    df_sales = pd.read_csv('sales.csv', encoding='utf-8-sig')
    df_sales['date'] = pd.to_datetime(df_sales['date'])

    print("판매 데이터:")
    print(df_sales.head(10))

    # 제품별 총 판매량
    print("\n제품별 총 판매량:")
    print(df_sales.groupby('product')['sales'].sum())

    # 제품별 평균 매출
    print("\n제품별 평균 매출:")
    print(df_sales.groupby('product')['revenue'].mean())

    # 일자별 총 매출
    print("\n일자별 총 매출 (상위 5일):")
    daily_revenue = df_sales.groupby('date')['revenue'].sum().sort_values(ascending=False)
    print(daily_revenue.head())

    # 주간별 집계
    df_sales['week'] = df_sales['date'].dt.isocalendar().week
    print("\n주간별 총 매출:")
    print(df_sales.groupby('week')['revenue'].sum())


def data_cleaning_example():
    """데이터 정제 예제"""
    print("\n[9] 데이터 정제")
    print("-" * 60)

    # 결측치와 이상치가 있는 데이터 생성
    dirty_data = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6, 7, 8],
        'name': ['A', 'B', 'C', 'D', None, 'F', 'G', 'H'],
        'age': [20, 25, None, 30, 22, 150, 28, 24],  # 150은 이상치
        'score': [85, 90, 88, None, 92, 78, 95, 89]
    })

    print("원본 데이터:")
    print(dirty_data)

    print("\n결측치 확인:")
    print(dirty_data.isnull().sum())

    # 결측치 처리
    df_clean = dirty_data.copy()

    # 이름의 결측치를 'Unknown'으로
    df_clean['name'].fillna('Unknown', inplace=True)

    # 나이의 결측치를 평균으로
    mean_age = df_clean['age'][df_clean['age'] < 100].mean()  # 이상치 제외
    df_clean['age'].fillna(mean_age, inplace=True)

    # 이상치 처리 (나이 100 이상을 평균으로)
    df_clean.loc[df_clean['age'] > 100, 'age'] = mean_age

    # 점수의 결측치를 중앙값으로
    df_clean['score'].fillna(df_clean['score'].median(), inplace=True)

    print("\n정제된 데이터:")
    print(df_clean)


def main():
    print("=" * 60)
    print("Pandas CSV 파일 처리 예제")
    print("=" * 60)

    # 샘플 CSV 파일 생성
    df, df_sales = create_sample_csv()

    # CSV 읽기
    df = read_csv_examples()

    # 데이터 탐색
    data_exploration(df)

    # 데이터 필터링
    data_filtering(df)

    # 데이터 집계
    data_aggregation(df)

    # 데이터 변환
    df_transformed = data_transformation(df)

    # 데이터 정렬
    data_sorting(df)

    # CSV 저장
    save_csv_examples(df)

    # 판매 데이터 분석
    sales_analysis()

    # 데이터 정제
    data_cleaning_example()

    print("\n" + "=" * 60)
    print("모든 예제가 완료되었습니다!")
    print("생성된 파일: students.csv, sales.csv, students_result.csv")
    print("             students_summary.csv, high_achievers.csv")
    print("=" * 60)


if __name__ == "__main__":
    main()
