"""
종합 프로젝트 1: 판매 데이터 분석 및 시각화
NumPy, Pandas, Matplotlib을 활용한 실전 데이터 분석
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


class SalesAnalyzer:
    """판매 데이터 분석 클래스"""

    def __init__(self):
        self.df = None

    def generate_sample_data(self, days=90):
        """샘플 판매 데이터 생성"""
        print("\n[1단계] 샘플 데이터 생성")
        print("-" * 60)

        np.random.seed(42)

        # 날짜 생성
        start_date = datetime(2024, 1, 1)
        dates = [start_date + timedelta(days=i) for i in range(days)]

        # 제품 리스트
        products = ['노트북', '마우스', '키보드', '모니터', '헤드셋']

        # 랜덤 데이터 생성
        data = []
        for date in dates:
            for _ in range(np.random.randint(3, 8)):  # 하루에 3-7건의 판매
                product = np.random.choice(products)

                # 제품별 가격 범위
                price_ranges = {
                    '노트북': (800000, 2000000),
                    '마우스': (20000, 80000),
                    '키보드': (50000, 150000),
                    '모니터': (200000, 500000),
                    '헤드셋': (30000, 100000)
                }

                price = np.random.randint(*price_ranges[product])
                quantity = np.random.randint(1, 5)
                revenue = price * quantity

                data.append({
                    'date': date,
                    'product': product,
                    'price': price,
                    'quantity': quantity,
                    'revenue': revenue
                })

        self.df = pd.DataFrame(data)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['month'] = self.df['date'].dt.month
        self.df['weekday'] = self.df['date'].dt.day_name()

        print(f"✓ {len(self.df)}건의 판매 데이터 생성 완료")
        print(f"\n데이터 미리보기:")
        print(self.df.head(10))

        # CSV 저장
        self.df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')
        print(f"\n✓ sales_data.csv 파일로 저장 완료")

    def basic_statistics(self):
        """기본 통계 분석"""
        print("\n[2단계] 기본 통계 분석")
        print("-" * 60)

        print("=== 전체 통계 ===")
        print(f"총 판매 건수: {len(self.df):,}건")
        print(f"총 매출: {self.df['revenue'].sum():,}원")
        print(f"평균 거래액: {self.df['revenue'].mean():,.0f}원")
        print(f"최고 거래액: {self.df['revenue'].max():,}원")
        print(f"최저 거래액: {self.df['revenue'].min():,}원")

        print("\n=== 제품별 통계 ===")
        product_stats = self.df.groupby('product').agg({
            'revenue': ['sum', 'mean', 'count']
        }).round(0)
        product_stats.columns = ['총매출', '평균매출', '판매건수']
        product_stats = product_stats.sort_values('총매출', ascending=False)
        print(product_stats)

        print("\n=== 월별 통계 ===")
        monthly_stats = self.df.groupby('month').agg({
            'revenue': ['sum', 'count']
        }).round(0)
        monthly_stats.columns = ['총매출', '판매건수']
        print(monthly_stats)

    def top_products(self):
        """베스트셀러 제품 분석"""
        print("\n[3단계] 베스트셀러 분석")
        print("-" * 60)

        # 제품별 총 매출
        product_revenue = self.df.groupby('product')['revenue'].sum().sort_values(ascending=False)

        print("=== 제품별 매출 순위 ===")
        for i, (product, revenue) in enumerate(product_revenue.items(), 1):
            percentage = (revenue / product_revenue.sum()) * 100
            print(f"{i}위: {product:8} - {revenue:,}원 ({percentage:.1f}%)")

        return product_revenue

    def time_series_analysis(self):
        """시계열 분석"""
        print("\n[4단계] 시계열 분석")
        print("-" * 60)

        # 일별 매출
        daily_revenue = self.df.groupby('date')['revenue'].sum()

        print("=== 일별 매출 통계 ===")
        print(f"평균 일매출: {daily_revenue.mean():,.0f}원")
        print(f"최고 일매출: {daily_revenue.max():,.0f}원 ({daily_revenue.idxmax().strftime('%Y-%m-%d')})")
        print(f"최저 일매출: {daily_revenue.min():,.0f}원 ({daily_revenue.idxmin().strftime('%Y-%m-%d')})")

        # 요일별 매출
        weekday_revenue = self.df.groupby('weekday')['revenue'].sum()
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekday_revenue = weekday_revenue.reindex(weekday_order)

        print("\n=== 요일별 평균 매출 ===")
        weekday_names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        for i, (day, revenue) in enumerate(weekday_revenue.items()):
            print(f"{weekday_names[i]}: {revenue:,.0f}원")

        return daily_revenue, weekday_revenue

    def visualize_analysis(self, product_revenue, daily_revenue, weekday_revenue):
        """분석 결과 시각화"""
        print("\n[5단계] 데이터 시각화")
        print("-" * 60)

        fig = plt.figure(figsize=(16, 10))
        fig.suptitle('판매 데이터 분석 대시보드', fontsize=20, fontweight='bold')

        # 1. 제품별 매출 (막대 그래프)
        ax1 = plt.subplot(2, 3, 1)
        bars = ax1.bar(product_revenue.index, product_revenue.values, color='skyblue')
        ax1.set_title('제품별 총 매출', fontsize=14, fontweight='bold')
        ax1.set_xlabel('제품')
        ax1.set_ylabel('매출 (원)')
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(axis='y', alpha=0.3)

        # 막대 위에 값 표시
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height/1000000:.0f}M',
                    ha='center', va='bottom', fontsize=9)

        # 2. 제품별 매출 비율 (원 그래프)
        ax2 = plt.subplot(2, 3, 2)
        ax2.pie(product_revenue.values, labels=product_revenue.index,
                autopct='%1.1f%%', startangle=90)
        ax2.set_title('제품별 매출 비율', fontsize=14, fontweight='bold')

        # 3. 일별 매출 추이 (선 그래프)
        ax3 = plt.subplot(2, 3, 3)
        ax3.plot(daily_revenue.index, daily_revenue.values, linewidth=2, color='green')
        ax3.set_title('일별 매출 추이', fontsize=14, fontweight='bold')
        ax3.set_xlabel('날짜')
        ax3.set_ylabel('매출 (원)')
        ax3.grid(True, alpha=0.3)
        plt.setp(ax3.xaxis.get_majorticklabels(), rotation=45)

        # 4. 요일별 매출 (가로 막대 그래프)
        ax4 = plt.subplot(2, 3, 4)
        weekday_names = ['월', '화', '수', '목', '금', '토', '일']
        ax4.barh(weekday_names, weekday_revenue.values, color='orange')
        ax4.set_title('요일별 총 매출', fontsize=14, fontweight='bold')
        ax4.set_xlabel('매출 (원)')
        ax4.grid(axis='x', alpha=0.3)

        # 5. 제품별 판매 수량 (막대 그래프)
        ax5 = plt.subplot(2, 3, 5)
        product_quantity = self.df.groupby('product')['quantity'].sum().sort_values(ascending=False)
        ax5.bar(product_quantity.index, product_quantity.values, color='coral')
        ax5.set_title('제품별 판매 수량', fontsize=14, fontweight='bold')
        ax5.set_xlabel('제품')
        ax5.set_ylabel('수량')
        ax5.tick_params(axis='x', rotation=45)
        ax5.grid(axis='y', alpha=0.3)

        # 6. 월별 매출 추이
        ax6 = plt.subplot(2, 3, 6)
        monthly_revenue = self.df.groupby('month')['revenue'].sum()
        ax6.plot(monthly_revenue.index, monthly_revenue.values,
                marker='o', linewidth=2, markersize=8, color='purple')
        ax6.set_title('월별 매출 추이', fontsize=14, fontweight='bold')
        ax6.set_xlabel('월')
        ax6.set_ylabel('매출 (원)')
        ax6.set_xticks(monthly_revenue.index)
        ax6.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')
        print("✓ 대시보드가 생성되었습니다 (sales_analysis_dashboard.png)")
        plt.show()

    def generate_report(self):
        """분석 보고서 생성"""
        print("\n[6단계] 분석 보고서 생성")
        print("-" * 60)

        report = []
        report.append("=" * 60)
        report.append("판매 데이터 분석 보고서")
        report.append("=" * 60)
        report.append(f"\n분석 기간: {self.df['date'].min().strftime('%Y-%m-%d')} ~ {self.df['date'].max().strftime('%Y-%m-%d')}")
        report.append(f"분석 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        report.append("\n\n1. 전체 요약")
        report.append("-" * 60)
        report.append(f"총 판매 건수: {len(self.df):,}건")
        report.append(f"총 매출: {self.df['revenue'].sum():,}원")
        report.append(f"평균 거래액: {self.df['revenue'].mean():,.0f}원")

        report.append("\n\n2. 베스트셀러 제품")
        report.append("-" * 60)
        product_revenue = self.df.groupby('product')['revenue'].sum().sort_values(ascending=False)
        for i, (product, revenue) in enumerate(product_revenue.items(), 1):
            percentage = (revenue / product_revenue.sum()) * 100
            report.append(f"{i}위: {product} - {revenue:,}원 ({percentage:.1f}%)")

        report.append("\n\n3. 주요 인사이트")
        report.append("-" * 60)
        best_product = product_revenue.index[0]
        best_revenue = product_revenue.values[0]
        report.append(f"• 최고 매출 제품: {best_product} ({best_revenue:,}원)")

        daily_revenue = self.df.groupby('date')['revenue'].sum()
        best_day = daily_revenue.idxmax().strftime('%Y-%m-%d')
        report.append(f"• 최고 매출 날짜: {best_day} ({daily_revenue.max():,}원)")

        monthly_revenue = self.df.groupby('month')['revenue'].sum()
        best_month = monthly_revenue.idxmax()
        report.append(f"• 최고 매출 월: {best_month}월 ({monthly_revenue.max():,}원)")

        report.append("\n" + "=" * 60)

        # 콘솔 출력
        report_text = "\n".join(report)
        print(report_text)

        # 파일 저장
        with open('sales_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)

        print("\n✓ 보고서가 sales_analysis_report.txt 파일로 저장되었습니다.")

    def run_analysis(self):
        """전체 분석 실행"""
        print("=" * 60)
        print("판매 데이터 분석 프로젝트")
        print("=" * 60)

        # 1. 데이터 생성
        self.generate_sample_data(days=90)

        # 2. 기본 통계
        self.basic_statistics()

        # 3. 베스트셀러 분석
        product_revenue = self.top_products()

        # 4. 시계열 분석
        daily_revenue, weekday_revenue = self.time_series_analysis()

        # 5. 시각화
        self.visualize_analysis(product_revenue, daily_revenue, weekday_revenue)

        # 6. 보고서 생성
        self.generate_report()

        print("\n" + "=" * 60)
        print("분석이 완료되었습니다!")
        print("생성된 파일:")
        print("  - sales_data.csv: 원본 데이터")
        print("  - sales_analysis_dashboard.png: 시각화 대시보드")
        print("  - sales_analysis_report.txt: 분석 보고서")
        print("=" * 60)


def main():
    analyzer = SalesAnalyzer()
    analyzer.run_analysis()


if __name__ == "__main__":
    main()
