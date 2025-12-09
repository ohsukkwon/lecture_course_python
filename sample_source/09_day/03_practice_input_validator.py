"""
파일명: 03_practice_input_validator.py
설명: 실습 - 입력 검증 시스템 (예외 처리 활용)
Filename: 03_practice_input_validator.py
Description: Practice - Input validation system using exception handling
"""

import re
from datetime import datetime

print("="*70)
print("입력 검증 시스템 (Input Validation System)")
print("="*70)
print()

# ===== 사용자 정의 예외 클래스들 (Custom exception classes) =====

class ValidationError(Exception):
    """검증 실패 기본 예외"""
    pass

class EmptyValueError(ValidationError):
    """빈 값 예외"""
    pass

class InvalidFormatError(ValidationError):
    """잘못된 형식 예외"""
    pass

class OutOfRangeError(ValidationError):
    """범위 초과 예외"""
    pass

class InvalidLengthError(ValidationError):
    """잘못된 길이 예외"""
    pass

# ===== 1. 기본 검증 함수들 (Basic validation functions) =====
print("="*70)
print("1. 기본 검증 함수들 (Basic Validation Functions)")
print("="*70)
print()

def validate_not_empty(value, field_name="값"):
    """
    빈 값이 아닌지 검증 (Validate not empty)
    """
    if not value or (isinstance(value, str) and not value.strip()):
        raise EmptyValueError(f"{field_name}은(는) 비어 있을 수 없습니다")
    return True

def validate_length(value, min_len=None, max_len=None, field_name="값"):
    """
    길이 검증 (Validate length)
    """
    length = len(value)

    if min_len is not None and length < min_len:
        raise InvalidLengthError(
            f"{field_name}은(는) 최소 {min_len}자 이상이어야 합니다 (현재: {length}자)"
        )

    if max_len is not None and length > max_len:
        raise InvalidLengthError(
            f"{field_name}은(는) 최대 {max_len}자 이하여야 합니다 (현재: {length}자)"
        )

    return True

def validate_range(value, min_val=None, max_val=None, field_name="값"):
    """
    범위 검증 (Validate range)
    """
    if min_val is not None and value < min_val:
        raise OutOfRangeError(
            f"{field_name}은(는) {min_val} 이상이어야 합니다 (현재: {value})"
        )

    if max_val is not None and value > max_val:
        raise OutOfRangeError(
            f"{field_name}은(는) {max_val} 이하여야 합니다 (현재: {value})"
        )

    return True

# 테스트 (Test)
print("📋 기본 검증 테스트:")

try:
    validate_not_empty("", "이름")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    validate_not_empty("홍길동", "이름")
    print(f"  ✓ 이름 검증 성공")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    validate_length("ab", min_len=3, max_len=10, field_name="비밀번호")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    validate_range(15, min_val=18, max_val=100, field_name="나이")
except ValidationError as e:
    print(f"  ❌ {e}")

print()

# ===== 2. 형식 검증 함수들 (Format validation functions) =====
print("="*70)
print("2. 형식 검증 함수들 (Format Validation Functions)")
print("="*70)
print()

