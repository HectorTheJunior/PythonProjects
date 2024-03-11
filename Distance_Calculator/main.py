from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def calculate_distance_km(home, target) -> float|None:
    if home and target:
        distance = geodesic(home.coordinates(), target.coordinates()).km
    return distance


def get_distance_km(home: str, target: str) -> float|None:
    home_coors = get_coordinates(home)
    target_coors = get_coordinates(target)

    if distance := calculate_distance_km(home_coors, target_coors):
        print(f'{home} --> {target}')
        print(f'{distance:.2f} km')
        return distance
    else:
        print("Failed to calculate the distance")


def get_coordinates(address) -> Coordinates|None:
    geolocator = Nominatim(user_agent='distance_calculator')

    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def main():
    home_address = input('Enter first address: ')
    target_address = input('Enter second address: ')
    print("Calculating.....")
    get_distance_km(home=home_address, target=target_address)


main()
