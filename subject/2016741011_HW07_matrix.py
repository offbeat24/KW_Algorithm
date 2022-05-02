#랜덤 사이즈의 랜덤 행렬에서 최대값 길찾기
import random

size = random.randint(1, 11)
maxsum = [[0]*(size+1) for _ in range(size+1)]
matrix = list()

for _ in range(size) :  
    matrix.append(list(random.sample(range(1,100), size)))

print(matrix)

for i in range(1, size+1) :
    for j in range(1, size+1) :
        maxsum[i][j] = matrix[i-1][j-1] + max(maxsum[i-1][j], maxsum[i][j-1])
        
print(maxsum[size][size])
