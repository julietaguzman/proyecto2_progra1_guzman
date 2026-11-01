# TPI 2 - Consulta de Satélites

**Estudiante:** Julieta Guzman
**Materia:** Programación I - UNRN

## Descripcion:
Este programa consiste en una linea de comando que lee un archivo JSON con la informacion de los satelites, calcula la posicion a traves de 'skyfield' y permite consultar los datos con la clase 'Satelite'. Para esto ofrece dos tipos de consultas:
- **Resumen:** Muestra la cantidad de satélites y las estadísticas de altitud (mínimo, máximo y promedio) agrupados por tipo de órbita (LEO, MEO, GEO, HEO).
- **Zona:** Filtra y muestra la descripción de los satélites que se encuentran dentro de un área geográfica delimitada por coordenadas.

## Ejercucion:
Para consultar resumen: 
''' bash
python consultar_satelites.py datos/satelites.json resumen
'''
Para consultar zona:
''' bash
python consultar_satelites.py datos/satelites.json zona longitud minima latitud minima longitud maxima latitud maxima 
'''

## Pruebas unitarias:
El proyecto cuenta con pruebas unitarias para la clase Satelite y el modulo catalogo. Ejercucion:
''' bash
pytest --cov=. --cov-report=html
'''