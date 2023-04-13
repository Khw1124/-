def read_single_digit(num) :
    if num == 1 :
        return '일'
    elif num == 2 :
        return '이'
    elif num == 3 :
        return '삼'
    elif num == 4 :
        return '사'
    elif num == 5 :
        return '오'
    elif num == 6 :
        return '육'
    elif num == 7 :
        return '칠'
    elif num == 8 :
        return '팔'
    elif num == 9 :
        return '구'
    else :
        return '영'
def read_number(number) :
    a = number // 100
    b = (number % 100) // 10
    c = (number % 100) % 10
    return read_single_digit(a) + ' ' + read_single_digit(b) + ' ' + read_single_digit(c)

num = int(input('세 자리 정수 입력:'))
result = read_number(num)
print(result)
