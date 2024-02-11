from src.tablaAsignacion import TablaAsignacion

class DNI:

    def __init__(self, dni):
        self.dni = dni
        self.comprobar_dni_esta_bien_formado()
        

    def comprobar_dni_esta_bien_formado(self):
        try:
            assert type(self.dni) == str
            assert len(self.dni) == 9
        except:
            raise Exception('El dni no tiene el formato adecuado. Tiene que ser un str de 9 dígitos')
        try:
            int(self.dni[:-1])
        except:
            raise Exception('Los 8 primeros dígitos del dni tienen que ser números')
        try:
            tabla = TablaAsignacion()
            assert self.dni[-1] in tabla.mostrar_tabla() 
        except:
            raise Exception('El último dígito del dni tiene que ser una letra válida')


    def get_dni(self):
        return self.dni[:]
    
    def get_letra_correcta(self):
        tabla = TablaAsignacion()
        return tabla.calcular_letra(self.get_dni())
    
    def comprobar_dni(self):
        dni = self.get_dni()
        if dni[-1] == self.get_letra_correcta():
            return True  
        else:
            return False
    
    def crear_string_con_dni_y_letra_correcta(self): 
        if self.comprobar_dni() == True:
            return self.get_dni() + '\n' + 'Correcto'
        else:
           return self.get_dni() + '\n' + f'Incorrecto, la letra es la: {self.get_letra_correcta()}'
    
    def printar_dni_y_letra_correcta(self):
        print(self.crear_string_con_dni_y_letra_correcta())

if __name__== '__main__':

    dni1 = DNI('64628834F')
    dni1.printar_dni_y_letra_correcta()


