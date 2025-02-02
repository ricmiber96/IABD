
# ventas 50000:150000
# gastos_material 5000:20000,
# gastos_personal 20000:50000
# gastos_publicidad 3000:10000
# gastos_eléctricos 2000:7000
set.seed(123)

# Definir la función para generar la lista rangos_filas
generar_rangos_filas <- function() {
  rangos_filas <- list(
    ventas = matrix(sample(50000:150000, 12, replace = TRUE),nrow = 1, ncol = 12),
    gastos_material = matrix(sample(5000:20000, 12, replace = TRUE),nrow = 1, ncol = 12),
    gastos_personal = matrix(sample(20000:50000, 12, replace = TRUE),nrow = 1, ncol = 12),
    gastos_publicidad = matrix(sample(3000:10000, 12, replace = TRUE),nrow = 1, ncol = 12),
    gastos_electricos = matrix(sample(2000:7000, 12, replace = TRUE),nrow = 1, ncol = 12)
  )
}

meses_array <- c("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

# Llamar a la función para obtener la lista
rangos_filas <- generar_rangos_filas()

# Combinar los vectores de la lista en un solo vector
datos_matriz_tienda1 <- unlist(rangos_filas)
matriz_tienda1 <- matrix(datos_matriz_tienda1, nrow=5, ncol= 12)
rownames(matriz_tienda1) <- names(rangos_filas)
colnames(matriz_tienda1) <- c(meses_array)


rangos_filas_2 <- generar_rangos_filas()
datos_matriz_tienda2 <- unlist(rangos_filas_2)
matriz_tienda2 <- matrix(datos_matriz_tienda2, nrow=5, ncol= 12)

rownames(matriz_tienda2) <- names(rangos_filas_2)
colnames(matriz_tienda2) <- c(meses_array)

#Calculos globales
print("Calculos globales")
total_ventas <- sum(matriz_tienda1["ventas", ] + matriz_tienda2["ventas", ])
print(paste("Total ventas:",total_ventas))

total_gastos_material <- sum(matriz_tienda1["gastos_material", ] + matriz_tienda2["gastos_material", ])
print(paste("Total gastos material:", total_gastos_material))

total_gastos_personal <- sum(matriz_tienda1["gastos_personal", ] + matriz_tienda2["gastos_personal", ])
print(paste("Total gastos personal:", total_gastos_personal))

total_gastos_publicidad <- sum(matriz_tienda1["gastos_publicidad", ] + matriz_tienda2["gastos_publicidad", ])
print(paste("Total Gastos Publicidad: ",total_gastos_publicidad))

total_gastos_electricos <- sum(matriz_tienda1["gastos_electricos", ] + matriz_tienda2["gastos_electricos", ])
print(paste("Total Gastos Electricos: ", total_gastos_electricos))

total_gastos = total_gastos_material + total_gastos_personal + total_gastos_publicidad + total_gastos_electricos
print(paste("Total gastos", total_gastos))

beneficio_global = total_ventas - total_gastos
print(paste("Beneficio global ", beneficio_global))

#Calculos por tienda
print("Calculos por tienda")

generar_ventas_tienda <- function(matriz) { 
  
  ventas <- sum(matriz["ventas",])
  
  print(ventas)
  return(ventas)
}

# beneficio_tienda1 = sum(matriz_tienda1["ventas", ] - matriz_tienda1["gastos", ])

# beneficio_tienda2 = sum(matriz_tienda2["ventas", ] - matriz_tienda2["gastos", ])

beneficio_tienda1 <- generar_ventas_tienda(matriz_tienda1)
beneficio_tienda2 <- generar_ventas_tienda(matriz_tienda2)

print(paste("Beneficio tienda 1:", beneficio_tienda1))

print(paste("Beneficio tienda 2:", beneficio_tienda2))

#Calculos por mes
print("Calculos por mes")




