
class User:

    def __init__(self, username='', password=''):
        self.username = username
        self.password = password

    @staticmethod
    def json_parse(json):
        user = User()
        user.username = json['username']
        user.password = json['password']
        return user

