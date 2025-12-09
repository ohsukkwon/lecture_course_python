# 1일차: 파이썬 소개 및 환경 설정

## 학습 목표
- 파이썬의 특징과 활용 분야 이해
- 파이썬 개발 환경 구축하기
- 첫 프로그램 작성 및 실행하기
- 기본 입출력 이해하기

---

## 1. 파이썬이란?

### 1.1 파이썬의 정의
- 1991년 귀도 반 로섬(Guido van Rossum)이 개발한 고급 프로그래밍 언어
- 간결하고 읽기 쉬운 문법으로 초보자도 쉽게 배울 수 있음
- 인터프리터 언어로 즉시 실행 가능

### 1.2 파이썬의 특징

**1) 간결하고 읽기 쉬운 문법**
```python
# Python
print("Hello, World!")

// Java (비교)
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**2) 다양한 플랫폼 지원**
- Windows, macOS, Linux 등 모든 운영체제에서 실행 가능

**3) 풍부한 라이브러리**
- 표준 라이브러리와 수많은 외부 패키지 지원
- 거의 모든 작업을 라이브러리로 처리 가능

**4) 객체지향 프로그래밍 지원**
- 클래스와 객체를 이용한 체계적인 프로그래밍

**5) 동적 타이핑**
- 변수 타입을 미리 선언할 필요 없음
- 실행 시간에 자동으로 타입 결정

### 1.3 파이썬의 활용 분야

| 분야 | 설명 | 주요 라이브러리 |
|------|------|-----------------|
| 웹 개발 | 웹 애플리케이션 개발 | Django, Flask, FastAPI |
| 데이터 분석 | 데이터 처리 및 분석 | Pandas, NumPy, Matplotlib |
| 인공지능/머신러닝 | AI 모델 개발 및 학습 | TensorFlow, PyTorch, scikit-learn |
| 자동화 | 반복 작업 자동화 | Selenium, PyAutoGUI |
| 과학 계산 | 수치 계산 및 시뮬레이션 | SciPy, SymPy |
| 게임 개발 | 2D 게임 개발 | Pygame |

---

## 2. 파이썬 설치

### 2.1 Windows 설치

1. **공식 웹사이트 접속**
   - https://www.python.org/downloads/

2. **최신 버전 다운로드**
   - "Download Python 3.x.x" 버튼 클릭

3. **설치 진행**
   - ✅ "Add Python to PATH" 체크 (매우 중요!)
   - "Install Now" 클릭

4. **설치 확인**
```bash
python --version
# 또는
python3 --version
```

### 2.2 macOS 설치

**방법 1: 공식 인스톨러**
```bash
# 공식 웹사이트에서 다운로드 후 설치
python3 --version
```

**방법 2: Homebrew 이용**
```bash
# Homebrew 설치 후
brew install python3
python3 --version
```

### 2.3 Linux 설치

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# 확인
python3 --version
```

---

## 3. 개발 환경 구축

### 3.1 통합 개발 환경 (IDE) 소개

#### Visual Studio Code (VS Code) - 추천
- **장점**: 가볍고 빠르며, 확장 기능 풍부
- **다운로드**: https://code.visualstudio.com/

**VS Code 설정**
1. VS Code 설치
2. Extensions에서 "Python" 검색 후 설치 (Microsoft 제공)
3. Extensions에서 "Pylance" 설치 (코드 자동완성)

#### PyCharm
- **장점**: 파이썬 전용 IDE, 강력한 디버깅 기능
- **다운로드**: https://www.jetbrains.com/pycharm/
- **버전**: Community Edition (무료) 또는 Professional (유료)

#### Jupyter Notebook
- **장점**: 데이터 분석 및 시각화에 최적화
- **설치**:
```bash
pip install jupyter
jupyter notebook
```

### 3.2 가상 환경 (Virtual Environment)

프로젝트별로 독립적인 파이썬 환경을 만들어 패키지 충돌 방지

