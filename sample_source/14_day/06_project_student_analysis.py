"""
종합 프로젝트 2: 학생 성적 분석 및 시각화
NumPy, Pandas, Matplotlib을 활용한 교육 데이터 분석
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


class StudentAnalyzer:
    """학생 성적 분석 클래스"""

    def __init__(self):
        self.df = None

    def generate_sample_data(self, n_students=50):
        """샘플 학생 데이터 생성"""
        print("\n[1단계] 샘플 데이터 생성")
        print("-" * 60)

        np.random.seed(42)

        # 학생 ID 생성
        student_ids = [f"S{i:04d}" for i in range(1, n_students + 1)]

        # 이름 생성 (성 + 이름)
        last_names = ['김', '이', '박', '최', '정', '강', '조', '윤', '장', '임']
        first_names = ['민준', '서연', '예준', '하은', '도윤', '지우', '시우', '서현', '주원', '수아']
        names = [np.random.choice(last_names) + np.random.choice(first_names)
                for _ in range(n_students)]

        # 학년 및 반
        grades = np.random.choice([1, 2, 3], n_students)
        classes = np.random.choice([1, 2, 3, 4], n_students)

        # 성적 생성 (정규 분포)
        math_scores = np.random.normal(75, 12, n_students).astype(int)
        english_scores = np.random.normal(78, 10, n_students).astype(int)
        science_scores = np.random.normal(72, 13, n_students).astype(int)
        korean_scores = np.random.normal(80, 11, n_students).astype(int)

        # 0-100 범위로 제한
        math_scores = np.clip(math_scores, 0, 100)
        english_scores = np.clip(english_scores, 0, 100)
        science_scores = np.clip(science_scores, 0, 100)
        korean_scores = np.clip(korean_scores, 0, 100)

        # 출석률 생성
        attendance = np.random.uniform(85, 100, n_students).round(1)

        # 데이터프레임 생성
        self.df = pd.DataFrame({
            'student_id': student_ids,
            'name': names,
            'grade': grades,
            'class': classes,
            'math': math_scores,
            'english': english_scores,
            'science': science_scores,
            'korean': korean_scores,
            'attendance': attendance
        })

        print(f"✓ {n_students}명의 학생 데이터 생성 완료")
        print(f"\n데이터 미리보기:")
        print(self.df.head(10))

        # CSV 저장
        self.df.to_csv('students_data.csv', index=False, encoding='utf-8-sig')
        print(f"\n✓ students_data.csv 파일로 저장 완료")

    def calculate_statistics(self):
        """통계 계산"""
        print("\n[2단계] 성적 통계 계산")
        print("-" * 60)

        # 총점 및 평균 계산
        subjects = ['math', 'english', 'science', 'korean']
        self.df['total'] = self.df[subjects].sum(axis=1)
        self.df['average'] = self.df[subjects].mean(axis=1).round(2)

        # 등급 부여
        def get_grade(avg):
            if avg >= 90:
                return 'A'
            elif avg >= 80:
                return 'B'
            elif avg >= 70:
                return 'C'
            elif avg >= 60:
                return 'D'
            else:
                return 'F'

        self.df['grade_letter'] = self.df['average'].apply(get_grade)

        # 등수 계산
        self.df['rank'] = self.df['total'].rank(ascending=False, method='min').astype(int)

        print("=== 전체 통계 ===")
        print(f"총 학생 수: {len(self.df)}명")
        print(f"\n평균 점수:")
        for subject in subjects:
            print(f"  {subject:8}: {self.df[subject].mean():.2f}점")
        print(f"  전체평균: {self.df['average'].mean():.2f}점")

        print(f"\n최고/최저 점수:")
        for subject in subjects:
            print(f"  {subject:8}: {self.df[subject].max()}점 / {self.df[subject].min()}점")

    def grade_distribution(self):
        """등급 분포 분석"""
        print("\n[3단계] 등급 분포 분석")
        print("-" * 60)

        grade_counts = self.df['grade_letter'].value_counts().sort_index()

        print("=== 등급별 학생 수 ===")
        for grade, count in grade_counts.items():
            percentage = (count / len(self.df)) * 100
            print(f"등급 {grade}: {count:2}명 ({percentage:5.1f}%)")

        return grade_counts

    def class_analysis(self):
        """학년/반별 분석"""
        print("\n[4단계] 학년/반별 분석")
        print("-" * 60)

        # 학년별 평균
        print("=== 학년별 평균 ===")
        grade_avg = self.df.groupby('grade')['average'].mean()
        for grade, avg in grade_avg.items():
            print(f"{grade}학년: {avg:.2f}점")

        # 반별 평균 (학년별로)
        print("\n=== 학년/반별 평균 ===")
        class_avg = self.df.groupby(['grade', 'class'])['average'].mean()
        for (grade, cls), avg in class_avg.items():
            print(f"{grade}학년 {cls}반: {avg:.2f}점")

        return grade_avg, class_avg

    def top_students(self, n=10):
        """상위권 학생 분석"""
        print(f"\n[5단계] 상위 {n}명 학생")
        print("-" * 60)

        top = self.df.nlargest(n, 'total')

        print(f"{'순위':<5} {'학번':<8} {'이름':<8} {'학년':<5} {'반':<5} {'총점':<7} {'평균':<7}")
        print("-" * 60)

        for idx, row in top.iterrows():
            print(f"{int(row['rank']):<5} {row['student_id']:<8} {row['name']:<8} "
                  f"{int(row['grade'])}학년   {int(row['class'])}반   "
                  f"{int(row['total']):>4}점  {row['average']:>6.2f}점")

        return top

    def subject_correlation(self):
        """과목 간 상관관계"""
        print("\n[6단계] 과목 간 상관관계 분석")
        print("-" * 60)

        subjects = ['math', 'english', 'science', 'korean']
        correlation = self.df[subjects].corr()

        print("상관계수 행렬:")
        print(correlation.round(3))

        return correlation

    def visualize_analysis(self, grade_counts, grade_avg, correlation):
        """분석 결과 시각화"""
        print("\n[7단계] 데이터 시각화")
        print("-" * 60)

        fig = plt.figure(figsize=(16, 10))
        fig.suptitle('학생 성적 분석 대시보드', fontsize=20, fontweight='bold')

        subjects = ['math', 'english', 'science', 'korean']
        subject_names = ['수학', '영어', '과학', '국어']

        # 1. 과목별 평균 점수 (막대 그래프)
        ax1 = plt.subplot(2, 3, 1)
        subject_means = [self.df[sub].mean() for sub in subjects]
        bars = ax1.bar(subject_names, subject_means, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'])
        ax1.set_title('과목별 평균 점수', fontsize=14, fontweight='bold')
        ax1.set_ylabel('평균 점수')
        ax1.set_ylim(0, 100)
        ax1.grid(axis='y', alpha=0.3)

        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom')

        # 2. 등급 분포 (원 그래프)
        ax2 = plt.subplot(2, 3, 2)
        colors = ['#2ecc71', '#3498db', '#f39c12', '#e74c3c', '#95a5a6']
        ax2.pie(grade_counts.values, labels=grade_counts.index,
                autopct='%1.1f%%', colors=colors, startangle=90)
        ax2.set_title('등급 분포', fontsize=14, fontweight='bold')

        # 3. 학년별 평균 (막대 그래프)
        ax3 = plt.subplot(2, 3, 3)
        ax3.bar(grade_avg.index.astype(str), grade_avg.values, color='#9b59b6')
        ax3.set_title('학년별 평균 점수', fontsize=14, fontweight='bold')
        ax3.set_xlabel('학년')
        ax3.set_ylabel('평균 점수')
        ax3.set_ylim(0, 100)
        ax3.grid(axis='y', alpha=0.3)

        # 4. 과목별 점수 분포 (박스 플롯)
        ax4 = plt.subplot(2, 3, 4)
        data_to_plot = [self.df[sub] for sub in subjects]
        bp = ax4.boxplot(data_to_plot, labels=subject_names, patch_artist=True)
        for patch, color in zip(bp['boxes'], ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']):
            patch.set_facecolor(color)
        ax4.set_title('과목별 점수 분포', fontsize=14, fontweight='bold')
        ax4.set_ylabel('점수')
        ax4.grid(axis='y', alpha=0.3)

        # 5. 총점 히스토그램
        ax5 = plt.subplot(2, 3, 5)
        ax5.hist(self.df['total'], bins=20, edgecolor='black', alpha=0.7, color='#e67e22')
        ax5.set_title('총점 분포', fontsize=14, fontweight='bold')
        ax5.set_xlabel('총점')
        ax5.set_ylabel('학생 수')
        ax5.axvline(self.df['total'].mean(), color='red',
                   linestyle='--', linewidth=2, label=f"평균: {self.df['total'].mean():.1f}")
        ax5.legend()
        ax5.grid(axis='y', alpha=0.3)

        # 6. 출석률 vs 평균 점수 (산점도)
        ax6 = plt.subplot(2, 3, 6)
        scatter = ax6.scatter(self.df['attendance'], self.df['average'],
                            alpha=0.6, c=self.df['average'], cmap='RdYlGn', s=100)
        ax6.set_title('출석률 vs 평균 점수', fontsize=14, fontweight='bold')
        ax6.set_xlabel('출석률 (%)')
        ax6.set_ylabel('평균 점수')
        plt.colorbar(scatter, ax=ax6, label='평균 점수')
        ax6.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('student_analysis_dashboard.png', dpi=300, bbox_inches='tight')
        print("✓ 대시보드가 생성되었습니다 (student_analysis_dashboard.png)")
        plt.show()

    def generate_report(self, top_students):
        """분석 보고서 생성"""
        print("\n[8단계] 분석 보고서 생성")
        print("-" * 60)

        report = []
        report.append("=" * 60)
        report.append("학생 성적 분석 보고서")
        report.append("=" * 60)
        report.append(f"\n총 학생 수: {len(self.df)}명")
        report.append(f"분석 일시: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")

        report.append("\n\n1. 전체 성적 통계")
        report.append("-" * 60)
        subjects = ['math', 'english', 'science', 'korean']
        for subject in subjects:
            mean_score = self.df[subject].mean()
            report.append(f"{subject:8}: 평균 {mean_score:.2f}점")

        report.append(f"\n전체 평균: {self.df['average'].mean():.2f}점")

        report.append("\n\n2. 등급 분포")
        report.append("-" * 60)
        grade_counts = self.df['grade_letter'].value_counts().sort_index()
        for grade, count in grade_counts.items():
            percentage = (count / len(self.df)) * 100
            report.append(f"등급 {grade}: {count}명 ({percentage:.1f}%)")

        report.append("\n\n3. 상위 10명")
        report.append("-" * 60)
        for idx, row in top_students.head(10).iterrows():
            report.append(f"{int(row['rank'])}위: {row['name']} - 총점 {int(row['total'])}점, 평균 {row['average']:.2f}점")

        report.append("\n\n4. 주요 인사이트")
        report.append("-" * 60)

        # 최고 과목
        subject_means = {sub: self.df[sub].mean() for sub in subjects}
        best_subject = max(subject_means, key=subject_means.get)
        report.append(f"• 가장 높은 평균 과목: {best_subject} ({subject_means[best_subject]:.2f}점)")

        # 우수 학생 비율
        excellent = len(self.df[self.df['average'] >= 90])
        report.append(f"• 평균 90점 이상 학생: {excellent}명 ({excellent/len(self.df)*100:.1f}%)")

        # 출석률과 성적 상관관계
        corr = self.df['attendance'].corr(self.df['average'])
        report.append(f"• 출석률과 성적 상관계수: {corr:.3f}")

        report.append("\n" + "=" * 60)

        # 콘솔 출력
        report_text = "\n".join(report)
        print(report_text)

        # 파일 저장
        with open('student_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)

        print("\n✓ 보고서가 student_analysis_report.txt 파일로 저장되었습니다.")

    def run_analysis(self):
        """전체 분석 실행"""
        print("=" * 60)
        print("학생 성적 분석 프로젝트")
        print("=" * 60)

        # 1. 데이터 생성
        self.generate_sample_data(n_students=50)

        # 2. 통계 계산
        self.calculate_statistics()

        # 3. 등급 분포
        grade_counts = self.grade_distribution()

        # 4. 학년/반별 분석
        grade_avg, class_avg = self.class_analysis()

        # 5. 상위권 학생
        top_students = self.top_students(n=10)

        # 6. 과목 상관관계
        correlation = self.subject_correlation()

        # 7. 시각화
        self.visualize_analysis(grade_counts, grade_avg, correlation)

        # 8. 보고서 생성
        self.generate_report(top_students)

        print("\n" + "=" * 60)
        print("분석이 완료되었습니다!")
        print("생성된 파일:")
        print("  - students_data.csv: 원본 데이터")
        print("  - student_analysis_dashboard.png: 시각화 대시보드")
        print("  - student_analysis_report.txt: 분석 보고서")
        print("=" * 60)


def main():
    analyzer = StudentAnalyzer()
    analyzer.run_analysis()


if __name__ == "__main__":
    main()