def validate_email(email):
    """
    이메일 형식 검증 (Validate email format)
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise InvalidFormatError(f"올바르지 않은 이메일 형식: {email}")
    return True

def validate_phone(phone):
    """
    전화번호 형식 검증 (Validate phone format - Korean)
    """
    # 010-1234-5678 또는 01012345678 형식
    pattern = r'^01[0-9]-?\d{3,4}-?\d{4}$'
    if not re.match(pattern, phone):
        raise InvalidFormatError(f"올바르지 않은 전화번호 형식: {phone}")
    return True

def validate_date(date_str, format_str='%Y-%m-%d'):
    """
    날짜 형식 검증 (Validate date format)
    """
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        raise InvalidFormatError(
            f"올바르지 않은 날짜 형식: {date_str} (예상 형식: {format_str})"
        )

def validate_password(password):
    """
    비밀번호 강도 검증 (Validate password strength)
    - 최소 8자 이상
    - 대문자, 소문자, 숫자 각각 최소 1개
    """
    if len(password) < 8:
        raise InvalidLengthError("비밀번호는 최소 8자 이상이어야 합니다")

    if not any(c.isupper() for c in password):
        raise InvalidFormatError("비밀번호에 대문자가 최소 1개 포함되어야 합니다")

    if not any(c.islower() for c in password):
        raise InvalidFormatError("비밀번호에 소문자가 최소 1개 포함되어야 합니다")

    if not any(c.isdigit() for c in password):
        raise InvalidFormatError("비밀번호에 숫자가 최소 1개 포함되어야 합니다")

    return True

# 테스트 (Test)
print("🔍 형식 검증 테스트:")

test_cases = [
    ("이메일", validate_email, "test@example.com", True),
    ("이메일", validate_email, "invalid-email", False),
    ("전화번호", validate_phone, "010-1234-5678", True),
    ("전화번호", validate_phone, "010-12-5678", False),
    ("날짜", validate_date, "2025-01-15", True),
    ("날짜", validate_date, "2025/01/15", False),
    ("비밀번호", validate_password, "MyPass123", True),
    ("비밀번호", validate_password, "weak", False),
]

for field, validator, value, should_pass in test_cases:
    try:
        validator(value)
        if should_pass:
            print(f"  ✓ {field} '{value}' 검증 성공")
        else:
            print(f"  ⚠️  {field} '{value}' 검증 성공 (실패 예상)")
    except ValidationError as e:
        if not should_pass:
            print(f"  ✓ {field} '{value}' 검증 실패 (예상됨): {e}")
        else:
            print(f"  ❌ {field} '{value}' 검증 실패 (성공 예상): {e}")

print()

# ===== 3. 복합 검증 클래스 (Composite validator class) =====
print("="*70)
print("3. 복합 검증 클래스 (Composite Validator)")
print("="*70)
print()

class UserValidator:
    """사용자 정보 검증기"""

    @staticmethod
    def validate_username(username):
        """사용자명 검증"""
        validate_not_empty(username, "사용자명")
        validate_length(username, min_len=3, max_len=20, field_name="사용자명")

        # 영문자, 숫자, 언더스코어만 허용
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            raise InvalidFormatError(
                "사용자명은 영문자, 숫자, 언더스코어만 사용 가능합니다"
            )

        return True

    @staticmethod
    def validate_age(age):
        """나이 검증"""
        if not isinstance(age, int):
            raise InvalidFormatError("나이는 정수여야 합니다")

        validate_range(age, min_val=0, max_val=150, field_name="나이")
        return True

    @staticmethod
    def validate_user_data(data):
        """사용자 데이터 전체 검증"""
        errors = []

        # 각 필드 검증
        try:
            UserValidator.validate_username(data.get('username', ''))
        except ValidationError as e:
            errors.append(f"사용자명: {e}")

        try:
            validate_email(data.get('email', ''))
        except ValidationError as e:
            errors.append(f"이메일: {e}")

        try:
            validate_phone(data.get('phone', ''))
        except ValidationError as e:
            errors.append(f"전화번호: {e}")

        try:
            UserValidator.validate_age(data.get('age'))
        except ValidationError as e:
            errors.append(f"나이: {e}")

        try:
            validate_password(data.get('password', ''))
        except ValidationError as e:
            errors.append(f"비밀번호: {e}")

        if errors:
            raise ValidationError("\n  ".join(["검증 오류:"] + errors))

        return True

# 테스트 (Test)
print("👤 사용자 데이터 검증 테스트:")

# 올바른 데이터 (Valid data)
valid_user = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'phone': '010-1234-5678',
    'age': 25,
    'password': 'MyPass123'
}

try:
    UserValidator.validate_user_data(valid_user)
    print("  ✓ 올바른 데이터 검증 성공")
except ValidationError as e:
    print(f"  ❌ {e}")

# 잘못된 데이터 (Invalid data)
invalid_user = {
    'username': 'ab',  # 너무 짧음
    'email': 'invalid-email',  # 잘못된 형식
    'phone': '010-12-5678',  # 잘못된 형식
    'age': 200,  # 범위 초과
    'password': 'weak'  # 약한 비밀번호
}

print("\n  잘못된 데이터 검증:")
try:
    UserValidator.validate_user_data(invalid_user)
except ValidationError as e:
    print(f"  ❌ {e}")

print()

# ===== 4. 데코레이터를 활용한 검증 (Validation with decorators) =====
print("="*70)
print("4. 데코레이터를 활용한 검증")
print("="*70)
print()

def validate_input(**validators):
    """
    입력 검증 데코레이터
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 인자 검증
            for arg_name, validator_func in validators.items():
                if arg_name in kwargs:
                    try:
                        validator_func(kwargs[arg_name])
                    except ValidationError as e:
                        raise ValidationError(f"{arg_name} 검증 실패: {e}")

            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_input(
    email=validate_email,
    age=lambda x: validate_range(x, min_val=18, max_val=100, field_name="나이")
)
def register_user(username, email, age):
    """사용자 등록"""
    return f"✓ {username}({email}, {age}세) 등록 성공"

# 테스트 (Test)
print("📝 데코레이터 검증 테스트:")

try:
    result = register_user("홍길동", email="hong@example.com", age=25)
    print(f"  {result}")
except ValidationError as e:
    print(f"  ❌ {e}")

try:
    result = register_user("김철수", email="invalid", age=15)
except ValidationError as e:
    print(f"  ❌ {e}")

print()

# ===== 5. 실전 예제 - 회원가입 폼 (User registration form) =====
print("="*70)
print("5. 실전 예제 - 회원가입 폼")
print("="*70)
print()

