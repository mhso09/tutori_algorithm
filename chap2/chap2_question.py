from typing import Any, Sequence
# # 학생 5명의 점수를 받아 합계와 평균 구하기
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
# # 요구사항 1번
# student = int(input("학생 수를 입력하세요 :"))
# x = [None] * student

# # 요구사항 3번
# # 최댓값
# def max_of(a: Sequence) -> Any:
#     maximum = a[0]
#     for i in range(1, len(a)):
#         if a[i] > maximum:
#             maximum = a[i]
#     return maximum
# # 최솟값
# def min_of(a: Sequence) -> Any:
#     minimum = a[0]
#     for i in range(1, len(a)):
#         if a[i] < minimum:
#             minimum = a[i]
#     return minimum

# for i in range(len(x)):
#     total = 0
#     x[i] = int(input(f'{i+1}번째 학생의 점수를 입력하세요 :'))
#     total += x[i]

# print(x, total)
# upgrade = int(input('확인하거나 수정할 학생의 번호를 선택하세요 :'))

# # 요구사항 2번
# for z, name in enumerate(x, 1):
#     if upgrade == z:
#         print('{}번째 학생의 점수는 {}'.format(z, name))
#         answer = str(input('수정하시겠습니까 ? ( Y / N ) :'))
#         answer.strip().upper()

#         if answer == 'y':
#             a = int(input('수정할 값을 입력하세요 :'))
#             total += a
#             x[i] = a
#             print('수정되었습니다.')
            
#         elif answer == 'n':
#             print('종료합니다.')
#         else :
#             pass
#     else:
#         pass

# ''''''
# print(f' 최대값 : {max_of(x)} \n 최소값 : {min_of(x)} \n 총합 : {total} \n 평균값 : {total / len(x)}')

'''입력, 수정, 삭제, 찾기'''
names = []
scores = []
menu_list = ["1", "2", "3", "4", "5", "6"]
Menu_names = ["입력", "출력", "수정", "삭제", "검색", "종료"]
bFinish = False
# 입력
def insert():
    name = input('학생의 이름 : ')
    score = int(input('점수 등록 : '))
    names.append(name)
    scores.append(score)
    print('등록되었습니다.')
    ins = input('계속 입력하시겠습니까? Y / N')
    ins.upper()
    if ins == 'y':
        insert()
    elif ins == 'n':
        return
    elif ins != 'n':
        while True:
            ins = input('다시 입력해주세요.')
            ins.upper()
            if ins == 'y':
                insert()
            elif ins == 'n':
                break

# 수정
def update():
    name = input('수정할 학생의 이름 : ')
    if name in names:
        idx = names.index(name)
        score = int(input('학생의 점수를 변경합니다. : '))
        scores[idx] = score
        print('수정되었습니다.')
    else :
        print('등록되지 않은 학생입니다.')

# 비어있는지 확인
def nEmpty():
    n = len(names)
    if n == 0:
        return True
    else:
        return False

#리스트 확인
def list_all():
    print('list')
    bEmpty = nEmpty()
    if bEmpty == True: # names 안에 값이 없음
        print('비어있습니다.')
        return
    for i, name in enumerate(names):
        score = scores[i]
        full_score = 0
        print('{0}번째 학생 {1} 점수 {2}'.format(i+1,name,score))
        while i >= 0:
            full_score += scores[i]
            i -= 1
    print(f'총{len(names)}, 총점수 {full_score}')

while not bFinish:
    print('menu\n','-' * 27)
    for a,k in enumerate(Menu_names):
        print(a+1,k)
    print('-' * 27)
    menu = ''
    while True:
        menu = input('메뉴를 선택하세요.')
        menu = menu.strip().upper()
        if menu in menu_list:
            break
    if menu == '1':
        insert()
    elif menu == '2':
        print('모든 학생들을 출력합니다.')
        list_all()
    elif menu == '3':
        update()
    elif menu == '6':
        print('종료합니다.')
        bFinish = True
