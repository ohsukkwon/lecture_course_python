# 14일차: 데이터 분석 & 시각화

## 학습 목표
- NumPy를 활용한 배열 연산 및 수치 계산
- Pandas를 활용한 데이터 처리 및 분석
- Matplotlib/Seaborn을 활용한 데이터 시각화
- 실전 데이터 분석 프로젝트 수행
- CSV/Excel 파일 읽기 및 처리

---

## 1. NumPy 기초

### 1.1 NumPy란?
- **Numerical Python**의 약자
- 다차원 배열 객체와 배열 연산을 위한 라이브러리
- 과학 계산, 데이터 분석의 기본 도구
- 빠른 연산 속도 (C언어 기반)

### 1.2 NumPy 설치
```bash
pip install numpy
```

### 1.3 배열 생성 및 기본 연산
```python
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # [1 2 3 4 5]
print(type(arr))  # <class 'numpy.ndarray'>

# 2차원 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)
print(arr2d.shape)  # (2, 3)

# 특수 배열 생성
zeros = np.zeros((3, 3))      # 0으로 채운 배열
ones = np.ones((2, 4))        # 1로 채운 배열
arange = np.arange(0, 10, 2)  # [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # 균등 분할

# 랜덤 배열
random_arr = np.random.rand(3, 3)  # 0~1 사이 난수
random_int = np.random.randint(1, 100, size=10)  # 정수 난수
```

### 1.4 배열 연산
```python
# 기본 연산
arr = np.array([1, 2, 3, 4, 5])

print(arr + 10)    # [11 12 13 14 15]
print(arr * 2)     # [ 2  4  6  8 10]
print(arr ** 2)    # [ 1  4  9 16 25]

# 배열 간 연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)  # [5 7 9]
print(arr1 * arr2)  # [ 4 10 18]

# 통계 함수
data = np.array([10, 20, 30, 40, 50])

print(np.sum(data))    # 150
print(np.mean(data))   # 30.0
print(np.std(data))    # 14.14... (표준편차)
print(np.min(data))    # 10
print(np.max(data))    # 50
print(np.median(data)) # 30.0
```

### 1.5 인덱싱과 슬라이싱
```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])      # 10
print(arr[-1])     # 50
print(arr[1:4])    # [20 30 40]

# 2차원 배열
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d[0, 0])    # 1
print(arr2d[1, 2])    # 6
print(arr2d[:, 0])    # [1 4 7] (첫 번째 열)
print(arr2d[0, :])    # [1 2 3] (첫 번째 행)

# 조건 인덱싱
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])   # [4 5]
```

---

## 2. Pandas 기초

### 2.1 Pandas란?
- 데이터 조작 및 분석을 위한 라이브러리
- **DataFrame**: 표 형태의 데이터 구조 (엑셀과 유사)
- **Series**: 1차원 데이터 구조
- 데이터 전처리, 정제, 분석의 핵심 도구

### 2.2 Pandas 설치
```bash
pip install pandas
```

### 2.3 Series와 DataFrame
```python
import pandas as pd

# Series 생성
s = pd.Series([10, 20, 30, 40, 50])
print(s)

s_named = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s_named['a'])  # 10

# DataFrame 생성
data = {
    'name': ['철수', '영희', '민수'],
    'age': [25, 23, 27],
    'score': [85, 92, 78]
}
df = pd.DataFrame(data)
print(df)

#    name  age  score
# 0   철수   25     85
# 1   영희   23     92
# 2   민수   27     78
```

### 2.4 데이터 읽기/쓰기
```python
# CSV 파일 읽기
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', encoding='utf-8')

# Excel 파일 읽기
df = pd.read_excel('data.xlsx')

# CSV 파일 쓰기
df.to_csv('output.csv', index=False)

# Excel 파일 쓰기
df.to_excel('output.xlsx', index=False)
```

### 2.5 데이터 탐색
```python
# 데이터프레임 정보 확인
df.head()         # 처음 5행
df.tail()         # 마지막 5행
df.info()         # 데이터 타입 및 결측치 정보
df.describe()     # 통계 요약
df.shape          # (행, 열) 크기
df.columns        # 열 이름
df.dtypes         # 각 열의 데이터 타입

# 특정 열 선택
df['name']        # Series로 반환
df[['name', 'age']]  # DataFrame으로 반환

# 특정 행 선택
df.loc[0]         # 첫 번째 행 (레이블 기반)
df.iloc[0]        # 첫 번째 행 (위치 기반)
df.loc[0:2]       # 0~2행
```

### 2.6 데이터 필터링
```python
# 조건 필터링
df[df['age'] > 25]               # 나이가 25보다 큰 행
df[df['score'] >= 80]            # 점수가 80 이상인 행
df[(df['age'] > 20) & (df['score'] > 80)]  # 복합 조건

# 여러 조건
high_score = df[df['score'] > 85]
young = df[df['age'] < 25]
```

