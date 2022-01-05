from Database import database, cursor

class Car:
    def __init__(self, manufacture, model, color, owner_id):
        self.manufacture = manufacture
        self.model = model
        self.color = color
        self.owner_id = owner_id
    
    @staticmethod
    def register_car(manufacture, model, color, owner_id):
        try:
            cursor.execute(f"INSERT INTO `cars` (`manufacture`, `model`, `color`,  `owner_id`) VALUES ('{manufacture}', '{model}', '{color}', {owner_id})")
            database.commit()
            return Car(manufacture, model, color, owner_id)
        except:
            raise Exception("Notika kļūda! Mēģiniet vēlreiz!")
