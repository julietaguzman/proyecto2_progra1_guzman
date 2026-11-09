import pytest
import json
from catalogo import leer_archivo, crear_catalogo, resumen_por_orbita, satelites_en_zona
from satelite import Satelite

def test_leer_archivo():
    resultado = leer_archivo("datos/satelites.json")
    assert type(resultado) is list
    assert len(resultado) > 0

def test_crear_catalogo():
    registros = [
        {
        "OBJECT_NAME": "CALSPHERE 1",
        "OBJECT_ID": "1964-063C",
        "EPOCH": "2026-10-14T14:21:25.466688",
        "MEAN_MOTION": 13.76730837,
        "ECCENTRICITY": 0.00243553,
        "INCLINATION": 90.2208,
        "RA_OF_ASC_NODE": 74.5342,
        "ARG_OF_PERICENTER": 291.4443,
        "MEAN_ANOMALY": 198.023,
        "EPHEMERIS_TYPE": 0,
        "CLASSIFICATION_TYPE": "U",
        "NORAD_CAT_ID": 900,
        "ELEMENT_SET_NO": 999,
        "REV_AT_EPOCH": 8785,
        "BSTAR": 0.00056429819,
        "MEAN_MOTION_DOT": 5.64e-06,
        "MEAN_MOTION_DDOT": 0
        },
        {
        "OBJECT_NAME": "CALSPHERE 2",
        "OBJECT_ID": "1964-063E",
        "EPOCH": "2026-10-14T11:27:54.596736",
        "MEAN_MOTION": 13.52908228,
        "ECCENTRICITY": 0.00169509,
        "INCLINATION": 90.2317,
        "RA_OF_ASC_NODE": 78.5946,
        "ARG_OF_PERICENTER": 237.821,
        "MEAN_ANOMALY": 195.4493,
        "EPHEMERIS_TYPE": 0,
        "CLASSIFICATION_TYPE": "U",
        "NORAD_CAT_ID": 902,
        "ELEMENT_SET_NO": 999,
        "REV_AT_EPOCH": 87239,
        "BSTAR": 5.6971978e-05,
        "MEAN_MOTION_DOT": 4.7e-07,
        "MEAN_MOTION_DDOT": 0
        },
        {
        "OBJECT_NAME": "LCS 1",
        "OBJECT_ID": "1965-034C",
        "EPOCH": "2026-10-14T05:23:16.941696",
        "MEAN_MOTION": 9.89310992,
        "ECCENTRICITY": 0.00109039,
        "INCLINATION": 32.1401,
        "RA_OF_ASC_NODE": 254.3932,
        "ARG_OF_PERICENTER": 186.1791,
        "MEAN_ANOMALY": 173.8573,
        "EPHEMERIS_TYPE": 0,
        "CLASSIFICATION_TYPE": "U",
        "NORAD_CAT_ID": 1361,
        "ELEMENT_SET_NO": 999,
        "REV_AT_EPOCH": 22167,
        "BSTAR": 0.0011283058,
        "MEAN_MOTION_DOT": 1.7e-07,
        "MEAN_MOTION_DDOT": 0
        }]

    resultado = crear_catalogo(registros)
    
    assert len(resultado) == 3
    assert resultado[0].nombre == "CALSPHERE 1"
    assert resultado[0].num_catalogo == 900 
    assert resultado[1].nombre == "CALSPHERE 2"
    assert resultado[1].num_catalogo == 902
    assert resultado[2].nombre == "LCS 1"
    assert resultado[2].num_catalogo == 1361

def test_resumen_por_orbita():
    satelites = [
        Satelite("A", 1, 0, 0, 400),
        Satelite("B", 2, 0, 0, 2000),
        Satelite("C", 3, 0, 0, 3000)
    ]

    resumen = resumen_por_orbita(satelites)
    assert resumen["LEO"]["cantidad"] == 1
    assert resumen["MEO"]["cantidad"] == 2
    assert resumen["MEO"]["min"] == 2000
    assert resumen["MEO"]["max"] == 3000
    assert resumen["MEO"]["promedio"] == 2500.0

def test_satelites_en_zona():
    satelites = [
            Satelite("Adentro", 1, -40, -70, 400),
            Satelite("Afuera", 2, 50, 50, 4000),
        ]

    encontrados = satelites_en_zona(satelites, -76.30, -46.13, -66.30, -36.13)  # Bariloche
    assert len(encontrados) == 1
    assert encontrados[0].nombre == "Adentro"

    

