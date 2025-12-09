"""
파일명: 06_practice_string_processing.py
설명: 실습 과제 - 문자열 처리 및 환율 계산기
Filename: 06_practice_string_processing.py
Description: Practice assignment - String processing and currency converter
"""

# ===== 실습 1: 문자열 처리 (String Processing) =====

print("="*60)
print("실습 1: 문자열 처리 (String Processing)")
print("="*60)
print()

# 사용자로부터 문장 입력받기 (Get sentence from user)
sentence = input("문장을 입력하세요 (Enter a sentence): ")

print("\n" + "="*60)
print("분석 결과 (Analysis Results)")
print("="*60)

# 1. 전체 길이 (Total length)
length = len(sentence)
print(f"1. 전체 길이 (Length): {length}자")

# 2. 대문자로 변환 (Convert to uppercase)
uppercase = sentence.upper()
print(f"2. 대문자 (Uppercase): {uppercase}")

# 3. 소문자로 변환 (Convert to lowercase)
lowercase = sentence.lower()
print(f"3. 소문자 (Lowercase): {lowercase}")

# 4. 단어 개수 (Word count)
words = sentence.split()
word_count = len(words)
print(f"4. 단어 개수 (Word count): {word_count}개")

# 5. 역순 출력 (Reverse)
reversed_sentence = sentence[::-1]
print(f"5. 역순 (Reversed): {reversed_sentence}")

# 추가 분석 (Additional analysis)
print("\n" + "-"*60)
print("추가 분석 (Additional Analysis)")
print("-"*60)

# 6. 첫 글자 대문자 (Capitalize first letter)
capitalized = sentence.capitalize()
print(f"6. 첫 글자 대문자 (Capitalized): {capitalized}")

# 7. 각 단어 첫 글자 대문자 (Title case)
title_case = sentence.title()
print(f"7. 각 단어 첫 글자 대문자 (Title): {title_case}")

# 8. 공백 제거 (Remove whitespace)
stripped = sentence.strip()
print(f"8. 양쪽 공백 제거 (Stripped): '{stripped}'")

# 9. 특정 문자 개수 세기 (Count specific character)
if sentence:
    first_char = sentence[0]
    count = sentence.count(first_char)
    print(f"9. '{first_char}' 문자 개수 (Count): {count}개")

# 10. 문자 타입 분석 (Character type analysis)
alpha_count = sum(c.isalpha() for c in sentence)
digit_count = sum(c.isdigit() for c in sentence)
space_count = sum(c.isspace() for c in sentence)
special_count = len(sentence) - alpha_count - digit_count - space_count

print(f"\n10. 문자 타입 분석 (Character Type Analysis):")
print(f"    - 알파벳 (Alphabets): {alpha_count}개")
print(f"    - 숫자 (Digits): {digit_count}개")
print(f"    - 공백 (Spaces): {space_count}개")
print(f"    - 특수문자 (Special chars): {special_count}개")

print()

# ===== 실습 2: 환율 계산기 (Currency Converter) =====

print("="*60)
print("실습 2: 환율 계산기 (Currency Converter)")
print("="*60)
print()

# 환율 정보 (2024년 기준 예시) (Exchange rates - 2024 example)
USD_TO_KRW = 1325.0  # 1 USD = 1,325 KRW
EUR_TO_KRW = 1445.0  # 1 EUR = 1,445 KRW
JPY_TO_KRW = 8.95  # 100 JPY = 895 KRW (per 100 yen)
CNY_TO_KRW = 182.5  # 1 CNY = 182.5 KRW

print("현재 환율 정보 (Current Exchange Rates)")
print("-"*60)
print(f"💵 USD (미국 달러): 1 USD = {USD_TO_KRW:,.2f} KRW")
print(f"💶 EUR (유로): 1 EUR = {EUR_TO_KRW:,.2f} KRW")
print(f"💴 JPY (일본 엔): 100 JPY = {JPY_TO_KRW * 100:,.2f} KRW")
print(f"💴 CNY (중국 위안): 1 CNY = {CNY_TO_KRW:,.2f} KRW")
print()

# 메뉴 출력 (Display menu)
print("변환할 통화를 선택하세요 (Choose currency to convert)")
print("-"*60)
print("1. USD (미국 달러) → KRW (원)")
print("2. EUR (유로) → KRW (원)")
print("3. JPY (일본 엔) → KRW (원)")
print("4. CNY (중국 위안) → KRW (원)")
print("5. 모든 통화 비교 (Compare all currencies)")
print()

# 사용자 선택 (User selection)
choice = input("선택 (Choice) [1-5]: ")

print()
print("="*60)

