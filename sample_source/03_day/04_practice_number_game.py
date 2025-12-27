"""
파일명: 04_practice_number_game.py
설명: 실습 과제 - 숫자 맞추기 게임
Filename: 04_practice_number_game.py
Description: Practice - Number guessing game
"""

import random

print("="*70)
print("숫자 맞추기 게임 (Number Guessing Game)")
print("="*70)
print()

# 게임 설명 (Game instructions)
print("🎮 게임 설명:")
print("  - 컴퓨터가 1부터 100 사이의 숫자를 하나 생각합니다")
print("  - Computer thinks of a number between 1 and 100")
print("  - 여러분이 그 숫자를 맞춰보세요!")
print("  - Try to guess the number!")
print("  - 힌트를 드립니다: '더 큰 수' 또는 '더 작은 수'")
print("  - Hints provided: 'Higher' or 'Lower'")
print()

# 난이도 선택 (Difficulty selection)
print("난이도를 선택하세요 (Choose difficulty):")
print("1. 쉬움 (Easy) - 10번 시도")
print("2. 보통 (Normal) - 7번 시도")
print("3. 어려움 (Hard) - 5번 시도")
print()

difficulty = input("선택 (1/2/3) [2]: ") or "2"

if difficulty == "1":
    max_attempts = 10
    difficulty_name = "쉬움 (Easy)"
elif difficulty == "3":
    max_attempts = 5
    difficulty_name = "어려움 (Hard)"
else:
    max_attempts = 7
    difficulty_name = "보통 (Normal)"

print(f"\n선택한 난이도: {difficulty_name}")
print(f"시도 횟수: {max_attempts}번")
print()

# 정답 생성 (Generate answer)
answer = random.randint(1, 100)
attempts = 0  # 시도 횟수 카운터 (Attempt counter)
guess_history = []  # 추측 기록 (Guess history)

print("="*70)
print("게임 시작! (Game Start!)")
print("="*70)
print()

# 메인 게임 루프 (Main game loop)
while attempts < max_attempts:
    # 현재 상태 표시 (Show current status)
    print(f"[시도 {attempts + 1}/{max_attempts}]")

    if guess_history:
        print(f"지금까지 추측: {guess_history}")
        print(f"Previous guesses: {guess_history}")

    # 사용자 입력 (User input)
    try:
        guess_input = input("숫자를 입력하세요 (1-100) [Enter number]: ")
        guess = int(guess_input)

        # 입력 검증 (Input validation)
        if guess < 1 or guess > 100:
            print("❌ 1부터 100 사이의 숫자를 입력하세요!")
            print("   Please enter a number between 1 and 100!")
            print()
            continue

        # 시도 횟수 증가 (Increment attempt counter)
        attempts += 1
        guess_history.append(guess)

        # 정답 확인 (Check answer)
        if guess == answer:
            # 정답! (Correct!)
            print()
            print("🎉"*20)
            print(f"정답입니다! (Correct!)")
            print(f"숫자는 {answer}였습니다!")
            print(f"The number was {answer}!")
            print(f"시도 횟수: {attempts}번 (Attempts: {attempts})")
            print("🎉"*20)

            # 평가 (Rating)
            if attempts <= 3:
                rating = "천재! (Genius!)"
            elif attempts <= 5:
                rating = "훌륭해요! (Excellent!)"
            elif attempts <= 7:
                rating = "잘했어요! (Good job!)"
            else:
                rating = "성공! (Success!)"

            print(f"\n평가: {rating}")
            break

        elif guess < answer:
            # 더 큰 수 (Higher)
            print(f"⬆️  더 큰 수를 입력하세요! (Try a higher number!)")
            print(f"   {guess}보다 큽니다 ({guess} is too low)")

        else:
            # 더 작은 수 (Lower)
            print(f"⬇️  더 작은 수를 입력하세요! (Try a lower number!)")
            print(f"   {guess}보다 작습니다 ({guess} is too high)")

        print()

    except ValueError:
        print("❌ 숫자만 입력하세요! (Please enter numbers only!)")
        print()

else:
    # 시도 횟수 초과 (Out of attempts)
    print()
    print("😢"*20)
    print("아쉽네요! 시도 횟수를 모두 사용했습니다.")
    print("Sorry! You've used all your attempts.")
    print(f"정답은 {answer}였습니다!")
    print(f"The answer was {answer}!")
    print("😢"*20)

# 게임 통계 (Game statistics)
print()
print("="*70)
print("게임 통계 (Game Statistics)")
print("="*70)
print(f"총 시도 횟수: {attempts}번 (Total attempts: {attempts})")
print(f"추측한 숫자들: {guess_history}")
print(f"Guessed numbers: {guess_history}")

if guess_history:
    print(f"최소 추측값: {min(guess_history)} (Minimum guess: {min(guess_history)})")
    print(f"최대 추측값: {max(guess_history)} (Maximum guess: {max(guess_history)})")

print()

# 이진 탐색 전략 안내 (Binary search strategy guide)
print("="*70)
print("💡 Tip: 이진 탐색 전략을 사용하면 더 빨리 찾을 수 있어요!")
print("   Using binary search strategy helps you find faster!")
print("   1. 먼저 50을 시도 (First try 50)")
print("   2. 힌트에 따라 범위를 절반으로 줄이기 (Narrow down by half)")
print("   3. 예: 50 → 75 → 87 → ... (Example: 50 → 75 → 87 → ...)")
print("="*70)

print()
print("게임 종료! 플레이해 주셔서 감사합니다! 🎮")
print("Game Over! Thank you for playing! 🎮")
