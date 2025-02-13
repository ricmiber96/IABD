package module1_fundamentals

object Variables extends App {

    //  1.1 Declaración de Variables (val vs var)
    val nombre: String = "Scala" // Inmutable
    var edad: Int = 25 // Mutable

    println(s"Nombre: $nombre, Edad: $edad")

    edad = 26 // ✅ Se puede cambiar porque es var
    // nombre = "Java" ❌ Error: no se puede cambiar un val

    println(s"Edad actualizada: $edad")

    //  1.2 Tipos de Datos en Scala
    val mensaje: String = "Hola, Scala"
    val numero: Int = 42
    val decimal: Double = 3.14
    val esScalaGenial: Boolean = true
    val letra: Char = 'S'

    println(s"Mensaje: $mensaje, Número: $numero, Decimal: $decimal, ¿Scala es genial? $esScalaGenial, Letra: $letra")
  
    // Inferencia de Tipos
    val mensaje2 = "Hola, Scala"  // Scala infiere que es un String
    val numero2 = 42              // Scala infiere que es un Int

    //  1.3 Mutabilidad vs Inmutabilidad
    var contador: Int = 0
    contador = contador + 1 // Se modifica el valor
    println(contador) // 1

    val contador2: Int = 0
    // contador = contador + 1  ❌ Error: No se puede modificar un val

    // ➡️ Regla de oro: Usa val siempre que puedas, y var solo si realmente necesitas cambiar el valor.

    // 🚀 Ejercicios para Practicar
    // 1️⃣ Declara una variable val que almacene tu nombre.
    // 2️⃣ Declara una variable var que almacene tu edad y actualízala.
    // 3️⃣ Prueba a cambiar el valor de un val y observa el error que da Scala.
    // 4️⃣ Crea una variable de cada tipo (String, Int, Double, Boolean, Char) e imprime sus valores.

    

}