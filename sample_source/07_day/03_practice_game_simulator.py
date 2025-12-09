"""
파일명: 03_practice_game_simulator.py
설명: 실습 - 다양한 게임 시뮬레이터 (random 모듈 활용)
Filename: 03_practice_game_simulator.py
Description: Practice - Various game simulators using random module
"""

import random
from datetime import datetime
from collections import Counter

print("="*70)
print("게임 시뮬레이터 모음 (Game Simulator Collection)")
print("="*70)
print()

# ===== 1. 주사위 굴리기 시뮬레이터 (Dice rolling simulator) =====
print("="*70)
print("1. 주사위 굴리기 시뮬레이터 (Dice Rolling Simulator)")
print("="*70)
print()

def roll_dice(num_dice=1, sides=6):
    """
    주사위를 굴립니다 (Roll dice)

    Args:
        num_dice: 주사위 개수 (Number of dice)
        sides: 주사위 면의 수 (Number of sides)

    Returns:
        주사위 결과 리스트 (List of dice results)
    """
    return [random.randint(1, sides) for _ in range(num_dice)]


def print_dice(value):
    """
    주사위를 시각적으로 출력합니다 (Print dice visually)
    """
    dice_art = {
        1: ["┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘"],
        2: ["┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘"],
        3: ["┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘"],
        4: ["┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘"],
        5: ["┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘"],
        6: ["┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘"],
    }

    if 1 <= value <= 6:
        for line in dice_art[value]:
            print(line)


# 데모: 주사위 굴리기 (Demo: Roll dice)
print("🎲 주사위 1개 굴리기:")
result = roll_dice(1)[0]
print_dice(result)
print(f"결과: {result}")

print("\n🎲 주사위 2개 굴리기:")
results = roll_dice(2)
print(f"결과: {results}, 합계: {sum(results)}")

print("\n🎲 주사위 3개 굴리기 (10번):")
for i in range(10):
    results = roll_dice(3)
    print(f"  시도 {i+1}: {results} → 합계: {sum(results)}")

print()

# ===== 2. 동전 던지기 시뮬레이터 (Coin flip simulator) =====
print("="*70)
print("2. 동전 던지기 시뮬레이터 (Coin Flip Simulator)")
print("="*70)
print()

def flip_coin():
    """
    동전을 던집니다 (Flip coin)

    Returns:
        'H' (앞면) 또는 'T' (뒷면)
    """
    return random.choice(['H', 'T'])


def flip_multiple_coins(num_flips):
    """
    여러 번 동전을 던집니다 (Flip multiple coins)
    """
    results = [flip_coin() for _ in range(num_flips)]
    heads = results.count('H')
    tails = results.count('T')

    print(f"🪙 동전 {num_flips}번 던지기:")
    print(f"결과: {' '.join(results)}")
    print(f"앞면(H): {heads}번 ({heads/num_flips*100:.1f}%)")
    print(f"뒷면(T): {tails}번 ({tails/num_flips*100:.1f}%)")

    return results


# 데모: 동전 던지기 (Demo: Flip coins)
flip_multiple_coins(20)
print()

flip_multiple_coins(100)
print()

# ===== 3. 가위바위보 게임 (Rock-Paper-Scissors game) =====
print("="*70)
print("3. 가위바위보 게임 (Rock-Paper-Scissors Game)")
print("="*70)
print()

def play_rps(player_choice):
    """
    가위바위보 게임을 합니다 (Play rock-paper-scissors)

    Args:
        player_choice: 'rock', 'paper', 또는 'scissors'

    Returns:
        게임 결과 (Game result)
    """
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    # 결과 판정 (Determine result)
    if player_choice == computer_choice:
        result = "무승부 (Tie)"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = "승리 (Win)"
    else:
        result = "패배 (Lose)"

    return {
        'player': player_choice,
        'computer': computer_choice,
        'result': result
    }


