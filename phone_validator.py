#написать валидатор номера телефона с его использованием

def main():
    phone_number = input('Введите номер в формате +код страны(код города)номер телефона: ')
    match phone_number:
        case str() as phone_number if phone_number[0] == '+' and phone_number.count('(') == 1 and phone_number.count(')') == 1:
            phone_number = phone_number.strip('+')
        case _:
            print('Вы ввели неправильный формат номера либо это не номер')
            return
        
    phone_number_split = phone_number.split('(')
    phone_number_split_split = phone_number_split[1].split(')')
    city_code = phone_number_split_split[0]
    local_phone = phone_number_split_split[1]
    country_code = phone_number_split[0]
    proverka = (country_code, city_code, local_phone)

    match proverka:
        case (country_code, city_code, local_phone) if len(country_code)<1:
            print('проверка 1')
        case (country_code, city_code, local_phone) if country_code[0]=='1' and len(country_code)>4 or country_code[0]!='1' and len(country_code)>3:
            print('проверка 2')
        case (country_code, city_code, local_phone) if country_code=='375' and len(city_code)+len(local_phone)!=9:
            print('проверка 3')
        case (country_code, city_code, local_phone) if city_code.isnumeric() and country_code.isnumeric() and local_phone.isnumeric() == True:
            print('Все гуд')
        case _:
            print('проверка 4')
       
        

if __name__== '__main__':
    main()
