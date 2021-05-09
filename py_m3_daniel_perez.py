vehicles = []
vehicle_properties = ["id", "fabricante", "modelo", "color", "id_motor"]

class Vehicle:
    def __init__(self, id, fabricante, modelo, color, motor):
        self.id = id
        self.fabricante = fabricante
        self.modelo = modelo
        self.color = color
        self.motor = motor

    def __str__(self):
        return f"Vehicle(id={self.id}, " \
               f"fabricante = {self.fabricante}, " \
               f"modelo = {self.modelo}, " \
               f"color = {self.color}, " \
               f"motor = {self.motor} " \
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





def find_vehicle(id_vehicle):
    for vehicle in vehicles:
        if vehicle.id == id_vehicle:
            return vehicle


def delete_vehicle(id_vehicle):
    for vehicle in vehicles:
        if vehicle.id == id_vehicle:
            del (vehicles[id_vehicle - 1])
            print("El vehículo se ha borrado")

def edit_vehicle():

    product_index = int(input("Introduzca el índice del vehículo que desea editar de 1 a {}: ".format(len(vehicles))))

    property_edit = ''
    while property_edit not in vehicle_properties:
        property_edit = str(input("Introduzca la propiedad que desea editar: "
                                  "\"id\", "
                                  "\"fabricante\", "
                                  "\"modelo\", "                                 
                                  "\"color\", "
                                  "\"id_motor\", "
                                  "\"cc\", "
                                  "\"cv\", "
                                  "\"peso\": "))
        if property_edit not in vehicle_properties:
            continue

        if property_edit == "id":
            vehicles[product_index - 1].id = int(
                input("Introduzca el nuevo id del vehículo {}: ".format(product_index)))
        elif property_edit == "fabricante":
            vehicles[product_index - 1].fabricante = str(
                input("Introduzca el nuevo fabricante del vehículo {}: ".format(product_index)))
        elif property_edit == "modelo":
            vehicles[product_index - 1].modelo = str(
                input("Introduzca el nuevo modelo del vehículo {}: ".format(product_index)))
        elif property_edit == "color":
            vehicles[product_index - 1].color = str(
                input("Introduzca el nuevo color del vehículo {}: ".format(product_index)))
        elif property_edit == "id_motor":
            vehicles[product_index - 1].motor.id_motor = int(
                input("Introduzca el nuevo id del motor del vehículo {}: ".format(product_index)))
        elif property_edit == "cc":
            vehicles[product_index - 1].motor.cc = int(
                input("Introduzca los cc del motor del vehículo {}: ".format(product_index)))
        elif property_edit == "cv":
            vehicles[product_index - 1].motor.cv = int(
                input("Introduzca los cv del motor del vehículo {}: ".format(product_index)))
        elif property_edit == "peso":
            vehicles[product_index - 1].motor.peso = int(
                input("Introduzca el peso del motor del vehículo {}: ".format(product_index)))

        print("Vehículo {} modificado correctamente."
              .format(vehicles[product_index - 1].fabricante)
              )
while True:
    print("""
   Gestión de vehículos:
1- Consultar vehículos
2- Consultar un vehículo
3- Crear un vehículo    
4- Editar un  vehículo    
5- Borrar un vehículo    
6- Borrar todos los vehículos
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
        motor = Motor(id_motor, cc, cv, peso)
        vehicle = Vehicle(id, manufacturer, model, color, motor)

        vehicles.append(vehicle)
        print("Vehículo regitrado")

    if option == 4:
        edit_vehicle()

    if option == 5:
        if len(vehicles) == 0:
            print("No hay vehículos")
            continue
        id_vehicle = int(input("Introduce el índice del vehículo que deseas borrar de 1 a {}: ".format(len(vehicles))))
        Vehicle = delete_vehicle(id_vehicle)

    if option == 6:
        bucle = True
        while bucle:
            seguro = input("¿Seguro que quieres borrar todos los vehículos (s, n)? ")

            if seguro == "s":
                vehicles.clear()
                bucle = False
                print("Los vehículos han sido borrados ")
            elif seguro == "n":
                print("No se ha borrado ningún vehículo ")
                bucle = False
            else:
                print("Introduce 's' o 'n' ")

    if option == 7:
        break;

print("Fin")
