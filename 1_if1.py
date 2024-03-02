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

def define_activity(age):
    if age < 4:
        return 'Вы еще слишком малы'
    elif age < 7:
        return 'Вы учитесь в детском саду'
    elif age < 18:
        return 'Вы учитесь в школе'
    elif age < 24:
        return 'Вы учитесь в ВУЗе'
    else:
        return 'Вы уже работаете'
    
def main():
    age = int(input('Введите Ваш возраст: '))
    user_activity = define_activity(age)
    print(user_activity)

if __name__ == "__main__":
    main()
