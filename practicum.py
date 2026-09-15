WATER_PER_KG = 30
ML_TO_LITERS = 1000

print("Приветствую в приложении FitLife!")
user_name = input("Давайте познакомимся! Как Вас зовут? ")

try:
    user_age = int(input(f"Приветствую , {user_name}, теперь введите Ваш возраст: "))
except ValueError:
    print("Возраст должен быть целым числом")

try:
    user_weight = float(input("Теперь введите,пожалуйста, Ваш вес в килограммах: "))
except ValueError:
    print("Введите вес числовым значением - пример: 60.5")

try:
    user_height = float(input("И ваш рост в метрах: "))
except ValueError:
    print("Введите вес числовым значением - пример: 1.65")

def bmi_calculation(weight: float, height: float):
    bmi = weight / (height ** 2)

    return bmi

def water_calculation(weight: float):
    water_ml = weight * WATER_PER_KG
    water_liters = water_ml / ML_TO_LITERS
    return water_liters

def report():
    print()
    print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
    print(f"Твой Индекс Массы Тела: {round(bmi_calculation(user_weight, user_height), 1)}")
    print(f"Рекомендуемая норма воды: {round(water_calculation(user_weight), 1)} в день")
    print()
    print("Расчет окончен. Будьте здоровы!")

report()
