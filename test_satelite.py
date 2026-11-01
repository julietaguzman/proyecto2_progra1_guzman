import pytest
from satelite import parametros_latitud, parametros_longitud, parametros_altitud

# Test de latitud

def test_latitud_normal_valido():
    assert parametros_latitud(-80) == -80.0
    assert parametros_latitud(5) == 5.0
    assert parametros_latitud(80) == 80.0

def test_latitud_limite_valido():
    assert parametros_latitud(-90) == -90.0 
    assert parametros_latitud(90) == 90.0 

def test_latitud_invalido():
    with pytest.raises(ValueError):
        parametros_latitud(-100)
    with pytest.raises(ValueError): 
        parametros_latitud(100) 

# Test de longitud

def test_longitud_normal_valido():
    assert parametros_longitud(-170) == -170.0
    assert parametros_longitud(-33) == -33.0
    assert parametros_longitud(170) == 170.0

def test_longitud_limite_valido():
    assert parametros_longitud(-180) == -180.0 
    assert parametros_longitud(180) == 180.0 

def test_longitud_invalido():
    with pytest.raises(ValueError):
        parametros_longitud(-200)
    with pytest.raises(ValueError): 
        parametros_longitud(200) 

# Test de altitud

def test_altitud_normal_valido():
    assert parametros_altitud(100) == 100.0
    assert parametros_altitud(5000) == 5000.0
    
def test_altitud_invalido():
    with pytest.raises(ValueError):
        parametros_altitud(99)
    with pytest.raises(ValueError): 
        parametros_altitud(0) 