```bash
# 가상 환경 생성
python -m venv myenv

# 활성화
# Windows
myenv\Scripts\activate

# macOS/Linux
source myenv/bin/activate

# 비활성화
deactivate
```

---

## 4. 첫 프로그램 작성

### 4.1 대화형 모드 (Interactive Mode)

터미널에서 Python 실행:
```bash
python
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 3
5
>>> exit()
```

### 4.2 스크립트 모드 (Script Mode)

파일로 저장하여 실행:

**hello.py**
```python
print("Hello, World!")
```

**실행**
```bash
python hello.py
```

### 4.3 기본 출력 함수

```python
# 기본 출력
print("안녕하세요!")

# 여러 값 출력
print("Python", "Programming", "2024")

# 구분자 변경
print("Apple", "Banana", "Cherry", sep=", ")

# 줄바꿈 제거
print("Hello", end=" ")
print("World")  # 결과: Hello World
```

---

## 5. 기본 입출력

### 5.1 input() 함수

사용자로부터 입력 받기:
```python
name = input("이름을 입력하세요: ")
print("안녕하세요,", name, "님!")
```

**주의**: input()은 항상 문자열(str)을 반환합니다!

### 5.2 형 변환과 입력

```python
# 숫자 입력 받기
age = int(input("나이를 입력하세요: "))
print(f"당신은 {age}살입니다.")

# 실수 입력 받기
height = float(input("키를 입력하세요 (cm): "))
print(f"당신의 키는 {height}cm입니다.")
```

---

## 6. 주석 (Comments)

### 6.1 한 줄 주석

```python
# 이것은 한 줄 주석입니다
print("Hello")  # 코드 옆에도 작성 가능
```

### 6.2 여러 줄 주석

```python
"""
이것은 여러 줄 주석입니다.
여러 줄에 걸쳐 설명을 작성할 수 있습니다.
docstring으로도 사용됩니다.
"""

'''
작은따옴표 3개로도 가능합니다.
'''
```

---

## 7. 코딩 스타일 가이드 (PEP 8)

### 7.1 들여쓰기
- 공백 4칸 사용 (탭 대신 스페이스)

### 7.2 변수명 규칙
```python
# Good
user_name = "John"
user_age = 25

# Bad
userName = "John"  # camelCase는 함수/메서드명에 사용
UserName = "John"  # PascalCase는 클래스명에 사용
```

### 7.3 줄 길이
- 한 줄은 최대 79자

### 7.4 공백
```python
# Good
x = 5
result = x + 10

# Bad
x=5
result=x+10
```

---

## 실습 과제

### 과제 1: 파이썬 설치 확인
1. Python 최신 버전 설치
2. 터미널에서 `python --version` 실행하여 버전 확인
3. 스크린샷 캡처

### 과제 2: IDE 설정
1. VS Code 또는 PyCharm 설치
2. Python 확장 프로그램 설치
3. 새 파이썬 파일 생성 및 "Hello, World!" 출력

### 과제 3: 자기소개 프로그램
사용자로부터 이름, 나이, 직업을 입력받아 자기소개를 출력하는 프로그램 작성

**실행 예시:**
```
이름을 입력하세요: 김철수
나이를 입력하세요: 25
직업을 입력하세요: 학생

=== 자기소개 ===
이름: 김철수
나이: 25세
직업: 학생
```

### 과제 4: 간단한 계산 프로그램
두 개의 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 출력하는 프로그램 작성

---

## 참고 자료

- 공식 문서: https://docs.python.org/ko/3/
- PEP 8 스타일 가이드: https://peps.python.org/pep-0008/
- Python 튜토리얼: https://docs.python.org/ko/3/tutorial/

---

## 다음 시간 예고

2일차에는 **변수, 자료형, 연산자**에 대해 학습합니다.
- 다양한 자료형 (int, float, str, bool)
- 형 변환 (Type Casting)
- 다양한 연산자 활용
- 문자열 포맷팅

**미리 준비**: 계산기를 사용해 본 경험 되돌아보기