def rps_tournament(num_rounds=10):
    """
    가위바위보 토너먼트를 진행합니다 (Run RPS tournament)
    """
    print(f"🎮 가위바위보 토너먼트 ({num_rounds}판)")
    print("-" * 70)

    choices = ['rock', 'paper', 'scissors']
    stats = {'Win': 0, 'Lose': 0, 'Tie': 0}

    for i in range(num_rounds):
        player_choice = random.choice(choices)  # 자동 플레이
        result = play_rps(player_choice)

        # 한글 변환 (Convert to Korean)
        kr_names = {'rock': '바위', 'paper': '보', 'scissors': '가위'}
        player_kr = kr_names[result['player']]
        computer_kr = kr_names[result['computer']]

        # 결과 카운트 (Count results)
        result_type = result['result'].split()[0]
        stats[result_type] += 1

        # 출력 (Print)
        print(f"  라운드 {i+1}: 플레이어({player_kr}) vs 컴퓨터({computer_kr}) → {result['result']}")

    print("\n📊 최종 결과:")
    print(f"  승리: {stats['Win']}회 ({stats['Win']/num_rounds*100:.1f}%)")
    print(f"  패배: {stats['Lose']}회 ({stats['Lose']/num_rounds*100:.1f}%)")
    print(f"  무승부: {stats['Tie']}회 ({stats['Tie']/num_rounds*100:.1f}%)")


# 데모: 가위바위보 (Demo: RPS)
rps_tournament(15)
print()

# ===== 4. 로또 번호 생성기 (Lotto number generator) =====
print("="*70)
print("4. 로또 번호 생성기 (Lotto Number Generator)")
print("="*70)
print()

def generate_lotto_numbers():
    """
    로또 번호를 생성합니다 (Generate lotto numbers)
    1~45 중 6개를 중복 없이 선택
    """
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)


def generate_multiple_lotto(num_sets=5):
    """
    여러 세트의 로또 번호를 생성합니다 (Generate multiple lotto sets)
    """
    print(f"🎰 로또 번호 {num_sets}세트 생성:")
    print("-" * 70)

    for i in range(num_sets):
        numbers = generate_lotto_numbers()
        print(f"  [{i+1}] {numbers}")

    print()


# 데모: 로또 번호 생성 (Demo: Generate lotto numbers)
generate_multiple_lotto(10)

# ===== 5. 카드 덱 시뮬레이터 (Card deck simulator) =====
print("="*70)
print("5. 카드 덱 시뮬레이터 (Card Deck Simulator)")
print("="*70)
print()

def create_deck():
    """
    카드 덱을 생성합니다 (Create card deck)
    """
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    deck = [f"{rank}{suit}" for suit in suits for rank in ranks]
    return deck


def shuffle_deck(deck):
    """
    카드를 섞습니다 (Shuffle deck)
    """
    shuffled = deck.copy()
    random.shuffle(shuffled)
    return shuffled


def deal_cards(deck, num_cards):
    """
    카드를 나눠줍니다 (Deal cards)
    """
    return [deck.pop() for _ in range(min(num_cards, len(deck)))]


# 데모: 카드 게임 (Demo: Card game)
print("🃏 카드 덱 생성 및 섞기:")
deck = create_deck()
print(f"전체 카드 수: {len(deck)}")
print(f"처음 10장: {deck[:10]}")

shuffled_deck = shuffle_deck(deck)
print(f"\n섞은 후 처음 10장: {shuffled_deck[:10]}")

print("\n🎴 포커 게임 시뮬레이션 (4명의 플레이어):")
players = ['플레이어1', '플레이어2', '플레이어3', '플레이어4']
for player in players:
    hand = deal_cards(shuffled_deck, 5)
    print(f"  {player}: {hand}")

print(f"\n남은 카드: {len(shuffled_deck)}장")
print()

# ===== 6. 확률 시뮬레이션 (Probability simulation) =====
print("="*70)
print("6. 확률 시뮬레이션 (Probability Simulation)")
print("="*70)
print()

