class Person:
    __id =123
    name = ''
    age = 0
    def __init__(self,name, age):
        self.name= name
        self.age=age
        self.__id=123
    def __get_id(self):
        return self.__id


class User(Person):
    def __init__(self, pas):
        __
