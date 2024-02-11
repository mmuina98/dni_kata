

class TablaAsignacion:

    def __init__(self):
        self.tabla = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        #self.tabla = {0:'T', 1:'R', 2:'W', 3:'A', 4:'G', 5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D', 10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z', 15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L', 20: 'C', 21: 'K', 22: 'E'}
    
    def mostrar_tabla(self, position = None):
        tabla = self.tabla
        return tabla

    def devolver_letra(self, position):
        return self.tabla[position]

    def calcular_letra(self, dni):
        dni = int(dni[:-1])
        posicion_letra = dni % 23
        return self.devolver_letra(posicion_letra)

