def is_valid_temperature (value):
    """숫자로 변환 가능한 값인지 검사합니다."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False
