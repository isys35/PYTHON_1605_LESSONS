age = int(input('Введите ваш возраст: '))

# if age < 18:
#     print('Вы еще молоды!')
# elif 18 <= age < 60:
#     print('Вам еще работать и работать!')
#     if age == 21:
#         print('Вам пора в лес!')
# else:
#     print('Вам пора на пенсию!')
#
# if age < 18:
#     print('Вы еще молоды!')
# else:
#     print('Вам еще работать и работать!')


command = input('Введите команду: ')

match command:
    case 'left':
        print('Вы повернули налево')
    case 'right':
        print('Вы повернули направо')
    case 'forward':
        print('Вы пошли вперед')


state = 'Молодой' if age < 18 else 'Взрослый'



variable = 100