def simulate_dice_sum(num_simulations=1000):
    """
    주사위 2개의 합 확률을 시뮬레이션합니다
    (Simulate probability of dice sum)
    """
    print(f"🎲 주사위 2개 합계 시뮬레이션 ({num_simulations}번):")
    print("-" * 70)

    results = []
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        results.append(dice1 + dice2)

    # 빈도 계산 (Calculate frequency)
    frequency = Counter(results)

    # 결과 출력 (Print results)
    for sum_value in range(2, 13):
        count = frequency[sum_value]
        percentage = (count / num_simulations) * 100
        bar = '█' * int(percentage)
        print(f"  {sum_value:2d}: {bar} {count}회 ({percentage:.1f}%)")

    print()


# 데모: 확률 시뮬레이션 (Demo: Probability simulation)
simulate_dice_sum(10000)

# ===== 7. 몬티 홀 문제 시뮬레이션 (Monty Hall problem) =====
print("="*70)
print("7. 몬티 홀 문제 시뮬레이션 (Monty Hall Problem)")
print("="*70)
print()

def monty_hall_simulation(num_simulations=1000):
    """
    몬티 홀 문제를 시뮬레이션합니다
    (Simulate Monty Hall problem)

    설명: 3개의 문 중 하나에 상품이 있고, 나머지 2개는 꽝입니다.
          참가자가 문을 선택하면, 진행자가 꽝인 문 하나를 열어줍니다.
          이때 선택을 바꾸는 것이 유리한가?
    """
    print(f"🚪 몬티 홀 문제 시뮬레이션 ({num_simulations}번):")
    print("-" * 70)

    stay_wins = 0  # 선택 유지 시 승리
    switch_wins = 0  # 선택 변경 시 승리

    for _ in range(num_simulations):
        # 상품 위치와 첫 선택 (Prize location and first choice)
        prize_door = random.randint(1, 3)
        first_choice = random.randint(1, 3)

        # 진행자가 열 수 있는 문 (Door host can open)
        doors = {1, 2, 3}
        doors.discard(prize_door)  # 상품이 있는 문 제외
        doors.discard(first_choice)  # 참가자가 선택한 문 제외
        opened_door = random.choice(list(doors)) if doors else None

        # 선택을 바꿨을 때의 문 (Door when switching)
        remaining_doors = {1, 2, 3}
        remaining_doors.discard(first_choice)
        remaining_doors.discard(opened_door)
        switch_choice = list(remaining_doors)[0] if remaining_doors else first_choice

        # 결과 판정 (Determine results)
        if first_choice == prize_door:
            stay_wins += 1
        if switch_choice == prize_door:
            switch_wins += 1

    # 결과 출력 (Print results)
    stay_percentage = (stay_wins / num_simulations) * 100
    switch_percentage = (switch_wins / num_simulations) * 100

    print(f"선택 유지 (Stay): {stay_wins}회 승리 ({stay_percentage:.1f}%)")
    print(f"선택 변경 (Switch): {switch_wins}회 승리 ({switch_percentage:.1f}%)")
    print()
    print("💡 결론: 선택을 바꾸는 것이 약 2배 더 유리합니다!")
    print()


# 데모: 몬티 홀 시뮬레이션 (Demo: Monty Hall simulation)
monty_hall_simulation(10000)

# ===== 8. 랜덤 이름 생성기 (Random name generator) =====
print("="*70)
print("8. 랜덤 이름 생성기 (Random Name Generator)")
print("="*70)
print()

def generate_random_name():
    """
    랜덤한 한국 이름을 생성합니다 (Generate random Korean name)
    """
    last_names = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
    first_names = [
        '민준', '서준', '예준', '도윤', '시우',
        '서연', '서윤', '지우', '서현', '민서'
    ]

    last_name = random.choice(last_names)
    first_name = random.choice(first_names)

    return f"{last_name}{first_name}"


# 데모: 이름 생성 (Demo: Name generation)
print("🎭 랜덤 이름 20개 생성:")
names = [generate_random_name() for _ in range(20)]
print(f"{', '.join(names)}")
print()

