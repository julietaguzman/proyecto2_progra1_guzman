import json
from satelite import Satelite
from funciones_base import obtener_posicion

def leer_archivo(ruta):
    with open(ruta, "r") as archivo:
        return json.load(archivo)

def catalogo(registros):
    satelites = []
    for registro in registros:
        latitud, longitud, altitud = obtener_posicion(registro)
        satelite = Satelite(
            nombre = registro["OBJECT_NAME"],
            num_catalogo = int(registro["NORAD_CAT_ID"]),
            latitud = latitud,
            longitud = longitud, 
            altitud = altitud
        )
        satelites.append(satelite)
    return satelites

def resumen_por_orbita(satelites):
    agrupados = {}
    for satelite in satelites:
        tipo = satelite.tipo_orbital()
        if tipo not in agrupados:
            agrupados[tipo] = []
        agrupados[tipo].append(satelite.altitud)

    resumen = {}
    for tipo, altitudes in agrupados.items():
        resumen[tipo] = {
        "cantidad": len(altitudes),
        "min": min(altitudes),
        "max": max(altitudes),
        "promedio": sum(altitudes) / len(altitudes),
    }
    return resumen

def satellites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max):
    return [
        satelite
        for satelite in satelites
        if satelite.esta_en_zona(lon_min, lat_min, lon_max, lat_max)
    ]