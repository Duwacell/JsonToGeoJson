import json
import pandas as pd
import geojson

def data2geojson(df):
    features = []
    insert_features = lambda X: features.append(
                                geojson.Feature(geometry=geojson.Point((X["lon"],X["lat"])),
                                properties=dict(ID=X["name"])))
    df.apply(insert_features, axis=1)
    with open('map1.json', 'w', encoding='utf8') as fp:
        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)

with open('jsonfile.json',encoding="utf-8") as f:
    data = json.load(f)
bookmarks = data['portals']['idOthers']['bkmrk']
data = []
df = pd.DataFrame(data,columns=['lat','lon','name'])

for i in bookmarks:
    name = bookmarks[i]['label']
    x = bookmarks[i]['latlng'].split(",")
    lat = float(x[0])
    lon = float(x[1])
    df = df.append({'lat': lat,'lon': lon,'name':name},ignore_index=True)
data2geojson(df)
