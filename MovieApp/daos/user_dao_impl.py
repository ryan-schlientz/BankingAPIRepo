

from models.user import User
from util.db_connection import connection


class UserDAOImpl:

    @staticmethod
    def get_user(user: User):
        sql = "SELECT * FROM users WHERE username = '" + user.username + "' and password = '" + user.password + "'"

        cursor = connection.cursor()
        cursor.execute(sql)

        connection.commit()

        # records = cursor.fetchall()
        #
        # user_list = []
        #
        # for record in records:
        #     user = User(record[0], record[1])
        #
        #     user_list.append(user.__dict__)
        #
        # return user_list

        record = cursor.fetchone()

        user = User(record[0], record[1])

        return user.__dict__

