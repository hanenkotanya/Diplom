#написать генератор фейковых личностей

#Ввести из командной строки натуральное число и сгенерировать в файл 'people.xlsx' #таблицу с колонками:
#Номер|Фамилия|Имя|Отчество

from russian_names import RussianNames
import openpyxl
number= input('Введите целое число: ')

def create_person(number):
    if number.isnumeric() and int(number) !=0:
        number_int=int(number)
        person=RussianNames(count=number_int,output_type='list').get_batch()
        # print(person) это добавляла для себя для наглядности
        person_list=list(person)
        # print(person_list) это добавляла для себя для наглядности
        wb = openpyxl.Workbook()
        ws = wb.active
        for i in person_list:
            ws.append(i)
        wb.save('vch.xlsx')
        print('Вы создали .xlsx таблицу')
    else:
        print('Вы ввели некорректное число')


create_person(number)

 

        

        
    

