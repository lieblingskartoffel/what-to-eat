class LikedDishes:
    @staticmethod
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
