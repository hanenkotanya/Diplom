#Посчитать попарные расстояния между Минском, Брестом, Витебском, Гомелем, Гродно и Могилёвым и вывести в виде HTML-таблицы.
#Координаты городов: https://www.geonames.org/search.html?q=&country=BY


from math import acos, sin, cos, radians, asin, sqrt 
import re 
 
CITIES = {  
        'Брест': ["52° 5' 51''", "23° 41' 15''"],  
        'Витебск': ["55° 11' 25''", "30° 12' 17''"],  
        'Гомель': ["52° 26' 4''", "30° 58' 31''"],  
        'Гродно': ["53° 41' 18''", "23° 49' 32''"],  
        'Минск': ["53° 54' 0''", "27° 34' 0''"],  
        'Могилев': ["53° 55' 0''", "30° 20' 41''"]  
    } 
 
def lat_lon_str_to_radians(val: str) -> float: 
    temp_val =  re.split("° |' |''", val) 
    temp_val = list(filter(None,temp_val)) 
    degress=(int(temp_val[0]))+(int(temp_val[1]))/60+(int(temp_val[2]))/3600
    radians_val = radians(degress) 
    return radians_val 
 
def distance(lat1: float, lon1: float, lat2: float, lon2:float) -> float: 
    D_Lo = lon2 - lon1  
    D_La = lat2 - lat1  
    P = sin(D_La / 2)**2 + cos(lat1) * cos(lat2) * sin(D_Lo / 2)**2  
    Q = 2 * asin(sqrt(P))  
    R_km = 6371.01  
    return(Q * R_km) 
 
def searh_table_distance(coordinates: dict[str, tuple[str, str]]): 
    result_list = [] 
    for i,(city_name, (coordinates_for_main_city1, coordinates_for_main_city2)) in enumerate(coordinates.items()): 
        radians_for_main_city1 = lat_lon_str_to_radians(coordinates_for_main_city1) 
        radians_for_main_city2 = lat_lon_str_to_radians(coordinates_for_main_city2) 
        city_distance = [] 
        for j,(other_city_name, (coordinates_for_other_city1, coordinates_for_other_city2)) in enumerate(coordinates.items()): 
            radians_for_other_city1 = lat_lon_str_to_radians(coordinates_for_other_city1) 
            radians_for_other_city2 = lat_lon_str_to_radians(coordinates_for_other_city2) 
            single_city_distance = distance(radians_for_main_city1,radians_for_main_city2,radians_for_other_city1,radians_for_other_city2) 
            rounded_distance = round(single_city_distance,2) 
            city_distance.append(str(rounded_distance)) 

        result_list.append([city_name, tuple(city_distance)]) 
    
    print(result_list)
    return result_list 
 
def generate_html_body(distances: list[str, tuple[float, float, float, float, float,float]]) -> str: 
    city_names = [] 
    html_body = "" 
    table_header = "" 
    table_rows = "" 
    city_names.append("Расстояние") 
    print(distances) 
    for i,(city_name, (dict1,dict2,dict3,dict4,dict5,dict6)) in enumerate(distances): 
        city_names.append(city_name) 
        table_rows += ("<tr>" 
                     "<td>"+city_name+"</td>" 
                     "<td>"+dict1+"</td>" 
                     "<td>"+dict2+"</td>" 
                     "<td>"+dict3+"</td>" 
                     "<td>"+dict4+"</td>" 
                     "<td>"+dict5+"</td>" 
                     "<td>"+dict6+"</td>" 
                     "</tr>") 
    for item in city_names: 
        table_header += "<th>"+item+"</th>" 
    table_header = "<tr>"+table_header+"</tr>" 
    html_body = '<table  border="1">'+table_header+table_rows+'/<table>' 
    return html_body 
     
 
intermediate_result = searh_table_distance(CITIES) 
html = generate_html_body(intermediate_result) 
print(html) 
 
with open ('test.html', 'w') as f: 
    f.write(str(html))
