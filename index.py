import json
import random
import sqlite3


def setup_initial_data(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE tblPerson (personName NVARCHAR(100), personId INTEGER PRIMARY KEY);''')
    cur.execute('''INSERT INTO tblPerson (personName, personId) VALUES('Caroline',1),
    ('Josh',2);''')
    cur.execute('''CREATE TABLE tblLikedDish (dishName NVARCHAR(255), restaurantId INTEGER, personId INTEGER);''')
    cur.execute('''INSERT INTO tblLikedDish (restaurantId, dishName, personId) VALUES
        (
      5,
      "Stone Pot Bibimbap",
      1
    ),
    (
      5,
      "A19. Crispy Rice Cake Skewer",
      1
    ),
    (
      3,
      "Mama Lucca Sub",
      1
    ),
    (
      3,
      "The Paulitician Sandwich",
      2
    ),
    (
      3,
      "Jumbo Chocolate Brownie",
      2
    ),
    (
      3,
      "Jumbo Smores Cookie",
      1
    ),
    (
      6,
      "Torta Asada",
      2
    ),
    (
      6,
      "Torta Asada",
      1
    ),
    (
      7,
      "Taro Puff",
      1
    ),
    (
      9,
      "Macaroni & Cheese",
      1
    ),
    (
      9,
      "Chicken & Ranch Quesadilla",
      2
    ),
    (
      9,
      "Brussels Sprouts",
      1
    ),
    (
      4,
      "Chana Paneer Masala",
      2
    ),
    (
      4,
      "Peshawari Naan",
      2
    ),
    (
      4,
      "5 Piece Vegetable Pakora",
      2
    ),
    (
      4,
      "Palak Paneer",
      1
    ),
    (
      4,
      "Naan",
      1
    ),
    (
      1,
      "Cheese Tortellone, Chicken, and Broccoli Alfredo",
      1
    ),
    (
      1,
      "Bacon, Steak, and Cheese Sandwich",
      2
    ),
    (
      10,
      "Moussaka Plate",
      1
    ),
    (
      4,
      "Lamb Biryani",
      2
    ),
    (
      2,
      "Kafta Kabob Plate",
      1
    ),
    (
      2,
      "Lamb Shawarma Plate",
      2
    ),
    (
      11,
      "Chicken and Waffles",
      1
    ),
    (
      11,
      "Shiitake Tempura Makimono",
      1
    ),
    (
      11,
      "Small Boneless Wings",
      2
    ),
    (
      8,
      "Drunken Noodle",
      2
    ),
    (
      8,
      "Pad Thai",
      1
    ),
    (
      13,
      "Katsu Don D",
      1
    ),
    (
      15,
      "Palak Paneer Pizza",
      1
    ),
    (
      15,
      "Chicken Tikka Pizza",
      2
    ),
    (
      16,
      "Qabelee",
      1
    ),
    (
      5,
      "Spicy Pork Bulgogi",
      2
    ),
    (
      5,
      "Beef Bulgogi",
      1
    );''')

    con.commit()
    return con


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
#setup_initial_data(con)
gotten_restaurants = get_restaurants(con)
gotten_restaurants = gotten_restaurants
chosen_restaurant = choose_random_restaurant(gotten_restaurants)
chosen_restaurant_name = chosen_restaurant[1]
liked_dishes_for_restaurant = get_liked_dishes_for_restaurant(con, chosen_restaurant[0])
print('Order from ' + chosen_restaurant_name + ' (' + chosen_restaurant[3] + ') on '
      + chosen_restaurant[2] + '.\n' + liked_dishes_for_restaurant)
con.close()
