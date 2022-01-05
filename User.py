from Database import cursor, database

class User:
    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname

    @staticmethod
    def login(name, password):
        try:
            cursor.execute(f"SELECT * FROM `users` WHERE BINARY `name` = '{ name }' AND `password` = '{ password }'")
            data = cursor.fetchall()[0]
            return User(data[0], data[1], data[2])
        except:
            raise Exception("Nav atrasts šāds lietotājs")
  

    @staticmethod
    def register(name, surname, password):
        if User.is_user_exist(name) == False:
            try:
                cursor.execute(f"INSERT INTO `users` (`name`, `surname`, `password`) VALUES ('{ name }', '{ surname }', '{ password }')")
                database.commit()
                return User.login(name, password)
            except:
                raise Exception("Kaut kas nogāja greizi!")
        else:
            raise Exception("Lietotājs ar tādu vārdu jau reģistrēts!")

    @staticmethod
    def is_user_exist(name):
        try:
            cursor.execute(f"SELECT * FROM `users` WHERE BINARY `name` = '{ name }' ")
            cursor.fetchall()[0]
            return True
        except:
            return False
