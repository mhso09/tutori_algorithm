# 자료형을 정하지 않은 리스트 원소 확인
x = [15,64,7,3.14,[32,55],'abc']
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')
# 옅은 복사
x = [[1,2,3],[4,5,6]]
y = x.copy()
x[0][1] = 9
print(x,y)

# 깊은 복사
import copy
x = [[1, 2, 3], [4, 5, 6]]
y = copy.deepcopy(x)
x[0][1] = 9
print(x, y)