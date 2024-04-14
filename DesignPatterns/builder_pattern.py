

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print('======= DETAILS =======')
        print(self.name)
        print(self.age)


class UserBuilder:

    def __init__(self):
        self.name=None
        self.age=0

    def build_name(self, name):
        self.name=name
        return self
    
    def build_age(self, age):
        self.age=age
        return self
    
    def build(self):
        return User(
            self.name,
            self.age
        )


user_instance = UserBuilder().build_name('hardik').build_age(23).build()

user_instance.printDetails()
