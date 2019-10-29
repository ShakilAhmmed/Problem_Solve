import math

x1, y1 = input().split()
x2, y2 = input().split()
f_result = float(x2) - float(x1)
s_result = float(y2) - float(y1)
m_result = (f_result * f_result) + (s_result * s_result)
print("{0:.4f}".format(math.sqrt(m_result)))
