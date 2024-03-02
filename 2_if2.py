"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def string_comparison(first_string, second_string):
  if type(first_string) != str or type(second_string) != str:
    return 0
  elif first_string == second_string:
    return 1
  elif len(first_string) > len(second_string) and second_string == ("learn"):
    return 3
  elif len(first_string) > len(second_string):
    return 2

  


string_result_1 = string_comparison(2, "Привет")
print(string_result_1)

string_result_2 = string_comparison("Привет", "Привет")
print(string_result_2)

string_result_3 = string_comparison("Приветттттт", "Привет")
print(string_result_3)

string_result_4 = string_comparison("Привет", "learn")
print(string_result_4)



if __name__ == "__string_comparison__":
    string_comparison()
