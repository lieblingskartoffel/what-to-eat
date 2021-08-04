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


def get_liked_dishes():
    liked_dishes_file = open('liked_dishes.json')
    liked_dishes = json.load(liked_dishes_file)
    return liked_dishes


def get_liked_dishes_for_restaurant(liked_dishes, restaurant_name):
    liked_dishes_for_given_restaurant = [liked_dish for liked_dish in liked_dishes.get('liked_dishes') if liked_dish.get('restaurant_name') == restaurant_name]
    liked_dishes_string = ''
    for dish in liked_dishes_for_given_restaurant:
        liked_dishes_string += dish.get('who_liked_it') + ' liked ' + dish.get('dish_name') + '.\n'
    return liked_dishes_string


# Main execution
gotten_restaurants = get_restaurants()
gotten_restaurants = gotten_restaurants.get('restaurants')
chosen_restaurant = choose_random_restaurant(gotten_restaurants)
chosen_restaurant_name = chosen_restaurant.get('name')
liked_dishes_for_restaurant = get_liked_dishes_for_restaurant(get_liked_dishes(), chosen_restaurant_name)
print('Order from ' + chosen_restaurant_name + ' (' + chosen_restaurant.get('cuisine') + ') on '
      + chosen_restaurant.get('app') + '.\n' + liked_dishes_for_restaurant)
