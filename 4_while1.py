"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
  question = ""
  while question != 'Хорошо':
    print('как дела?')
    question = input()
  print('Ну и славненько.')


    
if __name__ == "__main__":
    hello_user()
