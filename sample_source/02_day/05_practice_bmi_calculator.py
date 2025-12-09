"""
파일명: 05_practice_bmi_calculator.py
설명: 실습 과제 - BMI 계산기
Filename: 05_practice_bmi_calculator.py
Description: Practice assignment - BMI Calculator
"""

print("="*60)
print("BMI 계산기 (BMI Calculator)")
print("="*60)
print()

# BMI 공식: BMI = 체중(kg) / (신장(m) ** 2)
# BMI Formula: BMI = weight(kg) / (height(m) ** 2)

# 사용자 정보 입력 (Get user information)
print("신체 정보를 입력하세요 (Enter your body information)")
print("-"*60)

name = input("이름 (Name): ")
height_cm = float(input("키 (Height in cm): "))
weight_kg = float(input("몸무게 (Weight in kg): "))

print()
print("="*60)

# 키를 미터로 변환 (Convert height to meters)
height_m = height_cm / 100

# BMI 계산 (Calculate BMI)
bmi = weight_kg / (height_m ** 2)

# BMI 판정 (BMI classification)
# 18.5 미만: 저체중 (Underweight)
# 18.5 ~ 22.9: 정상 (Normal)
# 23.0 ~ 24.9: 비만 전단계 (Pre-obese)
# 25.0 이상: 비만 (Obese)

if bmi < 18.5:
    category = "저체중 (Underweight)"
    status_icon = "⚠️"
elif 18.5 <= bmi < 23.0:
    category = "정상 (Normal)"
    status_icon = "✅"
elif 23.0 <= bmi < 25.0:
    category = "비만 전단계 (Pre-obese)"
    status_icon = "⚠️"
else:
    category = "비만 (Obese)"
    status_icon = "🚨"

# 결과 출력 (Display results)
print(f"{'BMI 계산 결과 (BMI Calculation Result)':^60}")
print("="*60)
print(f"이름 (Name): {name}")
print(f"키 (Height): {height_cm}cm ({height_m}m)")
print(f"몸무게 (Weight): {weight_kg}kg")
print("-"*60)
print(f"BMI: {bmi:.2f}")
print(f"판정 (Category): {status_icon} {category}")
print("="*60)

# 상세 정보 출력 (Detailed information)
print("\n┌" + "─"*58 + "┐")
print(f"│ {'BMI 범위 (BMI Range)':<25} │ {'판정 (Category)':<28} │")
print("├" + "─"*58 + "┤")
print(f"│ {'18.5 미만 (Below 18.5)':<25} │ {'저체중 (Underweight)':<28} │")
print(f"│ {'18.5 ~ 22.9':<25} │ {'정상 (Normal)':<28} │")
print(f"│ {'23.0 ~ 24.9':<25} │ {'비만 전단계 (Pre-obese)':<28} │")
print(f"│ {'25.0 이상 (25.0 and above)':<25} │ {'비만 (Obese)':<28} │")
print("└" + "─"*58 + "┘")

# 건강 조언 (Health advice)
print("\n" + "="*60)
print("건강 조언 (Health Advice)")
print("="*60)

if bmi < 18.5:
    print("⚠️  저체중입니다. 균형잡힌 영양 섭취가 필요합니다.")
    print("   You are underweight. Balanced nutrition is needed.")
elif 18.5 <= bmi < 23.0:
    print("✅  정상 체중입니다. 현재 상태를 유지하세요!")
    print("   You have normal weight. Maintain your current condition!")
elif 23.0 <= bmi < 25.0:
    print("⚠️  비만 전단계입니다. 식단 조절과 운동이 권장됩니다.")
    print("   You are pre-obese. Diet control and exercise are recommended.")
else:
    print("🚨  비만입니다. 적극적인 체중 관리가 필요합니다.")
    print("   You are obese. Active weight management is needed.")

# 표준 체중 계산 (Calculate standard weight)
# 표준 체중 = (키(m) ** 2) * 22 (Normal weight formula)
standard_weight = (height_m ** 2) * 22
weight_difference = weight_kg - standard_weight

print(f"\n표준 체중 (Standard Weight): {standard_weight:.1f}kg")
if weight_difference > 0:
    print(f"현재 체중은 표준 체중보다 {weight_difference:.1f}kg 더 많습니다.")
    print(f"Your weight is {weight_difference:.1f}kg more than standard.")
elif weight_difference < 0:
    print(f"현재 체중은 표준 체중보다 {abs(weight_difference):.1f}kg 적습니다.")
    print(f"Your weight is {abs(weight_difference):.1f}kg less than standard.")
else:
    print("현재 체중은 표준 체중과 동일합니다!")
    print("Your weight equals the standard weight!")

# 목표 체중 제안 (Suggest target weight)
if bmi < 18.5:
    target_bmi = 20.0
    target_weight = (height_m ** 2) * target_bmi
    print(f"\n권장 목표 체중 (Recommended target): {target_weight:.1f}kg (BMI 20)")
    print(f"목표까지: +{target_weight - weight_kg:.1f}kg")
elif bmi >= 25.0:
    target_bmi = 22.0
    target_weight = (height_m ** 2) * target_bmi
    print(f"\n권장 목표 체중 (Recommended target): {target_weight:.1f}kg (BMI 22)")
    print(f"목표까지: -{weight_kg - target_weight:.1f}kg")

print("\n" + "="*60)
print("BMI 계산 완료! (BMI Calculation Completed!)")
print("="*60)

# 추가 정보: 칼로리 섭취 권장량 (Additional info: Recommended calorie intake)
print("\n💡 추가 정보 (Additional Information)")
print("-"*60)

# 기초대사량 간단 계산 (Simple BMR calculation)
# 남성: BMR = 66 + (13.7 × 체중) + (5 × 키) - (6.8 × 나이)
# 여성: BMR = 655 + (9.6 × 체중) + (1.8 × 키) - (4.7 × 나이)

print("일일 권장 칼로리 섭취량 (Recommended daily calorie intake):")
print("  - 저체중 (Underweight): 목표 체중 달성을 위해 +300~500 kcal")
print("  - 정상 체중 (Normal): 현재 체중 유지를 위한 균형 있는 식단")
print("  - 과체중/비만 (Overweight/Obese): 체중 감량을 위해 -300~500 kcal")
print("\n※ 정확한 건강 관리는 전문의와 상담하세요.")
print("  For accurate health management, consult a healthcare professional.")
