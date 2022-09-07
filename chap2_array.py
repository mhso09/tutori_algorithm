# 학생 5명의 점수를 받아 합계와 평균 구하기
# print("학생 그룹 점수의 합계와 평균을 구합니다.")

# score1 = int(input("1번 학생의 점수 : "))
# score2 = int(input("2번 학생의 점수 : "))
# score3 = int(input("3번 학생의 점수 : "))
# score4 = int(input("4번 학생의 점수 : "))
# score5 = int(input("5번 학생의 점수 : "))
# total = 0

# total += score1
# total += score2
# total += score3
# total += score4
# total += score5
# print(f'합계 : {total}점 \n 평균 : {total/5}점')

'''
요구사항 1 : 학생 수를 변경하는 경우
요구사항 2 : 특정 학생의 시험 점수를 확인하거나 변경하는 경우
요구사항 3 : 최저점과 최고점을 구하거나 정렬이 필요한 경우

'''

# 리스트 기초
list1 = []
list2 = [1,2,3,]
list3 = ['a','b','c',]
print(list1, list2, list3)
# 원소 = 리스트 내부의 값
list4 = list() # 빈 리스트
list5 = list('abc') # ['a','b','c']문자열의 각 문자로부터 원소 생성
list6 = list([1,2,3]) # [1,2,3] 리스트로부터 원소 생성
list7 = list((1,2,3)) # [1,2,3] 튜플로부터 원소 생성
list8 = list({1,2,3}) # [1,2,3] 집합으로부터 원소 생성
print(list4, list5, list6, list7, list8)
# 특정 범위의 정수로 구성된 리스트는 range()와 list()의 조합
list09 = list(range(7))  # [0, 1, 2, 3, 4, 5, 6]
list10 = list(range(3, 8))  # [3, 4, 5, 6, 7]
list11 = list(range(3, 15, 2))  # [3, 5, 7, 9, 11, 13]
print(list09, list10, list11)

# 튜플 기초
tuple01 = ()
tuple02 = 1,
tuple03 = (1,)
tuple04 = 1,2,3
tuple05 = 1,2,3,
tuple06 = (1,2,3)
tuple07 = (1,2,3,)
tuple08 = "a", "b", "c",
# tuple의 값이 하나인 경우 끝에 ,를 쓰지 않으면 단순변수가 되기 때문에 꼭 사용하자
tuple09 = tuple()  # 빈 튜플
tuple10 = tuple('abc')  # ('a','b','c')문자열의 각 문자로부터 원소 생성
tuple11 = tuple([1, 2, 3])  # (1,2,3) 리스트로부터 원소 생성
tuple12 = tuple((1, 2, 3))  # (1,2,3) 집합으로부터 원소 생성
#리스트와 마찬가지로 range사용 가능
tuple13 = tuple(range(7)) # (0, 1, 2, 3, 4, 5, 6)
tuple14 = tuple(range(3, 8)) # (3, 4, 5, 6, 7)
tuple15 = tuple(range(3, 15, 2)) # (3, 5, 7, 9, 11, 13)
print(tuple13, tuple14, tuple15)
# 좌변에 여러 변수를 넣고 우변에 리스트나 튜플을 넣으면 좌변의 변수에 풀어 대입 이를 언팩 이라고 한다.
x = [1,2,3]
a,b,c = x
print((a, b, c)) # (1, 2, 3)

