def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 2, 3]) == 2.0
assert average_num([1, "2", 3]) == 2.0
assert average_num(["4", "5", 1]) == 3.33
assert average_num([1.5, 2.5]) == 2.0
assert average_num(["3.5", 2]) == "Bad request"
assert average_num([1, "abc", 3]) == "Bad request"
assert average_num(['']) == "Bad request"
assert average_num(["0", 0, 0]) == 0.0
assert average_num([-1, "-2", 3]) == 0.0
assert average_num(["", 1]) == "Bad request"

print("All tests passed.")