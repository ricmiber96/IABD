error id: 
file://<WORKSPACE>/src/main/scala/module1_fundamentals/Variables.scala
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
|empty definition using fallback
non-local guesses:
	 -siempre.
	 -siempre#
	 -siempre().
	 -scala/Predef.siempre.
	 -scala/Predef.siempre#
	 -scala/Predef.siempre().

Document text:

```scala
package module1_fundamentals

object Variables extends App {

    val nombre: String = "Scala" // Inmutable
    var edad: Int = 25 // Mutable

    println(s"Nombre: $nombre, Edad: $edad")

    edad = 26 // ✅ Se puede cambiar porque es var
    // nombre = "Java" ❌ Error: no se puede cambiar un val

    println(s"Edad actualizada: $edad")

}
```

#### Short summary: 

empty definition using pc, found symbol in pc: 