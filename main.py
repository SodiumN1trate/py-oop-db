from User import User
from Car import Car

user_registred = input("Vai Jūs esat reģistrējušies(y/n)?: ")

while True:
    while True:
        if user_registred == 'y':
            name = input("Ievadiet savu vārdu: ")
            password = input("Ievadiet savu paroli: ")
            try:
                user = User.login(name, password)
                break
            except Exception as e:
                print(e)

        elif user_registred == 'n':
            name = input("Ievadiet savu vārdu: ")
            surname = input("Ievadiet Uzvārdu: ")
            password = input("Ievadiet paroli: ")
            try:
                user = User.register(name, surname, password)
                break
            except Exception as e:
                print(e)

        else:
            print("Nepareiza ievade!")

    what_to_do = input("Vēlaties reģistrēt jaunu automašīnu?(y/n): ")
    if what_to_do.lower() == 'y':
        manufacture = input("Ievadiet automobīļa marku: ")
        model = input("Ievadiet automobīļa modeli: ")
        color = input("Ievadiet automobīļa krāsu: ")
        try:
            car = Car.register_car(manufacture, model, color, user.id)
        except Exception as e:
            print(e)
    else:
        break
