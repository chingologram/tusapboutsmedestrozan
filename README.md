## Tus apbouts me destrozan

Un poema digital interactivo basado en Reddit.

El código permite escribir posts que se modifiquen a sí mismos. Sos libre de copiarlo para hacer juegos, obras de literatura digital, o lo que te parezca.


### Transformación del poema

El poema usa una CFG para interpretar el "árbol sintáctico" del poema, que puede tener varios tipos de caracter: caracteres, caracteres tachados, símbolos unicode... 
Una CFG parecía la mejor solución porque hay caracteres como las tachaduras que ocupan varios espacios.


Luego, el programa va reemplazando las hojas del árbol según las interacciones con el mismo post.
Los caracteres son "destruídos" en forma aleatoria, pero siguiendo siempre la misma semilla para que los caracteres tachados sean los mismos entre cada ejecución.


---

https://instagram.com/chingologram
https://twitter.com/chingologram
