import folium
import json
import math

m=folium.Map(location=[45.5236, -122.6750])
m.save('map.html')

nomefile = "meteorriti!!!.json"

with open(nomefile, 'r') as met:
    meteore = met.read()


meteoriti = json.loads(meteore)
# print(meteoriti[10000])

i=0

# for met in meteoriti:
#     if i!=3462:
#         if meteoriti[i]["geolocation"] == meteoriti[3462]["year"]:
#             meteoriti[i]["geolocation"] = "NaN"
#         if meteoriti[i]["long"] == meteoriti[3462]["year"]:
#             meteoriti[i]["long"] = "NaN"
#         if meteoriti[i]["lat"] == meteoriti[3462]["year"]:
#             meteoriti[i]["lat"] = "NaN"
#     i+=1


# print(i)
# print(type(meteoriti[3462]["year"]))
# print(meteoriti[3462]["year"])
# print(meteoriti[3438]["geolocation"])
nan=meteoriti[3462]["year"]

if (meteoriti[3462]["year"] == math.isnan(nan)):
    print("ok")

# file_pulito = "meteorriti!!!.json"

# with open(file_pulito, "w", encoding="utf-8") as f:
#     json.dump(meteoriti, f, ensure_ascii=False, indent=4)
print(lat=meteoriti[0]["geolocation"][0])

# for met in meteoriti:
#     if meteoriti["geolocation"] != "NaN":
#         folium.Marker(
#             lat=meteoriti["geolocation"][0],
#             location=
#         )