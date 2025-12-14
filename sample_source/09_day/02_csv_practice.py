"""
파일명: 02_csv_practice.py
설명: CSV 파일 완벽 가이드 - 실전 예제 중심
Filename: 02_csv_practice.py
Description: Complete CSV file guide - Practice-focused examples
"""

import csv
import os
from datetime import datetime

print("="*70)
print("CSV 파일 완벽 가이드 (Complete CSV File Guide)")
print("="*70)
print()

# 작업 디렉토리 확인 (Check working directory)
print(f"현재 작업 디렉토리: {os.getcwd()}")
print()

# ===== 1. CSV 파일 쓰기 - 기본 (Writing CSV - Basic) =====
print("="*70)
print("1. CSV 파일 쓰기 - 학생 성적 데이터")
print("="*70)
print()

# 학생 성적 데이터 (Student grade data)
students = [
    ['학번', '이름', '수학', '영어', '과학'],
    ['2024001', '김철수', 95, 88, 92],
    ['2024002', '이영희', 88, 95, 90],
    ['2024003', '박민수', 92, 85, 88],
    ['2024004', '최지연', 85, 90, 95],
    ['2024005', '정수진', 90, 92, 87],
]

# CSV 파일로 저장 (Save to CSV file)
filename = 'students_grades.csv'

with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(students)

print(f"✓ '{filename}' 파일이 생성되었습니다.")
print(f"  총 {len(students)}줄 (헤더 포함) 작성됨")
print()

# ===== 2. CSV 파일 읽기 - 기본 (Reading CSV - Basic) =====
print("="*70)
print("2. CSV 파일 읽기")
print("="*70)
print()

