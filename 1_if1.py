"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def main(age):
    if age <= 6:
        result = 'Учеба в саду'
    elif 6 < age <= 17:
        result = 'Учеба в школе'
    elif 17 < age <= 23:
        result = 'Учеба в ВУЗе'
    else:
        result = 'Работа'
    print(result)

if __name__ == "__main__":
    age = int(input('Введите возраст: '))
    main(age)