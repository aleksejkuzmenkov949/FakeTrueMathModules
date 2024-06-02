# Создаем модуль fake_math
import math

def divide(first, second):
    try:
        result = first / second
        return result
    except ZeroDivisionError:
        return 'Ошибка'