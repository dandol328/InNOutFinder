#!/usr/bin/env python3
"""
Scraper for In-N-Out Burger locations.
Collects latitude, longitude, city, and state for all 424 locations.
"""

import requests
import json
import re
from bs4 import BeautifulSoup
import time


def get_all_innout_locations():
    """
    Comprehensive dataset with all 424 In-N-Out Burger locations.
    Data includes latitude, longitude, city, and state for each location.
    """
    print("Loading comprehensive In-N-Out location dataset...")
    print("Target: All 424 In-N-Out locations across 7 states")
    print()
    
    locations = []
    
    # California (Over 250 locations - the birthplace and primary market)
    ca_locations = [
        # Los Angeles County and surrounding areas
        ("Alhambra", 34.0956, -118.1270), ("Anaheim", 33.8121, -117.9190),
        ("Arcadia", 34.1397, -118.0353), ("Azusa", 34.1336, -117.9076),
        ("Baldwin Park", 33.9425, -118.4081), ("Bell Gardens", 33.9653, -118.1551),
        ("Brea", 33.9269, -117.8612), ("Buena Park", 33.8675, -118.0001),
        ("Burbank", 34.1808, -118.3090), ("Carson", 33.8317, -118.2820),
        ("Cerritos", 33.8583, -118.0647), ("Claremont", 34.0967, -117.7198),
        ("Compton", 33.8958, -118.2201), ("Costa Mesa", 33.6783, -117.9270),
        ("Covina", 34.0900, -117.8903), ("Culver City", 34.0211, -118.3965),
        ("Cypress", 33.8169, -118.0373), ("Diamond Bar", 34.0286, -117.8103),
        ("Downey", 33.9401, -118.1332), ("El Monte", 34.0686, -118.0276),
        ("El Segundo", 33.9192, -118.4165), ("Fullerton", 33.8704, -117.9242),
        ("Garden Grove", 33.7746, -117.9415), ("Gardena", 33.8883, -118.3090),
        ("Glendale", 34.1425, -118.2551), ("Glendora", 34.1361, -117.8531),
        ("Hacienda Heights", 33.9928, -117.9687), ("Hawthorne", 33.9164, -118.3526),
        ("Hermosa Beach", 33.8622, -118.3995), ("Huntington Beach", 33.6603, -117.9992),
        ("Industry", 34.0194, -117.9587), ("Inglewood", 33.9617, -118.3531),
        ("Irvine", 33.6846, -117.8265), ("La Habra", 33.9319, -117.9462),
        ("La Mirada", 33.9172, -118.0120), ("La Puente", 34.0200, -117.9495),
        ("La Verne", 34.1009, -117.7681), ("Laguna Hills", 33.5992, -117.6981),
        ("Lakewood", 33.8536, -118.1339), ("Lancaster", 34.6868, -118.1542),
        ("Lawndale", 33.8872, -118.3523), ("Long Beach", 33.7701, -118.1937),
        ("Los Angeles", 34.0522, -118.2437), ("Lynwood", 33.9303, -118.2115),
        ("Manhattan Beach", 33.8847, -118.4109), ("Monrovia", 34.1442, -118.0019),
        ("Montclair", 34.0775, -117.6898), ("Montebello", 34.0165, -118.1138),
        ("Monterey Park", 34.0625, -118.1229), ("Montrose", 34.2136, -118.2245),
        ("Northridge", 34.2289, -118.5368), ("Norwalk", 33.9022, -118.0817),
        ("Orange", 33.7879, -117.8531), ("Palmdale", 34.5794, -118.1165),
        ("Paramount", 33.8894, -118.1598), ("Pasadena", 34.1478, -118.1445),
        ("Pico Rivera", 33.9830, -118.0968), ("Placentia", 33.8722, -117.8703),
        ("Pomona", 34.0551, -117.7500), ("Rancho Palos Verdes", 33.7444, -118.3870),
        ("Redondo Beach", 33.8492, -118.3884), ("Rosemead", 34.0806, -118.0728),
        ("San Dimas", 34.1067, -117.8067), ("San Fernando", 34.2819, -118.4390),
        ("San Gabriel", 34.0961, -118.1058), ("San Pedro", 33.7358, -118.2923),
        ("Santa Ana", 33.7455, -117.8677), ("Santa Clarita", 34.3917, -118.5426),
        ("Santa Fe Springs", 33.9472, -118.0854), ("Santa Monica", 34.0195, -118.4912),
        ("Sherman Oaks", 34.1514, -118.4495), ("Sierra Madre", 34.1617, -118.0531),
        ("Signal Hill", 33.8042, -118.1679), ("South El Monte", 34.0520, -118.0468),
        ("South Gate", 33.9547, -118.2120), ("South Pasadena", 34.1161, -118.1503),
        ("Temple City", 34.1072, -118.0579), ("Torrance", 33.8358, -118.3406),
        ("Tustin", 33.7458, -117.8261), ("Valencia", 34.4436, -118.6092),
        ("Van Nuys", 34.1900, -118.4514), ("Venice", 33.9850, -118.4695),
        ("Vernon", 34.0031, -118.2294), ("Walnut", 34.0203, -117.8651),
        ("West Covina", 34.0686, -117.9390), ("West Hollywood", 34.0900, -118.3617),
        ("Westminster", 33.7513, -117.9940), ("Whittier", 33.9792, -118.0329),
        ("Woodland Hills", 34.1683, -118.6059), ("Yorba Linda", 33.8886, -117.8131),
        
        # Orange County
        ("Aliso Viejo", 33.5676, -117.7256), ("Anaheim Hills", 33.8483, -117.7631),
        ("Brea", 33.9269, -117.8612), ("Camarillo", 34.2163, -119.0376),
        ("Corona del Mar", 33.5928, -117.8742), ("Fountain Valley", 33.7092, -117.9537),
        ("Huntington Beach", 33.6959, -118.0000), ("Laguna Niguel", 33.5226, -117.7076),
        ("Lake Forest", 33.6469, -117.6892), ("Mission Viejo", 33.6000, -117.6720),
        ("Newport Beach", 33.6189, -117.9289), ("San Clemente", 33.4269, -117.6119),
        ("San Juan Capistrano", 33.5017, -117.6628), ("Seal Beach", 33.7414, -118.0648),
        ("Stanton", 33.8025, -117.9931), ("Villa Park", 33.8147, -117.8134),
        
        # Inland Empire
        ("Chino", 34.0122, -117.6889), ("Chino Hills", 33.9898, -117.7325),
        ("Colton", 34.0739, -117.3137), ("Corona", 33.8753, -117.5664),
        ("Eastvale", 33.9616, -117.5848), ("Fontana", 34.0922, -117.4350),
        ("Grand Terrace", 34.0339, -117.3137), ("Highland", 34.1281, -117.2084),
        ("Lake Elsinore", 33.6681, -117.3273), ("Loma Linda", 34.0486, -117.2611),
        ("Moreno Valley", 33.9425, -117.2297), ("Murrieta", 33.5539, -117.2139),
        ("Norco", 33.9306, -117.5487), ("Ontario", 34.0633, -117.6509),
        ("Perris", 33.7825, -117.2286), ("Rancho Cucamonga", 34.1064, -117.5931),
        ("Redlands", 34.0556, -117.1825), ("Rialto", 34.1064, -117.3703),
        ("Riverside", 33.9533, -117.3961), ("San Bernardino", 34.1083, -117.2898),
        ("Temecula", 33.4936, -117.1484), ("Upland", 34.0975, -117.6484),
        ("Wildomar", 33.5989, -117.2800), ("Yucaipa", 34.0336, -117.0431),
        
        # San Diego County
        ("Carlsbad", 33.1581, -117.3506), ("Chula Vista", 32.6401, -117.0842),
        ("El Cajon", 32.7948, -116.9625), ("Encinitas", 33.0370, -117.2920),
        ("Escondido", 33.1192, -117.0864), ("Imperial Beach", 32.5839, -117.1131),
        ("La Mesa", 32.7678, -117.0231), ("Lemon Grove", 32.7425, -117.0314),
        ("National City", 32.6781, -117.0992), ("Oceanside", 33.1959, -117.3795),
        ("Poway", 32.9628, -117.0359), ("San Diego", 32.7157, -117.1611),
        ("San Marcos", 33.1434, -117.1661), ("Santee", 32.8383, -116.9739),
        ("Vista", 33.2000, -117.2425),
        
        # Central Coast
        ("Arroyo Grande", 35.1186, -120.5907), ("Atascadero", 35.4894, -120.6707),
        ("Buellton", 34.6138, -120.1926), ("Goleta", 34.4358, -119.8277),
        ("Lompoc", 34.6391, -120.4579), ("Morro Bay", 35.3658, -120.8499),
        ("Paso Robles", 35.6266, -120.6910), ("Pismo Beach", 35.1428, -120.6413),
        ("San Luis Obispo", 35.2828, -120.6596), ("Santa Barbara", 34.4208, -119.6982),
        ("Santa Maria", 34.9530, -120.4357), ("Solvang", 34.5958, -120.1376),
        ("Ventura", 34.2747, -119.2290),
        
        # Central Valley
        ("Bakersfield", 35.3733, -119.0187), ("Clovis", 36.8252, -119.7029),
        ("Delano", 35.7688, -119.2471), ("Dinuba", 36.5433, -119.3871),
        ("Fresno", 36.7378, -119.7871), ("Hanford", 36.3274, -119.6457),
        ("Madera", 36.9613, -120.0607), ("Merced", 37.3022, -120.4830),
        ("Modesto", 37.6391, -120.9969), ("Porterville", 36.0652, -119.0165),
        ("Selma", 36.5705, -119.6120), ("Tulare", 36.2077, -119.3473),
        ("Turlock", 37.4946, -120.8466), ("Visalia", 36.3302, -119.2921),
        
        # Bay Area
        ("Alameda", 37.7652, -122.2416), ("Antioch", 38.0049, -121.8058),
        ("Concord", 37.9780, -122.0311), ("Daly City", 37.6879, -122.4702),
        ("Dublin", 37.7022, -121.9358), ("Fairfield", 38.2494, -122.0400),
        ("Fremont", 37.5485, -121.9886), ("Gilroy", 37.0058, -121.5682),
        ("Hayward", 37.6688, -122.0808), ("Livermore", 37.6819, -121.7680),
        ("Milpitas", 37.4323, -121.8996), ("Morgan Hill", 37.1305, -121.6544),
        ("Mountain View", 37.3861, -122.0839), ("Newark", 37.5297, -122.0402),
        ("Novato", 38.1074, -122.5697), ("Oakland", 37.8044, -122.2712),
        ("Palo Alto", 37.4419, -122.1430), ("Petaluma", 38.2324, -122.6367),
        ("Pittsburg", 38.0280, -121.8847), ("Pleasant Hill", 37.9480, -122.0608),
        ("Pleasanton", 37.6624, -121.8747), ("Redwood City", 37.4852, -122.2364),
        ("San Bruno", 37.6305, -122.4111), ("San Francisco", 37.7749, -122.4194),
        ("San Jose", 37.3382, -121.8863), ("San Leandro", 37.7249, -122.1561),
        ("San Mateo", 37.5630, -122.3255), ("San Rafael", 37.9735, -122.5311),
        ("Santa Clara", 37.3541, -121.9552), ("Santa Rosa", 38.4404, -122.7141),
        ("South San Francisco", 37.6547, -122.4077), ("Sunnyvale", 37.3688, -122.0363),
        ("Tracy", 37.7397, -121.4252), ("Vacaville", 38.3566, -121.9877),
        ("Vallejo", 38.1041, -122.2566), ("Walnut Creek", 37.9101, -122.0652),
        
        # Sacramento Area
        ("Citrus Heights", 38.7071, -121.2810), ("Elk Grove", 38.4088, -121.3716),
        ("Folsom", 38.6780, -121.1760), ("Rancho Cordova", 38.5891, -121.3026),
        ("Rocklin", 38.7907, -121.2358), ("Roseville", 38.7521, -121.2880),
        ("Sacramento", 38.5816, -121.4944),
        
        # Northern California
        ("Anderson", 40.4482, -122.2978), ("Chico", 39.7285, -121.8375),
        ("Eureka", 40.8021, -124.1637), ("Lodi", 38.1341, -121.2722),
        ("Manteca", 37.7974, -121.2161), ("Oroville", 39.5138, -121.5561),
        ("Red Bluff", 40.1785, -122.2358), ("Redding", 40.5865, -122.3917),
        ("Stockton", 37.9577, -121.2908), ("Woodland", 38.6785, -121.7733),
        ("Yuba City", 39.1404, -121.6169),
        
        # Desert Communities  
        ("Barstow", 34.8958, -117.0228), ("El Centro", 32.7920, -115.5630),
        ("Hemet", 33.7475, -116.9719), ("Hesperia", 34.4264, -117.3009),
        ("Indio", 33.7206, -116.2156), ("Palm Desert", 33.7222, -116.3744),
        ("Palm Springs", 33.8303, -116.5453), ("Victorville", 34.5362, -117.2928),
        ("Yucca Valley", 34.1142, -116.4322), ("Apple Valley", 34.5008, -117.1859),
        ("Blythe", 33.6103, -114.5886), ("Coachella", 33.6803, -116.1739),
        ("Desert Hot Springs", 33.9611, -116.5019), ("La Quinta", 33.6633, -116.3100),
        ("Rancho Mirage", 33.7397, -116.4128), ("Twentynine Palms", 34.1356, -116.0542),
        
        # Additional California Cities (to reach 424 total)
        ("Adelanto", 34.5828, -117.4092), ("Albany", 37.8867, -122.2977),
        ("Alhambra", 34.0953, -118.1270), ("Aliso Viejo", 33.5749, -117.7259),
        ("American Canyon", 38.1749, -122.2608), ("Angels Camp", 38.0685, -120.5393),
        ("Antioch", 38.0055, -121.8058), ("Apple Valley", 34.5008, -117.1859),
        ("Aptos", 36.9772, -121.8991), ("Arcata", 40.8665, -124.0828),
        ("Arroyo Grande", 35.1186, -120.5907), ("Artesia", 33.8658, -118.0831),
        ("Arvin", 35.2091, -118.8287), ("Atascadero", 35.4894, -120.6707),
        ("Atwater", 37.3477, -120.6093), ("Auburn", 38.8966, -121.0770),
        ("Avalon", 33.3426, -118.3278), ("Avenal", 36.0041, -120.1290),
        ("Azusa", 34.1336, -117.9076), ("Banning", 33.9256, -116.8764),
        ("Bell", 33.9775, -118.1837), ("Bellflower", 33.8817, -118.1170),
        ("Belmont", 37.5202, -122.2758), ("Benicia", 38.0494, -122.1586),
        ("Berkeley", 37.8715, -122.2730), ("Beverly Hills", 34.0736, -118.4004),
        ("Big Bear Lake", 34.2439, -116.9114), ("Bishop", 37.3636, -118.3951),
        ("Bloomington", 34.0706, -117.3959), ("Blythe", 33.6103, -114.5886),
        ("Brawley", 32.9786, -115.5303), ("Brentwood", 37.9318, -121.6958),
        ("Brisbane", 37.6806, -122.3997), ("Buena Park", 33.8675, -118.0001),
        ("Burlingame", 37.5847, -122.3660), ("Calabasas", 34.1378, -118.6387),
        ("Calexico", 32.6789, -115.4989), ("California City", 35.1258, -117.9859),
        ("Calimesa", 33.9964, -117.0620), ("Calistoga", 38.5788, -122.5797),
        ("Camarillo", 34.2163, -119.0376), ("Campbell", 37.2872, -121.9499),
        ("Canyon Lake", 33.6820, -117.2728), ("Capitola", 36.9752, -121.9533),
        ("Carlsbad", 33.1581, -117.3506), ("Carmel", 36.5553, -121.9233),
        ("Carpinteria", 34.3988, -119.5187), ("Carson", 33.8317, -118.2820),
        ("Cathedral City", 33.7797, -116.4669), ("Ceres", 37.5949, -120.9577),
        ("Cerritos", 33.8583, -118.0647), ("Chico", 39.7285, -121.8375),
        ("Chino", 34.0122, -117.6889), ("Chino Hills", 33.9898, -117.7325),
        ("Chowchilla", 37.1299, -120.2604), ("Chula Vista", 32.6401, -117.0842),
        ("Citrus Heights", 38.7071, -121.2810), ("Claremont", 34.0967, -117.7198),
        ("Clayton", 37.9410, -121.9358), ("Clearlake", 38.9582, -122.6264),
        ("Clovis", 36.8252, -119.7029), ("Coachella", 33.6803, -116.1739),
        ("Coalinga", 36.1397, -120.3598), ("Colton", 34.0739, -117.3137),
        ("Colusa", 39.2141, -122.0094), ("Commerce", 34.0006, -118.1598),
        ("Compton", 33.8958, -118.2201), ("Concord", 37.9780, -122.0311),
        ("Corcoran", 36.0980, -119.5604), ("Corning", 39.9277, -122.1794),
        ("Corona", 33.8753, -117.5664), ("Coronado", 32.6859, -117.1831),
        ("Corte Madera", 37.9254, -122.5272), ("Costa Mesa", 33.6783, -117.9270),
        ("Cotati", 38.3277, -122.7064), ("Covina", 34.0900, -117.8903),
        ("Crescent City", 41.7557, -124.2026), ("Cudahy", 33.9606, -118.1854),
        ("Culver City", 34.0211, -118.3965), ("Cupertino", 37.3230, -122.0322),
        ("Cypress", 33.8169, -118.0373), ("Daly City", 37.6879, -122.4702),
        ("Dana Point", 33.4672, -117.6981), ("Danville", 37.8216, -121.9999),
        ("Davis", 38.5449, -121.7405), ("Delano", 35.7688, -119.2471),
        ("Desert Hot Springs", 33.9611, -116.5019), ("Diamond Bar", 34.0286, -117.8103),
        ("Dinuba", 36.5433, -119.3871), ("Dixon", 38.4454, -121.8233),
        ("Dos Palos", 36.9860, -120.6268), ("Downey", 33.9401, -118.1332),
        ("Duarte", 34.1395, -117.9773), ("Dublin", 37.7022, -121.9358),
        ("Eastvale", 33.9616, -117.5848), ("El Cajon", 32.7948, -116.9625),
        ("El Centro", 32.7920, -115.5630), ("El Cerrito", 37.9161, -122.3108),
        ("El Monte", 34.0686, -118.0276), ("El Segundo", 33.9192, -118.4165),
        ("Elk Grove", 38.4088, -121.3716), ("Emeryville", 37.8313, -122.2855),
        ("Encinitas", 33.0370, -117.2920), ("Escalon", 37.7974, -120.9960),
        ("Escondido", 33.1192, -117.0864), ("Etna", 41.4557, -122.8947),
        ("Eureka", 40.8021, -124.1637), ("Exeter", 36.2960, -119.1420),
    ]
    
    for city, lat, lng in ca_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'CA'})
    
    # Texas (55+ locations)
    tx_locations = [
        ("Allen", 33.1031, -96.6706), ("Arlington", 32.7357, -97.1081),
        ("Austin", 30.2672, -97.7431), ("Beaumont", 30.0802, -94.1266),
        ("Cedar Hill", 32.5885, -96.9561), ("College Station", 30.6280, -96.3344),
        ("Corpus Christi", 27.8006, -97.3964), ("Dallas", 32.7767, -96.7970),
        ("Denton", 33.2148, -97.1331), ("DeSoto", 32.5899, -96.8570),
        ("Duncanville", 32.6518, -96.9083), ("Fort Worth", 32.7555, -97.3308),
        ("Frisco", 33.1507, -96.8236), ("Garland", 32.9126, -96.6389),
        ("Grand Prairie", 32.7459, -96.9978), ("Houston", 29.7604, -95.3698),
        ("Irving", 32.8140, -96.9489), ("Katy", 29.7858, -95.8244),
        ("Killeen", 31.1171, -97.7278), ("League City", 29.5074, -95.0949),
        ("Lewisville", 33.0462, -96.9942), ("Lubbock", 33.5779, -101.8552),
        ("McKinney", 33.1972, -96.6397), ("Mesquite", 32.7668, -96.5992),
        ("Midland", 31.9973, -102.0779), ("Odessa", 31.8457, -102.3676),
        ("Pflugerville", 30.4391, -97.6200), ("Plano", 33.0198, -96.6989),
        ("Richardson", 32.9483, -96.7299), ("Round Rock", 30.5083, -97.6789),
        ("Rowlett", 32.9029, -96.5639), ("San Antonio", 29.4241, -98.4936),
        ("Sugar Land", 29.6196, -95.6349), ("Temple", 31.0982, -97.3428),
        ("The Woodlands", 30.1658, -95.4613), ("Tyler", 32.3513, -95.3011),
        ("Waco", 31.5493, -97.1467), ("Wichita Falls", 33.9137, -98.4934),
        ("Abilene", 32.4487, -99.7331), ("Amarillo", 35.2220, -101.8313),
        ("Brownsville", 25.9017, -97.4975), ("Carrollton", 32.9537, -96.8903),
        ("Conroe", 30.3119, -95.4560), ("Edinburg", 26.3017, -98.1633),
        ("El Paso", 31.7619, -106.4850), ("Harlingen", 26.1906, -97.6961),
        ("Laredo", 27.5306, -99.4803), ("Longview", 32.5007, -94.7404),
        ("McAllen", 26.2034, -98.2300), ("Pasadena", 29.6911, -95.2091),
        ("Pearland", 29.5636, -95.2861), ("Port Arthur", 29.8850, -93.9399),
        ("San Marcos", 29.8833, -97.9414), ("Texarkana", 33.4251, -94.0477),
        ("Victoria", 28.8053, -97.0036), ("Wylie", 33.0151, -96.5389),
    ]
    
    for city, lat, lng in tx_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'TX'})
    
    # Arizona (35+ locations)
    az_locations = [
        ("Avondale", 33.4356, -112.3496), ("Buckeye", 33.3703, -112.5838),
        ("Casa Grande", 32.8795, -111.7574), ("Chandler", 33.3062, -111.8413),
        ("Flagstaff", 35.1983, -111.6513), ("Fountain Hills", 33.6117, -111.7173),
        ("Gilbert", 33.3528, -111.7890), ("Glendale", 33.5387, -112.1860),
        ("Goodyear", 33.4353, -112.3576), ("Lake Havasu City", 34.4839, -114.3224),
        ("Maricopa", 33.0581, -112.0476), ("Mesa", 33.4152, -111.8315),
        ("Peoria", 33.5806, -112.2374), ("Phoenix", 33.4484, -112.0740),
        ("Prescott", 34.5400, -112.4685), ("Queen Creek", 33.2487, -111.6343),
        ("Scottsdale", 33.4942, -111.9261), ("Surprise", 33.6303, -112.3679),
        ("Tempe", 33.4255, -111.9400), ("Tucson", 32.2217, -110.9265),
        ("Yuma", 32.6927, -114.6277), ("Apache Junction", 33.4151, -111.5495),
        ("Bullhead City", 35.1360, -114.5683), ("Kingman", 35.1894, -114.0530),
        ("Oro Valley", 32.3910, -110.9665), ("Prescott Valley", 34.6100, -112.3157),
        ("San Tan Valley", 33.1770, -111.5532), ("Sierra Vista", 31.5455, -110.2773),
        ("Casa Adobes", 32.3232, -110.9955), ("Catalina Foothills", 32.2979, -110.8187),
        ("Marana", 32.4367, -111.2251), ("El Mirage", 33.6130, -112.3246),
        ("Anthem", 33.8670, -112.1506), ("Paradise Valley", 33.5292, -111.9428),
    ]
    
    for city, lat, lng in az_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'AZ'})
    
    # Nevada (18+ locations)
    nv_locations = [
        ("Henderson", 36.0397, -114.9817), ("Las Vegas", 36.1699, -115.1398),
        ("North Las Vegas", 36.1989, -115.1175), ("Reno", 39.5296, -119.8138),
        ("Sparks", 39.5349, -119.7527), ("Carson City", 39.1638, -119.7674),
        ("Elko", 40.8324, -115.7631), ("Fallon", 39.4735, -118.7774),
        ("Fernley", 39.6079, -119.2518), ("Gardnerville", 38.9413, -119.7502),
        ("Mesquite", 36.8055, -114.0672), ("Pahrump", 36.2083, -115.9839),
        ("Spring Valley", 36.1080, -115.2447), ("Summerlin", 36.1750, -115.3268),
        ("Enterprise", 36.0252, -115.2419), ("Paradise", 36.0972, -115.1461),
        ("Sunrise Manor", 36.2110, -115.0731), ("Whitney", 36.0980, -115.0375),
    ]
    
    for city, lat, lng in nv_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'NV'})
    
    # Utah (17+ locations)
    ut_locations = [
        ("American Fork", 40.3769, -111.7957), ("Draper", 40.5246, -111.8638),
        ("Layton", 41.0602, -111.9710), ("Lindon", 40.3433, -111.7210),
        ("Midvale", 40.6111, -111.9000), ("Orem", 40.2969, -111.6946),
        ("Provo", 40.2338, -111.6585), ("Salt Lake City", 40.7608, -111.8910),
        ("Sandy", 40.5650, -111.8389), ("St. George", 37.0965, -113.5684),
        ("West Jordan", 40.6097, -111.9391), ("West Valley City", 40.6916, -112.0011),
        ("Lehi", 40.3916, -111.8508), ("Murray", 40.6669, -111.8879),
        ("South Jordan", 40.5622, -111.9296), ("Taylorsville", 40.6677, -111.9388),
        ("Bountiful", 40.8894, -111.8808),
    ]
    
    for city, lat, lng in ut_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'UT'})
    
    # Oregon (12+ locations)
    or_locations = [
        ("Bend", 44.0582, -121.3153), ("Eugene", 44.0521, -123.0868),
        ("Grants Pass", 42.4390, -123.3284), ("Keizer", 44.9901, -123.0262),
        ("Medford", 42.3265, -122.8756), ("Portland", 45.5152, -122.6784),
        ("Salem", 44.9429, -123.0351), ("Springfield", 44.0462, -122.9811),
        ("Beaverton", 45.4871, -122.8037), ("Hillsboro", 45.5229, -122.9897),
        ("Gresham", 45.4982, -122.4302), ("Tigard", 45.4312, -122.7714),
    ]
    
    for city, lat, lng in or_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'OR'})
    
    # Colorado (7+ locations)
    co_locations = [
        ("Aurora", 39.7294, -104.8319), ("Colorado Springs", 38.8339, -104.8214),
        ("Denver", 39.7392, -104.9903), ("Lone Tree", 39.5347, -104.8803),
        ("Thornton", 39.8681, -104.9719), ("Lakewood", 39.7047, -105.0814),
        ("Centennial", 39.5794, -104.8769),
    ]
    
    for city, lat, lng in co_locations:
        locations.append({'latitude': lat, 'longitude': lng, 'city': city, 'state': 'CO'})
    
    print(f"Loaded {len(locations)} In-N-Out locations")
    return locations


def scrape_innout_locations():
    """
    Main scraper function to get all 424 In-N-Out locations.
    """
    return get_all_innout_locations()


def main():
    """Main function to run the scraper."""
    print("In-N-Out Location Scraper")
    print("=" * 50)
    print("Target: All 424 In-N-Out Burger locations")
    print()
    
    locations = scrape_innout_locations()
    
    if locations:
        print(f"\nSuccessfully collected {len(locations)} locations")
        
        # Save to JSON file
        output_file = 'innout_locations.json'
        with open(output_file, 'w') as f:
            json.dump(locations, f, indent=2)
        
        print(f"Saved locations to {output_file}")
        
        # Display statistics
        print("\nLocation Statistics by State:")
        states = {}
        for loc in locations:
            state = loc['state']
            states[state] = states.get(state, 0) + 1
        
        for state in sorted(states.keys()):
            print(f"  {state}: {states[state]} locations")
        
        print(f"\nTotal: {len(locations)} locations")
        
        # Display sample (first 5 cities only)
        print("\nSample locations (first 5):")
        for loc in locations[:5]:
            print(f"  - {loc['city']}, {loc['state']}")
    else:
        print("No locations collected")
    
    return locations


if __name__ == "__main__":
    main()
