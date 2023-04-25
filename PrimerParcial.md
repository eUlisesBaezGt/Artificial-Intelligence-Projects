# Artificial-Intelligence-Projects

Este proyecto corresponde a la entrega del primer parcial; que abarca los algoritmos de búsqueda no informados: a lo ancho, costo uniforme, a lo profundo, profundidad limitada, profundidad iterativa, y bidireccional.





General

El salón se dividirá en grupos de 3 a 5 integrantes. Cada equipo entregará los archivos de ejecución de su programa (se recomienda hacer un sólo archivo de código) junto con la documentación de dicho programa. El código debe ser ejecutable y la documentación debe ser en formato PDF. El o los archivos de código y el archivo de documentación deben ser comprimidos en formato ZIP para su carga al sistema.

Grafo

Los alumnos usarán el grafo unidireccional contenido en el archivo "1erParcialGrafoUnidireccional.kmz". Para abrir el archivo kmz, se recomienda usar la página web de Google Earth: https://earth.google.com/web/@24.14771269,-101.93346641,1777.0598936a,3194509.63612531d,30.0011098y,0h,0t,0r

Una vez ahí, cargar el archivo en la página en la barra lateral/proyectos/nuevo proyecto/importar archivo kml del ordenador. Se recomienda quitar toda leyenda en barra latera/estilo del mapa/simplificado.

Las ciudades a utilizar están localizadas con un marcador; mientras que sus conexiones y sus pesos se encuentran en la linea recta (ruta) entre las ciudades. Al hacer click sobre cualquier línea de conexión/ruta, se despliega un cuadro de diálogo con el peso correspondiente.

Los alumnos transformarán el grafo unidireccional en un grafo dirigido iniciando con la ciudad de Cancun con dirección hacia la izquierda del mapa. Este proceso es similar al realizado en los ejercicios durante la clase.

Una vez obtenido el grafo dirigido; los estudiantes usarán este grafo junto con sus pesos como un grafo de entrada para el código. Los estudiantes harán otra versión del mismo grafo dirigido, pero con todos los pesos de las acciones/vértices con el mismo valor; este será otra entrada para el código.

Código

Los alumnos de cada grupo deben de programar, en el lenguaje de programación de su preferencia, los algoritmos de búsqueda no informados vistos en este parcial - ver descripción del proyecto. Las implementaciones de los algoritmos deben ser propias; esto es, sin utilizar librerías para realizar la búsqueda. Las librerías permitidas son para la de generación del grafo/árbol y para obtener el tiempo de ejecución. El código debe ser 1 por equipo y abarcar o siguiente:

Entrada:

Se debe de pedir al usuario los siguiente: nodo de inicio, nodo final, y límite de profundidad.
El código debe aceptar y procesar el grafo de búsqueda anexado con pesos diferentes en cada acción y otra versión del mismo grafo con pesos iguales en cada acción.
Proceso interno

El código debe estandarizar los nombres de los nodos para ser procesados independientemente si se escriben en mayúsculas o minúsculas o una combinación de ambos.
El código debe verificar que el nodo de inicio y objetivo sean válidos.
El código primeramente ejecuta la búsqueda por anchura y determina si los pesos en todas las acciones del árbol de búsqueda son iguales o no. Si los pesos son iguales, entonces imprime en pantalla como resultado el camino del nodo inicio al nodo final junto con el tiempo de ejecución del algoritmo (pared o procesador) y finaliza la ejecución.
Si los pesos de las acciones en el árbol de búsqueda son diferentes, entonces ejecuta los siguientes algoritmos de búsqueda, en cualquier orden: Costo uniforme, profundidad, profundidad limitada, profundidad iterativa y bidireccional (con un algoritmo de búsqueda no informado de elección del equipo).
Una vez finalizada la ejecución de todos los algoritmos; los tiempos de ejecución de cada búsqueda deben ser comparados e identificar aquella búsqueda con el menor tiempo
Salida

El código debe mostrar en pantalla el grafo procesado/árbol de búsqueda.
El resultado de la búsqueda; en forma de camino o de mensaje de error.
El costo del camino recorrido; de ser pertinente.
El nivel de profundidad en la que se encontró la respuesta/camino o en la que se detuvo la búsqueda; de ser pertinente.
El tiempo total de ejecución de cada algoritmo de búsqueda.
La búsqueda con el menor tiempo de ejecución.
Documentación

El archivo de documentación debe ser en formato PDF y debe de contener lo siguiente:

Imagen del grafo dirigido con los pesos respectivos para cada actividad/vértice. Este se obtiene del grafo unidireccional incluido en el archivo "1erParcialGrafoUnidireccional.kmz".
Instrucciones para ejecutar el código y leer el resultado obtenido.
Descripción de las funciones o clases u objetos utilizados para implementar cada uno de los algoritmos de búsqueda incluidos en el programa. La descripción debe presentar el objetivo de la función/clase/objeto, los procesos/variables internas relevantes y su funcionamiento, y el resultado de la función/clase/objeto.
El orden de ejecución de las funciones o clases u objetos más relevantes del código; esto es, de las búsquedas.
Ejemplos de las entradas de cada función/clase/objetos (puede incluir figuras) y su correspondiente salida (puede incluir figuras).
Restricciones del código. Esto es, errores comprobados, limitaciones detectadas y posibles mejoras.
El documento debe estar debidamente seccionado:
Portada con nombres de los participantes, clase, fecha de entrega
Tabla de contenido
Tabla de figuras
