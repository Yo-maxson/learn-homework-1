"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    sr = 0
    ratings = [{'school_class': '4a', 'scores': [3,4,3,5,5,4,4]}, 
  {'school_class': '4б', 'scores': [4,3,4,4,3,5,2]},
  {'school_class': '4в', 'scores': [3,4,3,5,5,4,4]},
  {'school_class': '4в', 'scores': [5,5,4,5,5,4,3]}]
    for i in ratings:
      sr = i["scores"] + i+1["scores"]
    print(sr)
    
    
if __name__ == "__main__":

    main()


