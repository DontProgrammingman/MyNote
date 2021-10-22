import pickle
import datetime
import hashlib
import os

Login_PasswordList = 'Login_PasswordList.data'
Notes_List_USER = 'Notes_List_USER.data'


class USER:

    my_dict = dict() # Словарь для хранения логина и пароля

    def __init__(self, Login, password): # Инициализация класса
        self.Login = Login
        self.password = password

    def __setitem__(self, password): # Регистрация пользователя
        self.Login = input('Введите ваш логин: ')
        password = input('Введите ваш пароль: ')
        self.password = input('Введите ваш пароль еще раз: ')
        if self.Login in USER.my_dict:
            print('Такой пользователь уже есть введите другой логин!')
        elif password == self.password:
            self.password = hashlib.md5(self.password.encode()).hexdigest()
            USER.my_dict[self.Login] = self.password
            if self.Login in USER.my_dict:
                f = open(Login_PasswordList, 'wb')
                pickle.dump(USER.my_dict, f)
                f.close()
                print('Создан контакт {} с паролем {}'.format(self.Login, password))
            else:
                print('Произошла ошибка обратитесь Администратору!')
        else:
            print('Пароль не совпал!\nПопробуете еще раз')

    def __delitem__(self): # Удаление пользователя
        self.Login = input('Кого удалить?\n')
        del USER.my_dict[self.Login]
        print('Пользователь {} был удален'.format(self.Login))
        f = open(Login_PasswordList, 'wb')
        pickle.dump(USER.my_dict, f)
        f.close()

    def loading():
        f = open(Login_PasswordList, 'rb')
        try:
            try:
                USER.my_dict = pickle.load(f)
                f.close()
            except EOFError:
                f.close()
        except TypeError:
            f.close()

    loading = staticmethod(loading)

    def Extaction(self): # Вход пользователя
        self.Login = input('Введите свой логин: ')
        self.password = input('Введите свой пароль: ')
        if self.Login in USER.my_dict:
            self.password = hashlib.md5(self.password.encode()).hexdigest()
            if self.password in USER.my_dict[self.Login]:
                print('Поздравляю вы вошли в свой учетную запись!')
                os.system('pause')
                return True
            else:
                print('Вы не правильно ввели пароль')
                os.system('pause')
        else:
            print('Еще нет такого пользователя или вы ввели не правильное имя пользователя')
            os.system('pause')

    def search(self): # Отобразить всех пользователей
        f = open(Login_PasswordList, 'rb')
        USER.my_dict = pickle.load(f)
        f.close()
        print(USER.my_dict)
        os.system('pause')

    def Changes(self, Login):
        print(
            '''Измененния пароля
            ---------------------
            1 - Продолжить
            2 - Отмена''')
        exp = int(input())
        if exp == 1:
            print('Введите новый пароль')
            self.password = input()
            print('Повторите новый пароль')
            password = input()
            if self.password == password:
                self.password = hashlib.md5(self.password.encode()).hexdigest()
                USER.my_dict[self.Login] = self.password
                print('Новый пароль {}'.format(password))
                f = open(Login_PasswordList, 'wb')
                pickle.dump(USER.my_dict, f)
                f.close()
        if exp == 2:
            print('Действие отменнено')
            os.system('pause')

