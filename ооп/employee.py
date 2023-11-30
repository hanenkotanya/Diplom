#Создайте класс Employee, который будет иметь атрибуты name, position и salary, а также методы get_salary(), возвращающий зарплату работника, и get_tax(), возвращающий #сумму налога на зарплату (20% от зарплаты).

class Employee():
    def __init__(self, name, position, salary):
        self.name=name
        self.position=position
        if self:
            try:
                self.salary=float(salary)
            except:
                print('Зарплата должна быть введена числом')
                salary=input('Введите зарплату: ')
                self.salary=float(salary)
    def get_salary(self):
        return self.salary
    def get_tax(self):
        return self.salary*0.2
    
employee=Employee('Ivan','intern',600)
print(employee.get_salary())
print(employee.get_tax())
employee1=Employee('Maria','intern','шестьсот')
print(employee1.get_salary())
print(employee1.get_tax())
