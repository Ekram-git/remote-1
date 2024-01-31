import random

def get_random_car_brand():
    car_brands = ["Toyota", "Honda", "Ford", "BMW", "Volkswagen", "BMW"]
    random_select = random.choice(car_brands)
    return random_select

def get_random_model_year():
    return random.randint(2000, 2022)

if __name__ == "__main__":
    random_car = get_random_car_brand()
    random_year = get_random_model_year()

    print("Randomly selected car brand:", random_car)
    print("Random model year:", random_year)