class NOTE:
    MyList = dict() # Хранения Пользователя дат и записей

    def __init__(self, Login, Day): # Инициализация класса
        self.Login = Login
        self.Day = Day

    def __setitem__(self, Login): # Создание записи
        self.Login = Login
        print('''Создание записи!
        Выберите день на который хотите создать запись
        Если запись на сегодня то нажмите три раза Enter
        Если не важен год или месяц оставьте поле пустое''')
        year = input('Год: ')
        month = input('Месяц: ')
        day = input('День: ')

        if len(year) <= 0:
            if len(month) <= 0:
                if len(day) <= 0:  # Создание Записи на Сегодня
                    self.Day = datetime.date.today()
                    print('Введите свою запись на день:\n------------------------------------------\n')
                    self.Note = input()
                    if len(self.Note) > 0:  # Проверка длинны Записи
                        if self.Login in NOTE.MyList:
                            if self.Day in NOTE.MyList[self.Login]:
                                NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                                if self.Note in NOTE.MyList[self.Login][self.Day]:
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                      NOTE.MyList[self.Login]))
                                    os.system('pause')
                                else:
                                    print('Запись не создана, произошла ошибка!')
                                    os.system('pause')
                            else:
                                NOTE.MyList[self.Login] = {self.Day: self.Note}
                                print(NOTE.MyList[self.Login])
                                if self.Note in NOTE.MyList[self.Login][self.Day]:
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                      NOTE.MyList[self.Login]))
                                    os.system('pause')
                                else:
                                    print('Запись не создана, произошла ошибка!')
                                    os.system('pause')
                        else:
                            NOTE.MyList[self.Login] = {self.Day: self.Note}
                            if self.Note in NOTE.MyList[self.Login][self.Day]:
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                  NOTE.MyList[self.Login]))
                                os.system('pause')
                            else:
                                print('Запись не создана, произошла ошибка!')
                                os.system('pause')

                    else:  # Если запись пуста
                        print('Ошибка Запись пустая!')
                        os.system('pause')
                else:
                    self.Day = datetime.date(datetime.date.today().year, datetime.date.today().month,
                                             int(day))  # Только день вводим пользователем
                    print('Введите свою запись на день:\n------------------------------------------\n')
                    self.Note = input()
                    if len(self.Note) > 0:  # Проверка длинны Записи
                        if self.Login in NOTE.MyList:
                            if self.Day in NOTE.MyList[self.Login]:
                                NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                                if self.Note in NOTE.MyList[self.Login][self.Day]:
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                      NOTE.MyList[self.Login]))
                                    os.system('pause')
                                else:
                                    print('Запись не создана, произошла ошибка!')
                                    os.system('pause')
                            else:
                                NOTE.MyList[self.Login] = {self.Day: self.Note}
                                print(NOTE.MyList[self.Login])
                                if self.Note in NOTE.MyList[self.Login][self.Day]:
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                      NOTE.MyList[self.Login]))
                                    os.system('pause')
                                else:
                                    print('Запись не создана, произошла ошибка!')
                                    os.system('pause')
                        else:
                            NOTE.MyList[self.Login] = {self.Day: self.Note}
                            if self.Note in NOTE.MyList[self.Login][self.Day]:
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                  NOTE.MyList[self.Login]))
                                os.system('pause')
                            else:
                                print('Запись не создана, произошла ошибка!')
                                os.system('pause')

                    else:  # Если запись пуста
                        print('Ошибка Запись пустая!')
                        os.system('pause')
            else:
                self.Day = datetime.date(datetime.date.today().year, int(month),
                                         int(day))  # Только месяц и день вводимы пользователем
                print('Введите свою запись на день:\n------------------------------------------\n')
                self.Note = input()
                if len(self.Note) > 0:  # Проверка длинны Записи
                    if self.Login in NOTE.MyList:
                        if self.Day in NOTE.MyList[self.Login]:
                            NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                            if self.Note in NOTE.MyList[self.Login][self.Day]:
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                  NOTE.MyList[self.Login]))
                                os.system('pause')
                            else:
                                print('Запись не создана, произошла ошибка!')
                                os.system('pause')
                        else:
                            NOTE.MyList[self.Login] = {self.Day: self.Note}
                            print(NOTE.MyList[self.Login])
                            if self.Note in NOTE.MyList[self.Login][self.Day]:
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                                  NOTE.MyList[self.Login]))
                                os.system('pause')
                            else:
                                print('Запись не создана, произошла ошибка!')
                                os.system('pause')
                    else:
                        NOTE.MyList[self.Login] = {self.Day: self.Note}
                        if self.Note in NOTE.MyList[self.Login][self.Day]:
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                              NOTE.MyList[self.Login]))
                            os.system('pause')
                        else:
                            print('Запись не создана, произошла ошибка!')
                            os.system('pause')

                else:  # Если запись пуста
                    print('Ошибка Запись пустая!')
                    os.system('pause')
        else:
            self.Day = datetime.date(int(year), int(month), int(day))  # День полностью Вводим пользователем
            print('Введите свою запись на день:\n------------------------------------------\n')
            self.Note = input()
            if len(self.Note) > 0:  # Проверка длинны Записи
                if self.Login in NOTE.MyList:
                    if self.Day in NOTE.MyList[self.Login]:
                        NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                        if self.Note in NOTE.MyList[self.Login][self.Day]:
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                              NOTE.MyList[self.Login]))
                            os.system('pause')
                        else:
                            print('Запись не создана, произошла ошибка!')
                            os.system('pause')
                    else:
                        NOTE.MyList[self.Login] = {self.Day: self.Note}
                        print(NOTE.MyList[self.Login])
                        if self.Note in NOTE.MyList[self.Login][self.Day]:
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                              NOTE.MyList[self.Login]))
                            os.system('pause')
                        else:
                            print('Запись не создана, произошла ошибка!')
                            os.system('pause')
                else:
                    NOTE.MyList[self.Login] = {self.Day: self.Note}
                    if self.Note in NOTE.MyList[self.Login][self.Day]:
                        f = open(Notes_List_USER, 'wb')
                        pickle.dump(NOTE.MyList, f)
                        f.close()
                        print('Пользователь: {}\nСоздал Запись {}'.format(self.Login,
                                                                          NOTE.MyList[self.Login]))
                        os.system('pause')
                    else:
                        print('Запись не создана, произошла ошибка!')
                        os.system('pause')

            else:  # Если запись пуста
                print('Ошибка Запись пустая!')
                os.system('pause')

    def __delitem__(self, Login): # Удаление записи
        self.Login = Login
        print(NOTE.MyList[self.Login])
        day = input('От какого дня хотите удалить запись?(если от сегодня то Enter)\n')
        mounth = input('От какого месяца хотите удалить?(если от нынешнего то нажмите Enter\n')
        year = input('От какого месяца хотите удалить?(если от нынешнего то нажмите Enter)\n')
        if len(year) <= 0:
            if len(mounth) <= 0:
                if len(day) <= 0:
                    self.Day = datetime.date.today()
                    if len(NOTE.MyList[self.Login]) < 1:
                        if len(NOTE.MyList[self.Login][self.Day]) < 1:
                            print(NOTE.MyList[self.Login][self.Day])
                            Number = 0
                            val = input('Какую запись удалить?\n')
                            for value in NOTE.MyList[self.Login][self.Day]:
                                if val == value:
                                    print(val)
                                    print('''Вы уверены?
                                    1 -> Да
                                    2 -> Нет''')
                                    qustion = int(input())
                                    if qustion == 1:
                                        del NOTE.MyList[self.Login][self.Day][Number]
                                        f = open(Notes_List_USER, 'wb')
                                        pickle.dump(NOTE.MyList, f)
                                        f.close()
                                        print(NOTE.MyList[self.Login][self.Day])
                                        os.system('pause')
                                    else:
                                        print('Действие отмененно!')
                                        print(NOTE.MyList[self.Login][self.Day])
                                        os.system('pause')
                                        break
                                else:
                                    Number += 1
                                    continue
                        else:
                            print(NOTE.MyList[self.Login][self.Day])
                            print('''Вы уверены что хотите удалить эту запись?
                            1 -> Да
                            2 -> Нет''')
                            qustion = int(input())
                            if qustion == 1:
                                del NOTE.MyList[self.Login][self.Day]
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print(NOTE.MyList[self.Login])
                                os.system('pause')
                            else:
                                print('Действие отмененно!')
                                os.system('pause')
                    else:
                        print(NOTE.MyList[self.Login])
                        print('''Вы уверены что хотите удалить эту запись?
                                                    1 -> Да
                                                    2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login]
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print(NOTE.MyList[self.Login])
                            os.system('pause')
                        else:
                            print('Действие отмененно!')
                            os.system('pause')
                else:
                    self.Day = datetime.date(datetime.date.today().year, datetime.date.today().month, int(day))
                    if len(NOTE.MyList[self.Login]) < 1:
                        if len(NOTE.MyList[self.Login][self.Day]) < 1:
                            print(NOTE.MyList[self.Login][self.Day])
                            Number = 0
                            val = input('Какую запись удалить?\n')
                            for value in NOTE.MyList[self.Login][self.Day]:
                                if val == value:
                                    print(val)
                                    print('''Вы уверены?
                                    1 -> Да
                                    2 -> Нет''')
                                    qustion = int(input())
                                    if qustion == 1:
                                        del NOTE.MyList[self.Login][self.Day][Number]
                                        f = open(Notes_List_USER, 'wb')
                                        pickle.dump(NOTE.MyList, f)
                                        f.close()
                                        print(NOTE.MyList[self.Login][self.Day])
                                        os.system('pause')
                                    else:
                                        print('Действие отмененно!')
                                        print(NOTE.MyList[self.Login][self.Day])
                                        os.system('pause')
                                        break
                                else:
                                    Number += 1
                                    continue
                        else:
                            print(NOTE.MyList[self.Login][self.Day])
                            print('''Вы уверены что хотите удалить эту запись?
                            1 -> Да
                            2 -> Нет''')
                            qustion = int(input())
                            if qustion == 1:
                                del NOTE.MyList[self.Login][self.Day]
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print(NOTE.MyList[self.Login])
                                os.system('pause')
                            else:
                                print('Действие отмененно!')
                                os.system('pause')
                    else:
                        print(NOTE.MyList[self.Login])
                        print('''Вы уверены что хотите удалить эту запись?
                                                    1 -> Да
                                                    2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login]
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print(NOTE.MyList[self.Login])
                            os.system('pause')
                        else:
                            print('Действие отмененно!')
                            os.system('pause')
            else:
                self.Day = datetime.date(datetime.date.today().year, int(mounth), int(day))
                if len(NOTE.MyList[self.Login]) < 1:
                    if len(NOTE.MyList[self.Login][self.Day]) < 1:
                        print(NOTE.MyList[self.Login][self.Day])
                        Number = 0
                        val = input('Какую запись удалить?\n')
                        for value in NOTE.MyList[self.Login][self.Day]:
                            if val == value:
                                print(val)
                                print('''Вы уверены?
                                1 -> Да
                                2 -> Нет''')
                                qustion = int(input())
                                if qustion == 1:
                                    del NOTE.MyList[self.Login][self.Day][Number]
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    print(NOTE.MyList[self.Login][self.Day])
                                    os.system('pause')
                                else:
                                    print('Действие отмененно!')
                                    print(NOTE.MyList[self.Login][self.Day])
                                    os.system('pause')
                                    break
                            else:
                                Number += 1
                                continue
                    else:
                        print(NOTE.MyList[self.Login][self.Day])
                        print('''Вы уверены что хотите удалить эту запись?
                        1 -> Да
                        2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login][self.Day]
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            print(NOTE.MyList[self.Login])
                            os.system('pause')
                        else:
                            print('Действие отмененно!')
                            os.system('pause')
                else:
                    print(NOTE.MyList[self.Login])
                    print('''Вы уверены что хотите удалить эту запись?
                                                1 -> Да
                                                2 -> Нет''')
                    qustion = int(input())
                    if qustion == 1:
                        del NOTE.MyList[self.Login]
                        f = open(Notes_List_USER, 'wb')
                        pickle.dump(NOTE.MyList, f)
                        f.close()
                        print(NOTE.MyList[self.Login])
                        os.system('pause')
                    else:
                        print('Действие отмененно!')
                        os.system('pause')
        else:
            self.Day = datetime.date(int(year), int(mounth), int(day))
            if len(NOTE.MyList[self.Login]) < 1:
                if len(NOTE.MyList[self.Login][self.Day]) < 1:
                    print(NOTE.MyList[self.Login][self.Day])
                    Number = 0
                    val = input('Какую запись удалить?\n')
                    for value in NOTE.MyList[self.Login][self.Day]:
                        if val == value:
                            print(val)
                            print('''Вы уверены?
                            1 -> Да
                            2 -> Нет''')
                            qustion = int(input())
                            if qustion == 1:
                                del NOTE.MyList[self.Login][self.Day][Number]
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                print(NOTE.MyList[self.Login][self.Day])
                                os.system('pause')
                            else:
                                print('Действие отмененно!')
                                print(NOTE.MyList[self.Login][self.Day])
                                os.system('pause')
                                break
                        else:
                            Number += 1
                            continue
                else:
                    print(NOTE.MyList[self.Login][self.Day])
                    print('''Вы уверены что хотите удалить эту запись?
                    1 -> Да
                    2 -> Нет''')
                    qustion = int(input())
                    if qustion == 1:
                        del NOTE.MyList[self.Login][self.Day]
                        f = open(Notes_List_USER, 'wb')
                        pickle.dump(NOTE.MyList, f)
                        f.close()
                        print(NOTE.MyList[self.Login])
                        os.system('pause')
                    else:
                        print('Действие отмененно!')
                        os.system('pause')
            else:
                print(NOTE.MyList[self.Login])
                print('''Вы уверены что хотите удалить эту запись?
                                            1 -> Да
                                            2 -> Нет''')
                qustion = int(input())
                if qustion == 1:
                    del NOTE.MyList[self.Login]
                    f = open(Notes_List_USER, 'wb')
                    pickle.dump(NOTE.MyList, f)
                    f.close()
                    print(NOTE.MyList[self.Login])
                    os.system('pause')
                else:
                    print('Действие отмененно!')
                    os.system('pause')

    def Changes(self, Login): # Измененние записи
        self.Login = Login
        print('Какую Запись хотите изменить?')
        print(NOTE.MyList[self.Login])
        day = input('От какого дня хотите изменить запись?(если от сегодня то Enter)\n')
        mounth = input('От какого месяца хотите изменить запись?(если от нынешнего то нажмите Enter\n')
        year = input('От какого месяца хотите изменить запись?(если от нынешнего то нажмите Enter)\n')
        if len(year) <= 0:
            if len(mounth) <= 0:
                if len(day) <= 0:
                    self.Day = datetime.date.today()
                    print(NOTE.MyList[self.Login][self.Day])
                    if len(NOTE.MyList[self.Login][self.Day]) < 1:
                        print(NOTE.MyList[self.Login][self.Day])
                        Number = 0
                        val = input('Какую запись изменить?\n')
                        for value in NOTE.MyList[self.Login][self.Day]:
                            if val == value:
                                print(val)
                                print('''Вы уверены?
                                                         1 -> Да
                                                         2 -> Нет''')
                                qustion = int(input())
                                if qustion == 1:
                                    del NOTE.MyList[self.Login][self.Day][Number]
                                    print('Новая запись')
                                    self.Note = input()
                                    NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                                    print('Изменнения внесены теперь выглядит так!')
                                    print(NOTE.MyList[self.Login])
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    os.system('pause')
                                else:
                                    print('Действие отменнено!')
                                    print(NOTE.MyList[self.Login][self.Day])
                                    os.system('pause')
                                    break
                            else:
                                Number += 1
                                continue
                    else:
                        print(NOTE.MyList[self.Login][self.Day])
                        print('''Вы уверены что хотите изменить эту запись?
                                                1 -> Да
                                                2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login][self.Day]
                            print('Новая запись')
                            self.Note = input()
                            NOTE.MyList[self.Login] = {self.Day: self.Note}
                            print('Изменнения внесены теперь выглядит так!')
                            print(NOTE.MyList[self.Login])
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            os.system('pause')
                        else:
                            print('Действие отмененно!')
                            os.system('pause')
                else:
                    self.Day = datetime.date(datetime.date.today().year, datetime.date.today().month, int(day))
                    print(NOTE.MyList[self.Login][self.Day])
                    if len(NOTE.MyList[self.Login][self.Day]) < 1:
                        print(NOTE.MyList[self.Login][self.Day])
                        Number = 0
                        val = input('Какую запись изменить?\n')
                        for value in NOTE.MyList[self.Login][self.Day]:
                            if val == value:
                                print(val)
                                print('''Вы уверены?
                                                                             1 -> Да
                                                                             2 -> Нет''')
                                qustion = int(input())
                                if qustion == 1:
                                    del NOTE.MyList[self.Login][self.Day][Number]
                                    print('Новая запись')
                                    self.Note = input()
                                    NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                                    print('Изменнения внесены теперь выглядит так!')
                                    print(NOTE.MyList[self.Login])
                                    f = open(Notes_List_USER, 'wb')
                                    pickle.dump(NOTE.MyList, f)
                                    f.close()
                                    os.system('pause')
                                else:
                                    print('Действие отменнено!')
                                    print(NOTE.MyList[self.Login][self.Day])
                                    os.system('pause')
                                    break
                            else:
                                Number += 1
                                continue
                    else:
                        print(NOTE.MyList[self.Login][self.Day])
                        print('''Вы уверены что хотите изменить эту запись?
                                                                    1 -> Да
                                                                    2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login][self.Day]
                            print('Новая запись')
                            self.Note = input()
                            NOTE.MyList[self.Login] = {self.Day: self.Note}
                            print('Изменнения внесены теперь выглядит так!')
                            print(NOTE.MyList[self.Login])
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            os.system('pause')
                        else:
                            print('Действие отмененно!')
                            os.system('pause')
            else:
                self.Day = datetime.date(datetime.date.today().year, int(mounth), int(day))
                print(NOTE.MyList[self.Login][self.Day])
                if len(NOTE.MyList[self.Login][self.Day]) < 1:
                    print(NOTE.MyList[self.Login][self.Day])
                    Number = 0
                    val = input('Какую запись изменить?\n')
                    for value in NOTE.MyList[self.Login][self.Day]:
                        if val == value:
                            print(val)
                            print('''Вы уверены?
                                                                         1 -> Да
                                                                         2 -> Нет''')
                            qustion = int(input())
                            if qustion == 1:
                                del NOTE.MyList[self.Login][self.Day][Number]
                                print('Новая запись')
                                self.Note = input()
                                NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                                print('Изменнения внесены теперь выглядит так!')
                                print(NOTE.MyList[self.Login])
                                f = open(Notes_List_USER, 'wb')
                                pickle.dump(NOTE.MyList, f)
                                f.close()
                                os.system('pause')
                            else:
                                print('Действие отменнено!')
                                print(NOTE.MyList[self.Login][self.Day])
                                os.system('pause')
                                break
                        else:
                            Number += 1
                            continue
                else:
                    print(NOTE.MyList[self.Login][self.Day])
                    print('''Вы уверены что хотите изменить эту запись?
                                                                1 -> Да
                                                                2 -> Нет''')
                    qustion = int(input())
                    if qustion == 1:
                        del NOTE.MyList[self.Login][self.Day]
                        print('Новая запись')
                        self.Note = input()
                        NOTE.MyList[self.Login] = {self.Day: self.Note}
                        print('Изменнения внесены теперь выглядит так!')
                        print(NOTE.MyList[self.Login])
                        f = open(Notes_List_USER, 'wb')
                        pickle.dump(NOTE.MyList, f)
                        f.close()
                        os.system('pause')
                    else:
                        print('Действие отмененно!')
                        os.system('pause')
        else:
            self.Day = datetime.date(int(year), int(mounth), int(day))
            print(NOTE.MyList[self.Login][self.Day])
            if len(NOTE.MyList[self.Login][self.Day]) < 1:
                print(NOTE.MyList[self.Login][self.Day])
                Number = 0
                val = input('Какую запись изменить?\n')
                for value in NOTE.MyList[self.Login][self.Day]:
                    if val == value:
                        print(val)
                        print('''Вы уверены?
                                                                     1 -> Да
                                                                     2 -> Нет''')
                        qustion = int(input())
                        if qustion == 1:
                            del NOTE.MyList[self.Login][self.Day][Number]
                            print('Новая запись')
                            self.Note = input()
                            NOTE.MyList[self.Login][self.Day] = [NOTE.MyList[self.Login][self.Day], self.Note]
                            print('Изменнения внесены теперь выглядит так!')
                            print(NOTE.MyList[self.Login])
                            f = open(Notes_List_USER, 'wb')
                            pickle.dump(NOTE.MyList, f)
                            f.close()
                            os.system('pause')
                        else:
                            print('Действие отменнено!')
                            print(NOTE.MyList[self.Login][self.Day])
                            os.system('pause')
                            break
                    else:
                        Number += 1
                        continue
            else:
                print(NOTE.MyList[self.Login][self.Day])
                print('''Вы уверены что хотите изменить эту запись?
                                                            1 -> Да
                                                            2 -> Нет''')
                qustion = int(input())
                if qustion == 1:
                    del NOTE.MyList[self.Login][self.Day]
                    print('Новая запись')
                    self.Note = input()
                    NOTE.MyList[self.Login] = {self.Day: self.Note}
                    print('Изменнения внесены теперь выглядит так!')
                    print(NOTE.MyList[self.Login])
                    f = open(Notes_List_USER, 'wb')
                    pickle.dump(NOTE.MyList, f)
                    f.close()
                    os.system('pause')
                else:
                    print('Действие отмененно!')
                    os.system('pause')

    def loading():
        f = open(Notes_List_USER, 'rb')
        try:
            try:
                NOTE.MyList = pickle.load(f)
                f.close()
            except EOFError:
                f.close()
        except TypeError:
            f.close()

    loading = staticmethod(loading)

    def view(self, Login): # Просмотр записей одним пользователем
        self.Login = Login
        f = open(Notes_List_USER, 'rb')
        NOTE.MyList = pickle.load(f)
        f.close()
        print(NOTE.MyList[self.Login])
        os.system('pause')

U = USER('', '')
USER.loading()

while True:
    try:
        os.system('cls')
        print(
            '''Добро пожаловать!
            ------------------------
            1 - Вы новый пользователь
            2 - Вы существующий пользователь
            3 - Выход
            ''')

        choose = int(input())

        if choose == 1:
            os.system('cls')
            U.__setitem__('')

        if choose == 2:
            if len(USER.my_dict) < 1:
                os.system('cls')
                print('Пользователей еще нет!')
            else:
                if U.Extaction():
                    N = NOTE('', '')
                    NOTE.loading()
                    try:
                        if len(NOTE.MyList[U.Login]) <= 1:
                            while True:
                                os.system('cls')
                                print(
                                '''Меню Пользователя: {}
                                Выши записи\n{}\n
                                -----------------
                                0 -> Просмотр записи
                                1 -> Создание записи
                                2 -> Редактирование записи
                                3 -> Удаление записи
                                4 -> Назад
                                5 -> Выход
                                6 -> Удалить пользователя
                                7 -> Отобразить пользователей
                                8 -> Изменить пароль'''.format(U.Login, N.MyList[U.Login]))
                                CH = int(input())
                                if CH == 0:
                                    N.view(U.Login)
                                if CH == 1:
                                    N.__setitem__(U.Login)
                                if CH == 2:
                                    N.Changes(U.Login)
                                if CH == 3:
                                    N.__delitem__(U.Login)
                                    break
                                if CH == 4:
                                    break
                                if CH == 5:
                                    choose = 3
                                    break
                                if CH == 6:
                                    U.__delitem__()
                                    break
                                if CH == 7:
                                    U.search()
                                if CH == 8:
                                    U.Changes(U.Login)
                    except KeyError:
                        while True:
                            os.system('cls')
                            print(
                            '''Меню Пользователя: {}
                            -----------------
                            1 -> Создание записи
                            2 -> Назад
                            3 -> Выход
                            4 -> Удалить пользователя
                            5 -> Отобразить пользователей
                            6 -> Изменить пароль'''.format(U.Login))
                            CH = int(input())
                            if CH == 1:
                                os.system('cls')
                                N.__setitem__(U.Login)
                            if CH == 2:
                                os.system('cls')
                                break
                            if CH == 3:
                                os.system('cls')
                                choose = 3
                                break
                            if CH == 4:
                                os.system('cls')
                                if U.__delitem__() == U.Login:
                                    CH == 4
                                    break
                                else:
                                    break
                            if CH == 5:
                                os.system('cls')
                                U.search()
                            if CH == 6:
                                U.Changes(U.Login)


        if choose == 3:
            print('До свидание!')
            os.system('cls')
            break

    except ValueError:
        print('Ошибка введеные данные не могут быть обработаны')
    except KeyboardInterrupt:
        print('Вы отменили операцию')