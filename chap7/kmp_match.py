# KMP법으로 문자열 검색

def kmp_match(txt:str, pat:str) -> int:
    # KMP법으로 문자열 검색
    pt = 0 # txt 따라가는 커서
    pp = 0 # pat 따라가는 커서
    skip = [0] * (len(pat) + 1) # 건너뛰기 표

    # 건너뛰기표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]
    
    return pt - pp if pp == len(pat) else -1

if __name__ == "__main__":
    s1 = input('텍스트 입력 : ')
    s2 = input('패턴 입력 : ')

    idx = kmp_match(s1, s2)

    if idx == -1:
        print('텍스트 안에 패턴이 없습니다.')
    else:
        print('{}번째 문자가 일치합니다.'.format(idx + 1))