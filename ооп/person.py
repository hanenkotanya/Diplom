#Создайте класс Person, который будет иметь атрибуты name и age, а также метод say_hello(), выводящий на экран строку "Привет, меня зовут <name> и мне <age> лет.".

class Person():
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет')
i=Person('Tanya', 27)
i.say_hello()