class RegistrationForm:
    """회원가입 폼"""

    def __init__(self):
        self.errors = []

    def add_error(self, field, message):
        """오류 추가"""
        self.errors.append(f"{field}: {message}")

    def is_valid(self, data):
        """폼 유효성 검사"""
        self.errors = []

        # 사용자명 검증
        try:
            UserValidator.validate_username(data.get('username', ''))
        except ValidationError as e:
            self.add_error('username', str(e))

        # 이메일 검증
        try:
            validate_email(data.get('email', ''))
        except ValidationError as e:
            self.add_error('email', str(e))

        # 비밀번호 검증
        try:
            validate_password(data.get('password', ''))
        except ValidationError as e:
            self.add_error('password', str(e))

        # 비밀번호 확인
        if data.get('password') != data.get('password_confirm'):
            self.add_error('password_confirm', '비밀번호가 일치하지 않습니다')

        # 전화번호 검증 (선택사항)
        phone = data.get('phone', '').strip()
        if phone:
            try:
                validate_phone(phone)
            except ValidationError as e:
                self.add_error('phone', str(e))

        # 나이 검증
        try:
            age = data.get('age')
            if age is not None:
                UserValidator.validate_age(int(age))
        except (ValueError, TypeError):
            self.add_error('age', '나이는 유효한 숫자여야 합니다')
        except ValidationError as e:
            self.add_error('age', str(e))

        # 약관 동의 확인
        if not data.get('agree_terms', False):
            self.add_error('agree_terms', '약관에 동의해야 합니다')

        return len(self.errors) == 0

    def get_errors(self):
        """오류 목록 반환"""
        return self.errors

# 테스트 (Test)
print("📋 회원가입 폼 검증:")

form = RegistrationForm()

# 테스트 케이스 1: 올바른 데이터
test_data_1 = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'password': 'MyPass123',
    'password_confirm': 'MyPass123',
    'phone': '010-1234-5678',
    'age': 25,
    'agree_terms': True
}

if form.is_valid(test_data_1):
    print("  ✓ 테스트 1 통과: 모든 데이터가 유효함")
else:
    print("  ❌ 테스트 1 실패:")
    for error in form.get_errors():
        print(f"    - {error}")

# 테스트 케이스 2: 잘못된 데이터
test_data_2 = {
    'username': 'ab',  # 너무 짧음
    'email': 'invalid',  # 잘못된 형식
    'password': 'weak',  # 약한 비밀번호
    'password_confirm': 'different',  # 비밀번호 불일치
    'phone': '010-12-5678',  # 잘못된 형식
    'age': -5,  # 음수
    'agree_terms': False  # 약관 미동의
}

print("\n  테스트 2: 잘못된 데이터")
if form.is_valid(test_data_2):
    print("  ⚠️  테스트 2 통과 (실패 예상)")
else:
    print("  ✓ 테스트 2: 예상된 오류 발견")
    for error in form.get_errors():
        print(f"    - {error}")

print()

# ===== 6. 안전한 입력 받기 함수 (Safe input functions) =====
print("="*70)
print("6. 안전한 입력 받기 함수 (Safe Input Functions)")
print("="*70)
print()

def safe_input_int(prompt, min_val=None, max_val=None, default=None):
    """
    안전한 정수 입력 (Safe integer input)
    실제 input() 대신 시뮬레이션
    """
    # 시뮬레이션용 테스트 값
    test_values = ['abc', '-5', '200', '25']

    for test_value in test_values:
        print(f"{prompt} [입력: {test_value}]", end=" ")
        try:
            value = int(test_value)
            if min_val is not None and value < min_val:
                print(f"❌ {min_val} 이상의 값을 입력하세요")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ {max_val} 이하의 값을 입력하세요")
                continue
            print(f"✓ {value}")
            return value
        except ValueError:
            print("❌ 올바른 숫자를 입력하세요")

    return default

# 테스트 (Test)
print("🔢 안전한 정수 입력 테스트:")
result = safe_input_int("나이를 입력하세요 (0-150):", min_val=0, max_val=150)
print(f"\n최종 입력값: {result}")

print()

print("="*70)
print("입력 검증 시스템 완료!")
print("="*70)
print()
print("💡 입력 검증 핵심 원칙:")
print("   1. 사용자 입력은 항상 검증하세요")
print("   2. 명확하고 도움이 되는 오류 메시지 제공")
print("   3. 검증 로직을 재사용 가능하게 작성")
print("   4. 클라이언트와 서버 모두에서 검증")
print("   5. 보안을 고려한 검증 (SQL 인젝션, XSS 등)")
print()
print("💡 Input Validation Key Principles:")
print("   1. Always validate user input")
print("   2. Provide clear and helpful error messages")
print("   3. Write reusable validation logic")
print("   4. Validate on both client and server")
print("   5. Consider security (SQL injection, XSS, etc.)")
