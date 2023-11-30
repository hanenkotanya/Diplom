#Создайте класс BankAccount, который будет иметь атрибуты balance и interest_rate, а также методы deposit() и withdraw(), изменяющие баланс на указанную сумму, и метод #add_interest(), добавляющий проценты к балансу.

class BankAccount():
    def __init__(self,balance, interest_rate):
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
    def proverka(self):
        if self:
            try:
                self.many=float(input('Введите сумму транзакции числом: '))
                return self.many
            except:
                print('Вы ввели не число!')
                self.many=float(input('Введите сумму транзакции числом: '))

    def deposit(self):
        print('Ваш баланс сейчас: {:.2f}'.format(self.balance))
        self.proverka()
        self.balance=self.balance+self.many
        print('Баланс пополнился и составляет теперь: {:.2f}'.format(self.balance))
        return self.balance

    def withdraw(self):
        print('Ваш баланс сейчас: {:.2f}'.format(self.balance))
        self.proverka()
        self.balance=self.balance-self.many
        print('Сумма списалась и баланс составляет теперь: {:.2f}'.format(self.balance))
        return self.balance

    def add_interest(self):
        if self.balance>0:
            print('Ваш баланс сейчас: {:.2f}'.format(self.balance))
            self.balance=self.balance+self.balance*(self.interest_rate/100)
            print('Проценты добавлены к балансу, баланс составляет: {:.2f}'.format(self.balance))
            return self.balance
        

person =BankAccount(1000,5)
person.deposit()
person.withdraw()
person.add_interest()

person2 =BankAccount('сто',5)
person2.deposit()

person3 =BankAccount(200,'пять')
person3.deposit()
