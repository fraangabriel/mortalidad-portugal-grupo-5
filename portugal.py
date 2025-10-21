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

# E3
def gCenso(edad):
    if 0 <= edad <= 14:
        return '0-14 años'
    elif  15 <= edad <= 64:
        return '15-64 años'
    elif 65 <= edad:
        return '65 años y más'
    else:
        return 'Ninguna otra etapa' # Para años fuera de los rangos definidos

# E4
def etapa(edad):
    if 0 <= edad <= 5:
        return 'Infancia'
    elif  6 <= edad <= 11:
        return 'Ninez'
    elif 12 <= edad <= 19:
        return 'Pubertad y Adolescencia'
    elif 20 <= edad <= 39:
        return 'Adultos jóvenes'
    elif 40 <= edad <= 49:
        return 'Adultos intermedios'
    elif 50 <= edad <= 59:
        return 'Adultos maduros'
    elif 60 <= edad <= 69:
        return 'Viejos incipientes'
    elif 70 <= edad <= 84:
        return 'Viejos intermedios'
    elif 85 <= edad:
        return 'Viejos avanzados'
    else:
        return 'Ninguna otra etapa' # Para años fuera de los rangos definidos


# función para crear las columnas nuevas
df0['T3'] = df0['Year'].apply(decada)
df0['T4'] = df0['Year'].apply(epoca_economica)

df0['E3'] = df0['Age'].apply(gCenso)
df0['E4'] = df0['Age'].apply(etapa)

# ver si muestra nuevas columnas
print(df0.head())
print(df0.tail())

# filtro según E3 para mostrar el promedio mx
# -------------------------------------------------
mx_grouped_by_E3 = df0.groupby('E3')['mx'].mean()
mx_grouped_by_T4 = df0.groupby('T4')['mx'].mean()

# ver el resultado
print("")
print("Valor de 'mx' según 'E3':")
print(mx_grouped_by_E3)

print("")
print("Valor de 'mx' según 'T4':")
print(mx_grouped_by_T4)

print(mx_grouped_by_T4.info())