import pytest

from src.tablaAsignacion import TablaAsignacion

def injector():
    tabla = TablaAsignacion()
    return tabla

def test_mostrar_tabla():
    assert type(injector().mostrar_tabla()) == list

def test_devolver_letra():
    assert injector().devolver_letra(0) == 'T'
    assert injector().devolver_letra(3) == 'A'
    assert injector().devolver_letra(6) == 'Y'
    assert injector().devolver_letra(9) == 'D'
    assert injector().devolver_letra(12) == 'N'
    assert injector().devolver_letra(15) == 'S'
    assert injector().devolver_letra(22) == 'E'

def test_calcular_letra():
    assert injector().calcular_letra('64628834F') == 'F'
    assert injector().calcular_letra('99565004M') == 'M'
    assert injector().calcular_letra('15602023L') == 'L'
    assert injector().calcular_letra('07462467W') == 'W'
    assert injector().calcular_letra('23688657Z') == 'Z'
    assert injector().calcular_letra('66250804V') == 'V'
    assert injector().calcular_letra('47471420H') == 'H'

