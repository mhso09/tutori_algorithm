'''3장에서 배울 알고리즘은 배열검색이며 선형검색 이진검색 해시법이 있다.
선형검색 : 무작위로 늘어놓은 데이터 집합에서 검색을 수행
이진검색 : 일정한 규칙으로 늘어놓은 데이터 집합에서 아주 빠른 검색을 수행
해시법 : 추가, 삭제가 자주 일어나는 데이터 집합에서 아주 빠른 검색을 수행
 - 체인법 : 같은 해시값 데이터를 연결 리스트로 연결하는 방법
 - 오픈주소법 : 데이터를 위한 해시값이 충돌할 때 재해시하는 방법'''

# while 문으로 작성한 선형 검색 알고리즘
from typing import Any, Sequence

def seq_search(a:Sequence, key:Any) -> int:
    # 시퀸스 a에서 key와 값이 같은 원소를 선형검색(while)
    i = 0

    while True:
        if i == len(a):
            return -1 # 검색에 실패하여 -1을 반환
        if a[i] == key:
            return i # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
        i += 1

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