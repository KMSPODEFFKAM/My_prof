import folium
import geojson

def run(file_name:str):

    m = folium.Map(location=[61, 105], zoom_start=3)

    style = {'color': '#FF0000'}

    with open(file_name, encoding='utf-8') as file:
        gj = geojson.load(file)

    folium.GeoJson(gj, name='Границы', style_function=lambda x: style).add_to(m)

    m.save('test.html')

if __name__ == '__main__':
    run('russia_geojson_wgs84.geojson')