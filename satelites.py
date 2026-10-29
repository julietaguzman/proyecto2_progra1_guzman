class Satelite:
    def __init__(self, nombre, num_catalogo, latitud, longitud, altitud):
        self.nombre = nombre_vacio(nombre)
        self.num_catalogo = numeros_catalogo(num_catalogo)
        self.latitud = parametros_latitud(latitud)
        self.longitud = parametros_longitud(longitud)
        self.altitud = parametros_altitud(altitud)

def nombre_vacio(nombre):
    nombre_limpio = nombre.strip()
    if type(nombre) is not str or not nombre_limpio:
        raise ValueError ("El nombre esta vacio")
    return nombre_limpio

def numeros_catalogo(num_catalogo):
    if type(num_catalogo) is not int:
        raise ValueError (f"El numero del catalogo no es entero {num_catalogo}")
    return num_catalogo

def parametros_latitud(latitud):
    if (type(latitud) is not int and type(latitud) is not float) or not  (-90 <= latitud <= 90):
        raise ValueError (f"La latitud debe estar entre -90 y 90: {latitud}")
    return float(latitud)

def parametros_longitud(longitud):
    if (type(longitud) is not int and type(longitud) is not float) or not (-180 <= longitud <= 180):
        raise ValueError (f"La longitud debe estar entre -180 y 180: {longitud}")
    return float(longitud)
 
def parametros_altitud(altitud):
    if (type(altitud) is not int and type(altitud) is not float) or not altitud > 100:
        raise ValueError (f"La altitud debe ser de al menos 100 km: {altitud}")
    return float(altitud)

def tipo_orbita(self):
    if self.altitud < 2000: 
        return "LEO"
    elif 2000 <= self.altitud < 34000: 
        return "MEO"
    elif 34000 <= self.altitud <= 37000: 
        return "GEO"
    elif self.altitud > 37000: 
        return "HEO"

def ficha(self):
    return (f"{self.nombre} | {self.num_catalogo} | {self.tipo_orbita} | {self.altitud} km")

def esta_en_zona(self, long_min, lat_min, long_max, lat_max):
    return (long_min <= self.longitud <= long_max and lat_min <= self.latitud <= lat_max)
