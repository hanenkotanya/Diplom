#Создайте класс Person, который будет иметь атрибуты name и age, а также метод say_hello(), выводящий на экран строку "Привет, меня зовут <name> и мне <age> лет." #Реализуйте также метод can_vote(), который будет возвращать True, если возраст человека больше или равен 18 лет.


class Person():
    def __init__(self,name, age):
        self.name=name
        if self:
            try:
                self.age=int(age)
            except:
                print('Вы ввели не число!')
                self.age=int(input('Введите возраст: '))
        

    def say_hello(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} лет')

    def can_vote(self):
        if int(self.age)>=18:
            return True
        
i=Person('Tanya','27')
i.say_hello()
print(i.can_vote())

you=Person('Olga','двадцать')
you.say_hello()
print(you.can_vote())
