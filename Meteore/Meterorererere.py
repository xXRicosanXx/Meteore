import folium
import json
import math


with open("meteoriti.json", "r", encoding="utf-8") as f:
    meteoriti = json.load(f)


m = folium.Map(location=[45.5236, -122.6750], zoom_start=2)
i = 0

for met in meteoriti:
    lat = met.get("lat")
    lon = met.get("long")


    if lat == "NaN" or lon == "NaN":
        continue
    if lat == None or lon == None:
        continue
    if str(lat).lower() == "nan" or str(lon).lower() == "nan":
        continue
    if math.isnan(lat) or math.isnan(lon):
        continue

    folium.Marker(
        location=[lat, lon],
    ).add_to(m)
    i += 1

print("Meteoriti validi sulla mappa:", i)


m.save("map.html")
print("Mappa generata: map.html")
