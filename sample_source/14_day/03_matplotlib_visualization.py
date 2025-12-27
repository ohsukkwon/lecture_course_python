"""
Matplotlib 데이터 시각화
선 그래프, 막대 그래프, 산점도, 히스토그램 등
"""

import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


def example_line_plot():
    """선 그래프 예제"""
    print("\n[1] 선 그래프 (Line Plot)")

    # 데이터 생성
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)
    plt.title('선 그래프 예제', fontsize=16)
    plt.xlabel('X축', fontsize=12)
    plt.ylabel('Y축', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()


def example_multiple_lines():
    """여러 선 그래프"""
    print("\n[2] 여러 선 그래프")

    x = np.arange(0, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label='sin(x)', color='red', linewidth=2)
    plt.plot(x, y2, label='cos(x)', color='blue', linewidth=2)
    plt.title('삼각함수 그래프', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.show()


def example_bar_chart():
    """막대 그래프"""
    print("\n[3] 막대 그래프 (Bar Chart)")

    categories = ['A', 'B', 'C', 'D', 'E']
    values = [25, 40, 30, 55, 35]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=['red', 'blue', 'green', 'orange', 'purple'])
    plt.title('막대 그래프 예제', fontsize=16)
    plt.xlabel('카테고리', fontsize=12)
    plt.ylabel('값', fontsize=12)
    plt.grid(axis='y', alpha=0.3)

    # 막대 위에 값 표시
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}',
                ha='center', va='bottom', fontsize=10)

    plt.show()


def example_horizontal_bar():
    """가로 막대 그래프"""
    print("\n[4] 가로 막대 그래프")

    categories = ['제품A', '제품B', '제품C', '제품D', '제품E']
    values = [120, 85, 150, 95, 110]

    plt.figure(figsize=(10, 6))
    plt.barh(categories, values, color='skyblue')
    plt.title('제품별 판매량', fontsize=16)
    plt.xlabel('판매량', fontsize=12)
    plt.ylabel('제품', fontsize=12)
    plt.grid(axis='x', alpha=0.3)
    plt.show()


def example_scatter_plot():
    """산점도"""
    print("\n[5] 산점도 (Scatter Plot)")

    np.random.seed(42)
    x = np.random.rand(50) * 100
    y = np.random.rand(50) * 100
    colors = np.random.rand(50)
    sizes = np.random.rand(50) * 500

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    plt.title('산점도 예제', fontsize=16)
    plt.xlabel('X축', fontsize=12)
    plt.ylabel('Y축', fontsize=12)
    plt.colorbar(scatter, label='색상')
    plt.grid(True, alpha=0.3)
    plt.show()


def example_histogram():
    """히스토그램"""
    print("\n[6] 히스토그램 (Histogram)")

    np.random.seed(42)
    data = np.random.normal(100, 15, 1000)  # 평균 100, 표준편차 15

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, edgecolor='black', alpha=0.7, color='green')
    plt.title('정규 분포 히스토그램', fontsize=16)
    plt.xlabel('값', fontsize=12)
    plt.ylabel('빈도', fontsize=12)
    plt.axvline(data.mean(), color='red', linestyle='--', linewidth=2, label=f'평균: {data.mean():.1f}')
    plt.legend(fontsize=12)
    plt.grid(axis='y', alpha=0.3)
    plt.show()


def example_pie_chart():
    """원 그래프"""
    print("\n[7] 원 그래프 (Pie Chart)")

    labels = ['Python', 'Java', 'JavaScript', 'C++', 'Others']
    sizes = [35, 25, 20, 10, 10]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
    explode = (0.1, 0, 0, 0, 0)  # Python만 강조

    plt.figure(figsize=(10, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('프로그래밍 언어 선호도', fontsize=16)
    plt.axis('equal')
    plt.show()


def example_subplots():
    """서브플롯 (여러 그래프)"""
    print("\n[8] 서브플롯 (여러 그래프)")

    x = np.linspace(0, 10, 100)

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('여러 그래프 예제', fontsize=16)

    # 1번 그래프: 선 그래프
    axes[0, 0].plot(x, np.sin(x), 'r-')
    axes[0, 0].set_title('sin(x)')
    axes[0, 0].grid(True, alpha=0.3)

    # 2번 그래프: 막대 그래프
    axes[0, 1].bar(['A', 'B', 'C', 'D'], [10, 20, 15, 25])
    axes[0, 1].set_title('막대 그래프')
    axes[0, 1].grid(axis='y', alpha=0.3)

    # 3번 그래프: 산점도
    axes[1, 0].scatter(np.random.rand(50), np.random.rand(50), alpha=0.5)
    axes[1, 0].set_title('산점도')
    axes[1, 0].grid(True, alpha=0.3)

    # 4번 그래프: 히스토그램
    axes[1, 1].hist(np.random.randn(1000), bins=30, edgecolor='black')
    axes[1, 1].set_title('히스토그램')
    axes[1, 1].grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.show()


def example_real_world():
    """실전 예제: 월별 매출 분석"""
    print("\n[9] 실전 예제: 월별 매출 분석")

    months = ['1월', '2월', '3월', '4월', '5월', '6월']
    sales = [150, 180, 165, 200, 220, 195]
    costs = [90, 100, 95, 110, 120, 105]
    profit = [s - c for s, c in zip(sales, costs)]

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('월별 매출 분석 대시보드', fontsize=16, fontweight='bold')

    # 1. 매출 추이
    axes[0].plot(months, sales, marker='o', color='blue', linewidth=2, label='매출')
    axes[0].plot(months, costs, marker='s', color='red', linewidth=2, label='비용')
    axes[0].set_title('매출 및 비용 추이', fontsize=14)
    axes[0].set_xlabel('월', fontsize=12)
    axes[0].set_ylabel('금액 (만원)', fontsize=12)
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # 2. 이익
    bars = axes[1].bar(months, profit, color='green', alpha=0.7)
    axes[1].set_title('월별 이익', fontsize=14)
    axes[1].set_xlabel('월', fontsize=12)
    axes[1].set_ylabel('이익 (만원)', fontsize=12)
    axes[1].grid(axis='y', alpha=0.3)

    # 막대 위에 값 표시
    for bar in bars:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom')

    # 3. 비용 비율
    axes[2].pie([sum(sales), sum(costs)],
                labels=['매출', '비용'],
                autopct='%1.1f%%',
                colors=['#66b3ff', '#ff9999'],
                startangle=90)
    axes[2].set_title('총 매출 대비 비용', fontsize=14)

    plt.tight_layout()
    plt.show()


def main():
    print("=" * 60)
    print("Matplotlib 데이터 시각화 예제")
    print("=" * 60)
    print("\n각 예제를 실행하려면 함수 호출의 주석을 해제하세요.")
    print("모든 예제를 실행하면 여러 창이 차례로 열립니다.\n")

    # 예제 실행 (필요한 것만 주석 해제)
    example_line_plot()
    example_multiple_lines()
    example_bar_chart()
    example_horizontal_bar()
    example_scatter_plot()
    example_histogram()
    example_pie_chart()
    example_subplots()
    example_real_world()

    print("\n모든 시각화가 완료되었습니다!")


if __name__ == "__main__":
    main()
