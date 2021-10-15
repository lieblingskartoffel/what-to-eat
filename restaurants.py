import random


class Restaurant:
    @staticmethod
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

    @staticmethod
    def choose_random_restaurant(restaurants):
        number_of_restaurants = len(restaurants)
        chosen_index = random.randint(0, number_of_restaurants - 1)
        return restaurants[chosen_index]
