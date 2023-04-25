import math

cities_coordinates = {
    'CANCUN': (21.1213285,-86.9192738)
    ,'VALLADOLID': (20.688114,-88.2204456)
    ,'FELIPE CARRILLO PUERTO': (19.5778903,-88.0630853)
    ,'CAMPECHE': (19.8305682,-90.5798365)
    ,'MERIDA': (20.9800512,-89.7029587)
    ,'CIUDAD DEL CARMEN': (18.6118375,-91.8927345)
    ,'CHETUMAL': (18.5221567,-88.3397982)
    ,'VILLAHERMOSA': (17.9925264,-92.9881407)
    ,'TUXTLA': (16.7459857,-93.1996103)
    ,'FRANCISCO ESCARCEGA': (18.6061556,-90.8176486)
    ,'ACAYUCAN': (17.951096,-94.9306961)
    ,'TEHUANTEPEC': (16.320636,-95.27521)
    ,'ALVARADO': (18.7760455,-95.7731952)
    ,'OAXACA': (17.0812951,-96.7707511)
    ,'PUERTO ANGEL': (15.6679974,-96.4933733)
    ,'IZUCAR DE MATAMOROS': (18.5980563,-98.5076767)
    ,'TEHUACAN': (18.462191,-97.4437333)
    ,'PINOTEPA NACIONAL': (16.3442895,-98.1315923)
    ,'CUERNAVACA': (18.9318685,-99.3106054)
    ,'PUEBLA': (19.040034,-98.2630056)
    ,'ACAPULCO': (16.8354485,-99.9323491)
    ,'CIUDAD DE MEXICO': (19.3898319,-99.7180148)
    ,'IGUALA': (18.3444,-99.5652232)
    ,'CIUDAD ALTAMIRANO': (18.3547491,-100.6817619)
    ,'CORDOBA': (18.8901707,-96.9751108)
    ,'CHILPANCINGO': (17.5477072,-99.5324349)
    ,'TLAXCALA': (19.4167798,-98.4471127)
    ,'PACHUCA DE SOTO': (20.0825056,-98.8268184)
    ,'QUERETARO': (20.6121228,-100.4802576)
    ,'TOLUCA DE LERDO': (19.294109,-99.6662331)
    ,'ZIHUATANEJO': (17.6405745,-101.5601369)
    ,'VERACRUZ': (19.1787635,-96.2113357)
    ,'TUXPAN DE RODRIGUEZ CANO': (20.9596561,-97.4158767)
    ,'ATLACOMULCO': (19.7980152,-99.89317)
    ,'SALAMANCA': (20.5664927,-101.2176511)
    ,'SAN LUIS POTOSI': (22.1127046,-101.0261099)
    ,'PLAYA AZUL': (17.9842581,-102.357616)
    ,'TAMPICO': (22.2662251,-97.939526)
    ,'GUANAJUATO': (21.0250928,-101.3296402)
    ,'MORELIA': (19.7036417,-101.2761644)
    ,'GUADALAJARA': (20.6737777,-103.4054536)
    ,'AGUASCALIENTES': (21.8857199,-102.36134)
    ,'ZACATECAS': (22.7636293,-102.623638)
    ,'DURANGO': (24.0226824,-104.7177652)
    ,'COLIMA': (19.2400444,-103.7636273)
    ,'MANZANILLO': (19.0775491,-104.4789574)
    ,'CIUDAD VICTORIA': (23.7409928,-99.1783576)
    ,'TEPIC': (21.5009822,-104.9119242)
    ,'HIDALGO DEL PARRAL': (26.9489283,-105.8211168)
    ,'MAZATLAN': (23.2467283,-106.4923175)
    ,'SOTO LA MARINA': (23.7673729,-98.2157573)
    ,'MATAMOROS': (25.8433787,-97.5849847)
    ,'MONTERREY': (25.6487281,-100.4431819)
    ,'CHIHUAHUA': (28.6708592,-106.2047036)
    ,'TOPOLOBAMPO': (25.6012747,-109.0687891)
    ,'CULIACAN': (24.8049008,-107.4933545)
    ,'REYNOSA': (26.0312262,-98.3662435)
    ,'MONCLOVA': (26.907775,-101.4940069)
    ,'CIUDAD JUAREZ': (31.6538179,-106.5890206)
    ,'JANOS': (30.8898127,-108.208458)
    ,'CIUDAD OBREGON': (27.4827355,-110.0844111)
    ,'TORREON': (25.548597,-103.4719562)
    ,'OJINAGA': (29.5453292,-104.4305246)
    ,'NUEVO LAREDO': (27.4530856,-99.6881218)
    ,'AGUA PRIETA': (31.3115272,-109.5855873)
    ,'GUAYMAS': (27.9272572,-110.9779564)
    ,'PIEDRAS NEGRAS': (28.6910517,-100.5801829)
    ,'SANTA ANA': (30.5345457,-111.1580567)
    ,'HERMOSILLO': (29.082137,-111.059027)
    ,'MEXICALI': (32.6137391,-115.5203312)
    ,'TIJUANA': (32.4966818,-117.087892)
    ,'SAN FELIPE': (31.009535,-114.8727296)
    ,'ENSENADA': (31.8423096,-116.6799816)
    ,'SAN QUINTIN': (30.5711324,-115.9588544)
    ,'SANTA ROSALIA': (27.3408761,-112.2825762)
    ,'SANTO DOMINGO': (25.3487297,-111.9975909)
    ,'LA PAZ': (24.1164209,-110.3727673)
    ,'CABO SAN LUCAS': (22.8962253,-109.9505077)
}


def get_haversine_distances(goal_city): #calcula las heuristicas de haversiene
    distances = {}
    lat1, lon1 = cities_coordinates[goal_city]
    for city_name, (lat2, lon2) in cities_coordinates.items():
        r = 6371  # radio de la Tierra en km
        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distances[city_name] = r * c
    return distances


def main():

    ciudad = []
    c = 'VALLADOLID'
    for goal_city in cities_coordinates:
        # print(goal_city)
        heuristica = get_haversine_distances(goal_city)

        for city_name, costo in heuristica.items():

            ciudad.append(goal_city)
            ciudad.append(city_name)
            ciudad.append(costo)
    

    for i in range(0, len(ciudad),3):
            print(ciudad[i], ciudad[i+1], ciudad[i+2])
    
main()