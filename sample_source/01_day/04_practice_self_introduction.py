"""
파일명: 04_practice_self_introduction.py
설명: 실습 과제 - 자기소개 프로그램
Filename: 04_practice_self_introduction.py
Description: Practice assignment - Self-introduction program
"""

print("="*50)
print("자기소개 프로그램 (Self-Introduction Program)")
print("="*50)
print()

# 사용자 정보 입력받기 (Get user information)
name = input("이름을 입력하세요 (Enter your name): ")
age = input("나이를 입력하세요 (Enter your age): ")
job = input("직업을 입력하세요 (Enter your job): ")
hobby = input("취미를 입력하세요 (Enter your hobby): ")
location = input("거주 지역을 입력하세요 (Enter your location): ")

print()
print("="*50)
print("자기소개 (Self-Introduction)")
print("="*50)

# 방법 1: 기본 출력 (Method 1: Basic output)
print("이름:", name)
print("나이:", age, "세")
print("직업:", job)
print("취미:", hobby)
print("거주 지역:", location)

print()
print("="*50)

# 방법 2: f-string을 사용한 출력 (Method 2: Using f-string)
print(f"""
안녕하세요! 제 이름은 {name}입니다.
나이는 {age}세이고, 직업은 {job}입니다.
취미는 {hobby}를 즐기며, {location}에 살고 있습니다.

Hello! My name is {name}.
I am {age} years old and work as a {job}.
My hobby is {hobby}, and I live in {location}.
""")

print("="*50)

# 방법 3: 형식화된 출력 (Method 3: Formatted output)
print("\n┌" + "─"*48 + "┐")
print(f"│ {'항목 (Item)':<20} │ {'내용 (Content)':<22} │")
print("├" + "─"*48 + "┤")
print(f"│ {'이름 (Name)':<20} │ {name:<22} │")
print(f"│ {'나이 (Age)':<20} │ {age + '세 (' + age + ' years old)':<22} │")
print(f"│ {'직업 (Job)':<20} │ {job:<22} │")
print(f"│ {'취미 (Hobby)':<20} │ {hobby:<22} │")
print(f"│ {'거주 지역 (Location)':<20} │ {location:<22} │")
print("└" + "─"*48 + "┘")

print()

# 나이를 정수로 변환하여 추가 정보 출력 (Convert age to integer for additional info)
try:
    age_int = int(age)
    birth_year = 2024 - age_int + 1  # 한국 나이 기준 (Based on Korean age)

    print("="*50)
    print("추가 정보 (Additional Information)")
    print("="*50)
    print(f"출생 연도 (추정): {birth_year}년 (Estimated birth year: {birth_year})")
    print(f"10년 후 나이: {age_int + 10}세 (Age in 10 years: {age_int + 10})")
    print(f"20년 후 나이: {age_int + 20}세 (Age in 20 years: {age_int + 20})")

    # 연령대 판별 (Determine age group)
    if age_int < 20:
        age_group = "10대 (Teenager)"
    elif age_int < 30:
        age_group = "20대 (20s)"
    elif age_int < 40:
        age_group = "30대 (30s)"
    elif age_int < 50:
        age_group = "40대 (40s)"
    elif age_int < 60:
        age_group = "50대 (50s)"
    else:
        age_group = "60대 이상 (60s and above)"

    print(f"연령대: {age_group}")

except ValueError:
    # 나이가 숫자가 아닌 경우 (If age is not a number)
    print("\n※ 나이를 숫자로 입력하면 더 많은 정보를 볼 수 있습니다.")
    print("   (Enter age as a number to see more information)")

print("\n" + "="*50)
print("프로그램 종료 (Program ended)")
print("="*50)
