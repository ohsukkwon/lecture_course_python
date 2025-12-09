"""
파일명: 01_final_project_todo.py
설명: 최종 프로젝트 예제 - 할 일 관리 애플리케이션
Filename: 01_final_project_todo.py
Description: Final project example - TODO list application
"""

import json
from datetime import datetime

class TodoItem:
    """할 일 항목 클래스"""

    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority  # high, medium, low
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def toggle_complete(self):
        """완료 상태 토글"""
        self.completed = not self.completed

    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at
        }

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} ({self.priority})"


class TodoList:
    """할 일 목록 관리 클래스"""

    def __init__(self):
        self.todos = []

    def add_todo(self, title, description="", priority="medium"):
        """할 일 추가"""
        todo = TodoItem(title, description, priority)
        self.todos.append(todo)
        return todo

    def remove_todo(self, index):
        """할 일 삭제"""
        if 0 <= index < len(self.todos):
            removed = self.todos.pop(index)
            return removed
        return None

    def toggle_todo(self, index):
        """할 일 완료 상태 토글"""
        if 0 <= index < len(self.todos):
            self.todos[index].toggle_complete()
            return True
        return False

    def get_all_todos(self):
        """모든 할 일 반환"""
        return self.todos

    def get_pending_todos(self):
        """미완료 할 일 반환"""
        return [todo for todo in self.todos if not todo.completed]

    def get_completed_todos(self):
        """완료된 할 일 반환"""
        return [todo for todo in self.todos if todo.completed]

    def save_to_file(self, filename="todos.json"):
        """파일로 저장"""
        data = [todo.to_dict() for todo in self.todos]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_file(self, filename="todos.json"):
        """파일에서 로드"""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.todos = []
                for item in data:
                    todo = TodoItem(
                        item["title"],
                        item["description"],
                        item["priority"]
                    )
                    todo.completed = item["completed"]
                    todo.created_at = item["created_at"]
                    self.todos.append(todo)
            return True
        except FileNotFoundError:
            return False


def main():
    """메인 함수"""
    todo_list = TodoList()

    # 파일에서 로드 시도
    if todo_list.load_from_file():
        print("저장된 할 일 목록을 불러왔습니다.\n")

    while True:
        print("\n" + "="*60)
        print("할 일 관리 애플리케이션 (TODO List)")
        print("="*60)
        print("1. 할 일 추가")
        print("2. 할 일 목록 보기")
        print("3. 할 일 완료/취소")
        print("4. 할 일 삭제")
        print("5. 저장")
        print("6. 통계 보기")
        print("0. 종료")
        print("="*60)

        choice = input("\n선택: ")

        if choice == "1":
            # 할 일 추가
            print("\n--- 할 일 추가 ---")
            title = input("제목: ")
            description = input("설명 (선택사항): ")
            priority = input("우선순위 (high/medium/low) [medium]: ") or "medium"

            todo_list.add_todo(title, description, priority)
            print(f"✓ '{title}' 추가 완료!")

        elif choice == "2":
            # 할 일 목록 보기
            print("\n--- 할 일 목록 ---")
            all_todos = todo_list.get_all_todos()

            if not all_todos:
                print("할 일이 없습니다.")
            else:
                for i, todo in enumerate(all_todos):
                    print(f"{i+1}. {todo}")

        elif choice == "3":
            # 할 일 완료/취소
            print("\n--- 할 일 완료/취소 ---")
            all_todos = todo_list.get_all_todos()

            if not all_todos:
                print("할 일이 없습니다.")
            else:
                for i, todo in enumerate(all_todos):
                    print(f"{i+1}. {todo}")

                index = int(input("\n번호: ")) - 1
                if todo_list.toggle_todo(index):
                    status = "완료" if all_todos[index].completed else "미완료"
                    print(f"✓ '{all_todos[index].title}'를 {status}로 변경했습니다.")
                else:
                    print("❌ 잘못된 번호입니다.")

        elif choice == "4":
            # 할 일 삭제
            print("\n--- 할 일 삭제 ---")
            all_todos = todo_list.get_all_todos()

            if not all_todos:
                print("할 일이 없습니다.")
            else:
                for i, todo in enumerate(all_todos):
                    print(f"{i+1}. {todo}")

                index = int(input("\n삭제할 번호: ")) - 1
                removed = todo_list.remove_todo(index)
                if removed:
                    print(f"✓ '{removed.title}' 삭제 완료!")
                else:
                    print("❌ 잘못된 번호입니다.")

        elif choice == "5":
            # 저장
            todo_list.save_to_file()
            print("✓ 저장 완료!")

        elif choice == "6":
            # 통계
            print("\n--- 통계 ---")
            all_todos = todo_list.get_all_todos()
            pending = todo_list.get_pending_todos()
            completed = todo_list.get_completed_todos()

            print(f"전체 할 일: {len(all_todos)}개")
            print(f"미완료: {len(pending)}개")
            print(f"완료: {len(completed)}개")

            if all_todos:
                completion_rate = (len(completed) / len(all_todos)) * 100
                print(f"완료율: {completion_rate:.1f}%")

        elif choice == "0":
            # 종료
            print("\n저장하시겠습니까? (y/n): ", end="")
            if input().lower() == "y":
                todo_list.save_to_file()
                print("저장 완료!")

            print("프로그램을 종료합니다.")
            break

        else:
            print("❌ 잘못된 선택입니다.")


if __name__ == "__main__":
    print("="*60)
    print("파이썬 12일 완성 과정 - 최종 프로젝트")
    print("할 일 관리 애플리케이션")
    print("="*60)
    print("\n이 프로그램은 다음 기능을 포함합니다:")
    print("✓ 객체지향 프로그래밍")
    print("✓ 파일 입출력 (JSON)")
    print("✓ 예외 처리")
    print("✓ 리스트 컴프리헨션")
    print("✓ 클래스 메서드")
    print()

    # 데모 모드 또는 실제 실행
    demo_mode = input("데모 모드로 실행하시겠습니까? (y/n): ").lower() == "y"

    if demo_mode:
        # 데모: 자동으로 할 일 추가
        print("\n[데모 모드]")
        todo_list = TodoList()

        # 할 일 추가
        todo_list.add_todo("파이썬 복습하기", "1-12일차 내용 복습", "high")
        todo_list.add_todo("프로젝트 완성하기", "최종 프로젝트 코드 작성", "high")
        todo_list.add_todo("운동하기", "헬스장 가기", "medium")

        # 첫 번째 완료 처리
        todo_list.toggle_todo(0)

        # 목록 출력
        print("\n=== 할 일 목록 ===")
        for i, todo in enumerate(todo_list.get_all_todos(), 1):
            print(f"{i}. {todo}")

        # 통계
        print("\n=== 통계 ===")
        print(f"전체: {len(todo_list.get_all_todos())}개")
        print(f"미완료: {len(todo_list.get_pending_todos())}개")
        print(f"완료: {len(todo_list.get_completed_todos())}개")

        # 저장
        todo_list.save_to_file()
        print("\n✓ todos.json 파일로 저장되었습니다.")

    else:
        # 실제 실행
        try:
            main()
        except KeyboardInterrupt:
            print("\n\n프로그램이 중단되었습니다.")
        except Exception as e:
            print(f"\n오류 발생: {e}")

    print("\n" + "="*60)
    print("감사합니다! 파이썬 학습을 계속하세요! 🐍")
    print("="*60)
