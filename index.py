import sqlite3
from restaurants import Restaurant


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
gotten_restaurants = Restaurant.get_restaurants(con)
chosen_restaurant = Restaurant.choose_random_restaurant(gotten_restaurants)
liked_dishes_for_restaurant = get_liked_dishes_for_restaurant(con, chosen_restaurant[0])
print('Order from ' + chosen_restaurant[1] + ' (' + chosen_restaurant[3] + ') on '
      + chosen_restaurant[2] + '.\n' + liked_dishes_for_restaurant)
con.close()
