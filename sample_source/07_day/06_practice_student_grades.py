"""
실습 과제: 학생 성적 관리 시스템
정렬 알고리즘을 활용한 성적 관리 프로그램
"""


class Student:
    """학생 클래스"""

    def __init__(self, name, student_id, score):
        self.name = name
        self.student_id = student_id
        self.score = score

    def __repr__(self):
        return f"Student('{self.name}', {self.student_id}, {self.score})"

    def __str__(self):
        return f"{self.name:8} (ID: {self.student_id}) - {self.score}점"


class GradeManager:
    """성적 관리 시스템"""

    def __init__(self):
        self.students = []

    def add_student(self, name, student_id, score):
        """학생 추가"""
        student = Student(name, student_id, score)
        self.students.append(student)
        print(f"✓ {name} 학생이 추가되었습니다.")

    def display_students(self, title="학생 목록"):
        """학생 목록 출력"""
        print(f"\n{'=' * 50}")
        print(f"{title}")
        print(f"{'=' * 50}")

        if not self.students:
            print("등록된 학생이 없습니다.")
            return

        for i, student in enumerate(self.students, 1):
            print(f"{i:2}. {student}")

    def sort_by_name(self):
        """이름순 정렬 (가나다순)"""
        self.students.sort(key=lambda s: s.name)
        print("\n✓ 이름순으로 정렬되었습니다.")

    def sort_by_id(self):
        """학번순 정렬"""
        self.students.sort(key=lambda s: s.student_id)
        print("\n✓ 학번순으로 정렬되었습니다.")

    def sort_by_score_desc(self):
        """성적순 정렬 (높은 점수부터)"""
        self.students.sort(key=lambda s: s.score, reverse=True)
        print("\n✓ 성적순으로 정렬되었습니다. (높은 점수 → 낮은 점수)")

    def sort_by_score_asc(self):
        """성적순 정렬 (낮은 점수부터)"""
        self.students.sort(key=lambda s: s.score)
        print("\n✓ 성적순으로 정렬되었습니다. (낮은 점수 → 높은 점수)")

    def get_top_students(self, n=3):
        """상위 N명 학생 조회"""
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)
        return sorted_students[:n]

    def get_statistics(self):
        """통계 정보 출력"""
        if not self.students:
            print("등록된 학생이 없습니다.")
            return

        scores = [s.score for s in self.students]

        print(f"\n{'=' * 50}")
        print("성적 통계")
        print(f"{'=' * 50}")
        print(f"총 학생 수: {len(self.students)}명")
        print(f"최고 점수: {max(scores)}점")
        print(f"최저 점수: {min(scores)}점")
        print(f"평균 점수: {sum(scores) / len(scores):.2f}점")

        # 상위 3명
        print(f"\n[상위 3명]")
        top_students = self.get_top_students(3)
        for i, student in enumerate(top_students, 1):
            print(f"{i}위: {student}")

    def search_student(self, name):
        """학생 검색"""
        found = [s for s in self.students if name in s.name]

        if found:
            print(f"\n'{name}' 검색 결과: {len(found)}명")
            for student in found:
                print(f"  - {student}")
        else:
            print(f"\n'{name}'을(를) 찾을 수 없습니다.")


# ===== 실행 예제 =====


def main():
    print("=" * 50)
    print("학생 성적 관리 시스템")
    print("=" * 50)

    # 성적 관리자 생성
    manager = GradeManager()

    # 학생 추가
    print("\n[1단계] 학생 정보 입력")
    manager.add_student("김철수", "2024001", 85)
    manager.add_student("이영희", "2024002", 92)
    manager.add_student("박민수", "2024003", 78)
    manager.add_student("최지영", "2024004", 95)
    manager.add_student("정수현", "2024005", 88)
    manager.add_student("강민지", "2024006", 82)

    # 초기 목록 출력
    manager.display_students("초기 학생 목록")

    # 이름순 정렬
    print("\n" + "=" * 50)
    print("[2단계] 이름순 정렬")
    print("=" * 50)
    manager.sort_by_name()
    manager.display_students("이름순 정렬 결과")

    # 학번순 정렬
    print("\n" + "=" * 50)
    print("[3단계] 학번순 정렬")
    print("=" * 50)
    manager.sort_by_id()
    manager.display_students("학번순 정렬 결과")

    # 성적순 정렬 (높은 점수부터)
    print("\n" + "=" * 50)
    print("[4단계] 성적순 정렬")
    print("=" * 50)
    manager.sort_by_score_desc()
    manager.display_students("성적순 정렬 결과 (높은 점수 → 낮은 점수)")

    # 통계 출력
    print("\n" + "=" * 50)
    print("[5단계] 통계 정보")
    print("=" * 50)
    manager.get_statistics()

    # 학생 검색
    print("\n" + "=" * 50)
    print("[6단계] 학생 검색")
    print("=" * 50)
    manager.search_student("김")
    manager.search_student("영희")

    # 인터랙티브 모드 (선택적)
    print("\n" + "=" * 50)
    print("[추가] 인터랙티브 모드")
    print("=" * 50)
    print(
        """
다음 기능을 구현해보세요:
1. 사용자 입력으로 학생 추가
2. 정렬 방식 선택 메뉴
3. 특정 점수 범위 학생 조회
4. 학생 정보 수정/삭제
5. 파일로 저장/불러오기
"""
    )


if __name__ == "__main__":
    main()
