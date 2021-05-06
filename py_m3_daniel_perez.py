
class Vehicle:
    def __init__(self, id, manufacturer, model, color, engine):
        self.id = id
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.engine = engine

    def __str__(self):
        return f"Vehicle(id={self.id}, " \
               f"manufacturer = {self.manufacturer}, " \
               f"model = {self.model}, " \
               f"color = {self.color}, " \
               f"engine = {self.engine} " \
               f")"

    def __repr__(self):
        return self.__str__()


class Motor:
    def __init__(self, id_motor, cc, cv, peso):
        self.id_motor = id_motor
        self.cc = cc
        self.cv = cv
        self.peso = peso

    def __str__(self):
        return f"Motor(id_motor={self.id_motor}, " \
               f"cc = {self.cc}, " \
               f"cv = {self.cv}, " \
               f"peso = {self.peso} " \
               f")"

    def __repr__(self):
        return self.__str__()


vehicles = []


def find_vehicle(id_vehicle):
    for vehicle in vehicles:
        if vehicle.id == id_vehicle:
            return vehicle


def delete_vehicle(id_vehicle):
    for vehicle in vehicles:
        if vehicle.id == id_vehicle:
            del (vehicles[id_vehicle - 1])
            print("El vehículo se ha borrado")


while True:
    print("""
   Gestión de vehículos:
1- Consultar vehículos
2- Consultar un vehículo
3- Crear vehiculo    
4- Actualizar vehiculo    
5- Borrar vehiculo    
6- Borrar todos los vehiculos
7- Salir   

    """)

    option = int(input("Introduce una opción: "))
    if option == 1:
        if len(vehicles) == 0:
            print("No hay vehículos disponibles")
        else:
            print(vehicles)

    if option == 2:
        if len(vehicles) == 0:
            print("No hay vehículos disponibles")
            continue
        id_vehicle = int(input("Introduce el id del vehículo: "))
        Vehicle = find_vehicle(id_vehicle)
        if Vehicle is not None:
            print(vehicle)
        else:
            print("No se ha encontrado el vehículo")

    if option == 3:
        # variables
        id = int(input("Introduce el ID: "))
        manufacturer = input("Introduce el fabricante: ")
        model = input("Introduce el modelo: ")
        color = input("Introduce el color: ")
        id_motor = int(input("Introduce el ID del motor: "))
        cc = int(input("Introduce los cc del motor: "))
        cv = int(input("Introduce los cv del motor: "))
        peso = float(input("Introduce el peso del motor: "))
        # objetos
        engine = Motor(id_motor, cc, cv, peso)
        vehicle = Vehicle(id, manufacturer, model, color, engine)
        vehicles.append(vehicle)

    if option == 4:
        pass

    if option == 5:
        if len(vehicles) == 0:
            print("No hay vehículos")
            continue
        id_vehicle = int(input("Introduce el id del vehículo a borrar: "))
        Vehicle = delete_vehicle(id_vehicle)

    if option == 6:
        bucle = True
        while bucle:
            seguro = input("¿Seguro que quieres borrar todos los vehículos (si, no)? ")

            if seguro == "si":
                vehicles.clear()
                bucle = False
                print("Los vehículos han sido borrados ")
            elif seguro == "no":
                print("No se ha borrado ningún vehículo ")
                bucle = False
            else:
                print("Introduce si o no. ")

    if option == 7:
        break;

print("Fin")
