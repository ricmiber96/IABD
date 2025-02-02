# 1. Creacion de matriz
# Genera una matriz de 5 filas y 10 columnas cuyos elementos sean números aleatorios
# entre 1 y 100. Asegúrate de que los valores sean reproducibles utilizando una semilla fija.
set.seed(123) # Fijamos los números random para que se repitan en cada ejcucion
matriz <- matrix(sample(1:100, 50, replace = TRUE), nrow = 5, ncol = 10)

# 2. Cálculos estadísticos
# • Calcula los siguientes valores estadísticos para cada columna de la matriz:
# • Media
# • Mediana
# • Varianza
# • Desviación estándar
# Funciones para cada calculo estadisticos
funcionMedia <- function(matriz){ 
    return(colMeans(matriz))
}

funcionMediana <- function(matriz){ 
    return(apply(matriz, 2, median))
}

funcionVarianza <- function(matriz){
    return(apply(matriz,2,var))
}

funcionDesviacion <- function(matriz){
    return(apply(matriz,2, sd))
}

# Aplicamos las funciones
medias <- funcionMedia(matriz)
medianas <- funcionMediana(matriz)
varianzas <- funcionVarianza(matriz)
desviaciones <- funcionDesviacion(matriz)

# 3. Representación gráfica
# Funcion para representar los calculos estadisticos

verGraficas <- function(calculo, texto){
    par(mfrow = c(2, 2))
    barplot(calculo, main = texto,
    xlab = "Columnas", ylab = texto,
    col = rainbow(10))
}

verGraficas(medias, "Media")
verGraficas(medianas, "Mediana")
verGraficas(varianzas, "Varianza")
verGraficas(desviaciones, "Desviación Estándar")


#4. Calcular con una funcion los siguientes datos
# • Qué columna tiene la media más alta
columna_media_maxima <- which.max(medias)
print(paste("La columna con la media más alta es la columna", columna_media_maxima))

# • Qué columna tiene la varianza más baja
columna_varianza_minima <- which.min(varianzas)
print(paste("La columna con la varianza más baja es la columna", columna_varianza_minima))

# • ¿Existe alguna columna en la que la mediana sea significativamente distinta de la
# media?

#Calculamos la diferencia entre las mediana y la media de las columnas y nos quedamos con el valor max y valor min
mediana_dif <- abs(medias - apply(matriz, 2, median))

max_mediana_dif <- which.max(mediana_dif)
valor_max_mediana_dif <- max(mediana_dif)
min_mediana_dif <- which.min(mediana_dif)
valor_min_mediana_dif <- min(mediana_dif)

print(paste("La columna con la diferencia entre la mediana y la media más grande es la columna", max_mediana_dif))
print(paste("El valor de la diferencia entre la mediana y la media más grande es", valor_max_mediana_dif))
print(paste("La columna con la diferencia entre la mediana y la media más pequeña es la columna", min_mediana_dif))
print(paste("El valor de la diferencia entre la mediana y la media más pequeña es", valor_min_mediana_dif))

# • ¿Cómo describirías el comportamiento general de la desviación estándar entre las
# columnas? Las que tienen media y mediana más alta, tienen como resultado una desviación estándar mayor.