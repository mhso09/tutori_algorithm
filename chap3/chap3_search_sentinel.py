from typing import Any, Sequence
import copy

def seq_search(seq:Sequence, key:Any) -> int:
    # 시퀸스 seq에서 key와 값이 같은 원소를 선형검색(보초법)
    a = copy.deepcopy(seq)
    a.append(key) 
    ''' 배열 seq를 a로 복사하고 a의 마지막에 보초인 key를 추가.
    그러면 원래 배열 맨 끝에 보초를 추가한 새로운 배열이 완성
    '''

    i = 0
    while True:
        if a[i] == key:
            break # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
        i += 1
        # 배열 원소를 스캔하여 검색하는 과정을 반복
    return -1 if i == len(seq) else i
    ''' while 문에 의한 반복이 종료되면 찾은 원소가 배열의 원래 데이터인지 보초인지 판단해야한다.
    i 값이 len(seq)와 같으면 찾은 것이 보초이므로 검색 실패한 것을 나타내는 -1을 반환 그렇지 않으면 i를 반환
    '''
if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요 : ')) # num값을 입력받음
    x = [None] * num # 원소 수가 num인 배열 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('검색할 값을 입력: ')) # 검색할 키 ky를 입력받음

    idx = seq_search(x,ky) # ky와 값이 같은 원소를 x 에서 검색

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')