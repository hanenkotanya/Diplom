#Создайте класс BankAccount, который будет иметь атрибуты balance и interest_rate, а также методы deposit() и withdraw(), изменяющие баланс на указанную сумму, и метод #add_interest(), добавляющий проценты к балансу. Реализуйте также метод is_negative(), который будет возвращать True, если баланс отрицательный.

class BankAccount():
    def __init__(self,balance, interest_rate):
        self.balance=balance
        self.interest_rate=interest_rate
        if self:
            try:
                self.balance=float(balance)
            except:
                print('Вы ввели не число!')
                self.balance=float(input('Введите баланс: '))
        if self:
            try:
                self.interest_rate = float(interest_rate)
            except:
                print('Вы ввели не число!')
                self.interest_rate=float(input('Введите процент: '))

    def deposit(self):
        if self:
            try:
                self.many=float(input('Введите сумму пополнения числом: '))
            except:
                print('Вы ввели не число!')
                self.many=float(input('Введите сумму пополнения числом: '))
        self.balance=self.balance+self.many
        print('Баланс пополнился и составляет теперь: ' + str(self.balance))
        return self.balance

    def withdraw(self):
        if self:
            try:
                self.many=float(input('Введите сумму списания числом: '))
            except:
                print('Вы ввели не число!')
                self.many=float(input('Введите сумму списания числом: '))
        self.balance=self.balance-self.many
        print('Сумма списалась и баланс составляет теперь: ' + str(self.balance))
        return self.balance

    def add_interest(self):
        if self.balance>0:
            self.balance=self.balance+self.balance*(self.interest_rate/100)
            print('Проценты добавлены к балансу, баланс составляет: '+ str(self.balance))
            return self.balance
        else:
            pass #проценты от чего добавлять если баланс отрицательный?
        
    
    def is_negative(self):
        if self.balance<0:
            return True  
        else:
            return False      

person =BankAccount(1000,5)

person.deposit()
person.withdraw()
person.add_interest()
print(person.is_negative())

person2 =BankAccount(1,5)

person2.withdraw()
person2.add_interest()
print(person2.is_negative())
