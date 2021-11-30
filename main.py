from pprint import pprint


import os
path = os.path.join(os.getcwd(), 'recipes.txt')


with open(path, encoding="utf8") as file:
    # print(file.read())
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        count_ingr = int(file.readline().strip())
        structure = []
        for items in range(count_ingr):
            name, qantity, measure = file.readline().split(" | ")
            structure.append({'ingridient': name.strip(), 'qantity': int(qantity.strip()), 'measure': measure.strip()})
        cook_book[dish_name] = structure
        file.readline()

    print('Cook book=')
    pprint(cook_book)

    def create_order_list():
        person_count = int(input('Введите количество человек: '))
        dish_order = input('Введите название блюда: ')
        ...


    def get_shop_list_by_dishes(dishes, person_count):
        menu = cook_book
        list = {}
        try:
            for dish in dishes:
                for item in (menu[dish]):
                    count_ingr = dict[item['ingredient'], 'quantity': int(item['quantity']) * {person_count}, 'measure': item['measure']]
                    if list.get(item['ingredient_name']):


        except KeyError:
            print('Такого блюда у нас нет')
