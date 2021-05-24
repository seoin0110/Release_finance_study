#3.1 넘파이 배열

#3.1.1 배열 생성

import numpy as np
A = np.array([[1, 2], [3, 4]])
print(A)

#3.1.2 배열 정보 보기

print(type(A))
print(A.ndim)
print(A.shape)
print(A.dtype)
print(A.max(), A.mean(), A.min(), A.sum())

#3.1.3 배열의 접근

print(A[0])
print(A[1])
print(A[0][0], A[0][1])
print(A[1][0], A[1][1])
print(A[0, 0], A[0, 1])
print(A[1, 0], A[1, 1])
print(A[A>1])

#3.1.4 배열 형태 바꾸기

print(A)
print(A.T)
print(A)
print(A.flatten())

#3.1.5 배열의 연산

print(A)
print(A + A)
print(A - A)
print(A * A)
print(A / A)

#3.1.6 브로드캐스팅

print(A)
B = np.array([10, 100])
print(A * B)

#3.1.7 내적 구하기

print(B.dot(B))
print(A.dot(B))
