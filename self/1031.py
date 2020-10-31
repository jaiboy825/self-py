# 10월 31일 파이썬 간단한 문제 풀기
# 문자열 문제

# 1번 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요
letters = 'python'
# 결과 : p t
print(letters[0], letters[2])

# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요
license_plate = "24가 2210"
# 결과 : 2210
print(license_plate[-4:])

# 아래의 문자열에서 '홀'만 출력하세요
string = '홀짝홀짝홀짝'
# 결과 : 홀홀홀
print(string[::2])

# 문자열을 거꾸로 뒤집어 출력하세요
string = 'PYTHON'
# 결과 : NOHTYP
print(string[::-1])

# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요
phone_number = "010-1111-2222"
# 결과 : 01011112222
phone_number = phone_number.replace('-','')
print(phone_number)

# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요
url = "http://youtube.com"
# 결과 : com
url_split = url.split('.')
print(url_split[1])

# 아래 코드의 실행 결과 예상
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 결과 : 문자열은 수정할 수 없다.

# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요
string = 'abcdfe2a354a32a'
# 결과 : Abcdfe2A354A32A
string = string.replace('a', 'A')
print(string)

# 아래 코드의 실행 결과 예상
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# 결과 : abcd 그대로 출력됨 왜냐하면 replace 함수는 그냥 새로운 문자열 객체를 리턴해주기 때문