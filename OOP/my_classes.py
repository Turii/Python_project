
class People:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > - 0:
            self.__age = age
        else:
            print("Age can't be negative")


class Animal:
    pass


cat =Animal()
cat.name = "Mario"
cat.age = 4

