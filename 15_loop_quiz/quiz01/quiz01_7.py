# 피라미드 출력하기
'''
    *       # 공백 4, 별 1, 1번째 행
   ***      # 공백 3, 별 3, 2번째 행
  *****     # 공백 2, 별 5, 3번째 행
 *******    # 공백 1, 별 7, 4번째 행
*********   # 공백 0, 별 9, 5번째 행
'''

for i in range(5):  # 하나를 넣는 것은 몇 번 도는지임.   5번
    # 공백
    for j in range(5 - i - 1):   # 5- 0 = 5번, 4번 3번 2번 1번
        print(" ", end="")

    # 별 찍기
    # 1 3 5 7 9   1부터 2씩 증가
    # 별의 개수: 짝수: 2n, 홀수: 2n + 1(-1이라하면 i가 0부터 시작이라..)
    # (2 * i) + 1
    for k in range((2 * i) + 1):
        print("*", end="")


    print()




n = 5
for i in range(n):  # 0 1 2 3 4 : 5개의 행
    # 공백을 찍기 위한 for문
    # 공백의 규칙: (4 - i)만큼 찍어야 함.
    for j in range(n - i - 1): # 처음에 4번 돌아야 함. 4 - 0. 0부터 시작이므로 3이어야 하므로 -1을 함
        print(" ", end=" ")

    # 별을 찍기 위한 for문. 1부터 +2씩 증가
    # 별의 개수 규칙은 (행(i) * 2) - 1
    for k in range(1, (i + 1) * 2):
        print("*", end=" ")

    print() # 행이 끝나면 줄바꿈 처리
