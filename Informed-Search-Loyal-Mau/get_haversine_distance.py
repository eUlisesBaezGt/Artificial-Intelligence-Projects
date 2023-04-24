###############################
###############################
##### Informacion general #####
'''
    Proyecto: Calcular la heuristica de linea recta entre dos ciudades
    Universidad Panamericana
    Clase de Inteligencia Artificial
    Ari Barrera
    22-marzo-2023
    version 0.001

    El presente codigo calcula la distancia euclideana entre dos ciudades 
    de los Estados Unidos Mexicanos, utilizando las coordenadas geograficas 
    de un par de ciudades. Esta distancia es utilizada para obtener los
    valores de la heuristica para el proyecto del 2do Parcial de la materia.

    Ejecucion del programa
        Opcion 1) En una terminal que sobre el directorio donde radica este archivo escribir:
                    python get_euclidean_distance.py
        Opcion 2) Abrir el archivo con un editor de codigo y presionar el boton ejecutar
    
    Entradas:
        1) El nombre de una ciudad en Mexico que deseemos sea el destino
    
    Salidas:
        1) Imprime en pantalla los valores calculados de la heuristica de distancia de linea recta
'''

###############################
##### Dependencias #####
import math

###############################
##### Variables Globales #####
R = 6371000 #Earth's radius in meters

# diccionario con el nombre de las ciudades contenidas en el grafo y sus correspondientes coordenadas
#   geograficas en formato de latitud y longitud
cities_coordinates = {
    'Cancun': (21.1213285,-86.9192738)
    ,'Valladolid': (20.688114,-88.2204456)
    ,'FelipeCarrilloPuerto': (19.5778903,-88.0630853)
    ,'Campeche': (19.8305682,-90.5798365)
    ,'Merida': (20.9800512,-89.7029587)
    ,'CiudadDelCarmen': (18.6118375,-91.8927345)
    ,'Chetumal': (18.5221567,-88.3397982)
    ,'Villahermosa': (17.9925264,-92.9881407)
    ,'Tuxtla': (16.7459857,-93.1996103)
    ,'FranciscoEscarcega': (18.6061556,-90.8176486)
    ,'Acayucan': (17.951096,-94.9306961)
    ,'Tehuantepec': (16.320636,-95.27521)
    ,'Alvarado': (18.7760455,-95.7731952)
    ,'Oaxaca': (17.0812951,-96.7707511)
    ,'PuertoAngel': (15.6679974,-96.4933733)
    ,'IzucarDeMatamoros': (18.5980563,-98.5076767)
    ,'Tehuacan': (18.462191,-97.4437333)
    ,'PinotepaNacional': (16.3442895,-98.1315923)
    ,'Cuernavaca': (18.9318685,-99.3106054)
    ,'Puebla': (19.040034,-98.2630056)
    ,'Acapulco': (16.8354485,-99.9323491)
    ,'CiudadDeMexico': (19.3898319,-99.7180148)
    ,'Iguala': (18.3444,-99.5652232)
    ,'CiudadAltamirano': (18.3547491,-100.6817619)
    ,'Cordoba': (18.8901707,-96.9751108)
    ,'Chilpancingo': (17.5477072,-99.5324349)
    ,'Tlaxcala': (19.4167798,-98.4471127)
    ,'PachucaDeSoto': (20.0825056,-98.8268184)
    ,'Queretaro': (20.6121228,-100.4802576)
    ,'TolucaDeLerdo': (19.294109,-99.6662331)
    ,'Zihuatanejo': (17.6405745,-101.5601369)
    ,'Veracruz': (19.1787635,-96.2113357)
    ,'TuxpanDeRodriguezCano': (20.9596561,-97.4158767)
    ,'Atlacomulco': (19.7980152,-99.89317)
    ,'Salamanca': (20.5664927,-101.2176511)
    ,'SanLuisPotosi': (22.1127046,-101.0261099)
    ,'PlayaAzul': (17.9842581,-102.357616)
    ,'Tampico': (22.2662251,-97.939526)
    ,'Guanajuato': (21.0250928,-101.3296402)
    ,'Morelia': (19.7036417,-101.2761644)
    ,'Guadalajara': (20.6737777,-103.4054536)
    ,'Aguascalientes': (21.8857199,-102.36134)
    ,'Zacatecas': (22.7636293,-102.623638)
    ,'Durango': (24.0226824,-104.7177652)
    ,'Colima': (19.2400444,-103.7636273)
    ,'Manzanillo': (19.0775491,-104.4789574)
    ,'CiudadVictoria': (23.7409928,-99.1783576)
    ,'Tepic': (21.5009822,-104.9119242)
    ,'HidalgoDelParral': (26.9489283,-105.8211168)
    ,'Mazatlan': (23.2467283,-106.4923175)
    ,'SotoLaMarina': (23.7673729,-98.2157573)
    ,'Matamoros': (25.8433787,-97.5849847)
    ,'Monterrey': (25.6487281,-100.4431819)
    ,'Chihuahua': (28.6708592,-106.2047036)
    ,'Topolobampo': (25.6012747,-109.0687891)
    ,'Culiacan': (24.8049008,-107.4933545)
    ,'Reynosa': (26.0312262,-98.3662435)
    ,'Monclova': (26.907775,-101.4940069)
    ,'Juarez': (31.6538179,-106.5890206)
    ,'Janos': (30.8898127,-108.208458)
    ,'CiudadObregon': (27.4827355,-110.0844111)
    ,'Torreon': (25.548597,-103.4719562)
    ,'Ojinaga': (29.5453292,-104.4305246)
    ,'NuevoLaredo': (27.4530856,-99.6881218)
    ,'AguaPrieta': (31.3115272,-109.5855873)
    ,'Guaymas': (27.9272572,-110.9779564)
    ,'PiedrasNegras': (28.6910517,-100.5801829)
    ,'SantaAna': (30.5345457,-111.1580567)
    ,'Hermosillo': (29.082137,-111.059027)
    ,'Mexicalli': (32.6137391,-115.5203312)
    ,'Tijuana': (32.4966818,-117.087892)
    ,'SanFelipe': (31.009535,-114.8727296)
    ,'Ensenada': (31.8423096,-116.6799816)
    ,'SanQuintin': (30.5711324,-115.9588544)
    ,'SantaRosalia': (27.3408761,-112.2825762)
    ,'SantoDomingo': (25.3487297,-111.9975909)
    ,'LaPaz': (24.1164209,-110.3727673)
    ,'CaboSanLucas': (22.8962253,-109.9505077)
}

