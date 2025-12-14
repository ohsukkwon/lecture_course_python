"""
파일명: 02_practice_rpg_game.py
설명: 실습 - RPG 게임 시스템 (상속과 다형성 활용)
Filename: 02_practice_rpg_game.py
Description: Practice - RPG game system using inheritance and polymorphism
"""

import random
from abc import ABC, abstractmethod

print("="*70)
print("RPG 게임 시스템 (RPG Game System)")
print("="*70)
print()

# ===== 1. 기본 캐릭터 클래스 (Base Character class) =====
class Character(ABC):
    """캐릭터 기본 클래스 (추상 클래스)"""

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.level = 1
        self.exp = 0

    @abstractmethod
    def special_attack(self, target):
        """특수 공격 (추상 메서드)"""
        pass

    def basic_attack(self, target):
        """기본 공격"""
        damage = max(0, self.attack - target.defense + random.randint(-5, 5))
        target.take_damage(damage)
        return f"{self.name}의 기본 공격! {target.name}에게 {damage} 데미지"

    def take_damage(self, damage):
        """데미지 받기"""
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        """회복"""
        old_hp = self.hp
        self.hp = min(self.max_hp, self.hp + amount)
        healed = self.hp - old_hp
        return f"{self.name}이(가) {healed} HP 회복! (현재: {self.hp}/{self.max_hp})"

    def is_alive(self):
        """생존 여부"""
        return self.hp > 0

    def gain_exp(self, exp):
        """경험치 획득"""
        self.exp += exp
        if self.exp >= 100 * self.level:
            self.level_up()

    def level_up(self):
        """레벨 업"""
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        self.exp = 0
        return f"⭐ {self.name}이(가) 레벨 {self.level}로 올랐습니다!"

    def get_status(self):
        """상태 정보"""
        return (f"{self.name} (Lv.{self.level}) | "
                f"HP: {self.hp}/{self.max_hp} | "
                f"공격: {self.attack} | 방어: {self.defense} | "
                f"경험치: {self.exp}/{100 * self.level}")

    def __str__(self):
        hp_bar = '█' * (self.hp * 10 // self.max_hp)
        return f"{self.name} (Lv.{self.level}) [{hp_bar:10s}] {self.hp}/{self.max_hp} HP"


# ===== 2. 전사 클래스 (Warrior class) =====
class Warrior(Character):
    """전사 클래스"""

    def __init__(self, name):
        super().__init__(name, hp=150, attack=30, defense=15)
        self.rage = 0  # 분노 게이지

    def special_attack(self, target):
        """특수 공격: 강타"""
        damage = int(self.attack * 2 - target.defense)
        target.take_damage(damage)
        self.rage = min(100, self.rage + 20)
        return f"⚔️  {self.name}의 강타! {target.name}에게 {damage} 데미지 (분노: {self.rage}/100)"

    def berserker_mode(self):
        """광전사 모드 (분노 100 이상)"""
        if self.rage >= 100:
            self.attack += 10
            self.rage = 0
            return f"💢 {self.name}이(가) 광전사 모드 발동! 공격력 +10"
        return f"❌ 분노가 부족합니다 (현재: {self.rage}/100)"


# ===== 3. 마법사 클래스 (Mage class) =====
class Mage(Character):
    """마법사 클래스"""

    def __init__(self, name):
        super().__init__(name, hp=80, attack=40, defense=5)
        self.mana = 100
        self.max_mana = 100

    def special_attack(self, target):
        """특수 공격: 파이어볼"""
        mana_cost = 30
        if self.mana < mana_cost:
            return f"❌ 마나가 부족합니다 (현재: {self.mana}/{self.max_mana})"

        self.mana -= mana_cost
        damage = int(self.attack * 1.5)
        target.take_damage(damage)
        return f"🔥 {self.name}의 파이어볼! {target.name}에게 {damage} 데미지 (마나: {self.mana}/{self.max_mana})"

    def heal_spell(self, target):
        """치유 주문"""
        mana_cost = 25
        if self.mana < mana_cost:
            return f"❌ 마나가 부족합니다"

        self.mana -= mana_cost
        heal_amount = 40
        return target.heal(heal_amount) + f" (마나: {self.mana}/{self.max_mana})"

    def restore_mana(self, amount=20):
        """마나 회복"""
        self.mana = min(self.max_mana, self.mana + amount)
        return f"{self.name}이(가) {amount} 마나 회복! (현재: {self.mana}/{self.max_mana})"


# ===== 4. 궁수 클래스 (Archer class) =====
class Archer(Character):
    """궁수 클래스"""

    def __init__(self, name):
        super().__init__(name, hp=100, attack=35, defense=10)
        self.critical_rate = 0.3  # 치명타 확률 30%

    def special_attack(self, target):
        """특수 공격: 관통 화살"""
        base_damage = self.attack - target.defense // 2  # 방어력 관통
        is_critical = random.random() < self.critical_rate

        if is_critical:
            damage = int(base_damage * 2)
            target.take_damage(damage)
            return f"🎯 {self.name}의 치명타! {target.name}에게 {damage} 데미지!"
        else:
            damage = base_damage
            target.take_damage(damage)
            return f"🏹 {self.name}의 관통 화살! {target.name}에게 {damage} 데미지"

    def multi_shot(self, targets):
        """다중 공격"""
        results = []
        for target in targets:
            if target.is_alive():
                damage = self.attack // 2
                target.take_damage(damage)
                results.append(f"{target.name}에게 {damage} 데미지")
        return f"🏹🏹🏹 {self.name}의 다중 공격! " + ", ".join(results)


# ===== 5. 몬스터 기본 클래스 (Base Monster class) =====
class Monster(Character):
    """몬스터 기본 클래스"""

    def __init__(self, name, hp, attack, defense, exp_reward):
        super().__init__(name, hp, attack, defense)
        self.exp_reward = exp_reward

    def special_attack(self, target):
        """몬스터 특수 공격"""
        damage = int(self.attack * 1.3)
        target.take_damage(damage)
        return f"💥 {self.name}의 강력한 일격! {target.name}에게 {damage} 데미지"


# ===== 6. 구체적인 몬스터 클래스들 (Specific monster classes) =====
class Goblin(Monster):
    """고블린"""
    def __init__(self):
        super().__init__("고블린", hp=50, attack=15, defense=5, exp_reward=30)


class Orc(Monster):
    """오크"""
    def __init__(self):
        super().__init__("오크", hp=100, attack=25, defense=10, exp_reward=50)


class Dragon(Monster):
    """드래곤"""
    def __init__(self):
        super().__init__("드래곤", hp=300, attack=50, defense=30, exp_reward=200)

    def special_attack(self, target):
        """화염 브레스"""
        damage = int(self.attack * 2)
        target.take_damage(damage)
        return f"🔥🐉 {self.name}의 화염 브레스! {target.name}에게 {damage} 데미지!"


# ===== 7. 배틀 시스템 (Battle system) =====
class Battle:
    """전투 시스템"""

    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster
        self.turn = 1

    def hero_turn(self, action):
        """영웅 턴"""
        if action == 'basic':
            return self.hero.basic_attack(self.monster)
        elif action == 'special':
            return self.hero.special_attack(self.monster)
        elif action == 'heal':
            if isinstance(self.hero, Mage):
                return self.hero.heal_spell(self.hero)
            else:
                return self.hero.heal(20)
        return "❌ 알 수 없는 행동"

    def monster_turn(self):
        """몬스터 턴"""
        if random.random() < 0.3:  # 30% 확률로 특수 공격
            return self.monster.special_attack(self.hero)
        else:
            return self.monster.basic_attack(self.hero)

    def battle_round(self, hero_action='basic'):
        """전투 라운드"""
        print(f"\n===== 턴 {self.turn} =====")

        # 영웅 행동
        print(f"💫 {self.hero_turn(hero_action)}")

        # 몬스터 생존 확인
        if not self.monster.is_alive():
            print(f"\n🎉 {self.monster.name} 처치!")
            exp_gained = self.monster.exp_reward
            self.hero.gain_exp(exp_gained)
            print(f"📈 경험치 +{exp_gained} (현재: {self.hero.exp}/{100 * self.hero.level})")
            return 'hero_win'

        # 몬스터 행동
        print(f"👹 {self.monster_turn()}")

        # 영웅 생존 확인
        if not self.hero.is_alive():
            print(f"\n💀 {self.hero.name} 전투 불능...")
            return 'monster_win'

        # 상태 출력
        print(f"\n{self.hero}")
        print(f"{self.monster}")

        self.turn += 1
        return 'continue'


# ===== 8. 파티 시스템 (Party system) =====
class Party:
    """파티 시스템"""

    def __init__(self):
        self.members = []

    def add_member(self, character):
        """멤버 추가"""
        if len(self.members) < 4:
            self.members.append(character)
            return f"✓ {character.name}이(가) 파티에 합류했습니다"
        return "❌ 파티가 가득 찼습니다 (최대 4명)"

    def remove_member(self, character):
        """멤버 제거"""
        if character in self.members:
            self.members.remove(character)
            return f"✓ {character.name}이(가) 파티를 떠났습니다"
        return "❌ 해당 멤버가 파티에 없습니다"

    def get_alive_members(self):
        """생존한 멤버들"""
        return [member for member in self.members if member.is_alive()]

    def print_status(self):
        """파티 상태 출력"""
        print("\n" + "="*70)
        print(f"👥 파티 상태 (멤버 {len(self.members)}명)")
        print("="*70)
        for member in self.members:
            print(f"  {member}")
        print("="*70)


# ===== 데모 실행 (Demo execution) =====
def run_demo():
    """데모 모드로 실행"""
    print("\n" + "="*70)
    print("⚔️  RPG 게임 시스템 데모")
    print("="*70)

    # 캐릭터 생성
    print("\n1️⃣ 캐릭터 생성")
    print("-"*70)
    warrior = Warrior("용사")
    mage = Mage("마법사")
    archer = Archer("궁수")

    print(f"  생성: {warrior.name} (전사)")
    print(f"  생성: {mage.name} (마법사)")
    print(f"  생성: {archer.name} (궁수)")

    input("\n계속하려면 Enter를 누르세요...")

    # 파티 구성
    print("\n2️⃣ 파티 구성")
    print("-"*70)
    party = Party()
    print(f"  {party.add_member(warrior)}")
    print(f"  {party.add_member(mage)}")
    print(f"  {party.add_member(archer)}")

    party.print_status()

    input("\n계속하려면 Enter를 누르세요...")

    # 전투 1: 고블린
    print("\n3️⃣ 전투 시작 - 고블린 출현!")
    print("-"*70)
    goblin = Goblin()
    print(f"  {goblin.name} 등장! HP: {goblin.hp}")

    battle = Battle(warrior, goblin)

    # 자동 전투 (3턴)
    for _ in range(3):
        result = battle.battle_round(random.choice(['basic', 'special']))
        if result != 'continue':
            break
        input("\n다음 턴...")

    input("\n계속하려면 Enter를 누르세요...")

    # 마법사 스킬 테스트
    print("\n4️⃣ 마법사 스킬 테스트")
    print("-"*70)
    orc = Orc()
    print(f"  {orc.name} 등장!")

    print(f"\n  {mage.special_attack(orc)}")
    print(f"  {mage.restore_mana(30)}")
    print(f"  {mage.heal_spell(warrior)}")

    input("\n계속하려면 Enter를 누르세요...")

    # 궁수 치명타 테스트
    print("\n5️⃣ 궁수 치명타 테스트 (5회)")
    print("-"*70)
    test_monster = Goblin()

    for i in range(5):
        result = archer.special_attack(test_monster)
        print(f"  시도 {i+1}: {result}")
        if not test_monster.is_alive():
            test_monster = Goblin()

    input("\n계속하려면 Enter를 누르세요...")

    # 최종 상태
    print("\n6️⃣ 최종 파티 상태")
    print("-"*70)
    party.print_status()

    for member in party.members:
        print(f"\n  {member.get_status()}")

    print("\n" + "="*70)
    print("✅ 데모 완료")
    print("="*70)


# ===== 메인 실행 (Main execution) =====
if __name__ == "__main__":
    print("="*70)
    print("파이썬 11일차 - RPG 게임 시스템")
    print("Python Day 11 - RPG Game System")
    print("="*70)
    print("\n이 프로그램은 다음 개념을 포함합니다:")
    print("✓ 상속 (Inheritance)")
    print("✓ 다형성 (Polymorphism)")
    print("✓ 추상 클래스 (Abstract class)")
    print("✓ 메서드 오버라이딩 (Method overriding)")
    print("✓ super() 함수")
    print("✓ isinstance() 함수")
    print()

    # 데모 실행
    run_demo()

    print("\n" + "="*70)
    print("💡 상속의 장점:")
    print("   1. 코드 재사용성")
    print("   2. 계층적 구조 표현")
    print("   3. 다형성 구현")
    print("   4. 유지보수 용이")
    print("="*70)
    print("\n프로그램 종료 (Program ended)")
