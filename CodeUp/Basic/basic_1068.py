# 정수 1개를 입력받아 평가 출력하기
a = int(input())

if a <= 39:
    print("D")
else:
    if a <= 69:
        print("C")
    else:
        if a <= 89:
            print("B")
        else:
            print("A")