###############################
###############################
##### Funciones o Clases de Apoyo #####

# calcula la distancia euclideana entre dos ciudades por medio de las coordenas geograficas
# entrada:
#   origin = tupla que contiene la latitud y longitud de la ciudad de origen
#   goal = tupla que contiene la latitud y longitud de la ciudad destino
# salida:
#   regresa el valor numerico de la distancia euclideana redondeado
def haversine_distance_between_cities(origin,goal):
    # calcula la distancia euclideana entre dos ciudades y regresa su valor redondeado
    a = math.sin((math.radians(goal[0]-origin[0]))/2)**2 + math.cos(math.radians(origin[0]))*math.cos(math.radians(goal[0]))*(math.sin((math.radians(goal[1]-origin[1])/2)))**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    dist = round(R * c)
    return dist

###############################
###############################
##### Funciones o Clases Principales #####

# calcula la heuristica para una ciudad objetivo
# entrada:
#   goal_city = nombre de la ciudad objetivo
# salida:
#   regresa un diccionario con los valores numericos de la heuristica para la ciudad objetivo
#       introducida por el usuario
def calcular_heuristica_distancia_de_linea_recta(goal):
    # obtiene las coordenadas de la ciudad destino
    coordinate_goal = cities_coordinates[goal]

    # diccionario que contendra los valores de la heuristica de distancia de linea recta para
    # la ciudad de destino ingresada
    heuristic_linear_straight_distance = {}

    # itera a traves de todas las ciudades disponibles en el grafo
    for city_origin, coordinate_origin in cities_coordinates.items():
        # obtiene la distancia euclideana de las dos ciudades correspondientes
        euclidean_distance = haversine_distance_between_cities(coordinate_origin,coordinate_goal)
        # agrega al diccionario de heuristica la ciudad de origen y su valor de distancia de linea recta
        heuristic_linear_straight_distance[city_origin] = euclidean_distance
    
    # regresa el diccionario con los valores de la heuristica para la ciudad objetivo correspondiente
    return heuristic_linear_straight_distance


    
# funcion que encapsula la estructura general del programa
# entrada:
#   sin parametros
# salida:
#   imprime en pantalla los valores calculados de la heuristica de distancia de linea recta para las
#   ciudades del grafo de Mexico
def run(goal):
    # manda llamar a la funcion para calcular la heuristica
    hlsd = calcular_heuristica_distancia_de_linea_recta(goal)
    
    # regresa al programa principal el diccionario
    return hlsd


