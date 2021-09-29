import sqlite3
from restaurants import Restaurant
from liked_dishes import LikedDishes

# Main execution
con = sqlite3.connect('what-to-eat.db')
gotten_restaurants = Restaurant.get_restaurants(con)
chosen_restaurant = Restaurant.choose_random_restaurant(gotten_restaurants)
liked_dishes_for_restaurant = LikedDishes.get_liked_dishes_for_restaurant(con, chosen_restaurant[0])
print('Order from ' + chosen_restaurant[1] + ' (' + chosen_restaurant[3] + ') on '
      + chosen_restaurant[2] + '.\n' + liked_dishes_for_restaurant)
con.close()
