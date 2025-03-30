dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

keys = list(dct.keys())
values = list(dct.values())
catValues = keys + values

print("Keys: ", *keys, "\n", "Values: ", *values, "\n", "Cat: ", *catValues)