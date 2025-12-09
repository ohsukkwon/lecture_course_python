# 12일차: 실전 라이브러리 활용 및 최종 프로젝트

## 학습 목표
- 정규표현식(Regular Expression) 활용
- 웹 크롤링 기초 (requests, BeautifulSoup)
- 데이터 분석 기초 (pandas, numpy)
- API 활용하기
- 최종 프로젝트 개발

---

## 1. 정규표현식 (Regular Expression)

### 1.1 re 모듈 기본

```python
import re

# 패턴 매칭
text = "My phone number is 010-1234-5678"
pattern = r'\d{3}-\d{4}-\d{4}'

match = re.search(pattern, text)
if match:
    print(f"찾음: {match.group()}")  # 010-1234-5678

# 모든 매칭 찾기
text = "Email: abc@example.com, xyz@test.com"
pattern = r'\w+@\w+\.\w+'
emails = re.findall(pattern, text)
print(emails)  # ['abc@example.com', 'xyz@test.com']
```

### 1.2 주요 패턴

| 패턴 | 설명 |
|------|------|
| `.` | 임의의 한 문자 |
| `^` | 문자열 시작 |
| `$` | 문자열 끝 |
| `*` | 0회 이상 반복 |
| `+` | 1회 이상 반복 |
| `?` | 0회 또는 1회 |
| `{n}` | 정확히 n회 |
| `{n,}` | n회 이상 |
| `{n,m}` | n~m회 |
| `\d` | 숫자 [0-9] |
| `\w` | 문자, 숫자, _ |
| `\s` | 공백 문자 |
| `[abc]` | a, b, c 중 하나 |
| `[^abc]` | a, b, c가 아닌 것 |

### 1.3 실전 예제

```python
import re

# 이메일 검증
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# 전화번호 추출
def extract_phone_numbers(text):
    pattern = r'01\d-\d{3,4}-\d{4}'
    return re.findall(pattern, text)

# 문자열 치환
def mask_phone_number(text):
    pattern = r'(01\d)-(\d{3,4})-(\d{4})'
    return re.sub(pattern, r'\1-****-\2', text)

print(validate_email("test@example.com"))  # True
print(extract_phone_numbers("010-1234-5678, 011-987-6543"))
print(mask_phone_number("내 번호는 010-1234-5678입니다"))
```

---

## 2. 웹 크롤링 (Web Scraping)

### 2.1 requests 라이브러리

```python
import requests

# GET 요청
response = requests.get("https://example.com")
print(response.status_code)  # 200
print(response.text)  # HTML 내용

# POST 요청
data = {"username": "user", "password": "pass"}
response = requests.post("https://api.example.com/login", data=data)

# JSON API
response = requests.get("https://api.example.com/users")
users = response.json()
```

### 2.2 BeautifulSoup

```python
from bs4 import BeautifulSoup
import requests

# 웹 페이지 가져오기
url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 태그 찾기
title = soup.find('title')
print(title.text)

# 여러 태그 찾기
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# CSS 선택자
paragraphs = soup.select('p.content')
for p in paragraphs:
    print(p.text)
```

### 2.3 실전 크롤링 예제

```python
import requests
from bs4 import BeautifulSoup

def crawl_news_titles(url):
    """뉴스 제목 크롤링"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # 제목 추출 (사이트 구조에 따라 선택자 변경 필요)
        titles = soup.select('h2.news-title')

        return [title.text.strip() for title in titles]

    except requests.RequestException as e:
        print(f"오류 발생: {e}")
        return []

# 사용
# titles = crawl_news_titles("https://news.example.com")
# for title in titles:
#     print(title)
```

---

## 3. 데이터 분석 기초

### 3.1 NumPy

```python
import numpy as np

# 배열 생성
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 다차원 배열
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # (2, 3)

# 배열 연산
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # [5 7 9]
print(arr1 * 2)     # [2 4 6]

# 통계 함수
data = np.array([10, 20, 30, 40, 50])
print(np.mean(data))   # 평균: 30.0
print(np.median(data)) # 중앙값: 30.0
print(np.std(data))    # 표준편차: 14.14
```

### 3.2 Pandas

```python
import pandas as pd

# DataFrame 생성
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Incheon']
}
df = pd.DataFrame(data)
print(df)

# CSV 읽기/쓰기
# df = pd.read_csv('data.csv')
# df.to_csv('output.csv', index=False)

# 데이터 조회
print(df['name'])  # 열 선택
print(df.loc[0])   # 행 선택
print(df[df['age'] > 25])  # 조건 필터링

# 통계
print(df.describe())  # 기술통계
print(df['age'].mean())  # 평균

# 그룹화
grouped = df.groupby('city')['age'].mean()
print(grouped)
```

### 3.3 matplotlib (시각화)

```python
import matplotlib.pyplot as plt
import numpy as np

# 선 그래프
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# 막대 그래프
categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 55]
plt.bar(categories, values)
plt.title('Bar Chart')
plt.show()

# 히스토그램
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()
```

---

## 4. API 활용

### 4.1 REST API 기본

