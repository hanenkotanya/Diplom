#Создайте класс Dog, который будет иметь атрибуты name, breed и age, а также методы bark(), выводящий на экран строку "Гав-гав!" и метод get_human_age(), возвращающий #возраст собаки в "человеческих" годах (приблизительно).

class Dog():
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        if self:
            try:
                self.age=float(age)
            except:
                print('Вы ввели не число!')
                self.age=float(input('Введите возраст числом при создании объекта: ')) 


    def bark(self):
        print('Гав-гав!')

    def get_human_age(self):
        if self.age==0:
            print('Возраст должен быть больше 0')
        elif self.age<=2:
            print('Ваш собачий возраст: {:.2f}'.format(self.age*10.5))
        elif self.age>2:
            print('Ваш собачий возраст: {:.2f}'.format(2*10.5+(self.age-2)*4))


#каждый из первых двух лет жизни собаки приравнивается к 10,5 годам человеческой жизни, а все последующие – к четырем.
dog1=Dog('Bobik','poodle',2)
dog2=Dog('Snegok','spitz',8)
dog3=Dog('Kolbaska','dachshund',0)
dog4=Dog('Lucy','terrier','five')

dog1.bark()
dog4.bark()
dog1.get_human_age()
dog2.get_human_age()
dog3.get_human_age()
dog4.get_human_age()
