import json
import random
import sqlite3


def setup_initial_data(con):
    cur = con.cursor()
    cur.execute('''CREATE TABLE tblCuisine (cuisineName NVARCHAR(100), cuisineId INTEGER PRIMARY KEY);''')
    cur.execute('''INSERT INTO tblCuisine (cuisineName, cuisineId) VALUES('Italian',1),
    ('Mediterranean',2),
    ('Indian',3),
    ('Korean',4),
    ('Mexican',5),
    ('Thai',6),
    ('American',7),
    ('Greek',8),
    ('Japanese',9),
    ('Afghan',10),
    ('Tibetan',11),
    ('Deli',12),
    ('Chinese',13);''')
    cur.execute('''CREATE TABLE tblDeliveryApp (appName NVARCHAR(100), appId INTEGER PRIMARY KEY);''');
    cur.execute('''INSERT INTO tblDeliveryApp (appName, appId) VALUES('GrubHub',1),('DoorDash',2)''');
    cur.execute('''CREATE TABLE tblRestaurant (restaurantId INTEGER PRIMARY KEY, restaurantName NVARCHAR(100), appId INTEGER, cuisineId INTEGER);''')
    cur.execute('''INSERT INTO tblRestaurant (restaurantId, restaurantName, appId, cuisineId) VALUES(1,'Bob''s',1,1),
    (2,'PitaCambridge',1,2),
    (3,'Pauli''s',2,1),
    (4,'ShanAPunjab',1,3),
    (5,'Seoul',1,4),
    (6,'Tenoch',1,5),
    (7,'LemonThai',1,6),
    (8,'9Zaab',1,6),
    (9,'730TavernKitchenandPatio',1,7),
    (10,'GreekCorner',1,8),
    (11,'Crave',1,9),
    (12,'CitySlickerCafe',1,7),
    (13,'EbiSushi',1,9),
    (14,'Cinderella''s',1,1),
    (15,'HimalayanKitchen',1,3),
    (16,'Helmand',1,10),
    (17,'Avellino''s',1,1),
    (18,'OneRamenandSushi',1,9),
    (19,'MomoNCurry',1,3),
    (20,'Santouka',1,9),
    (21,'SweetRice',1,9),
    (22,'MojoRamen',1,9),
    (23,'TheHalalGuys',2,2),
    (24,'TheSmokeShop',2,7),
    (25,'TheCheesecakeFactory',2,7),
    (26,'ThePaintedBurro',2,5),
    (27,'Zaftigs',2,12),
    (28,'MainelyBurgers',2,7),
    (29,'DumplingHouse',2,13);''')

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
con = sqlite3.connect('what-to-eat.db')
# setup_initial_data(con)
gotten_restaurants = get_restaurants(con)
gotten_restaurants = gotten_restaurants
chosen_restaurant = choose_random_restaurant(gotten_restaurants)
chosen_restaurant_name = chosen_restaurant[1]
# liked_dishes_for_restaurant = get_liked_dishes_for_restaurant(get_liked_dishes(), chosen_restaurant_name)
print('Order from ' + chosen_restaurant_name + ' (' + chosen_restaurant[3] + ') on '
      + chosen_restaurant[2] + '.\n') #+ liked_dishes_for_restaurant)
