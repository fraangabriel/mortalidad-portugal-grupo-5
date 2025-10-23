# llamamos las librerias (el programa no porque ya trabajamos sobre el)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Mortalidad Portugal",
    page_icon="🇵🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# llamamos a los datos
df = pd.read_csv('portugal_tabla_de_mortalidad.csv' , sep = ';')

# el df original no debe tocarse, usamos df= para los ajustes
df0 = df.copy()

# se revisa que esté la data correctamente, dentro de py debe poner print siempre
print(df0.head())
print(df0.tail())
print(df.head())
print(df.tail())

# pido el resumen tecnico
print(df0.info())

# la columna de edad no es numérica, debemos hacer el cambio 
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
        return 'Niñez'
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

#lista con el orden exacto E3
orden_grupos_censales = [
    '0-14 años',
    '15-64 años',
    '65 años y más'
]
# establece el tipo de dato a categórico ordenado
e3_type_ordenado = pd.CategoricalDtype(categories=orden_grupos_censales, ordered=True)

# lista con el orden exacto E4
orden_etapas = [
    'Infancia',
    'Niñez',
    'Pubertad y Adolescencia',
    'Adultos jóvenes',
    'Adultos intermedios',
    'Adultos maduros',
    'Viejos incipientes',
    'Viejos intermedios',
    'Viejos avanzados'
]
# establece el tipo de dato a categórico ordenado
e4_type_ordenado = pd.CategoricalDtype(categories=orden_etapas, ordered=True)
print(orden_grupos_censales)
print(orden_etapas)

# inicio de los filtros y agrupaciones
# -------------------------------------------------
# filtros para mostrar promedios mx tasa de mortalidad
mx_promedio_year = df0.groupby('Year')['mx'].mean()
mx_promedio_E3 = df0.groupby('E3')['mx'].mean()
mx_promedio_E4 = df0.groupby('E4')['mx'].mean()
mx_promedio_T3 = df0.groupby('T3')['mx'].mean()
mx_promedio_T4 = df0.groupby('T4')['mx'].mean()

# filtros para mostrar promedios ex esperanza de vida
ex_promedio_E3 = df0.groupby('E3')['ex'].mean()
ex_promedio_E4 = df0.groupby('E4')['ex'].mean()
ex_promedio_T3 = df0.groupby('T3')['ex'].mean()
ex_promedio_T4 = df0.groupby('T4')['ex'].mean()

# filtro para mortalidad al nacer
df_nacer = df0[df0['Age'] == 0].copy()

# filtro para años específicos
df_1940 = df0[df0['Year'] == 1940].copy()
df_1960 = df0[df0['Year'] == 1960].copy()
df_1980 = df0[df0['Year'] == 1980].copy()
df_2000 = df0[df0['Year'] == 2000].copy()
df_2020 = df0[df0['Year'] == 2020].copy()

# cruces para variables