### 2.7 데이터 정렬
```python
# 정렬
df.sort_values('score')                    # 점수 오름차순
df.sort_values('score', ascending=False)   # 점수 내림차순
df.sort_values(['age', 'score'])           # 다중 정렬
```

### 2.8 데이터 집계 및 그룹화
```python
# 기본 통계
df['score'].mean()    # 평균
df['score'].sum()     # 합계
df['score'].max()     # 최댓값
df['score'].min()     # 최솟값

# 그룹화
df.groupby('age')['score'].mean()    # 나이별 평균 점수
df.groupby('age').agg({
    'score': ['mean', 'max', 'min']
})
```

### 2.9 결측치 처리
```python
# 결측치 확인
df.isnull()         # 결측치 위치 (True/False)
df.isnull().sum()   # 각 열의 결측치 개수

# 결측치 처리
df.dropna()                    # 결측치가 있는 행 삭제
df.fillna(0)                   # 결측치를 0으로 채움
df['score'].fillna(df['score'].mean())  # 평균값으로 채움
```

### 2.10 새 열 추가 및 수정
```python
# 새 열 추가
df['grade'] = ['A', 'A', 'B']
df['passed'] = df['score'] >= 80

# 열 수정
df['score'] = df['score'] + 5

# 열 삭제
df.drop('grade', axis=1, inplace=True)
```

---

## 3. 데이터 시각화

### 3.1 Matplotlib 기초

#### 설치
```bash
pip install matplotlib
```

#### 기본 그래프
```python
import matplotlib.pyplot as plt

# 선 그래프
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.grid(True)
plt.show()

# 막대 그래프
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]

plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()

# 산점도
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, color='red', marker='o')
plt.title('Scatter Plot')
plt.show()

# 히스토그램
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]

plt.hist(data, bins=5, edgecolor='black')
plt.title('Histogram')
plt.show()
```

#### 여러 그래프 그리기
```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 첫 번째 그래프
axes[0, 0].plot([1, 2, 3], [1, 4, 9])
axes[0, 0].set_title('Plot 1')

# 두 번째 그래프
axes[0, 1].bar(['A', 'B', 'C'], [10, 20, 15])
axes[0, 1].set_title('Plot 2')

# 세 번째 그래프
axes[1, 0].scatter([1, 2, 3], [2, 4, 6])
axes[1, 0].set_title('Plot 3')

# 네 번째 그래프
axes[1, 1].hist([1, 2, 2, 3, 3, 3], bins=3)
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
```

### 3.2 Seaborn으로 고급 시각화

#### 설치
```bash
pip install seaborn
```

#### Seaborn 기본
```python
import seaborn as sns
import pandas as pd

# 샘플 데이터
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'value': [10, 20, 15, 12, 25, 18]
})

# 막대 그래프
sns.barplot(data=df, x='category', y='value')
plt.show()

# 박스 플롯
sns.boxplot(data=df, x='category', y='value')
plt.show()

# 바이올린 플롯
sns.violinplot(data=df, x='category', y='value')
plt.show()

# 히트맵 (상관관계)
corr_data = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [2, 4, 6, 8],
    'C': [3, 5, 7, 9]
})

sns.heatmap(corr_data.corr(), annot=True, cmap='coolwarm')
plt.show()
```

### 3.3 Pandas와 시각화 연동
```python
import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임에서 직접 그래프 생성
df = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [100, 120, 140, 110, 150]
})

# 선 그래프
df.plot(x='month', y='sales', kind='line', marker='o')
plt.show()

# 막대 그래프
df.plot(x='month', y='sales', kind='bar')
plt.show()
```

---

## 4. 실전 데이터 분석 프로젝트

### 4.1 프로젝트: 판매 데이터 분석

```python
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 생성 (실제로는 CSV에서 읽어옴)
data = {
    'date': ['2024-01', '2024-02', '2024-03', '2024-04', '2024-05'],
    'product': ['A', 'B', 'A', 'B', 'A'],
    'sales': [100, 150, 120, 180, 140],
    'cost': [60, 90, 70, 100, 80]
}
df = pd.DataFrame(data)

# 1. 데이터 탐색
print("=== 데이터 정보 ===")
print(df.info())
print("\n=== 통계 요약 ===")
print(df.describe())

# 2. 이익 계산
df['profit'] = df['sales'] - df['cost']

# 3. 제품별 총 매출
product_sales = df.groupby('product')['sales'].sum()
print("\n=== 제품별 총 매출 ===")
print(product_sales)

# 4. 시각화
plt.figure(figsize=(12, 4))

# 월별 매출 추이
plt.subplot(1, 3, 1)
plt.plot(df['date'], df['sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xticks(rotation=45)

# 제품별 매출
plt.subplot(1, 3, 2)
product_sales.plot(kind='bar')
plt.title('Sales by Product')

# 매출 vs 비용
plt.subplot(1, 3, 3)
plt.scatter(df['cost'], df['sales'])
plt.xlabel('Cost')
plt.ylabel('Sales')
plt.title('Cost vs Sales')

plt.tight_layout()
plt.show()
```

