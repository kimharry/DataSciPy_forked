import matplotlib.pyplot as plt  # 지면 효율을 위해서 앞으로 이 줄은 생략함

x  = [x for x in range(-20, 20)] # -20에서 20사이의 수를 1의 간격으로 생성
y1 = [2*t for t in x]            # 2*x를 원소로 가지는 y1 함수
y2 = [t**2 + 5 for t in x]       # x**2 + 5를 원소로 가지는 y2 함수
y3 = [-t**2 - 5 for t in x]      # -x**2 - 5를 원소로 가지는 y3 함수
# 빨강색 점선, 녹색 실선과 세모기호, 파랑색 별표와 점선으로 각각의 함수를 표현
plt.plot(x, y1, 'r--', x, y2, 'g^-', x, y3, 'b*:')
plt.axis([-30, 30, -30, 30])    # 그림을 그릴 영역을 지정함
plt.show()