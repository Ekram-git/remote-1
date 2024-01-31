import random

def get_random_car_brand():
    car_brands = ["Toyota", "Honda", "Ford", "BMW", "Volkswagen", "BMW"]
    random_select = random.choice(car_brands)
    return random_select


if __name__ == "__main__":
    random_car = get_random_car_brand()
    print("Randomly selected car brand:", random_car)

