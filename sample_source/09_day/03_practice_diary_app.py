"""
파일명: 03_practice_diary_app.py
설명: 실습 - 파일 입출력을 활용한 일기장 애플리케이션
Filename: 03_practice_diary_app.py
Description: Practice - Diary application using file I/O
"""

import os
import json
from datetime import datetime

print("="*70)
print("일기장 애플리케이션 (Diary Application)")
print("="*70)
print()

# ===== 전역 변수 (Global variables) =====
DIARY_DIR = "diary_data"  # 일기 저장 디렉토리
DIARY_FILE = os.path.join(DIARY_DIR, "diaries.json")  # JSON 파일 경로

# ===== 1. 초기화 함수 (Initialization function) =====
def initialize():
    """
    일기장 디렉토리와 파일을 초기화합니다
    (Initialize diary directory and file)
    """
    # 디렉토리 생성 (Create directory)
    if not os.path.exists(DIARY_DIR):
        os.makedirs(DIARY_DIR)
        print(f"✓ '{DIARY_DIR}' 디렉토리가 생성되었습니다.")

    # 파일이 없으면 빈 리스트로 초기화 (Initialize with empty list if file doesn't exist)
    if not os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        print(f"✓ '{DIARY_FILE}' 파일이 생성되었습니다.")


# ===== 2. 일기 로드 함수 (Load diaries function) =====
def load_diaries():
    """
    저장된 일기를 불러옵니다 (Load saved diaries)

    Returns:
        일기 리스트 (List of diaries)
    """
    try:
        with open(DIARY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# ===== 3. 일기 저장 함수 (Save diaries function) =====
def save_diaries(diaries):
    """
    일기를 파일에 저장합니다 (Save diaries to file)

    Args:
        diaries: 일기 리스트 (List of diaries)
    """
    with open(DIARY_FILE, 'w', encoding='utf-8') as f:
        json.dump(diaries, f, ensure_ascii=False, indent=4)


# ===== 4. 일기 작성 함수 (Write diary function) =====
def write_diary(title, content, mood="보통"):
    """
    새 일기를 작성합니다 (Write new diary)

    Args:
        title: 제목 (Title)
        content: 내용 (Content)
        mood: 기분 (Mood)
    """
    diaries = load_diaries()

    # 새 일기 엔트리 (New diary entry)
    new_diary = {
        "id": len(diaries) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "title": title,
        "content": content,
        "mood": mood,
        "weather": "맑음"  # 기본값 (Default)
    }

    diaries.append(new_diary)
    save_diaries(diaries)

    print(f"✓ 일기가 저장되었습니다. (ID: {new_diary['id']})")
    return new_diary


# ===== 5. 일기 목록 보기 함수 (View diary list function) =====
def list_diaries():
    """
    모든 일기 목록을 보여줍니다 (Show all diary list)
    """
    diaries = load_diaries()

    if not diaries:
        print("📭 작성된 일기가 없습니다.")
        return

    print(f"\n{'='*70}")
    print(f"📔 일기 목록 (총 {len(diaries)}개)")
    print(f"{'='*70}")

    for diary in diaries:
        mood_emoji = {
            "매우 좋음": "😄",
            "좋음": "😊",
            "보통": "😐",
            "나쁨": "😔",
            "매우 나쁨": "😢"
        }.get(diary.get('mood', '보통'), '😐')

        print(f"\n[{diary['id']}] {diary['date']} {diary['time']} {mood_emoji}")
        print(f"    제목: {diary['title']}")
        print(f"    내용: {diary['content'][:50]}..." if len(diary['content']) > 50 else f"    내용: {diary['content']}")

    print(f"\n{'='*70}")


# ===== 6. 일기 상세 보기 함수 (View diary detail function) =====
def view_diary(diary_id):
    """
    특정 일기의 상세 내용을 봅니다 (View specific diary detail)

    Args:
        diary_id: 일기 ID (Diary ID)
    """
    diaries = load_diaries()

    # ID로 일기 찾기 (Find diary by ID)
    diary = next((d for d in diaries if d['id'] == diary_id), None)

    if not diary:
        print(f"❌ ID {diary_id}인 일기를 찾을 수 없습니다.")
        return None

    # 상세 정보 출력 (Print detail)
    print(f"\n{'='*70}")
    print(f"📖 일기 상세 정보 (ID: {diary['id']})")
    print(f"{'='*70}")
    print(f"날짜: {diary['date']}")
    print(f"시간: {diary['time']}")
    print(f"기분: {diary.get('mood', '보통')}")
    print(f"날씨: {diary.get('weather', '알 수 없음')}")
    print(f"\n제목: {diary['title']}")
    print(f"{'-'*70}")
    print(diary['content'])
    print(f"{'='*70}")

    return diary


# ===== 7. 일기 수정 함수 (Edit diary function) =====
def edit_diary(diary_id, title=None, content=None, mood=None):
    """
    일기를 수정합니다 (Edit diary)

    Args:
        diary_id: 일기 ID (Diary ID)
        title: 새 제목 (New title, optional)
        content: 새 내용 (New content, optional)
        mood: 새 기분 (New mood, optional)
    """
    diaries = load_diaries()

    # ID로 일기 찾기 (Find diary by ID)
    diary = next((d for d in diaries if d['id'] == diary_id), None)

    if not diary:
        print(f"❌ ID {diary_id}인 일기를 찾을 수 없습니다.")
        return False

    # 수정 (Edit)
    if title is not None:
        diary['title'] = title
    if content is not None:
        diary['content'] = content
    if mood is not None:
        diary['mood'] = mood

    # 수정 시간 기록 (Record edit time)
    diary['last_modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_diaries(diaries)
    print(f"✓ 일기 ID {diary_id}가 수정되었습니다.")
    return True


# ===== 8. 일기 삭제 함수 (Delete diary function) =====
def delete_diary(diary_id):
    """
    일기를 삭제합니다 (Delete diary)

    Args:
        diary_id: 일기 ID (Diary ID)
    """
    diaries = load_diaries()

    # ID로 일기 찾기 (Find diary by ID)
    diary = next((d for d in diaries if d['id'] == diary_id), None)

    if not diary:
        print(f"❌ ID {diary_id}인 일기를 찾을 수 없습니다.")
        return False

    diaries.remove(diary)
    save_diaries(diaries)
    print(f"✓ 일기 ID {diary_id}가 삭제되었습니다.")
    return True


# ===== 9. 일기 검색 함수 (Search diary function) =====
def search_diaries(keyword):
    """
    키워드로 일기를 검색합니다 (Search diaries by keyword)

    Args:
        keyword: 검색 키워드 (Search keyword)
    """
    diaries = load_diaries()

    # 제목 또는 내용에 키워드가 포함된 일기 찾기
    # (Find diaries with keyword in title or content)
    results = [d for d in diaries
               if keyword.lower() in d['title'].lower()
               or keyword.lower() in d['content'].lower()]

    if not results:
        print(f"❌ '{keyword}'를 포함하는 일기를 찾을 수 없습니다.")
        return []

    print(f"\n🔍 검색 결과: '{keyword}' ({len(results)}개)")
    print(f"{'='*70}")

    for diary in results:
        print(f"\n[{diary['id']}] {diary['date']} - {diary['title']}")
        # 키워드가 포함된 부분 하이라이트 (Highlight keyword)
        content_preview = diary['content'][:100]
        print(f"    {content_preview}...")

    return results


# ===== 10. 날짜별 일기 필터 함수 (Filter by date function) =====
def filter_by_date(target_date):
    """
    특정 날짜의 일기를 찾습니다 (Find diaries by date)

    Args:
        target_date: 날짜 (YYYY-MM-DD 형식)
    """
    diaries = load_diaries()

    # 해당 날짜의 일기 필터링 (Filter diaries by date)
    results = [d for d in diaries if d['date'] == target_date]

    if not results:
        print(f"❌ {target_date}에 작성된 일기가 없습니다.")
        return []

    print(f"\n📅 {target_date}의 일기 ({len(results)}개)")
    print(f"{'='*70}")

    for diary in results:
        print(f"\n[{diary['id']}] {diary['time']} - {diary['title']}")
        print(f"    {diary['content'][:80]}...")

    return results


# ===== 11. 기분별 통계 함수 (Mood statistics function) =====
def show_mood_statistics():
    """
    기분별 통계를 보여줍니다 (Show mood statistics)
    """
    diaries = load_diaries()

    if not diaries:
        print("📭 통계를 계산할 일기가 없습니다.")
        return

    # 기분별 카운트 (Count by mood)
    from collections import Counter
    mood_counts = Counter(d.get('mood', '보통') for d in diaries)

    print(f"\n{'='*70}")
    print("📊 기분 통계 (Mood Statistics)")
    print(f"{'='*70}")

    mood_emojis = {
        "매우 좋음": "😄",
        "좋음": "😊",
        "보통": "😐",
        "나쁨": "😔",
        "매우 나쁨": "😢"
    }

    total = len(diaries)
    for mood, count in mood_counts.most_common():
        emoji = mood_emojis.get(mood, '😐')
        percentage = (count / total) * 100
        bar = '█' * int(percentage / 2)
        print(f"{emoji} {mood:10s}: {bar} {count}개 ({percentage:.1f}%)")

    print(f"{'='*70}")


# ===== 12. 텍스트 파일로 내보내기 함수 (Export to text file) =====
def export_to_text():
    """
    모든 일기를 텍스트 파일로 내보냅니다
    (Export all diaries to text file)
    """
    diaries = load_diaries()

    if not diaries:
        print("❌ 내보낼 일기가 없습니다.")
        return False

    # 파일명 생성 (Generate filename)
    filename = f"diary_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(DIARY_DIR, filename)

    # 텍스트 파일로 저장 (Save to text file)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write(f"일기장 내보내기 (Diary Export)\n")
        f.write(f"내보낸 날짜: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"총 일기 수: {len(diaries)}개\n")
        f.write("="*70 + "\n\n")

        for diary in diaries:
            f.write(f"[{diary['id']}] {diary['date']} {diary['time']}\n")
            f.write(f"제목: {diary['title']}\n")
            f.write(f"기분: {diary.get('mood', '보통')}\n")
            f.write("-"*70 + "\n")
            f.write(diary['content'] + "\n")
            f.write("="*70 + "\n\n")

    print(f"✓ 일기가 '{filename}'으로 내보내졌습니다.")
    return True


# ===== 데모 실행 (Demo execution) =====
def run_demo():
    """
    데모 모드로 실행합니다 (Run in demo mode)
    """
    print("\n" + "="*70)
    print("📱 일기장 애플리케이션 데모")
    print("="*70)

    # 초기화 (Initialize)
    initialize()

    # 샘플 일기 작성 (Write sample diaries)
    print("\n1️⃣ 일기 작성하기")
    print("-"*70)

    write_diary(
        "첫 번째 일기",
        "오늘은 파이썬 공부를 시작했다. 파일 입출력에 대해 배웠는데 매우 흥미로웠다.",
        "좋음"
    )

    write_diary(
        "프로젝트 시작",
        "일기장 애플리케이션을 만들기 시작했다. JSON 파일을 사용해서 데이터를 저장하는 방법을 배웠다.",
        "매우 좋음"
    )

    write_diary(
        "디버깅의 하루",
        "오늘은 버그를 찾느라 시간이 많이 걸렸다. 하지만 결국 해결했다!",
        "보통"
    )

    write_diary(
        "주말 휴식",
        "주말이라 집에서 쉬었다. 좋은 책을 읽고 여유로운 시간을 보냈다.",
        "좋음"
    )

    input("\n계속하려면 Enter를 누르세요...")

    # 일기 목록 보기 (View diary list)
    print("\n2️⃣ 일기 목록 보기")
    print("-"*70)
    list_diaries()

    input("\n계속하려면 Enter를 누르세요...")

    # 일기 상세 보기 (View diary detail)
    print("\n3️⃣ 일기 상세 보기 (ID: 2)")
    print("-"*70)
    view_diary(2)

    input("\n계속하려면 Enter를 누르세요...")

    # 일기 검색 (Search diary)
    print("\n4️⃣ 일기 검색 (키워드: '파이썬')")
    print("-"*70)
    search_diaries("파이썬")

    input("\n계속하려면 Enter를 누르세요...")

    # 일기 수정 (Edit diary)
    print("\n5️⃣ 일기 수정 (ID: 3)")
    print("-"*70)
    print("기분을 '보통'에서 '좋음'으로 변경합니다...")
    edit_diary(3, mood="좋음")
    view_diary(3)

    input("\n계속하려면 Enter를 누르세요...")

    # 기분 통계 (Mood statistics)
    print("\n6️⃣ 기분 통계 보기")
    print("-"*70)
    show_mood_statistics()

    input("\n계속하려면 Enter를 누르세요...")

    # 텍스트 파일로 내보내기 (Export to text file)
    print("\n7️⃣ 텍스트 파일로 내보내기")
    print("-"*70)
    export_to_text()

    print("\n" + "="*70)
    print("✅ 데모 완료")
    print("="*70)


# ===== 메인 실행 (Main execution) =====
if __name__ == "__main__":
    print("="*70)
    print("파이썬 8일차 - 일기장 애플리케이션")
    print("Python Day 8 - Diary Application")
    print("="*70)
    print("\n이 프로그램은 다음 기능을 포함합니다:")
    print("✓ JSON 파일 입출력 (JSON file I/O)")
    print("✓ 파일 및 디렉토리 관리 (File and directory management)")
    print("✓ 데이터 CRUD 연산 (Data CRUD operations)")
    print("✓ 검색 및 필터링 (Search and filtering)")
    print("✓ 데이터 분석 및 통계 (Data analysis and statistics)")
    print("✓ 데이터 내보내기 (Data export)")
    print()

    # 데모 모드 실행 (Run demo mode)
    run_demo()

    print("\n" + "="*70)
    print("💡 파일 입출력 핵심 개념:")
    print("   1. 디렉토리 생성: os.makedirs()")
    print("   2. 파일 존재 확인: os.path.exists()")
    print("   3. JSON 저장: json.dump()")
    print("   4. JSON 로드: json.load()")
    print("   5. 파일 열기: open() with 'r', 'w', 'a' 모드")
    print("="*70)
    print("\n프로그램 종료 (Program ended)")
