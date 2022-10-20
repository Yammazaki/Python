

data = []

def create_contacts():
    new_contact = {'name':input('Имя:'), 'surname':input('Фамилия:'), 'phone':input('Телефон:')}
    data.append(new_contact)
    print('Контакт добавлен')



def check_contacts():
    print(data)



def looking_contacts():
    choise_users = input('Введите имя пользователя: ')
    for choise_users in data:
         User_name = choise_users.get('name')
         User_sur = choise_users.get('surname')
         Phone = choise_users.get('phone')
         print(f' Name - {User_name}, Sur-name - {User_sur}, phone - {Phone}')


def update_contacts():
    choise_users = input('Введите имя пользователя: ')
    for choise_users in data:
        choise_update = input('Что Вы хотите редактировать? 1 - Изменить имя, 2 - Изменить фамилию, 3 - Изменить телефон \n')
        if choise_update == '1':
            choise_users.get('name')
            new_redact = {'name':input('Введите новое имя: ')}
            choise_users.update(new_redact)
            print(data)
        if choise_update == '2':
            choise_users.get('surname')
        if choise_update == '3':
            choise_users.get('phone')

while True:
    choice = input(''' 1 - Создать контакт
2 - Просмотреть телефонную книгу
3 - Найти контакт 
4 - Редактировать контакт
5 - Удалить контакт
q - Exit
     ''')
    if choice == '1':
        create_contacts()
    if choice == '2':
        check_contacts()
    if choice == '3':
        looking_contacts()
    if choice == '4':
        update_contacts()
    if choice == '5':
        pass
    if choice == 'q':
        break