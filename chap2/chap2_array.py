from typing import Any, Sequence

# # 리스트 기초
# list1 = []
# list2 = [1,2,3,]
# list3 = ['a','b','c',]
# print(list1, list2, list3)
# # 원소 = 리스트 내부의 값
# list4 = list() # 빈 리스트
# list5 = list('abc') # ['a','b','c']문자열의 각 문자로부터 원소 생성
# list6 = list([1,2,3]) # [1,2,3] 리스트로부터 원소 생성
# list7 = list((1,2,3)) # [1,2,3] 튜플로부터 원소 생성
# list8 = list({1,2,3}) # [1,2,3] 집합으로부터 원소 생성
# print(list4, list5, list6, list7, list8)
# # 특정 범위의 정수로 구성된 리스트는 range()와 list()의 조합
# list09 = list(range(7))  # [0, 1, 2, 3, 4, 5, 6]
# list10 = list(range(3, 8))  # [3, 4, 5, 6, 7]
# list11 = list(range(3, 15, 2))  # [3, 5, 7, 9, 11, 13]
# print(list09, list10, list11)

# # 튜플 기초
# tuple01 = ()
# tuple02 = 1,
# tuple03 = (1,)
# tuple04 = 1,2,3
# tuple05 = 1,2,3,
# tuple06 = (1,2,3)
# tuple07 = (1,2,3,)
# tuple08 = "a", "b", "c",
# # tuple의 값이 하나인 경우 끝에 ,를 쓰지 않으면 단순변수가 되기 때문에 꼭 사용하자
# tuple09 = tuple()  # 빈 튜플
# tuple10 = tuple('abc')  # ('a','b','c')문자열의 각 문자로부터 원소 생성
# tuple11 = tuple([1, 2, 3])  # (1,2,3) 리스트로부터 원소 생성
# tuple12 = tuple((1, 2, 3))  # (1,2,3) 집합으로부터 원소 생성
# #리스트와 마찬가지로 range사용 가능
# tuple13 = tuple(range(7)) # (0, 1, 2, 3, 4, 5, 6)
# tuple14 = tuple(range(3, 8)) # (3, 4, 5, 6, 7)
# tuple15 = tuple(range(3, 15, 2)) # (3, 5, 7, 9, 11, 13)
# print(tuple13, tuple14, tuple15)
# # 좌변에 여러 변수를 넣고 우변에 리스트나 튜플을 넣으면 좌변의 변수에 풀어 대입 이를 언팩 이라고 한다.
# x = [1,2,3]
# a,b,c = x
# print((a, b, c)) # (1, 2, 3)

# #인덱스식 사용
# y = [11,22,33,44,55,66,77]
# print(y[2], y[-2]) # 33 66 -는 뒤에서부터 찾아옴
# y[-2] = 3.14
# print(y[-2]) # 3.14 해당 원소에 새로운 값을 대입
# # y[7] = 88
# # print(y) 이는 7번 원소가 없어서 에러 발생
# y.append(28) # 마지막 원소를 추가하여 해당 수를 대입
# print(y)

# #슬라이드식 원소 접근
# s = [11, 22, 33, 44, 55, 66, 77]
# print(s[0:6])  # [11, 22, 33, 44, 55, 66] 0~5까지 원소 출력
# print(s[:7:2])  # [11, 33, 55, 77] 0~6까지 2개씩 건너뛰며 출력
# print(s[-4:-2])  # [44, 55] 뒤에서 4번째부터 뒤에서 2번째 원소 출력
# print(s[:-8:-2])  # [77, 55, 33, 11] -1~-7까지 2개씩 건너뛰며 출력
# print(s[3:1]) # j값 1이 i값 3보다 작지만 오류는 없음

# # 배열 원소의 최댓값 구하기
# def max_of(a):
#     maximum = a[0]
#     for i in range(1,len(a)):
#         if a[i] > maximum:
#             maximum = a[i]

# 시퀸스 원소의 최댓값 구하기
# 시퀸스형 a원소의 최댓값 반환
def max_of(a: Sequence) -> Any:
    # 배열 a의 최댓값을 구하는 함수 정의
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
# 값을 받아 실행
if __name__=='__main__':
    print('배열의 최댓값 구하기')
    num = int(input('원소 수를 입력 : '))
    x = [None] * num # 원소가 num인 리스트 생성
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력 : '))
    print(f'최댓값 : {max_of(x)}')