import hashlib
import uuid
from my_function import *
from collections import defaultdict

if __name__ == '__main__':
#assigning ids to the cars
    assign_id = [dict(item, newId= uuid.uuid4()) for item in cars]

    print('Cars without ids',str(cars))
    print('Cars with ids',str(assign_id))
    categorize_cars_by_hp(cars)
    print('Slow cars:', str(slow_cars))
    print('Fast cars:', str(fast_cars))
    print('Sport cars', str(sport_cars))
    categorize_cars_by_price(cars)
    print('Cheap cars:', cheap_cars)
    print('Medium price cars', medium_price_cars)
    print('Expensive cars', expensive_cars)