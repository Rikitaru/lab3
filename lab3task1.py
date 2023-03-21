import random
import math
import matplotlib.pyplot as plt
C = 2000
s = 0

plt.xlim(xmax=1.5,xmin=0)
plt.ylim(ymax=1.5,ymin=0)
for i in range(C):
    x = random.random ()
    y = random.random ()
    y_predict=math.sqrt(1-x**2)
    if y_predict >= y:
        s=s+1
        plt.plot(x,y,'r+')
plt.show()
predict_value=4*s/C
print(predict_value)