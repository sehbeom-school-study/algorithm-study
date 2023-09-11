N = int(input())                        # 자료구조 개수 / (4)
A = list(map(int, input().split()))     # 0 큐 1 스택 / (0 1 1 0)
B = list(map(int, input().split()))     # 자료구조에 들어가 있는 원소들 / (1 2 3 4)
M = int(input())                        # 삽입할 원소의 개수 / (3)
C = list(map(int, input().split()))     # 삽입할 원소들의 값 / (2 4 7)

# 스택일 경우 무시 큐만 계산 
answer = []
for i in range(N):
    if A[i] == 0:
        answer.append(B[i])
C_r = C[::-1]
result = C_r + answer
for j in range(M):
    print(result.pop(), end = ' ')