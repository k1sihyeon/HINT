def is_abnormal(value, limit) :
    """측정값이 기준치를 초과하면 True 반환"""
    return value > limit

if __name__ == '___main___':
    print('테스트:', is_abnormal(35, 30)) # True
    print('테스트:', is_abnormal(20, 30)) # False
