class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users_list = []

    def add_user(self, user):
        if user not in self._users_list:
            self._users_list.append(user)
            print(f'Пользователь {user.get_name()} добавлен.')
        else:
            print('Ошибка. Такой пользователь уже существует.')

    def remove_user(self, user):
        if user in self._users_list:
            self._users_list.remove(user)
            print(f'Пользователь {user.get_name()} удалён.')
        else:
            print('Пользователь не найден.')

    def list_users(self):
        for user in self._users_list:
            print(f'{user.get_user_id()} - {user.get_name()}')

admin = Admin(1, 'Пётр Первый')
user1 = User(2, 'Антон Меньшиков')
user2 = User(3, 'Анна Каренина')

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()
admin.remove_user(user1)
admin.list_users()