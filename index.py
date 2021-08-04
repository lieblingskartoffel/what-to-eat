import json
import random


def get_restaurants():
    restaurant_file = open('food.json')
    restaurants = json.load(restaurant_file)
    return restaurants


def choose_random_restaurant(restaurants):
    number_of_restaurants = len(restaurants)
    chosen_index = random.randint(0, number_of_restaurants - 1)
    return restaurants[chosen_index]


# Main execution
gotten_restaurants = get_restaurants()
gotten_restaurants = gotten_restaurants.get('restaurants')
chosen_restaurant = choose_random_restaurant(gotten_restaurants)
print('Order from ' + chosen_restaurant.get('name') + ' (' + chosen_restaurant.get('cuisine') + ') on '
      + chosen_restaurant.get('app'))
