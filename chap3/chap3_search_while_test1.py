from chap3_search_while import seq_search

#seq_search()함수를 사용하여 실수 검색

print('실수를 검색합니다.')
print('종료를 원하시면 "end"를 입력하세요.')

num = 0
x = [] # 빈리스트 작성
while True:
    s = input(f'x[{num}] : ')
    if s == 'end':
        break
    x.append(float(s)) # 배열 맨 끝에 원소 추가
    num += 1

ky = float(input('검색할 값을 입력하세요 : '))

idx = seq_search(x,ky) # ky와 값이 같은 원소를 x에서 검색
if idx == -1:
    print('')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')

#seq_search()함수를 사용하여 특정 인덱스 검색

t = (4,7,5.6,2,3.14,1)
s = 'string'
a = ['DTS','AAC','FLAC']

print(f'{t}에서 5.6의 인덱스는 {seq_search(t,5.6)}입니다.')
print(f'{s}에서 n의 인덱스는 {seq_search(s,"n")}입니다.')
print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a,"DTS")}입니다.')
