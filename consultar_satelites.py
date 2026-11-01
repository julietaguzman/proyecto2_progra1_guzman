import sys 

from catalogo import(
    leer_archivo,
    crear_catalogo,
    resumen_por_orbita,
    satelites_en_zona
)

def mostrar_resumen(satelites):
    resumen = resumen_por_orbita(satelites)
    
    for tipo in resumen:
        datos = resumen[tipo]
        print(f"{tipo}: {datos['cantidad']} satelites | "
              f"Altitud minima: {datos['min']} km | "
              f"Altitud maxima: {datos['max']} km | "
              f"Altitud promedio: {datos['promedio']} km | "
        )
        
def mostrar_zona(satelites, lon_min, lat_min, lon_max, lat_max):
   zona = satelites_en_zona(satelites, lon_min, lat_min, lon_max, lat_max)
   cantidad = len(zona)
   print(f"Satelites en la zona: {cantidad}")

   for satelite in zona:
       print(satelite.ficha())
       
def main():
    if len(sys.argv) < 3:
        print("Uso: python consultar_satelites.py <satelites.json> resumen|zona")
        sys.exit(1)

    ruta = sys.argv[1]
    consulta = sys.argv[2]

    registros = leer_archivo(ruta)
    satelites = crear_catalogo(registros)

    if consulta == "resumen":
        mostrar_resumen(satelites)    
    elif consulta == "zona":
        if len(sys.argv) < 7:
            print("Uso: python consultar_satelites.py <archivo.json> zona <lon_min> <lat_min> <lon_max> <lat_max>")
            sys.exit(1)
        
        lon_min = float(sys.argv[3])
        lat_min = float(sys.argv[4])
        lon_max = float(sys.argv[5])
        lat_max = float(sys.argv[6])
        
        mostrar_zona(satelites, lon_min, lat_min, lon_max, lat_max) 
    
    else:
        print(f"Argumento invalido: {consulta}")
        sys.exit(1)

main()