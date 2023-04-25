Descripción

Este proyecto corresponde a la entrega del primer parcial; que abarca los algoritmos de búsqueda informados: greedy best-first, a*, weighted a*, beam, hill climbing, simulated annealing, genetic algorithms, ...



General

El salón se dividirá en grupos de 2 a 3 integrantes. Cada equipo entregará los archivos de ejecución de su programa (se recomienda hacer un sólo archivo de código). El o los archivos de código deben ser comprimidos en formato ZIP para su carga al sistema.

Grafo

Los alumnos usarán el grafo unidireccional contenido en el archivo “1erParcialGrafoUnidireccional.kmz". Para abrir el archivo kmz, se recomienda usar la página web de Google Earth: https://earth.google.com/web/@24.14771269,-101.93346641,1777.0598936a,3194509.63612531d,30.0011098y,0h,0t,0r

Una vez ahí, cargar el archivo en la página en la barra lateral/proyectos/nuevo proyecto/importar archivo kml del ordenador. Se recomienda quitar toda leyenda en barra latera/estilo del mapa/simplificado.

Las ciudades a utilizar están localizadas con un marcador; mientras que sus conexiones y sus pesos se encuentran en la linea recta (ruta) entre las ciudades. Al hacer click sobre cualquier línea de conexión/ruta, se despliega un cuadro de diálogo con el peso correspondiente.

Los alumnos transformarán el grafo unidireccional en un grafo dirigido iniciando con la ciudad de Cancun con dirección hacia la izquierda del mapa. Este proceso es similar al realizado en los ejercicios durante la clase.

Una vez obtenido el grafo dirigido; los estudiantes usarán este grafo junto con sus pesos como un grafo de entrada para el código. Los estudiantes harán otra versión del mismo grafo dirigido, pero con todos los pesos de las acciones/vértices con el mismo valor; este será otra entrada para el código.

Heurística

Los alumnos usarán como referencia el código del archivo “get_euclidean_distance.py”. Este código calcula la heurística de distancia de línea recta entre las ciudades y la ciudad objetivo para el grafo proporcionado previamente. 

Los alumnos reemplazarán la distancia Euclidiana por la distancia de Haversine. La implementación de la distancia debe ser sin usar librerías.

Código

Los alumnos de cada grupo deben de programar, en el lenguaje de programación de su preferencia, los algoritmos de búsqueda informados vistos en este parcial - ver descripción del proyecto. Las implementaciones de los algoritmos deben ser propias; esto es, sin utilizar librerías para realizar la búsqueda. Las librerías permitidas son para la de generación del grafo/árbol y para obtener el tiempo de ejecución. El código debe ser 1 por equipo y abarcar o siguiente:

Entrada:

Se debe de pedir al usuario los siguiente, cuando corresponda: algoritmo a ejecutar, nodo de inicio, nodo final, heurística, el valor de k, r, t0, i, ... 
Se debe pedir al usuario si desea ejecutar el código con o sin información paso a paso
El código debe aceptar y procesar el grafo de búsqueda anexado con pesos diferentes en cada acción y otra versión del mismo grafo con pesos iguales en cada acción.
Proceso interno

El código debe estandarizar los nombres de los nodos para ser procesados independientemente si se escriben en mayúsculas o minúsculas o una combinación de ambos.
El código debe verificar que el nodo de inicio y objetivo sean válidos.
El código debe contener un menú que solicite al usuario qué algoritmo desea ejecutar
El código debe mostrar en pantalla paso a paso la ejecución del algoritmo de búsqueda seleccionado, únicamente cuando el usuario solicita información paso a paso.
Dado el algoritmo seleccionado por el usuario, el código debe solicitar los parámetros correspondientes para su ejecución
Al finalizar la ejecución del algoritmo seleccionado, este debe regresar el resultado de la búsqueda (camino encontrado); así como el tiempo de ejecución del algoritmo expresado en segundos.
Salida

El código debe mostrar en pantalla el grafo procesado/árbol de búsqueda.
El resultado de la búsqueda; en forma de camino o de mensaje de error.
El costo del camino recorrido; de ser pertinente.
El número de iteración en que se encontró la respuesta o se finalizó la ejecución del algoritmo; de ser pertinente.
El tiempo total de ejecución del algoritmo de búsqueda ejecutado.
Documentación

Cada archivo de código debe estar propia y debidamente comentado para suplir la falta de un documento del proyecto. Un ejemplo de la documentación se puede ver en el archivo “get_euclidean_distance.py”. Los aspectos a cubrir son los siguientes:

Información general (Al inicio de cada archivo):
Nombre del proyecto
Nombre de la universidad
Nombre de la materia
Nombre de los integrantes del equipo
Fecha de entrega o generación del archivo
Versión del código
Breve descripción del propósito del código contenido en dicho archivo
Instrucciones para ejecutar el código y leer el resultado obtenido
Estar debidamente seccionado como sigue:
Dependencias - librerías, uso de archivos externos, etc
Variables globales
Funciones o Clases de apoyo - todas aquellas funciones o clases que ayudan a que el proceso principal del código funcione de manera correcta
Funciones o Clases principales - todas aquellas funciones o clases que ejecutan parte del proceso fundamental del código
Descripción de las funciones o clases u objetos utilizados para implementar cada uno de los algoritmos de búsqueda incluidos en el programa. La descripción debe presentar el objetivo de la función/clase/objeto, los procesos/variables internas relevantes y su funcionamiento, y el resultado de la función/clase/objeto.
Al inicio de cada función o clase, se debe incluir una descripción de sus parámetros de entrada (qué recibe como input) y su respuesta de ejecución (qué devuelve como resultado y/o qué genera tras su ejecución).
Cada función/clase debe contener el responsable de su implementación 


Evaluación

La siguiente métrica de evaluación será utilizada para obtener el puntaje máximo de calificación = 10.

Programación (Total = 5 pts):
Menú de selección de algoritmos: 0.5 pts
Tiempo de ejecución de cada algoritmo: 0.25 pts
Solicitud de parámetros de los algoritmos al usuario: 0.25 pts
Implementación de la distancia Haversine: 0.5 pts
Solicitud y ejecución de cada algoritmo con y sin información paso a paso: 0.5 pts
Algoritmos (3 de 5 pts):
Greedy best-first
A*
Weighted A*
Beam
Steepest hill climbing
Stochastic hill climbing
Simulated annealing
Genetic algorithms
Documentación (Total = 5 pts):  
Información general (2 de 5 pts):
Nombre del proyecto: 0.25 pts
Nombre de la universidad: 0.25 pts
Nombre de la materia: 0.25 pts
Nombre de los integrantes del equipo: 0.25 pts
Fecha de entrega o generación del archivo: 0.25 pts
Versión del código: 0.25 pts
Breve descripción del propósito del código contenido en dicho archivo: 0.25 pts
Instrucciones para ejecutar el código y leer el resultado obtenido: 0.25 pts
Código (3 de 5 pts):
Secciones (1 de 3 pts):
Dependencias: 0.25 pts
Variables globales: 0.25 pts
Funciones o Clases de apoyo: 0.25 pts
Funciones o Clases principales: 0.25 pts
Descripción de las funciones (1.5 de 3 pts):
Propósito: 0.5 pts (sólo si la función ejecuta como corresponde)
Parámetros de entrada: 0.5 pts (sólo si la función ejecuta como corresponde)
Salida o resultado de la ejecución: 0.5 pts (sólo si la función ejecuta como corresponde)
Nombre de los responsables de cada función (0.5 de 3 pts)
