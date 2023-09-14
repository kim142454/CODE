x = int(input("x값 요청"))
y = int(input("y값 요청"))

# and 는 논리 게이트로, 파이썬에서 두개 이상의 조건이 같을 때를 의미하며, 조건과 조건 사이에 적어 사용할 수 있다 

if x > 0 and y > 0:
    print("제 1사분면")

elif x > 0 and y < 0:
    print("제 4사분면")

elif x < 0 and y > 0:
    print("제 2사분면")

else:
    print("제 3사분면")