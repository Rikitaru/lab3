import matplotlib.pyplot as plt
import random
from tqdm import tqdm

list1 = []
def monte_carlo(n):
    results = 0
    for _ in tqdm(range(n)):
        results = results + random.randint(0,1)
        # Высчитывание возможных значений
        prob_value = results / (_ + 1)
        # Включение возможных значений в список
        list1.append(prob_value)
        plt.axhline(y=0.5, color='r', linestyle='-')
        plt.xlabel("Итераций")
        plt.ylabel("Вероятность")
        plt.plot(list1)
    plt.style.use('dark_background')
    plt.show()
    return results / n

answer = monte_carlo(3000)
print("Финальные значения: ", answer)
plt.show()