### 4.2 프로젝트: 학생 성적 분석

```python
# 학생 성적 데이터
students = pd.DataFrame({
    'name': ['철수', '영희', '민수', '지영', '수현', '민지'],
    'math': [85, 92, 78, 95, 88, 82],
    'english': [90, 88, 85, 92, 86, 89],
    'science': [88, 90, 80, 93, 91, 85]
})

# 총점 및 평균 계산
students['total'] = students[['math', 'english', 'science']].sum(axis=1)
students['average'] = students[['math', 'english', 'science']].mean(axis=1)

# 등수 매기기
students['rank'] = students['total'].rank(ascending=False)

# 상위 3명
top3 = students.nlargest(3, 'total')
print("=== 상위 3명 ===")
print(top3[['name', 'total', 'average']])

# 과목별 평균
subject_avg = students[['math', 'english', 'science']].mean()
print("\n=== 과목별 평균 ===")
print(subject_avg)

# 시각화
students.set_index('name')[['math', 'english', 'science']].plot(kind='bar', figsize=(10, 6))
plt.title('Student Scores by Subject')
plt.ylabel('Score')
plt.legend(title='Subject')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## 5. 실전 팁

### 5.1 한글 폰트 설정 (Matplotlib)
```python
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# 또는
import platform
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin':  # macOS
    plt.rc('font', family='AppleGothic')
```

### 5.2 데이터 전처리 체크리스트
```python
# 1. 데이터 로드
df = pd.read_csv('data.csv')

# 2. 기본 정보 확인
print(df.head())
print(df.info())
print(df.describe())

# 3. 결측치 확인
print(df.isnull().sum())

# 4. 중복 제거
df.drop_duplicates(inplace=True)

# 5. 데이터 타입 변환
df['date'] = pd.to_datetime(df['date'])

# 6. 이상치 제거 (IQR 방법)
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['value'] >= Q1 - 1.5*IQR) & (df['value'] <= Q3 + 1.5*IQR)]
```

---

## 실습 과제

### 과제 1: NumPy 배열 연산
- 1~100 사이의 난수 배열 생성
- 평균, 표준편차, 최댓값, 최솟값 계산
- 평균보다 큰 값만 필터링

### 과제 2: CSV 데이터 분석
- CSV 파일을 읽어서 데이터프레임 생성
- 결측치 처리
- 특정 조건으로 필터링
- 그룹별 통계 계산

### 과제 3: 데이터 시각화
- 여러 종류의 그래프 작성 (선, 막대, 산점도, 히스토그램)
- 서브플롯으로 여러 그래프 동시 표시

### 과제 4: 종합 분석 프로젝트
- 실제 데이터셋 다운로드 (Kaggle, 공공데이터포털)
- 탐색적 데이터 분석 (EDA)
- 인사이트 도출 및 시각화
- 분석 보고서 작성

### 과제 5: 대시보드 만들기
- 여러 차트를 조합한 대시보드 구성
- 주요 지표 요약
- 시각적으로 보기 좋은 레이아웃

---

## 추가 학습 자료

### 추천 데이터셋
- **Kaggle**: 다양한 데이터셋 및 경진대회
- **공공데이터포털**: 한국 정부 공개 데이터
- **UCI Machine Learning Repository**: 머신러닝 데이터셋
- **Seaborn 내장 데이터**: `sns.load_dataset()`

### 다음 단계 학습
- **고급 Pandas**: MultiIndex, Pivot Table, Time Series
- **머신러닝**: Scikit-learn을 활용한 예측 모델
- **딥러닝**: TensorFlow/PyTorch 입문
- **대시보드**: Streamlit, Dash, Plotly

### 유용한 라이브러리
- **Plotly**: 인터랙티브 시각화
- **Streamlit**: 웹 기반 데이터 앱
- **Jupyter Notebook**: 대화형 분석 환경
- **Scikit-learn**: 머신러닝 라이브러리

---

## 과정 수료를 축하합니다!

14일간의 파이썬 여정을 완주하셨습니다! 이제 여러분은:

- ✅ 파이썬 기본 문법을 마스터했습니다
- ✅ 데이터 구조와 알고리즘을 이해했습니다
- ✅ 객체지향 프로그래밍을 활용할 수 있습니다
- ✅ 데이터 분석과 시각화를 수행할 수 있습니다

### 앞으로의 여정

**단기 목표 (1-3개월)**
- 개인 프로젝트 1개 완성하기
- GitHub에 코드 업로드하기
- 온라인 코딩 챌린지 참여

**중기 목표 (3-6개월)**
- 웹 개발 또는 데이터 분석 특화
- 포트폴리오 3-5개 구축
- 오픈소스 프로젝트 기여

**장기 목표 (6-12개월)**
- 실무 프로젝트 경험
- 기술 블로그 운영
- 커뮤니티 활동 및 네트워킹

**계속 학습하고, 코딩하고, 성장하세요!**
