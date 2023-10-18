import pandas as pd
import re
import math


data = pd.read_csv('cities2.csv', encoding='utf-8')
earth_radius = 6371

def degrees_to_radians(coord_str):
    parts = re.match(r'(-?\d+\.\d+)° (\d+)\' ([NSWE])', coord_str)
    
    if parts:
        degrees = float(parts.group(1))
        minutes = float(parts.group(2))
        direction = parts.group(3)
        
        radians = math.radians(degrees + minutes / 60)
        if direction in ['S', 'W']:
            radians = -radians
        return radians
    else:
        return None


def radians_to_km(angle):
    distance = earth_radius * angle
    return distance

data['Latitude'] = data['Latitude'].apply(degrees_to_radians)
data['Longitude'] = data['Longitude'].apply(degrees_to_radians)

data['Latitude'] = data['Latitude'].apply(radians_to_km)
data['Longitude'] = data['Longitude'].apply(radians_to_km)


def distance_between_cities(lat1, lon1, lat2, lon2):
    lat_diff = lat2 - lat1
    lon_diff = lon2 - lon1
    distance = math.sqrt(lat_diff**2 + lon_diff**2)
    return distance

clusters = []
d = math.radians(10)
distance_in_km = earth_radius * (d)

for i in range(len(data)):
    current_city_cluster = [data.at[i, 'city']]
    for j in range(i + 1, len(data)):

        lat1, lon1 = data.at[i, 'Latitude'], data.at[i, 'Longitude']
        lat2, lon2 = data.at[j, 'Latitude'], data.at[j, 'Longitude']
        distance = distance_between_cities(lat1, lon1, lat2, lon2)
        
        if distance <= distance_in_km:
            current_city_cluster.append(data.at[j, 'city'])
    if len(current_city_cluster) > 1:
        clusters.append(current_city_cluster)

for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {', '.join(cluster)}")