# ===== 9. 랜덤 팀 나누기 (Random team division) =====
print("="*70)
print("9. 랜덤 팀 나누기 (Random Team Division)")
print("="*70)
print()

def divide_teams(members, num_teams=2):
    """
    멤버를 랜덤하게 팀으로 나눕니다 (Divide members into random teams)
    """
    shuffled = members.copy()
    random.shuffle(shuffled)

    teams = [[] for _ in range(num_teams)]
    for i, member in enumerate(shuffled):
        teams[i % num_teams].append(member)

    return teams


# 데모: 팀 나누기 (Demo: Team division)
members = ['김철수', '이영희', '박민수', '최지연', '정수진',
           '강동원', '이민호', '김수현', '송중기', '박보검']

print(f"👥 전체 멤버 ({len(members)}명):")
print(f"  {', '.join(members)}")

print("\n🎲 2팀으로 랜덤 분배:")
teams = divide_teams(members, 2)
for i, team in enumerate(teams, 1):
    print(f"  팀 {i} ({len(team)}명): {', '.join(team)}")

print("\n🎲 3팀으로 랜덤 분배:")
teams = divide_teams(members, 3)
for i, team in enumerate(teams, 1):
    print(f"  팀 {i} ({len(team)}명): {', '.join(team)}")

print()

# ===== 10. 랜덤 퀴즈 선택기 (Random quiz selector) =====
print("="*70)
print("10. 랜덤 퀴즈 선택기 (Random Quiz Selector)")
print("="*70)
print()

def select_random_questions(question_pool, num_questions):
    """
    문제 풀에서 랜덤하게 문제를 선택합니다
    (Select random questions from pool)
    """
    if num_questions > len(question_pool):
        num_questions = len(question_pool)

    selected = random.sample(question_pool, num_questions)
    return selected


# 데모: 퀴즈 선택 (Demo: Quiz selection)
question_pool = [
    {"id": 1, "question": "파이썬의 창시자는?", "answer": "귀도 반 로섬"},
    {"id": 2, "question": "파이썬의 첫 버전 출시 연도는?", "answer": "1991"},
    {"id": 3, "question": "리스트의 첫 번째 원소 인덱스는?", "answer": "0"},
    {"id": 4, "question": "파이썬의 주석 기호는?", "answer": "#"},
    {"id": 5, "question": "불변 리스트의 이름은?", "answer": "튜플"},
    {"id": 6, "question": "딕셔너리의 키-값을 반환하는 메서드는?", "answer": "items()"},
    {"id": 7, "question": "문자열을 리스트로 바꾸는 메서드는?", "answer": "split()"},
    {"id": 8, "question": "리스트에 원소를 추가하는 메서드는?", "answer": "append()"},
]

print(f"📚 전체 문제 수: {len(question_pool)}개")
print("\n🎯 랜덤으로 5문제 선택:")

selected_questions = select_random_questions(question_pool, 5)
for i, q in enumerate(selected_questions, 1):
    print(f"\n[문제 {i}] {q['question']}")
    print(f"정답: {q['answer']}")

print()

print("="*70)
print("게임 시뮬레이터 완료!")
print("="*70)
print()
print("💡 random 모듈 핵심 함수:")
print("   - random.randint(a, b): a~b 사이의 랜덤 정수")
print("   - random.choice(seq): 시퀀스에서 랜덤하게 하나 선택")
print("   - random.sample(seq, k): 시퀀스에서 중복 없이 k개 선택")
print("   - random.shuffle(list): 리스트를 무작위로 섞음")
print("   - random.random(): 0.0~1.0 사이의 랜덤 실수")
print()
print("💡 Random module key functions:")
print("   - random.randint(a, b): Random integer between a and b")
print("   - random.choice(seq): Randomly select one from sequence")
print("   - random.sample(seq, k): Select k items without replacement")
print("   - random.shuffle(list): Shuffle list in place")
print("   - random.random(): Random float between 0.0 and 1.0")
