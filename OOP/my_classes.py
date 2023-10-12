# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получения значений этого атрибута  нужно использовать методы get и set
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

# 5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий
