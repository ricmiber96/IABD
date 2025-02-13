# 🔹 Módulo 1: Fundamentos de Scala
### 1. Variables
- Declaración (`val` vs `var`)
- Tipos de datos en Scala
- Mutabilidad vs inmutabilidad

### 2. Expresiones
- Expresión vs instrucción
- Bloques de código como expresiones
- Operadores y evaluaciones

### 3. Funciones
- Declaración de funciones (`def`)
- Funciones inline (de una sola línea)
- Funciones anónimas (lambdas)
- Funciones de orden superior

### 4. Inferencias
- Inferencia de tipos en variables
- Inferencia de tipos en funciones
- Casos donde Scala no puede inferir el tipo


# 📌 1. Variables en Scala

## 🎯 Objetivos de la Clase
En esta clase aprenderás:
- Cómo declarar variables en Scala usando `val` y `var`.
- Los tipos de datos básicos en Scala.
- La diferencia entre **mutabilidad** e **inmutabilidad**.

---

## 🔹 1.1 Declaración de Variables (`val` vs `var`)

En Scala, existen dos formas principales de declarar variables:  
- **`val`** → Variable inmutable (su valor no puede cambiar).  
- **`var`** → Variable mutable (su valor puede cambiar).  

### **Ejemplo:**
```scala
object VariablesDemo {
  def main(args: Array[String]): Unit = {
    val nombre: String = "Scala" // Inmutable
    var edad: Int = 25 // Mutable

    println(s"Nombre: $nombre, Edad: $edad")

    edad = 26 // ✅ Se puede cambiar porque es var
    // nombre = "Java" ❌ Error: no se puede cambiar un val

    println(s"Edad actualizada: $edad")
  }
}



# 📌 2. Expresiones en Scala

## 🎯 Objetivos de la Clase
En esta clase aprenderás:
- La diferencia entre **expresión** e **instrucción**.
- Cómo los bloques de código pueden ser expresiones.
- El uso de operadores y evaluaciones en Scala.

---

## 🔹 2.1 Expresión vs Instrucción

En Scala, **casi todo es una expresión**, lo que significa que **devuelve un valor**.  
A diferencia de otros lenguajes, donde hay instrucciones que no devuelven nada, en Scala incluso un `if` devuelve un valor.

### **Ejemplo de Expresiones**
```scala
val resultado = 5 + 3  // 5 + 3 es una expresión que devuelve 8
val mayor = if (10 > 5) "Sí" else "No" // if devuelve un valor
```

### **Ejemplo de Instrucción (No devuelve valor)**

```scala
var x = 10
x = x + 5 // Modifica `x`, pero no devuelve un resultado como una expresión.
```


## 🔹 2.2 Bloques de Código como Expresiones
En Scala, un bloque de código es una expresión, y el valor de la última línea del bloque es su resultado.
#### Ejemplo de Bloque de Código
```scala
val resultado = {
  val a = 10
  val b = 20
  a + b  // Esta es la última expresión, por lo que `resultado` será 30
}
println(resultado) // 30

```

## 🔹 2.3 Operadores y Evaluaciones
Scala soporta operadores matemáticos, de comparación y lógicos, los cuales son expresiones porque devuelven valores.

### **Operadores Matemáticos**

| Operador | Descripción    | Ejemplo (a = 10, b = 3) |
|----------|----------------|-------------------------|
| `+`      | Suma           | `a + b` → `13`          |
| `-`      | Resta          | `a - b` → `7`           |
| `*`      | Multiplicación | `a * b` → `30`          |
| `/`      | División       | `a / b` → `3`           |
| `%`      | Módulo         | `a % b` → `1`           |

---

### **Operadores de Comparación**

| Operador | Descripción     | Ejemplo (x = 5, y = 10) |
|----------|-----------------|-------------------------|
| `==`     | Igual a         | `x == y` → `false`      |
| `!=`     | Diferente de     | `x != y` → `true`       |
| `>`      | Mayor que       | `x > y` → `false`       |
| `<`      | Menor que       | `x < y` → `true`        |
| `>=`     | Mayor o igual   | `x >= y` → `false`      |
| `<=`     | Menor o igual   | `x <= y` → `true`       |

---

### **Operadores Lógicos**

| Operador | Descripción     | Ejemplo (a = true, b = false) |
|----------|-----------------|-------------------------------|
| `&&`     | AND (y lógico)  | `a && b` → `false`            |
| `||`     | OR (o lógico)   | `a || b` → `true`             |
| `!`      | NOT (negación)  | `!a` → `false`                |


🚀 Ejercicios para Practicar
1️⃣ Escribe una expresión que evalúe si un número es par o impar usando if.
2️⃣ Crea un bloque de código que defina dos variables y devuelva su suma.
3️⃣ Usa operadores lógicos para verificar si un número está entre 5 y 10.
4️⃣ Prueba operadores matemáticos con diferentes valores e imprime los resultados.