#crea df9
# Year (año) por E3 (grandes grupos censales),
# calcula promedio de mx en cada subgrupo
mx_promedio_E3_por_Year = df0.groupby(['Year', 'E3'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E3_Year = mx_promedio_E3_por_Year.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E3'
df_mx_E3_Year['E3'] = df_mx_E3_Year['E3'].astype(e3_type_ordenado)
df_mx_E3_Year_ordenado = df_mx_E3_Year.sort_values(by=['Year', 'E3'])
# ver si da (se verifico contra filtros de excel para probar la estructura)
print("Combinación de mx promedio por Año (Year) y Grandes grupos censales (E3):")
print(df_mx_E3_Year_ordenado.head(10))

#crea df11
#T3 (década) por E3 (grandes grupos censales),
# calcula promedio de mx en cada subgrupo
mx_promedio_E3_por_T3 = df0.groupby(['T3', 'E3'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E3_T3 = mx_promedio_E3_por_T3.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E3'
df_mx_E3_T3['E3'] = df_mx_E3_T3['E3'].astype(e3_type_ordenado)
df_mx_E3_T3_ordenado = df_mx_E3_T3.sort_values(by=['T3', 'E3'])
# ver si da 
print("Combinación de mx promedio por Década (T3) y Grupo Censal (E3):")
print(df_mx_E3_T3_ordenado.head(10))


# crea df12
# T4 (etapas economicas) por E3 (grandes grupos censales),
# calcula promedio de mx en cada subgrupo
mx_promedio_E3_por_T4 = df0.groupby(['T4', 'E3'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E3_T4 = mx_promedio_E3_por_T4.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E4'
df_mx_E3_T4['E3'] = df_mx_E3_T4['E3'].astype(e3_type_ordenado)
df_mx_E3_T4_ordenado = df_mx_E3_T4.sort_values(by=['T4', 'E3'])
# ver si da 
print("Combinación de mx promedio por Etapas Económicas (T4) y Grupo Censal (E3):")
print(df_mx_E3_T4_ordenado.head(10))


#crea df13
# Year (año) por E4 (etapas de la vida),
# calcula promedio de mx en cada subgrupo
mx_promedio_E4_por_Year = df0.groupby(['Year', 'E4'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E4_Year = mx_promedio_E4_por_Year.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E4'
df_mx_E4_Year['E4'] = df_mx_E4_Year['E4'].astype(e4_type_ordenado)
df_mx_E4_Year_ordenado = df_mx_E4_Year.sort_values(by=['Year', 'E4'])
# ver si da (se verifico contra filtros de excel para probar la estructura)
print("Combinación de mx promedio por Año (Year) y Etapas de la Vida (E4):")
print(df_mx_E4_Year_ordenado.head(10))

# crea df15
# T3 (década) por E4 (etapas de la vida),
# calcula promedio de mx en cada subgrupo
mx_promedio_E4_por_T3 = df0.groupby(['T3', 'E4'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E4_T3 = mx_promedio_E4_por_T3.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E4'
df_mx_E4_T3['E4'] = df_mx_E4_T3['E4'].astype(e4_type_ordenado)
df_mx_E4_T3_ordenado = df_mx_E4_T3.sort_values(by=['T3', 'E4'])
# ver si da (se verifico contra filtros de excel para probar la estructura)
print("Combinación de mx promedio por Década (T3) y Etapas de la Vida (E4):")
print(df_mx_E4_T3_ordenado.head(10))


# crea df16
# T4 (etapas economicas) por E4 (etapas de la vida),
# calcula promedio de mx en cada subgrupo
mx_promedio_E4_por_T4 = df0.groupby(['T4', 'E4'])['mx'].mean()
# guarda resultado dataframe previo
df_mx_E4_T4 = mx_promedio_E4_por_T4.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E4'
df_mx_E4_T4['E4'] = df_mx_E4_T4['E4'].astype(e4_type_ordenado)
df_mx_E4_T4_ordenado = df_mx_E4_T4.sort_values(by=['T4', 'E4'])
# ver si da (se verifico contra filtros de excel para probar la estructura)
print("Combinación de mx promedio por Etapas Económicas (T4) y Etapas de la Vida (E4):")
print(df_mx_E4_T4_ordenado.head(10))

#crea df13_ex
# Year (año) por E4 (etapas de la vida),
# calcula promedio de ex en cada subgrupo
ex_promedio_E4_por_Year = df0.groupby(['Year', 'E4'])['ex'].mean()
# guarda resultado dataframe previo
df_ex_E4_Year = ex_promedio_E4_por_Year.reset_index()
# se aplica el tipo categórico ordenado a la columna 'E4'
df_ex_E4_Year['E4'] = df_ex_E4_Year['E4'].astype(e4_type_ordenado)
df_ex_E4_Year_ordenado = df_ex_E4_Year.sort_values(by=['Year', 'E4'])
# ver si da (se verifico contra filtros de excel para probar la estructura)
print("Combinación de mx promedio por Año (Year) y Etapas de la Vida (E4):")
print(df_ex_E4_Year_ordenado.head(10))

# inicio de los gráficos
# -------------------------------------------------
# Gráficos de Dispersión

dispersion1 = px.scatter(
  df_mx_E3_Year_ordenado,
    x='Year',
    y='E3',
    color='mx',
    size='mx',
    size_max=30,
    title='Tasa de Mortalidad por Año según Grandes Grupos Censales',
    labels={'mx': 'Tasa de Mortalidad ($m_x$)', 'Year': 'Año', 'E3': 'Grupo Censal'},
    template='plotly_white'
)
#dispersion1.show()

dispersion2 = px.scatter(
  df_mx_E4_Year_ordenado,
    x='Year',
    y='E4',
    color='mx',
    size='mx',
    size_max=30,
    title='Tasa de Mortalidad por Año según las Etapas de la Vida',
    labels={'mx': 'Tasa de Mortalidad ($m_x$)', 'Year': 'Año', 'E4': 'Etapa de Vida'},
    template='plotly_white'
)
#dispersion2.show()

# Aburrido, NO USAR
dispersion3 = px.scatter(
    df_mx_E3_T3_ordenado, 
    x='T3',
    y='E3',
    color='mx',
    size='mx',
    size_max=30,
    title='Tasa de Mortalidad Promedio por Década y Grupo Censal',
    labels={'mx': 'Tasa de Mortalidad Promedio ($m_x$)', 'T3': 'Década', 'E3': 'Grupo Censal'},
    template='plotly_white'
)
dispersion3.update_xaxes(tickangle=45) 
#dispersion3.show()

dispersion4 = px.scatter(
    df_mx_E4_T3_ordenado, 
    x='T3',
    y='E4',
    color='mx',
    size='mx',
    size_max=30,
    title='Tasa de Mortalidad promedio por Década y Etapa de Vida',
    labels={'mx': 'Tasa de Mortalidad Promedio ($m_x$)', 'T3': 'Década', 'E4': 'Etapa de Vida'},
    template='plotly_white'
)
dispersion4.update_xaxes(tickangle=45) 
#dispersion4.show()