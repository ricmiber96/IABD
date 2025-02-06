# 1. Creacion de matriz
# Genera una matriz de 5 filas y 10 columnas cuyos elementos sean números aleatorios
# entre 1 y 100. Asegúrate de que los valores sean reproducibles utilizando una semilla fija.
set.seed(123) # Fijamos los números random para que se repitan
matriz <- matrix(sample(1:100, 50, replace = TRUE), nrow = 5, ncol = 10)
print(matriz)


# 2. Cálculos estadísticos
# • Calcula los siguientes valores estadísticos para cada columna de la matriz:
# • Media
# • Mediana
# • Varianza
# • Desviación estándar
medias <- colMeans(matriz)
medianas <- apply(matriz, 2, median)
varianzas <- apply(matriz, 2, var)
desviaciones <- apply(matriz, 2, sd)

# 3. Representación gráfica
# • Utiliza gráficos de barras para mostrar los valores calculados en el punto anterior.
#  Cada gráfico debe contener:
# • Un título descriptivo.
# • Ejes claramente etiquetados.
# • Barras con colores distintos para cada gráfico.
par(mfrow = c(2, 2))
barplot(medias, main = "Media por columna",
xlab = "Columnas", ylab = "Media",
col = rainbow(10))
barplot(medianas, main = "Mediana por columna",
xlab = "Columnas", ylab = "Mediana",
col = rainbow(10))
barplot(varianzas, main = "Varianza por columna",
xlab = "Columnas", ylab = "Varianza",
col = rainbow(10))
barplot(desviaciones, main = "Desviación Estándar por columna",
xlab = "Columnas", ylab = "Desviación Estándar",
col = rainbow(10))