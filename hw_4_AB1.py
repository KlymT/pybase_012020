'''
Разработать приложение “Адресная книга”
Реквизиты контакта:
Фамилия - обязательно
Имя - обязательно
Отчество - опционально
Почтовый адрес
Список E-Mail в котором первый будет основным
Список телефонов
Список мессенджеров: пара значений - название (из предопределённого списка) и аккаунт

Функциональность

1. Меню действий пользователя
a. Создать контакт
b. Вывести список контактов на экран в виде красивой таблицы.
c. Изменить контакт
d. Удалить контакт
e. Сохранить список контактов на диск
f. Поиск контакта по подстроке
по фамилии
по имени
по всем реквизитам

2. Прочитать список контактов с диска (если есть файл) при запуске программы
3. При выходе спрашивать о необходимости сохранения списка контактов в файл на диск.
4. Вывести список контактов в текстовый файл (отчёт по всем реквизитам).
'''


class Contact:

    def __init__(self,  surname='', name='', patronymic=None):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mail_address = []
        self.e_mail = []
        self.phone_num = []
        self.messenger = {}
        global id
        id += 1
        self.id = id

    def __str__(self):
        return f"\n{self.id}: {self.name} {self.surname} {self.patronymic}\n{self.phone_num}\n{self.e_mail}\n{self.messenger}\n{self.mail_address}"


id = 0

contact1 = Contact()
contact1.name = 'Klym'
contact1.surname = 'Trybrat'
contact1.patronymic = 'Alexandrovich'
contact1.mail_address = 'Kyiv, Lva Tolstogo 57/2010'
contact1.e_mail = 'klimt@ukr.net'
contact1.phone_num = '12345678'
contact1.messenger = {1: 'vk', 2: 'telegram', 3: 'messenger'}

contact2 = Contact('vova', 'petrov', 'lva Tolstogo 25',)
# contact3 = Contact('ova', 'petrov', 'lva Tolstogo 25', 'kt@ukr.net', '9876543', 'telegram')
# contact4 = Contact('va', 'petrov', 'lva Tolstogo 25', 'kt@ukr.net', '9876543', 'telegram')
# contact5 = Contact('a', 'petrov', 'lva Tolstogo 25', 'kt@ukr.net', '9876543', 'telegram')

print(contact1, contact2)
# , contact3, contact4, contact5)


# class ContactsBook:
#
#     def __init__(self):
#         self.contacts = []
#
#
#     def __str__(self):


