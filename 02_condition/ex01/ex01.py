# 비교 연산자 사용
weight = int(input("체중을 입력하세요 : "))

# 만약에 몸무게가 55키로 미만이면 "치킨 먹자!!!"
if weight < 55:
    print("치킨 먹자!!!")

# 만약에 몸무게가 100키로 이상이면 "다이어트 시작!"
if weight >= 100:
    print("다이어트 시작!")

# 만약에 몸무게가 68키로이면
if weight == 68:
    print("당신의 몸무게는 68kg이군요")

# 만약에 몸무게가 75키로가 아니면
if weight != 75:
    print("당신의 몸무게는 75kg이 아닙니다.")