```python
import requests

# 공개 API 예제 (JSONPlaceholder)
base_url = "https://jsonplaceholder.typicode.com"

# GET - 데이터 조회
response = requests.get(f"{base_url}/posts/1")
post = response.json()
print(post['title'])

# POST - 데이터 생성
new_post = {
    'title': 'New Post',
    'body': 'This is content',
    'userId': 1
}
response = requests.post(f"{base_url}/posts", json=new_post)
print(response.status_code)  # 201

# PUT - 데이터 수정
updated_post = {'title': 'Updated Title'}
response = requests.put(f"{base_url}/posts/1", json=updated_post)

# DELETE - 데이터 삭제
response = requests.delete(f"{base_url}/posts/1")
```

### 4.2 API 래퍼 클래스

```python
import requests

class APIClient:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = self.session.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

# 사용
# client = APIClient("https://api.example.com", "your-api-key")
# data = client.get("users")
```

---

## 5. 최종 프로젝트 아이디어

### 5.1 프로젝트 1: 할 일 관리 애플리케이션

**기능:**
- 할 일 추가, 수정, 삭제
- 완료 표시
- 날짜별 필터링
- JSON 파일로 저장

**기술 스택:**
- 파일 입출력
- JSON 처리
- 객체지향 설계

### 5.2 프로젝트 2: 웹 크롤링 + 데이터 분석

**기능:**
- 특정 웹사이트에서 데이터 수집
- 데이터 정제 및 분석
- 결과 시각화
- CSV로 저장

**기술 스택:**
- requests, BeautifulSoup
- pandas, matplotlib
- 정규표현식

### 5.3 프로젝트 3: 간단한 블로그 시스템

**기능:**
- 게시글 작성, 조회, 수정, 삭제
- 카테고리 관리
- 검색 기능
- 파일로 저장

**기술 스택:**
- 객체지향 설계
- 파일 입출력
- 정규표현식

### 5.4 프로젝트 4: API 기반 날씨 애플리케이션

**기능:**
- 실시간 날씨 정보 조회
- 여러 도시 날씨 비교
- 날씨 데이터 저장 및 히스토리
- 데이터 시각화

**기술 스택:**
- REST API (OpenWeatherMap 등)
- JSON 처리
- pandas, matplotlib

### 5.5 프로젝트 5: 학생 성적 관리 시스템

**기능:**
- 학생 정보 관리 (CRUD)
- 성적 입력 및 조회
- 통계 분석 (평균, 등급 등)
- CSV 파일 import/export

**기술 스택:**
- 객체지향 설계
- CSV 처리
- pandas
- 예외 처리

---

## 6. 프로젝트 진행 가이드

### 6.1 프로젝트 단계

1. **요구사항 분석**
   - 기능 정의
   - 사용자 스토리 작성

2. **설계**
   - 클래스 다이어그램
   - 데이터 구조 설계
   - 파일 구조 설계

3. **구현**
   - 기능별 모듈 개발
   - 점진적 개발 (작은 단위부터)
   - 테스트 병행

4. **테스트**
   - 단위 테스트
   - 통합 테스트
   - 사용자 시나리오 테스트

5. **문서화**
   - README.md 작성
   - 주석 추가
   - 사용 설명서

### 6.2 코드 구조 예시

```
project/
│
├── main.py              # 메인 실행 파일
├── models/              # 데이터 모델
│   ├── __init__.py
│   └── user.py
├── services/            # 비즈니스 로직
│   ├── __init__.py
│   └── user_service.py
├── utils/               # 유틸리티 함수
│   ├── __init__.py
│   └── file_handler.py
├── data/                # 데이터 파일
│   └── users.json
├── tests/               # 테스트 코드
│   └── test_user.py
└── README.md            # 프로젝트 설명
```

---

## 7. 추가 학습 자료

### 7.1 다음 단계 학습 주제

**웹 개발:**
- Django / Flask 프레임워크
- FastAPI
- HTML, CSS, JavaScript 기초

**데이터 분석:**
- 고급 Pandas 기법
- 데이터 시각화 (Seaborn, Plotly)
- SQL과 데이터베이스

**머신러닝:**
- scikit-learn
- TensorFlow / PyTorch
- 데이터 전처리

**자동화:**
- Selenium (웹 자동화)
- 스케줄링 (APScheduler, Celery)
- API 개발

### 7.2 추천 리소스

- 공식 문서: https://docs.python.org/ko/3/
- Real Python: https://realpython.com/
- Python Package Index (PyPI): https://pypi.org/
- GitHub: 오픈소스 프로젝트 참여

---

## 최종 실습 과제

### 통합 프로젝트: 개인 선택
위의 프로젝트 아이디어 중 하나를 선택하거나 자신만의 프로젝트를 기획하여 개발합니다.

**제출 내용:**
1. 소스 코드
2. README.md (프로젝트 설명, 사용법)
3. 실행 결과 스크린샷
4. 회고 (어려웠던 점, 배운 점)

---

## 수료 후 학습 로드맵

1. **심화 학습**: 선택한 분야의 심화 과정
2. **실전 프로젝트**: 포트폴리오 프로젝트 개발
3. **오픈소스 참여**: GitHub에서 프로젝트 기여
4. **커뮤니티 활동**: 기술 블로그, 스터디 참여
5. **지속적 학습**: 최신 트렌드 팔로우

---

**축하합니다! 12일 파이썬 기초 과정을 완료하셨습니다!** 🎉

이제 여러분은 파이썬의 기초를 탄탄히 다지고, 실전 프로젝트를 개발할 수 있는 역량을 갖추었습니다. 계속해서 학습하고 실습하며 실력을 향상시키세요!
