def add(a, b):
    """Функция сложения"""
    return a + b

def subtract(a, b):
    """Функция вычитания"""
    return a - b

# Основная программа
print("Простой калькулятор")
print("Доступные операции:")
print("+ - сложение")
print("- - вычитание") 

# Получаем ввод от пользователя
try:
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+, -, *, /): ")
    num2 = float(input("Введите второе число: "))
    
    # Выполняем операцию в зависимости от введенного оператора
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    else:
        result = "Неверный оператор!"
    
    # Выводим результат
    print(f"Результат: {num1} {operator} {num2} = {result}")
    
except ValueError:
    print("Ошибка: пожалуйста, вводите только числа!")