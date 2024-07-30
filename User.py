class User:
    full_name = ""
    username = ""
    password = ""
    age = ""
    phone_num = ""
    id = ""

    def __init__(self, full_name, username, password, age, phone_num, id):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.age = age
        self.phone_num = phone_num
        self.id = id


current_user = User("", "", "", "", "", "")
