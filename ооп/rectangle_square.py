#Создайтекласс Rectangle, который будет иметь атрибуты width и height, а также методы get_area() и get_perimeter(), возвращающие площадь и периметр прямоугольника #соответственно. Реализуйте также метод is_square(), который будет возвращать True, если прямоугольник является квадратом.

class Rectangle():
    def __init__(self,width,height):
        self.width=width
        self.height=height
        if self:
            try:
                self.width=float(width)
            except:
                print('Вы ввели нечисловое значение')
                self.width=float(input('Введите значение width для объекта {self}: '))
            try:
                self.height=float(height)
            except:
                self.height=float(input('Введите значение height для объекта {self}: '))
   
    def get_area(self):
        print('Площадь фигуры равна: {:.1f}'.format(self.width*self.height))


    def get_perimeter(self):
        print('Периметр фигуры2 равен: {:.1f}'.format(2*(self.width+self.height)))


    def is_square(self):
        if self.width==self.height:
            print('True')

figure=Rectangle(2,2)
figure.get_area()
figure.is_square()

figure2=Rectangle(3,6)
figure2.get_perimeter()

figure3=Rectangle('dva',2)
figure3.is_square()




