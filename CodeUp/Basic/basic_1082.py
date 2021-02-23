# 16진수 구구단
sixteen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

a = input()
print('{0}*1={1}'.format(a, a))

for i in range(2, 16):
    ans = []    # 빈 리스트 생성
    num = sixteen.index('{0}'.format(a))    # 입력받은 문자의 인덱스 찾기
    multiply = int(num) * i    # 입력받은 문자의 숫자와 2부터 15까지 차례대로 곱하기
    quotient = multiply // 16               # 몫
    rest = multiply % 16                    # 나머지
    ans.append(sixteen[int(quotient)])      # 몫 부분을 ans에 저장
    ans.append(sixteen[rest])               # 나머지를 ans에 저장
    ans = ''.join(ans)                      # 몫 + 나머지
    print('{0}*{1}={2}'.format(a, sixteen[i], ans))