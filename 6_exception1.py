"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    try:
        user_response = ''
        while user_response.lower() != 'хорошо':
            user_response = input('Как дела? ')
            if user_response.lower() == 'хорошо':
                print('Отлично! То что нужно.')
            else:
                print('Подожду, пока не скажешь - хорошо')
    except KeyboardInterrupt:
        print('\nПока')

if __name__ == "__main__":
    hello_user()