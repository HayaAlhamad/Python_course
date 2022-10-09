from csv import DictReader
import os
import json
from pathlib import Path
from second_function import *





if __name__ == '__main__':
    slow_cars = []
    fast_cars = []
    sport_cars = []
    cheap_cars = []
    medium_price_cars = []
    expensive_cars = []
    new_brand = []
    desired_dir = "output_dir"
    #creating the directory
    create_output_directory()

#reading the data from the .csv file

    with open("inp.csv", 'r') as csv_file:
        dict_reader = DictReader(csv_file)
        list_of_dict = list(dict_reader)
# creating json file for the cars based on horse power
        for n in list_of_dict:
            if int(n['horse_power'])< 120:
                file_name = "slow_carss.JSON"
                full_path = os.path.join(desired_dir, file_name)
                slow_cars.append(n)
                with open(full_path, 'w') as json_file:
                    json.dump(slow_cars, json_file)
            elif 120 <= int(n['horse_power']) < 180:
                file_name = "fast_carss.JSON"
                full_path2 = os.path.join(desired_dir, file_name)
                fast_cars.append(n)
                with open(full_path2, 'w') as json_file:
                    json.dump(fast_cars, json_file )

            else:
                file_name = "sport_carss.JSON"
                full_path3 = os.path.join(desired_dir, file_name)
                sport_cars.append(n)
                with open(full_path3, 'w') as json_file:
                    json.dump(sport_cars, json_file )

#creating json files based on the price
            for i in list_of_dict:
                if int(i['price']) < 1000:
                    file_name = "cheap_carss.JSON"
                    full_path = os.path.join(desired_dir, file_name)
                    cheap_cars.append(i)
                    with open(full_path, 'w') as json_file:
                        json.dump(cheap_cars, json_file)
                elif 1000 <= int(i['price']) <= 5000:

                    file_name = "medium_price_carss.JSON"
                    full_path = os.path.join(desired_dir, file_name)
                    medium_price_cars.append(i)
                    with open(full_path, 'w') as json_file:
                        json.dump(medium_price_cars, json_file)
                else:
                    file_name = "expensive_carss.JSON"
                    full_path = os.path.join(desired_dir, file_name)
                    expensive_cars.append(i)
                    with open(full_path, 'w') as json_file:
                        json.dump(expensive_cars, json_file)

                brand_name = ""

#creating json file for each brand
            for j in list_of_dict:
                    brand_name = []
                    existing_brand = []
                    if brand_name != j['brand']:
                        filename = format(j['brand'])
                        full_path = os.path.join(desired_dir, filename)
                        brand_name.append(j)
                        with open(full_path, 'w') as json_file:
                            json.dump(brand_name, json_file)
                        existing_brand == brand_name

                    else:
                        with open(filename, 'r+') as json_file:
                            file_data = json.load(json_file)
                            file_data["brand"].append(existing_brand)
                            json.dump(file_data, json_file)


#







