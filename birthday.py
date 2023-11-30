#Назовем полуднём рождения дату, когда человеку исполняется целое число лет и ещё 6 #месяцев. Если в месяце меньше дней, то полудень рождения празднуется в последний #день месяца. Например, если ДР 31 декабря, то полуДР — 30 июня, а если 29 февраля, #то 29 августа.

#Напишите программу, которая спрашивает у пользователя дату рождения через точку #(например, "31.12.2001") и определяет его полудень рождения.


import datetime
from calendar import monthrange
def cheak_date(date):
    date_is_correct=True
    if date.count('.')!=2:
        print('Необходимо ввести дату рождения через точку (день.месяц.год)')
        date_is_correct=False
    else:
        d_m_y = date.split('.')
        day_str = d_m_y[0]
        month_str = d_m_y[1]
        year_str = d_m_y[2]
        if day_str.isnumeric() and month_str.isnumeric() and year_str.isnumeric():  
            day_int = int(day_str)
            month_int= int(month_str)
            year_int= int(year_str) 
        if not day_str.isnumeric() or not month_str.isnumeric() or not year_str.isnumeric():
            date_is_correct=False
            print('Необходимо указывать только числа')
        elif len(year_str) !=4:
            date_is_correct=False
            print('Вы неправильно ввели год')
        elif month_int >12 or len(month_str)>2 or month_int ==0:
            date_is_correct=False
            print ('Вы неправильно ввели месяц')
        elif day_int> monthrange(year_int,month_int)[1] or day_int==0:
            date_is_correct=False
            print ('Вы неправильно ввели число')
    if date_is_correct==True:
        month2= month_int+6
        year2=year_int
        day2=day_int
        if month_int+6>=12:
            month2 =6-(12-month_int)
            year2= year_int+1
        number_of_days=int(monthrange(year2,month2)[1])
        if day_int>number_of_days:
            day2=number_of_days
        poly_birthday= 'Ваш полудень рождения: '+str(day2)+'.'+str(month2)+'.'+str(year2)
        return poly_birthday


print('Ваша дата рождения?')
birthday = input('Введите свою дату рождения(день.месяц.год): ')
print(cheak_date(birthday))






    
