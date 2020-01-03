import sys

def data_user(): #ввод данных пользователем и расчет ИМТ
    global name, sex, age, height, weight, bmi
    name = input('Введите ваше ФИО: ')
    sex = input('Введите ваше пол (женский/мужской): ')
    age = int(input('Введите ваш возраст (лет): '))
    height = int(input('Введите ваш рост (см): '))
    weight = int(input('Введите ваш вес (кг): '))
    bmi2 = weight/(height**2/10000)
    bmi = round(bmi2, 1)
    return name, sex, age, height, weight, bmi

def grah_bmi(): #график ИМТ
    symb = str('_')
    x = 100 - int(bmi)
    print('0' +(symb*int(bmi)) +str(bmi) +(symb*x) +'100')

def dict_user():
    d  = {'пол' : sex,'возраст' : age, 'рост' : height, 'вес' : weight, 'ИМТ' : bmi}
    users[name] = d
    return users[name]

def commands(): #создание панели команд
    from prettytable import PrettyTable
    tbl = PrettyTable()
    tbl.field_names = ["№", "Команды"]
    tbl.add_row(["1", 'Вывести список пользователей'])
    tbl.add_row(["2", 'Добавить пользователя'])
    tbl.add_row(["3", 'Удалить пользователя'])
    tbl.add_row(["4", 'Выбрать пользователя'])
    tbl.add_row(["5", 'Завершить работу'])
    print(tbl)
    global numb
    numb = int(input('Введите номер команды:')) #удалила return


def show_list(): #вывод списка пользователей
    if numb == 1:
        if len(users) == 0:
            print("В систему не внесены данные о пользователях.")
        else:
            for key, value in users.items():
                print('Пользователь:\n\t ' + key, '\nДанные:\n\t' + str(value))

def add_user(): #добавление пользователя
    if numb == 2: 
        data_user()
        dict_user()
        #рекомендации
        if sex == str('мужской') or sex == str('м'):
            print('Уважаемый ' +str(name) + '! \nВаш пол: ' +str(sex) +'. \nВаш возраст: ' +str(age) + ' лет. \nВаш рост: ' +str(height) + ' см. \nВаш вес: ' +str(weight) +' кг.')
            print('Ваш индекс массы тела: ' +str(bmi) +'.')
        elif sex == str('женский') or sex == str('ж'):
            print('Уважаемая ' +str(name) + '! \nВаш пол: ' +str(sex) +'. \nВаш возраст: ' +str(age) + ' лет. \nВаш рост: ' +str(height) + ' см. \nВаш вес: ' +str(weight) +' кг.')
            print('Ваш индекс массы тела: ' +str(bmi) +'.')
        else:
            print(str(name) + '! \nВаш пол: ' +str(sex) +'. \nВаш возраст: ' +str(age) + ' лет. \nВаш рост: ' +str(height) + ' см. \nВаш вес: ' +str(weight) +' кг.')
            print('Ваш индекс массы тела: ' +str(bmi) +'.')                 
        if bmi > 0 and bmi < 15:
            print('Настоятельно рекомендуется набор массы тела. Если не получается – обратитесь к врачу.')    
        elif bmi > 15 and bmi < 18.5:
            print('Рекомендуется немного поправиться.')
        elif bmi > 18.5 and bmi < 25:
            print('Вы в отличной форме. Так держать!')
        elif bmi > 25 and bmi < 30:
            print('Рекомендуется снижение массы тела. Повышен риск неинфекционных и системных заболеваний.')
        elif bmi > 30:
            print('Настоятельно рекомендуется снижение массы тела. Высокий риск для здоровья! Высока вероятность заболеть неинфекционными или системными заболеваниями.')
        grah_bmi()

def delete_user(): #удаление пользователя
    if numb == 3: 
        del_user = input('Введите ФИО/ID пользователя:')
        if del_user in users:
            del(users[del_user])
        else:
            print('Такого пользователя нет в системе.')

def select_user(): #выбор пользователя
    if numb == 4: 
        show_user = input('Введите ФИО/ID пользователя:')
        if show_user in users:
            change = input('Хотите внести изменения (да/нет): ')
            if change == 'да':
                data_user()
                grah_bmi()
                dict_user()
                if show_user != name:
                    del(users[show_user])
            elif change == 'нет':
                print(' ')
        else:
            print('Такого пользователя нет в системе.')

def finish(): #завершение работы
    if numb == 5: 
        sys.exit()

users = dict()
while True:
    commands()
    show_list()
    add_user()
    delete_user()
    select_user()
    finish()
