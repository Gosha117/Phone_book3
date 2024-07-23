    
# Телефонная книжка


def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('file1.txt')
    
    while (choice!=9):

        if choice==1:
            print_phone_book(phone_book)
            
            
        elif choice==2:
            last_name=input('Введите фамилию: ')
            search_and_print_by_lastname(phone_book,last_name)
            
            
        elif choice==3:
            number=input('Введите номер телефона: ')
            search_and_print_by_phone(phone_book,number)
                     
            
        elif choice==4:  
            count = 0
            print('Добавление нового абонента')
            last_name = input('Введите фамилию: ')
            results = [entry for entry in phone_book if entry.get('Фамилия', '').strip() == last_name.strip()]
            if results:
                print("Абоненты с такой фамилией: ")
                print(search_and_print_by_lastname(phone_book,last_name))
                count = int(input('Для добавления абонента нажмите 1: '))
                if count != 1:
                    continue  
            name = input('Введите имя: ')
            number = input('Введите номер телефона: ')
            description = input('Введите описание абонента: ')
            print(add_entry(phone_book, last_name, name, number, description)) 
            write_txt('file1.txt', phone_book)           
          
              
        elif choice==5:
            last_name=input('Введите фамилию: ')
            count = 0
            for entry in phone_book:
                if entry.get('Фамилия', '').strip() == last_name.strip():
                    count += 1   
            print(search_and_print_by_lastname(phone_book,last_name))
            if count != 0:
                name = input('Введите имя: ')           
                number = input('Введите номер телефона: ')
                description = input('Введите описание абонента: ')
                new_data = {'Телефон' : number, 'Описание' : description}
                change_entry(phone_book, last_name, name, new_data)
                print_phone_book(phone_book)
                write_txt('file1.txt',phone_book)

                                         
        elif choice==6:
            last_name=input('Введите фамилию: ')
            results = [entry for entry in phone_book if entry.get('Фамилия', '').strip() == last_name.strip()]
            if results:
                print("Абоненты с такой фамилией: ")
                print(search_and_print_by_lastname(phone_book,last_name)) 
                name = input('Введите имя: ')
                del_rec(phone_book, last_name, name)
                print("Запись удалена")
                # print_phone_book(phone_book)
                write_txt('file1.txt',phone_book)
            else:
                print("Абонента с такой фамилией нет") 
                
                
        elif choice==7:
            phone_book = sort_phone_book(phone_book)
            print_phone_book(phone_book)
            
            
        elif choice==8:
            last_name=input('Введите фамилию: ')
            # print(search_and_print_by_lastname(phone_book,last_name))   
            contact_to_copy = search_and_print_by_lastname(phone_book,last_name)
            # print(contact_to_copy)
            if contact_to_copy:
                write_contact_to_file(contact_to_copy, 'new_phone_book.txt')
                print("Контакт записан.")
            else:
                print("Контакт не найден.")  
                
                        
        elif choice==9:
            print('Завершение работы')
            break
            
        choice=show_menu()
        

def show_menu():
    while True:
        print("\n Выберите действие:\n"
              "1. Отобразить весь справочник\n"
              "2. Найти абонента по фамилии\n"
              "3. Найти абонента по номеру телефона\n"
              "4. Добавить абонента в справочник\n"
              "5. Изменить данные\n"
              "6. Удалить запись из справочника\n"
              "7. Сортировка по фамилии\n"
              "8. Записать контракт в другой файл\n"
              "9. Закончить работу")
        try:
            choice = int(input())
            if 1 <= choice <= 9:
                return choice
            else:
                print("Пожалуйста, введите число от 1 до 9.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")


def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            line = line.strip()  # Удаляем начальные и конечные пробелы
            if line:  # Проверяем, что строка не пустая
                record = dict(zip(fields, line.split(',')))  # Создаем запись словаря
                phone_book.append(record)  # Добавляем запись в телефонную книгу

    return phone_book

       
# Поиск по фамилии        
def search_and_print_by_lastname(phone_book, last_name):
    results = [entry for entry in phone_book if entry.get('Фамилия', '').strip() == last_name.strip()]
    if not results:
        print(f"Абонент с фамилией '{last_name}' не найден.")
    else:
        print_phone_book(results)
    return results

              
# Поиск по номеру телефона        
def search_and_print_by_phone(phone_book, phone_number):
    results = [entry for entry in phone_book if entry.get('Телефон', '').strip() == phone_number.strip()]
    if not results:
        print(f"Абонент с номером телефона '{phone_number}' не найден.")
    else:
        print_phone_book(results)


# Добавление новой записи
def add_entry(phone_book, last_name, first_name, phone_number, description):
    new_entry = {
        'Фамилия': last_name,
        'Имя': first_name,
        'Телефон': phone_number,
        'Описание': description
    }
    phone_book.append(new_entry)   
    print("\nДобавлена новая запись:")
    print("Фамилия".ljust(20) + "Имя".ljust(10) + "Телефон".ljust(10) + "Описание")
    print("=" * 65)
    print(new_entry['Фамилия'].ljust(20) + new_entry['Имя'].ljust(10) + new_entry['Телефон'].ljust(10) + new_entry['Описание'].strip())    


# Измение записи
def change_entry(phone_book, last_name, first_name, new_data):
    for entry in phone_book:
        if entry.get('Фамилия', '').strip() == last_name.strip() and entry.get('Имя', '').strip() == first_name.strip():
            for key, value in new_data.items():
                entry[key] = value.strip()
            return True
    return False


# Удаление записи из справочника
def del_rec(phone_book, last_name, name):
    for i, entry in enumerate(phone_book):
        if entry.get('Фамилия', '').strip() == last_name.strip() and entry.get('Имя', '').strip() == name.strip():
            deleted_entry = phone_book.pop(i)
            return deleted_entry
    return None


# Печать справочника
def print_phone_book(phone_book):
    headers = ["N", "Фамилия", "Имя", "Телефон", "Описание"]
    col_widths = [3, 28, 15, 15, 40]  # Увеличены размеры столбцов для улучшения читаемости
    
    header_row = ''.join(header.ljust(width) for header, width in zip(headers, col_widths))
    print(header_row)
    print("=" * sum(col_widths))
    
    for i, entry in enumerate(phone_book, start=1):
        row = ''.join(entry.get(header, '').strip().ljust(width) for header, width in zip(headers[1:], col_widths[1:]))
        print(f"{str(i).ljust(col_widths[0])}. {row}")


# Чтение файла
def read_and_clean_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        # Удаляем пустые строки и строки, состоящие только из пробелов
        cleaned_lines = [line.strip() for line in lines if line.strip()]
    return cleaned_lines


# Сортировка книжки
def sort_phone_book(phone_book, sort_key='Фамилия'):
    return sorted(phone_book, key=lambda x: x.get(sort_key, '').strip())
    
    
# Запись контакта в файл
def write_contact_to_file(contact, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        for entry in contact:
            contact_str = ', '.join(f'{key}: {value}' for key, value in entry.items())
            file.write(contact_str + '\n') 
               
    
# Запись справочника в файл  
def write_txt(filename, phone_book):
    # clean_phone_book(phone_book)
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')


work_with_phonebook()        