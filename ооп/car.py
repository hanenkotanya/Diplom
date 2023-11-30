#Создайте класс Car, который будет иметь атрибуты make, model, year и speed, а также методы accelerate() и brake(), изменяющие скорость на указанную величину, и метод #get_speed(), возвращающий текущую скорость.

class Car():
    def __init__(self,model,year,speed):
        self.model=model
        self.year=year
        if self:
            try:
                self.speed=float(speed)
            except:
                print('Вы ввели не число!')
                self.speed=float(input('Введите скорость числом при создании объекта: '))
    
    def proverka(self):
        if self:
            try:
                self.speed_difference=float(input('Введите разницу скоростей: '))
            except:
                print('Вы ввели не число!')
                self.speed_difference=float(input('Введите разницу скоростей: '))   
        
                
    def accelerate(self):
        self.proverka()
        self.speed=self.speed+self.speed_difference
        print('Вы увеличили скорость на {} и теперь она {}'.format(self.speed_difference,self.speed) + 'км/ч')
        return self.speed
    
    def brake(self):
        self.proverka()
        self.speed=self.speed-self.speed_difference
        print('Вы уменьшили скорость на {} и теперь она {}'.format(self.speed_difference,self.speed) + 'км/ч')
        return self.speed
    def get_speed(self):
        print('Ваша текущая скорость {}'.format(self.speed) + 'км/ч')

peugeot=Car(307,2004,100)
peugeot.accelerate()
peugeot.brake()
peugeot.get_speed()

mercedes=Car('S-class','две тысячи четвертый','сто')
mercedes.accelerate()
mercedes.brake()
mercedes.get_speed()



