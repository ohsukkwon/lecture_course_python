"""
파일명: 02_practice_expense_tracker.py
설명: 최종 프로젝트 예제 - 가계부 (지출 관리) 애플리케이션
Filename: 02_practice_expense_tracker.py
Description: Final project - Expense tracking application
"""

import json
import os
from datetime import datetime
from collections import defaultdict

print("="*70)
print("가계부 애플리케이션 (Expense Tracker Application)")
print("="*70)
print()

# ===== 1. Expense 클래스 (Expense class) =====
class Expense:
    """지출 항목 클래스"""

    CATEGORIES = ['식비', '교통비', '쇼핑', '의료', '문화/여가', '기타']

    def __init__(self, amount, category, description="", date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 객체 생성"""
        expense = cls(
            data['amount'],
            data['category'],
            data.get('description', ''),
            data.get('date')
        )
        expense.created_at = data.get('created_at', expense.created_at)
        return expense

    def __str__(self):
        return f"[{self.date}] {self.category}: {self.amount:,}원 - {self.description}"

    def __repr__(self):
        return f"Expense({self.amount}, '{self.category}')"


# ===== 2. Budget 클래스 (Budget class) =====
class Budget:
    """예산 클래스"""

    def __init__(self, month, total_budget):
        self.month = month  # YYYY-MM 형식
        self.total_budget = total_budget
        self.category_budgets = {}

    def set_category_budget(self, category, amount):
        """카테고리별 예산 설정"""
        self.category_budgets[category] = amount

    def get_category_budget(self, category):
        """카테고리 예산 조회"""
        return self.category_budgets.get(category, 0)

    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            'month': self.month,
            'total_budget': self.total_budget,
            'category_budgets': self.category_budgets
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 객체 생성"""
        budget = cls(data['month'], data['total_budget'])
        budget.category_budgets = data.get('category_budgets', {})
        return budget


# ===== 3. ExpenseTracker 클래스 (Main application class) =====
class ExpenseTracker:
    """가계부 애플리케이션 메인 클래스"""

    def __init__(self, data_dir="expense_data"):
        self.data_dir = data_dir
        self.expenses = []
        self.budgets = {}  # month -> Budget
        self._initialize()

    def _initialize(self):
        """초기화"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self.load_data()

    def add_expense(self, amount, category, description="", date=None):
        """지출 추가"""
        if category not in Expense.CATEGORIES:
            return f"❌ 유효하지 않은 카테고리: {category}"

        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        self.save_data()
        return f"✓ 지출 추가: {expense}"

    def remove_expense(self, index):
        """지출 삭제"""
        if 0 <= index < len(self.expenses):
            removed = self.expenses.pop(index)
            self.save_data()
            return f"✓ 지출 삭제: {removed}"
        return "❌ 유효하지 않은 인덱스"

    def get_expenses(self, month=None, category=None):
        """지출 목록 조회 (필터링 가능)"""
        filtered = self.expenses

        if month:
            filtered = [e for e in filtered if e.date.startswith(month)]

        if category:
            filtered = [e for e in filtered if e.category == category]

        return filtered

    def get_total_expenses(self, month=None, category=None):
        """총 지출 계산"""
        expenses = self.get_expenses(month, category)
        return sum(e.amount for e in expenses)

    def set_budget(self, month, total_budget, category_budgets=None):
        """예산 설정"""
        budget = Budget(month, total_budget)
        if category_budgets:
            for category, amount in category_budgets.items():
                budget.set_category_budget(category, amount)

        self.budgets[month] = budget
        self.save_data()
        return f"✓ {month} 예산 설정: {total_budget:,}원"

    def get_budget_status(self, month):
        """예산 사용 현황"""
        if month not in self.budgets:
            return None

        budget = self.budgets[month]
        total_spent = self.get_total_expenses(month)
        remaining = budget.total_budget - total_spent

        status = {
            'month': month,
            'budget': budget.total_budget,
            'spent': total_spent,
            'remaining': remaining,
            'percentage': (total_spent / budget.total_budget * 100) if budget.total_budget > 0 else 0,
            'categories': {}
        }

        # 카테고리별 상태
        for category in Expense.CATEGORIES:
            cat_budget = budget.get_category_budget(category)
            cat_spent = self.get_total_expenses(month, category)

            if cat_budget > 0:
                status['categories'][category] = {
                    'budget': cat_budget,
                    'spent': cat_spent,
                    'remaining': cat_budget - cat_spent,
                    'percentage': (cat_spent / cat_budget * 100)
                }

        return status

    def get_statistics(self, month):
        """통계 정보"""
        expenses = self.get_expenses(month)

        if not expenses:
            return None

        # 카테고리별 지출
        category_totals = defaultdict(int)
        for expense in expenses:
            category_totals[expense.category] += expense.amount

        # 가장 많이 지출한 카테고리
        max_category = max(category_totals.items(), key=lambda x: x[1])

        # 평균 지출
        avg_expense = sum(e.amount for e in expenses) / len(expenses)

        return {
            'month': month,
            'total_expenses': len(expenses),
            'total_amount': sum(e.amount for e in expenses),
            'category_totals': dict(category_totals),
            'max_category': max_category,
            'avg_expense': avg_expense
        }

    def save_data(self):
        """데이터 저장"""
        # 지출 데이터 저장
        expenses_file = os.path.join(self.data_dir, 'expenses.json')
        expenses_data = [e.to_dict() for e in self.expenses]

        with open(expenses_file, 'w', encoding='utf-8') as f:
            json.dump(expenses_data, f, ensure_ascii=False, indent=4)

        # 예산 데이터 저장
        budgets_file = os.path.join(self.data_dir, 'budgets.json')
        budgets_data = {month: budget.to_dict() for month, budget in self.budgets.items()}

        with open(budgets_file, 'w', encoding='utf-8') as f:
            json.dump(budgets_data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        """데이터 로드"""
        # 지출 데이터 로드
        expenses_file = os.path.join(self.data_dir, 'expenses.json')
        if os.path.exists(expenses_file):
            with open(expenses_file, 'r', encoding='utf-8') as f:
                expenses_data = json.load(f)
                self.expenses = [Expense.from_dict(e) for e in expenses_data]

        # 예산 데이터 로드
        budgets_file = os.path.join(self.data_dir, 'budgets.json')
        if os.path.exists(budgets_file):
            with open(budgets_file, 'r', encoding='utf-8') as f:
                budgets_data = json.load(f)
                self.budgets = {month: Budget.from_dict(data)
                                for month, data in budgets_data.items()}

    def export_to_csv(self, month, filename=None):
        """CSV 파일로 내보내기"""
        import csv

        if filename is None:
            filename = f"expenses_{month}.csv"

        filepath = os.path.join(self.data_dir, filename)
        expenses = self.get_expenses(month)

        with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
            fieldnames = ['날짜', '카테고리', '금액', '설명']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for expense in expenses:
                writer.writerow({
                    '날짜': expense.date,
                    '카테고리': expense.category,
                    '금액': expense.amount,
                    '설명': expense.description
                })

        return f"✓ {filename}로 내보내기 완료"

    def print_expenses(self, month=None):
        """지출 목록 출력"""
        expenses = self.get_expenses(month)

        if not expenses:
            print(f"\n{'='*70}")
            print(f"지출 내역이 없습니다")
            print(f"{'='*70}")
            return

        print(f"\n{'='*70}")
        print(f"💰 지출 목록 ({month or '전체'}) - 총 {len(expenses)}건")
        print(f"{'='*70}")

        for i, expense in enumerate(expenses):
            print(f"{i+1}. {expense}")

        total = sum(e.amount for e in expenses)
        print(f"{'='*70}")
        print(f"총 지출: {total:,}원")
        print(f"{'='*70}")

    def print_budget_status(self, month):
        """예산 상태 출력"""
        status = self.get_budget_status(month)

        if not status:
            print(f"\n❌ {month} 예산이 설정되지 않았습니다")
            return

        print(f"\n{'='*70}")
        print(f"📊 {month} 예산 현황")
        print(f"{'='*70}")
        print(f"예산: {status['budget']:,}원")
        print(f"지출: {status['spent']:,}원 ({status['percentage']:.1f}%)")
        print(f"남은 금액: {status['remaining']:,}원")

        if status['remaining'] < 0:
            print(f"⚠️  예산 초과!")
        elif status['percentage'] > 80:
            print(f"⚠️  예산의 80% 이상 사용")

        # 카테고리별 상태
        if status['categories']:
            print(f"\n{'='*70}")
            print("📂 카테고리별 예산 현황")
            print(f"{'='*70}")

            for category, cat_status in status['categories'].items():
                bar_length = int(cat_status['percentage'] / 10)
                bar = '█' * bar_length
                print(f"\n{category}:")
                print(f"  예산: {cat_status['budget']:,}원")
                print(f"  지출: {cat_status['spent']:,}원 [{bar:10s}] {cat_status['percentage']:.1f}%")
                print(f"  남음: {cat_status['remaining']:,}원")

        print(f"{'='*70}")

    def print_statistics(self, month):
        """통계 정보 출력"""
        stats = self.get_statistics(month)

        if not stats:
            print(f"\n❌ {month} 지출 데이터가 없습니다")
            return

        print(f"\n{'='*70}")
        print(f"📈 {month} 통계")
        print(f"{'='*70}")
        print(f"총 지출 건수: {stats['total_expenses']}건")
        print(f"총 지출 금액: {stats['total_amount']:,}원")
        print(f"평균 지출: {stats['avg_expense']:,.0f}원")
        print(f"최다 지출 카테고리: {stats['max_category'][0]} ({stats['max_category'][1]:,}원)")

        print(f"\n{'='*70}")
        print("카테고리별 지출")
        print(f"{'='*70}")

        for category, amount in sorted(stats['category_totals'].items(),
                                       key=lambda x: x[1], reverse=True):
            percentage = (amount / stats['total_amount']) * 100
            bar = '█' * int(percentage / 2)
            print(f"{category:10s}: {bar:50s} {amount:>10,}원 ({percentage:>5.1f}%)")

        print(f"{'='*70}")


# ===== 데모 실행 (Demo execution) =====
def run_demo():
    """데모 모드로 실행"""
    print("\n" + "="*70)
    print("💰 가계부 애플리케이션 데모")
    print("="*70)

    # 트래커 생성
    tracker = ExpenseTracker()

    # 예산 설정
    print("\n1️⃣ 예산 설정 (2025-01)")
    print("-"*70)

    category_budgets = {
        '식비': 300000,
        '교통비': 100000,
        '쇼핑': 200000,
        '문화/여가': 150000
    }

    print(tracker.set_budget('2025-01', 1000000, category_budgets))

    input("\n계속하려면 Enter를 누르세요...")

    # 지출 추가
    print("\n2️⃣ 지출 추가하기")
    print("-"*70)

    expenses_data = [
        (50000, '식비', '식료품 구매', '2025-01-05'),
        (15000, '교통비', '택시 요금', '2025-01-05'),
        (80000, '쇼핑', '옷 구매', '2025-01-07'),
        (45000, '식비', '외식', '2025-01-08'),
        (30000, '문화/여가', '영화 관람', '2025-01-10'),
        (60000, '식비', '마트', '2025-01-12'),
        (25000, '교통비', '주유', '2025-01-13'),
        (120000, '쇼핑', '신발 구매', '2025-01-15'),
        (40000, '문화/여가', '콘서트', '2025-01-18'),
    ]

    for amount, category, desc, date in expenses_data:
        print(f"  {tracker.add_expense(amount, category, desc, date)}")

    input("\n계속하려면 Enter를 누르세요...")

    # 지출 목록
    print("\n3️⃣ 지출 목록 보기")
    print("-"*70)
    tracker.print_expenses('2025-01')

    input("\n계속하려면 Enter를 누르세요...")

    # 예산 현황
    print("\n4️⃣ 예산 현황")
    print("-"*70)
    tracker.print_budget_status('2025-01')

    input("\n계속하려면 Enter를 누르세요...")

    # 통계
    print("\n5️⃣ 통계 보기")
    print("-"*70)
    tracker.print_statistics('2025-01')

    input("\n계속하려면 Enter를 누르세요...")

    # CSV 내보내기
    print("\n6️⃣ CSV 파일로 내보내기")
    print("-"*70)
    print(f"  {tracker.export_to_csv('2025-01')}")

    print("\n" + "="*70)
    print("✅ 데모 완료")
    print("="*70)


# ===== 메인 실행 (Main execution) =====
if __name__ == "__main__":
    print("="*70)
    print("파이썬 12일차 - 가계부 애플리케이션")
    print("Python Day 12 - Expense Tracker Application")
    print("="*70)
    print("\n이 프로그램은 다음 개념을 포함합니다:")
    print("✓ 객체지향 프로그래밍 (OOP)")
    print("✓ 파일 입출력 (JSON, CSV)")
    print("✓ 예외 처리")
    print("✓ 데이터 구조 활용 (리스트, 딕셔너리)")
    print("✓ 클래스 메서드와 정적 메서드")
    print("✓ 데이터 분석 및 통계")
    print()

    # 데모 실행
    run_demo()

    print("\n" + "="*70)
    print("💡 최종 프로젝트 핵심 포인트:")
    print("   1. 여러 클래스를 조합하여 완전한 애플리케이션 구현")
    print("   2. 데이터 영속성 (파일 저장/로드)")
    print("   3. 사용자 친화적인 출력 형식")
    print("   4. 데이터 분석 및 시각화 (텍스트 기반)")
    print("   5. 예외 처리와 데이터 검증")
    print("="*70)
    print("\n축하합니다! 파이썬 12일 과정을 완료하셨습니다! 🎉")
    print("Congratulations! You've completed the 12-day Python course! 🎉")
