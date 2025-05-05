import math
import random
import statistics as stats

numbers = [random.randint(1,100) for _ in range(100)]

mean = stats.mean(numbers)
med = stats.median(numbers)
stdev = stats.stdev(numbers)
sum = math.sqrt(sum(numbers))

print(f"Среднее: {mean:.{2}f}, Медиана: {med:.{2}f}, Стандартное отклонение: {stdev:.{2}f},Корень из суммы : {sum:.{2}f}")