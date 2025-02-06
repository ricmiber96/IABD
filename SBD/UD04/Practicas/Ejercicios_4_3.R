# Ejercicio 4.1. Crear una función para calcular la media de un vector numérico y usarla
# para calcular la media del vector (1, 2, NA, 3, 4).

vector_numerico = c(1, 2, NA, 3, 4)

# Definimos la función
mean_function <- function(x) {
    # Calculamos la media del vector utilizando la función mean()
   count <- 0
   for (i in x) {
     if (!is.na(i)) {
        count <- count + i
     }
    }
    # Retornamos la media
    return (count / length(x))
  }


# Calculamos la media del vector
media_vector = mean_function(vector_numerico)
media_vector

# Ejercicio 4.2. Usar la función anterior para crear una función para calcular las medias
# de las columnas de un data frame numérico. La función debe devolver un vector con las
# medias de las columnas. Usarla para calcular el data frame formado por los vectores (1,
# 2, NA, 3, 4) y (-1, 0, -2, 0, NA).
df_mean_function = function(df) {
  for (i in df) {
    # Si la columna es numérica, calculamos la media y la añadimos al vector de medias
   print(paste(i))
   medias <- c(mean_function(i))
  }
  return (medias)
}

# Creamos el data frame

df = data.frame(column1 = c(1, 2, NA, 3, 4), column2 = c(-1, 0, -2, 0, NA))

# Calculamos las medias de las columnas
df_mean_function(df)