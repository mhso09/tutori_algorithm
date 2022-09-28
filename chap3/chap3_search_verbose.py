from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    # 시퀸스 a에서 key와 값이 같은 원소를 이진 검색(실행 과정을 출력)
    pl = 0 # 검색범위 맨 앞 원소의 인덱스
    pr = len(a) - 1 # 검색범위 맨 뒤 원소의 인덱스

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) +2) * '-')

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스

        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc -pl) * 4) * ' ' + '+',end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr - pc) * 4 -2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|',end='')
        for i in range(len(a)):
            print(f'{a[i]:4}',end='')
        print('\n   |')


        if a[pc] == key:
            return pc  # 검색 성공
        elif a[pc] < key:
            pl = pc + 1  # 검색 범위를 뒤쪽 절반으로 좁힘
        else:
            pr = pc - 1  # 검색 범위를 앞쪽 절반으로 좁힘
        if pl > pr:
            break
    return -1  # 검색 실패

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : '))  # num값을 입력받음
    x = [None] * num  # 원소 수가 num인 배열 생성

    print('배열 데이터를 오름차순으로 입력하세요 ')

    x[0] = int(input('x[0] : '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]:'))
            if x[i] >= x[i - 1]: # 바로 직전에 입력한 원소값보다 큰 값을 입력
                break

    ky = int(input('검색할 값을 입력: '))  # 검색할 키 ky를 입력받음

    idx = seq_search(x, ky)  # ky와 값이 같은 원소를 x 에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

'''이진검색의 경우 배열이 오름차순으로 정렬되어 있어야 한다.'''
