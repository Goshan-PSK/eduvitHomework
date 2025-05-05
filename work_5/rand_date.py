import random
from datetime import datetime, timedelta
from array import array

def genData(begin, end):
    delta = end - begin
    randDays = random.randint(0, delta.days)
    return begin + timedelta(days=randDays)

today = datetime.today()
fiveYearsAgo = datetime.today() - timedelta(days=5 * 365)

dates = [genData(fiveYearsAgo, today) for _ in range(10)]

dates.sort()

diffs = array('i')
for i in range(1, len(dates)):
    delta = (dates[i] - dates[i - 1]).days
    diffs.append(delta)

print("Разница между датами:")
for i in range(1, len(dates)):
    date1 = dates[i - 1].strftime('%Y-%m-%d')
    date2 = dates[i].strftime('%Y-%m-%d')
    diff = diffs[i - 1]
    print(f"Разница между {date1} и {date2}: {diff} дней")