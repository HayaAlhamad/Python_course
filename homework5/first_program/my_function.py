cars = [
    {
        "brand": "bmw",
        "model": 10,
        "horse_power": 120,
        "price": 10000
    },
    {
        "brand": "dacia",
        "model": 20,
        "horse_power": 100,
        "price": 500
    },
    {
        "brand": "mercedes",
        "model": 30,
        "horse_power": 150,
        "price": 30000
    },

    {
        "brand": "tesla",
        "model": 40,
        "horse_power": 200,
        "price": 40000
    },
    {
        "brand": "kia",
        "model": 50,
        "horse_power": 110,
        "price": 100
    },
    {
        "brand": "toyota",
        "model": 60,
        "horse_power": 100,
        "price": 1500
    }
]

# categorize the cars according to the number of horsepower
slow_cars = []
fast_cars = []
sport_cars = []


def categorize_cars_by_hp(cars):
    for n in cars:
        if n['horse_power'] < 120:
            slow_cars.append(n)
        elif 120 <= n['horse_power'] < 180:
            fast_cars.append(n)
        else:
            sport_cars.append(n)

    return slow_cars, fast_cars, sport_cars


# categorize the cars according to the price
cheap_cars = []
medium_price_cars = []
expensive_cars = []


def categorize_cars_by_price(cars):
    for i in cars:
        if i['price'] < 1000:
            cheap_cars.append(i)
        elif 1000 <= i['price'] <= 5000:
            medium_price_cars.append(i)
        else:
            expensive_cars.append(i)
    return cheap_cars, medium_price_cars, expensive_cars
# newlist = sorted(cars, key=lambda d: d['horse_power'])
