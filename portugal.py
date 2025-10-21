# llamamos las librerias (el programa no porque ya trabajamos sobre el)
import pandas as pd
import numpy as np
import plotly.express as px

# llamamos a los datos
df = pd.read_csv('portugal_tabla_de_mortalidad.csv' , sep = ';')

# el df original no debe tocarse, usamos df= para los ajustes
df0 = df

# se revisa que esté la data correctamente, dentro de py debe poner print siempre
print(df0.head())
print(df0.tail())

# pido el resumen tecnico
print(df0.info())

# la columna de edad no es numérica, debemos hacer el cambio en 3 etapas
df0['Age'] = pd.to_numeric(df0['Age'].str.replace('+', ''))

# pido el resumen tecnico para verificar el cambio en Age
print(df0.info())

# crea las funciones para T3, T4, E3 y E4
# T3
def decada(year):
    if 1940 <= year <= 1949:
        return '1940–1949'
    elif 1950 <= year <= 1959:
        return '1950–1959'
    elif 1960 <= year <= 1969:
        return '1960–1969'
    elif 1970 <= year <= 1979:
        return '1970–1979'
    elif 1980 <= year <= 1989:
        return '1980–1989'
    elif 1990 <= year <= 1999:
        return '1990–1999'
    elif 2000 <= year <= 2009:
        return '2000–2009'
    elif 2010 <= year <= 2019:
        return '2010–2019'
    elif 2020 <= year <= 2023:
        return '2020–2023'
    else:
        return 'Otra decada' # Para años fuera de los rangos definidos
    
    
# T4
def epoca_economica(year):
    if 1940 <= year <= 1946:
        return '1940–1946: reconstrucción posguerra'
    elif 1947 <= year <= 1972:
        return '1947–1972: expansión económica y transición demográfica'
    elif 1973 <= year <= 1990:
        return '1973–1990: crisis del petróleo y ajuste estructural'
    elif 1991 <= year <= 1998:
        return '1991–1998: apertura europea y modernización'
    elif 1999 <= year <= 2007:
        return '1999–2007: integración al euro y estabilidad'
    elif 2008 <= year <= 2014:
        return '2008–2014: crisis financiera global'
    elif 2015 <= year <= 2019:
        return '2015–2019: recuperación económica'
    elif 2020 <= year <= 2023:
        return '2020–2023: pandemia y reconfiguración demográfica'
    else:
        return 'Otro' # Para años fuera de los rangos definidos