with open(filename, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    data = list(reader)

    print("📄 파일 내용:")
    for row in data:
        print(f"  {row}")

print()

# ===== 3. CSV 딕셔너리 읽기/쓰기 (CSV with dictionaries) =====
print("="*70)
print("3. CSV 딕셔너리 형식으로 읽기/쓰기")
print("="*70)
print()

# 딕셔너리 리스트 데이터 (List of dictionaries)
products = [
    {'상품코드': 'P001', '상품명': '노트북', '가격': 1200000, '재고': 15},
    {'상품코드': 'P002', '상품명': '마우스', '가격': 25000, '재고': 50},
    {'상품코드': 'P003', '상품명': '키보드', '가격': 89000, '재고': 30},
    {'상품코드': 'P004', '상품명': '모니터', '가격': 350000, '재고': 20},
    {'상품코드': 'P005', '상품명': '헤드셋', '가격': 65000, '재고': 40},
]

# CSV 파일로 저장 (Save to CSV)
products_file = 'products.csv'
fieldnames = ['상품코드', '상품명', '가격', '재고']

with open(products_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 헤더 쓰기
    writer.writerows(products)

print(f"✓ '{products_file}' 파일이 생성되었습니다.")

# 딕셔너리 형식으로 읽기 (Read as dictionaries)
with open(products_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    print("\n📦 상품 목록:")
    for row in reader:
        print(f"  {row['상품코드']}: {row['상품명']} - {int(row['가격']):,}원 (재고: {row['재고']})")

print()

# ===== 4. CSV 데이터 분석 - 평균 계산 (CSV data analysis) =====
print("="*70)
print("4. CSV 데이터 분석 - 성적 통계")
print("="*70)
print()

with open('students_grades.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    students_data = list(reader)

print("📊 학생별 성적 및 평균:")
print("-" * 70)

for student in students_data:
    name = student['이름']
    math = int(student['수학'])
    english = int(student['영어'])
    science = int(student['과학'])
    average = (math + english + science) / 3

    print(f"{name:6s}: 수학 {math:2d}, 영어 {english:2d}, 과학 {science:2d} → 평균 {average:.1f}")

# 과목별 평균 (Subject averages)
print("\n📈 과목별 평균:")
print("-" * 70)

subjects = ['수학', '영어', '과학']
for subject in subjects:
    scores = [int(s[subject]) for s in students_data]
    avg = sum(scores) / len(scores)
    print(f"{subject}: {avg:.1f}점")

print()

# ===== 5. CSV 데이터 필터링 (Filtering CSV data) =====
print("="*70)
print("5. CSV 데이터 필터링")
print("="*70)
print()

# 가격이 10만원 이상인 상품만 필터링 (Filter products over 100,000)
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    expensive_products = [row for row in reader if int(row['가격']) >= 100000]

print("💰 가격이 10만원 이상인 상품:")
for product in expensive_products:
    print(f"  {product['상품명']}: {int(product['가격']):,}원")

# 재고가 30개 이하인 상품 (Products with stock <= 30)
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    low_stock = [row for row in reader if int(row['재고']) <= 30]

print("\n⚠️  재고가 30개 이하인 상품:")
for product in low_stock:
    print(f"  {product['상품명']}: 재고 {product['재고']}개")

print()

# ===== 6. CSV 데이터 수정 및 업데이트 (Updating CSV data) =====
print("="*70)
print("6. CSV 데이터 수정 및 업데이트")
print("="*70)
print()

# 상품 데이터 읽기 (Read product data)
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    products_list = list(reader)

# 특정 상품의 재고 업데이트 (Update stock for specific product)
for product in products_list:
    if product['상품코드'] == 'P002':  # 마우스
        old_stock = product['재고']
        product['재고'] = str(int(product['재고']) + 20)  # 재고 20개 추가
        print(f"✓ {product['상품명']} 재고 업데이트: {old_stock} → {product['재고']}")

# 수정된 데이터 저장 (Save updated data)
with open('products.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products_list)

print(f"✓ '{products_file}' 파일이 업데이트되었습니다.")
print()

# ===== 7. CSV에 새 데이터 추가 (Append data to CSV) =====
print("="*70)
print("7. CSV에 새 데이터 추가")
print("="*70)
print()

# 새 상품 추가 (Add new product)
new_products = [
    {'상품코드': 'P006', '상품명': '웹캠', '가격': 78000, '재고': 25},
    {'상품코드': 'P007', '상품명': 'USB허브', '가격': 32000, '재고': 35},
]

with open('products.csv', 'a', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerows(new_products)

print("✓ 새 상품 2개가 추가되었습니다:")
for product in new_products:
    print(f"  - {product['상품명']} ({product['상품코드']})")

# 전체 데이터 확인 (Check all data)
with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    all_products = list(reader)

print(f"\n📦 현재 총 상품 수: {len(all_products)}개")
print()

# ===== 8. CSV 데이터 정렬 (Sorting CSV data) =====
print("="*70)
print("8. CSV 데이터 정렬")
print("="*70)
print()

with open('products.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    products_list = list(reader)

# 가격 순으로 정렬 (Sort by price)
sorted_by_price = sorted(products_list, key=lambda x: int(x['가격']))

print("💵 가격 낮은 순:")
for product in sorted_by_price:
    print(f"  {product['상품명']:10s}: {int(product['가격']):>8,}원")

# 재고 순으로 정렬 (Sort by stock)
sorted_by_stock = sorted(products_list, key=lambda x: int(x['재고']), reverse=True)

print("\n📦 재고 많은 순:")
for product in sorted_by_stock:
    print(f"  {product['상품명']:10s}: {int(product['재고']):>3}개")

print()

# ===== 9. 실전 예제 - 판매 기록 관리 (Sales record management) =====
print("="*70)
print("9. 실전 예제 - 판매 기록 관리")
print("="*70)
print()

# 판매 기록 데이터 (Sales records)
sales = [
    {'날짜': '2025-01-01', '상품코드': 'P001', '수량': 2, '총액': 2400000},
    {'날짜': '2025-01-01', '상품코드': 'P002', '수량': 5, '총액': 125000},
    {'날짜': '2025-01-02', '상품코드': 'P003', '수량': 3, '총액': 267000},
    {'날짜': '2025-01-02', '상품코드': 'P001', '수량': 1, '총액': 1200000},
    {'날짜': '2025-01-03', '상품코드': 'P004', '수량': 2, '총액': 700000},
]

# 판매 기록 저장 (Save sales records)
sales_file = 'sales_records.csv'
sales_fieldnames = ['날짜', '상품코드', '수량', '총액']

with open(sales_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=sales_fieldnames)
    writer.writeheader()
    writer.writerows(sales)

print(f"✓ '{sales_file}' 파일이 생성되었습니다.")

# 판매 통계 분석 (Sales statistics)
with open(sales_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    sales_data = list(reader)

total_revenue = sum(int(sale['총액']) for sale in sales_data)
total_quantity = sum(int(sale['수량']) for sale in sales_data)

print(f"\n📈 판매 통계:")
print(f"  총 판매 건수: {len(sales_data)}건")
print(f"  총 판매 수량: {total_quantity}개")
print(f"  총 매출액: {total_revenue:,}원")

# 날짜별 매출 (Revenue by date)
from collections import defaultdict

revenue_by_date = defaultdict(int)
for sale in sales_data:
    revenue_by_date[sale['날짜']] += int(sale['총액'])

print(f"\n📅 날짜별 매출:")
for date, revenue in sorted(revenue_by_date.items()):
    print(f"  {date}: {revenue:,}원")

print()

# ===== 10. CSV 파일 병합 (Merging CSV files) =====
print("="*70)
print("10. CSV 파일 병합")
print("="*70)
print()

# 추가 판매 기록 (Additional sales records)
additional_sales = [
    {'날짜': '2025-01-04', '상품코드': 'P002', '수량': 10, '총액': 250000},
    {'날짜': '2025-01-04', '상품코드': 'P005', '수량': 3, '총액': 195000},
]

# 새 파일로 저장 (Save to new file)
additional_file = 'sales_records_additional.csv'
with open(additional_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=sales_fieldnames)
    writer.writeheader()
    writer.writerows(additional_sales)

# 두 파일 병합 (Merge two files)
merged_sales = []

# 첫 번째 파일 읽기 (Read first file)
with open(sales_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    merged_sales.extend(list(reader))

# 두 번째 파일 읽기 (Read second file)
with open(additional_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    merged_sales.extend(list(reader))

# 병합된 파일 저장 (Save merged file)
merged_file = 'sales_records_merged.csv'
with open(merged_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=sales_fieldnames)
    writer.writeheader()
    writer.writerows(merged_sales)

print(f"✓ 두 파일이 병합되어 '{merged_file}'로 저장되었습니다.")
print(f"  총 {len(merged_sales)}건의 판매 기록")
print()

# ===== 생성된 파일 목록 (List of created files) =====
print("="*70)
print("생성된 CSV 파일 목록")
print("="*70)

csv_files = [
    'students_grades.csv',
    'products.csv',
    'sales_records.csv',
    'sales_records_additional.csv',
    'sales_records_merged.csv',
]

for filename in csv_files:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"  ✓ {filename:30s} ({size:,} bytes)")

print()

print("="*70)
print("CSV 파일 처리 완료!")
print("="*70)
print()
print("💡 CSV 파일 처리 핵심 개념:")
print("   1. csv.writer() - 리스트 형식으로 쓰기")
print("   2. csv.DictWriter() - 딕셔너리 형식으로 쓰기")
print("   3. csv.reader() - 리스트 형식으로 읽기")
print("   4. csv.DictReader() - 딕셔너리 형식으로 읽기")
print("   5. encoding='utf-8-sig' - 한글 깨짐 방지")
print("   6. newline='' - 빈 줄 방지")
print()
print("💡 CSV File Processing Key Concepts:")
print("   1. csv.writer() - Write as list format")
print("   2. csv.DictWriter() - Write as dictionary format")
print("   3. csv.reader() - Read as list format")
print("   4. csv.DictReader() - Read as dictionary format")
print("   5. encoding='utf-8-sig' - Prevent Korean character issues")
print("   6. newline='' - Prevent blank lines")
