import json
import random
import sqlite3


def get_restaurants(con):
    cur = con.cursor()
    restaurants = cur.execute('''
        SELECT 
            restaurantId, restaurantName, appName, cuisineName 
        FROM 
            tblRestaurant 
        INNER JOIN tblDeliveryApp on tblRestaurant.appId = tblDeliveryApp.appId 
        INNER JOIN tblCuisine ON tblRestaurant.cuisineId = tblCuisine.cuisineId
    ''').fetchall()

    print(restaurants)
    return restaurants


def choose_random_restaurant(restaurants):
    number_of_restaurants = len(restaurants)
    chosen_index = random.randint(0, number_of_restaurants - 1)
    return restaurants[chosen_index]


def get_liked_dishes_for_restaurant(con, restaurant_id):
    cur = con.cursor()
    liked_dishes = cur.execute('''
                SELECT 
                    personName, dishName
                FROM 
                    tblLikedDish
                INNER JOIN tblPerson on tblLikedDish.personId = tblPerson.personId
                WHERE restaurantId = :restaurant_id
            ''', {"restaurant_id": restaurant_id}).fetchall()
    liked_dishes_string = ''
    for dish in liked_dishes:
        liked_dishes_string += dish[0] + ' liked ' + dish[1] + '.\n'
    return liked_dishes_string


# Main execution
con = sqlite3.connect('what-to-eat.db')
gotten_restaurants = get_restaurants(con)
gotten_restaurants = gotten_restaurants
chosen_restaurant = choose_random_restaurant(gotten_restaurants)
chosen_restaurant_name = chosen_restaurant[1]
liked_dishes_for_restaurant = get_liked_dishes_for_restaurant(con, chosen_restaurant[0])
print('Order from ' + chosen_restaurant_name + ' (' + chosen_restaurant[3] + ') on '
      + chosen_restaurant[2] + '.\n' + liked_dishes_for_restaurant)
con.close()
