import matplotlib.pyplot as plt
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# plt.plot([1, 2, 3, 4], [3, 6, 10, 12])
x_values = [1, 2, 3, 4]
y_values = [3, 6, 10, 12]
plt.plot(x_values, y_values, 'o--')
plt.xlabel('x축')
plt.ylabel('y축')
plt.show()
