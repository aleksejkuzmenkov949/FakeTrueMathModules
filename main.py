# Создаем модуль main
import fake_math as fm
import true_math as tm

# Импортируем функции divide из модулей fake_math и true_math
# с разными именами для избежания конфликта имен
fake_divide = fm.divide
true_divide = tm.divide

# Запускаем функции в модуле main и выводим результаты
result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)