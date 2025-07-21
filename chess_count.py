# 문제 출처 : https://www.acmicpc.net/problem/3003

chess = [1,1,2,2,2,8]
a = list(map(int, input().split()))

# 문제 풀이(1)
for i in range(len(chess)):
  print(chess[i] - a[i], end=' ')


# 문제 풀이(2)
print(' '.join([str(chess[i] - v) for i, v in enumerate(a)]))


# 문제 풀이(3)
import numpy as np
chess = np.array([1,1,2,2,2,8])
a = np.array(list(map(int, input().split())))

# '*'를 붙이면 이 배열을 하나씩 분해해서 개별 인자로 전달한다.
print(*chess - a)

# "print(*chess - a)" 같은 의미
# result = chess - a
# print(result[0], result[1], result[2], result[3], result[4], result[5])



# "*"
# 함수 호출 시 : print(*리스트) → 리스트 요소를 각각 전달
# 함수 정의 시 : def func(*args) → 가변 인자 받기
# 튜플/리스트 분해 : a, *b, c = [1, 2, 3, 4] → b는 [2, 3]

# * 언패킹 연산자 예제
# (1) print() 함수에서 언패킹
numbers = [1,2,3,4,5]
print(*numbers)    
# output : 1 2 3 4 5


# (2) 함수 인자 전달 시
def add(x, y, z):
    return x + y + z

nums = [1, 2, 3]
print(add(*nums))
# output : 6


# (3) 여러 변수에 나누기 (리스트 분해)
a, *b, c = [1, 2, 3, 4, 5]

print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5


# (4) 리스트/튜플/wlqgkq 합치기
a = [1, 2, 3]
b = [4, 5, 6]

merged = [*a, *b]
print(merged)
# output : [1, 2, 3, 4, 5, 6]


# (5) 딕셔너리에서도 사용 가능 (**)
# '**'는 딕셔너리의 key-value 쌍을 언패킹한다.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3}

merged = {**dict1, **dict2}
print(merged)
# output : {'a': 1, 'b': 2, 'c': 3}








