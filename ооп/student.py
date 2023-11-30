#Создайте класс Student, который будет иметь атрибуты name, age и grades, а также метод add_grade(), добавляющий оценку в список, метод get_average_grade(), #возвращающий среднюю оценку, и метод is_honors_student(), возвращающий True, если средний балл выше 4.5.

class Student():
    def __init__(self,name, age):
        self.name= name
        self.age = age
        self.grades =[]

    def add_grade(self, grade):
        if self:
            try: 
                self.grades.append(int(grade))
            except:
                grade=int(input('Введите оценку цифрой: '))
                self.grades.append(grade)
        return self.grades
                
        
    def get_average_grade(self):
        average_grande=sum(self.grades)/int(len(self.grades))
        return average_grande
    
    def is_honors_student(self):
        if self.get_average_grade()>4.5:
            print('True')

class1_student1=Student('vika_ivanova',21)
class1_student1.add_grade(10)
print(class1_student1.get_average_grade())
class1_student1.is_honors_student()


class1_student1.add_grade('десять')
class1_student1.get_average_grade()
class1_student1.is_honors_student()



   
    



    
