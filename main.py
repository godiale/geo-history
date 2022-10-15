import pandas as pd
import folium
import geopy
from geopy.extra.rate_limiter import RateLimiter


def coordinates(location):
    return tuple(location.point)[:2]


def icon(row):
    color = 'red' if 'Orber Str. 16' in row['Address'] \
        else 'orange' if pd.notna(row['Applied']) \
        else 'blue'
    return folium.Icon(color=color)


def main():
    geolocator = RateLimiter(geopy.Nominatim(user_agent="myGeocoder").geocode, min_delay_seconds=1.0)
    berlin = geolocator("Berlin Germany")

    df = pd.read_excel(io='input/Berlin.xlsx')
    df = df[['Address', 'Viewed', 'Applied']]
    df['Location'] = df['Address'].apply(geolocator)

    map1 = folium.Map(location=coordinates(berlin), zoom_start=12)
    df.apply(lambda row:
             folium.Marker(location=(coordinates(row['Location'])),
                           popup=row['Address'],
                           icon=icon(row))
             .add_to(map1), axis=1)

    map1.save("output/index.html")


if __name__ == '__main__':
    main()
