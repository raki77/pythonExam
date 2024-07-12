


# 예제 사용
# original_string = "naver"
# lpad_string = lpad(original_string, 10, '*')
# rpad_string = rpad(original_string, 10, '*')

# print("Left Padded:", lpad_string)  # Left Padded: *****naver
# print("Right Padded:", rpad_string)  # Right Padded: naver*****

def lpad(string, length, char=' '):
    """
    왼쪽으로 문자열을 채우는 함수
    :param string: 원본 문자열
    :param length: 최종 문자열의 길이
    :param char: 채울 문자 (기본값: 공백)
    :return: 채워진 문자열
    """
    return string.rjust(length, char)

def rpad(string, length, char=' '):
    """
    오른쪽으로 문자열을 채우는 함수
    :param string: 원본 문자열
    :param length: 최종 문자열의 길이
    :param char: 채울 문자 (기본값: 공백)
    :return: 채워진 문자열
    """
    return string.ljust(length, char)

