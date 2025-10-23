Sys.setlocale("LC_ALL", "en_US.UTF-8")
# -------------------- 
# Librerías necesarias ✅
# --------------------
library(tidyverse)
library(plotly)
library(ggplot2)

# --------------------
# Limpiando el dataset ✅
# --------------------
df <- read_delim("portugal_tabla_de_mortalidad.csv",
                 delim = ";")

df0 <- df %>%
  mutate(
    Age = gsub("\\+", "", Age),
    Age = as.integer(Age)
  )


# ---------
# Funciones ✅
# ---------

# T3: Decada
decada <- function(year) {
  if (year >= 1940 && year <= 1949) {
    return('1940–1949')
  } else if (year >= 1950 && year <= 1959) {
    return('1950–1959')
  } else if (year >= 1960 && year <= 1969) {
    return('1960–1969')
  } else if (year >= 1970 && year <= 1979) {
    return('1970–1979')
  } else if (year >= 1980 && year <= 1989) {
    return('1980–1989')
  } else if (year >= 1990 && year <= 1999) {
    return('1990–1999')
  } else if (year >= 2000 && year <= 2009) {
    return('2000–2009')
  } else if (year >= 2010 && year <= 2019) {
    return('2010–2019')
  } else if (year >= 2020 && year <= 2023) {
    return('2020–2023')
  } else {
    return('Otra decada')
  }
}

# T4: Epoca económica
epoca_economica <- function(year) {
  if (year >= 1940 && year <= 1946) {
    return('1940–1946: reconstrucción posguerra')
  } else if (year >= 1947 && year <= 1972) {
    return('1947–1972: expansión económica y transición demográfica')
  } else if (year >= 1973 && year <= 1990) {
    return('1973–1990: crisis del petróleo y ajuste estructural')
  } else if (year >= 1991 && year <= 1998) {
    return('1991–1998: apertura europea y modernización')
  } else if (year >= 1999 && year <= 2007) {
    return('1999–2007: integración al euro y estabilidad')
  } else if (year >= 2008 && year <= 2014) {
    return('2008–2014: crisis financiera global')
  } else if (year >= 2015 && year <= 2019) {
    return('2015–2019: recuperación económica')
  } else if (year >= 2020 && year <= 2023) {
    return('2020–2023: pandemia y reconfiguración demográfica')
  } else {
    return('Otro')
  }
}

# E3: gCenso
gCenso <- function(edad) {
  if (edad >= 0 && edad <= 14) {
    return('0-14 años')
  } else if (edad >= 15 && edad <= 64) {
    return('15-64 años')
  } else if (edad >= 65) {
    return('65 años y más')
  } else {
    return('Ninguna otra etapa')
  }
}

# E4: etapa
etapa <- function(edad) {
  if (edad >= 0 && edad <= 5) {
    return('Infancia')
  } else if (edad >= 6 && edad <= 11) {
    return('Niñez')
  } else if (edad >= 12 && edad <= 19) {
    return('Pubertad y Adolescencia')
  } else if (edad >= 20 && edad <= 39) {
    return('Adultos jóvenes')
  } else if (edad >= 40 && edad <= 49) {
    return('Adultos intermedios')
  } else if (edad >= 50 && edad <= 59) {
    return('Adultos maduros')
  } else if (edad >= 60 && edad <= 69) {
    return('Viejos incipientes')
  } else if (edad >= 70 && edad <= 84) {
    return('Viejos intermedios')
  } else if (edad >= 85) {
    return('Viejos avanzados')
  } else {
    return('Ninguna otra etapa')
  }
}

# Aplicar las funciones a las columnas usando sapply()
df0$T3 <- sapply(df0$Year, decada)
df0$T4 <- sapply(df0$Year, epoca_economica)

df0$E3 <- sapply(df0$Age, gCenso)
df0$E4 <- sapply(df0$Age, etapa)

sum(is.na(df0$E4))

# ----------------
# Orden categórico ✅
# ----------------

# lista con el orden exacto E3
orden_grupos_censales <- c(
  '0-14 años',
  '15-64 años',
  '65 años y más'
)

# lista con el orden exacto E4
orden_etapas <- c(
  'Infancia',
  'Niñez',
  'Pubertad y Adolescencia',
  'Adultos jóvenes',
  'Adultos intermedios',
  'Adultos maduros',
  'Viejos incipientes',
  'Viejos intermedios',
  'Viejos avanzados'
)


# Aplicar los factores ordenados a df0
df0 <- df0 %>%
  mutate(
    E3 = factor(E3, levels = orden_grupos_censales, ordered = TRUE),
    E4 = factor(E4, levels = orden_etapas, ordered = TRUE)
  )

cat("\n--- Orden de Grupos Censales ---\n")
print(orden_grupos_censales)
cat("\n--- Orden de Etapas ---\n")
print(orden_etapas)
cat("\n--- Estructura de E3 y E4 (factores ordenados) ---\n")

print(str(df0 %>%
            select(E3, E4)))
