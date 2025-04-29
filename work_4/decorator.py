def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator
def rectArea(length: float, width: float) -> float:
    return length * width

area = rectArea(5, 3)
print("Площадь:", area)