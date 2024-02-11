import pytest
from src.dni import DNI

def injector():
    dni = DNI('64628834F')
    return dni

def test_comprobar_dni_no_es_string():
    with pytest.raises(Exception):
        dni = DNI(943232323223)

def test_comprobar_dni_excede_longitud():
    with pytest.raises(Exception):
        dni = DNI('943232323223')

def test_comprobar_dni_8_primeros_digitos_son_numeros():
    with pytest.raises(Exception):
        dni = DNI('A12345678')

def test_comprobar_dni_ultimo_digito_letra_valida():
    with pytest.raises(Exception):
        dni = DNI('12345678I')

def test_comprobar_dni_esta_bien_formado():
    injector()

def test_get_dni():
    assert type(injector().get_dni()) == str
    assert len(injector().get_dni()) == 9

def test_get_letra_correcta():
    assert injector().get_letra_correcta() == 'F'

def test_comprobar_dni():
    assert injector().comprobar_dni() == True
    dni = DNI('64628834A')
    assert dni.comprobar_dni() == False

def test_crear_string_con_dni_y_letra_correcta():
    assert injector().crear_string_con_dni_y_letra_correcta() == '64628834F' + '\n' + 'Correcto'
    dni = DNI('64628834A')
    assert dni.crear_string_con_dni_y_letra_correcta() == '64628834A' + '\n' + f'Incorrecto, la letra es la: F'