if choice in ['1', '2', '3', '4']:
    # 금액 입력 (Enter amount)
    amount = float(input("금액을 입력하세요 (Enter amount): "))

    # 환율 계산 (Calculate exchange)
    if choice == '1':
        currency_name = "USD (미국 달러)"
        symbol = "💵"
        rate = USD_TO_KRW
        converted = amount * rate
    elif choice == '2':
        currency_name = "EUR (유로)"
        symbol = "💶"
        rate = EUR_TO_KRW
        converted = amount * rate
    elif choice == '3':
        currency_name = "JPY (일본 엔)"
        symbol = "💴"
        rate = JPY_TO_KRW
        converted = amount * rate
    else:  # choice == '4'
        currency_name = "CNY (중국 위안)"
        symbol = "💴"
        rate = CNY_TO_KRW
        converted = amount * rate

    # 결과 출력 (Display result)
    print(f"\n{symbol} 환율 계산 결과 (Exchange Result)")
    print("="*60)
    print(f"통화 (Currency): {currency_name}")
    print(f"환율 (Rate): 1 = {rate:,.2f} KRW")
    print(f"금액 (Amount): {amount:,.2f}")
    print("-"*60)
    print(f"변환 결과 (Result): {converted:,.2f} KRW")
    print("="*60)

    # 추가 정보 (Additional info)
    print(f"\n역환율 (Reverse rate): 1 KRW = {1/rate:.4f}")

    # 수수료 적용 (Apply commission)
    commission_rate = 0.02  # 2% 수수료
    commission = converted * commission_rate
    final_amount = converted - commission

    print(f"\n💡 참고: 실제 환전 시 수수료 적용 (2%)")
    print(f"   수수료 (Commission): -{commission:,.2f} KRW")
    print(f"   실수령액 (Final amount): {final_amount:,.2f} KRW")

elif choice == '5':
    # 모든 통화 비교 (Compare all currencies)
    print("모든 통화 비교 (Currency Comparison)")
    print("="*60)

    base_amount = float(input("기준 금액을 입력하세요 (Enter base amount): "))

    print(f"\n{base_amount:,.0f}원을 외화로 환전하면:")
    print("-"*60)

    usd_amount = base_amount / USD_TO_KRW
    eur_amount = base_amount / EUR_TO_KRW
    jpy_amount = base_amount / JPY_TO_KRW
    cny_amount = base_amount / CNY_TO_KRW

    print(f"💵 USD: {usd_amount:,.2f} 달러")
    print(f"💶 EUR: {eur_amount:,.2f} 유로")
    print(f"💴 JPY: {jpy_amount:,.2f} 엔")
    print(f"💴 CNY: {cny_amount:,.2f} 위안")

    print(f"\n외화를 원화로 환전하면:")
    print("-"*60)

    print(f"💵 {base_amount:,.0f} USD = {base_amount * USD_TO_KRW:,.2f} KRW")
    print(f"💶 {base_amount:,.0f} EUR = {base_amount * EUR_TO_KRW:,.2f} KRW")
    print(f"💴 {base_amount:,.0f} JPY = {base_amount * JPY_TO_KRW:,.2f} KRW")
    print(f"💴 {base_amount:,.0f} CNY = {base_amount * CNY_TO_KRW:,.2f} KRW")

else:
    print("❌ 잘못된 선택입니다! (Invalid choice!)")

print("\n" + "="*60)
print("프로그램 종료 (Program Ended)")
print("="*60)

# ===== 보너스: 대화형 환율 계산기 (Interactive Currency Converter) =====

print("\n\n" + "="*60)
print("보너스: 대화형 환율 계산기 (Interactive Mode)")
print("="*60)
print("※ 이 섹션은 참고용입니다 (This section is for reference)")
print()

"""
# 실제 실행 시 아래 주석을 해제하세요 (Uncomment below for actual execution)

while True:
    print("\n환율 계산기 메뉴:")
    print("1. 외화 → 원화")
    print("2. 원화 → 외화")
    print("3. 환율 정보 보기")
    print("0. 종료")

    menu = input("메뉴 선택: ")

    if menu == '0':
        print("프로그램을 종료합니다.")
        break
    elif menu == '1':
        # 외화 → 원화 변환 로직
        pass
    elif menu == '2':
        # 원화 → 외화 변환 로직
        pass
    elif menu == '3':
        # 환율 정보 출력
        pass
    else:
        print("잘못된 선택입니다.")
"""

print("\n💡 Tip: 실전에서는 API를 통해 실시간 환율 정보를 가져올 수 있습니다!")
print("   In practice, you can fetch real-time exchange rates via API!")
