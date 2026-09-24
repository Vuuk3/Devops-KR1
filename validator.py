# validator.py
def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация российского номера телефона."""
    import re
    pattern = r'^\+?7\d{10}$'
    cleaned = phone.replace('-', '').replace(' ', '')
    return bool(re.match(pattern, cleaned))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС по контрольной сумме."""
    import re

    cleaned = snils.replace('-', '').replace(' ', '')
    if not re.fullmatch(r'\d{11}', cleaned):
        return False

    numbers = [int(digit) for digit in cleaned[:9]]
    check_sum = int(cleaned[9:])
    calculated = sum((9 - index) * digit for index, digit in enumerate(numbers))

    if calculated < 100:
        expected = calculated
    elif calculated % 101 == 100:
        expected = 0
    else:
        expected = calculated % 101

    return expected == check_sum

