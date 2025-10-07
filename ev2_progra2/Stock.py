from Ingrediente import Ingrediente

class Stock:
    def __init__(self):
        self.lista_ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        for ingrediente in self.lista_ingredientes:
            if ingrediente.nombre == nombreingrediente:
                 self.lista_ingredientes.remove(ingrediente)

    def eliminar_ingrediente(self, nombre_ingrediente):
        for ingrediente in self.lista_ingredientes:
            if ingrediente.nombre == nombreingrediente:
                self.lista_ingredientes.remove()
                break

        pass    

    def verificar_stock(self):
        pass

    def actualizar_stock(self, nombre_ingrediente, nueva_cantidad):
        pass

    def obtener_elementos_menu(self):
        pass

