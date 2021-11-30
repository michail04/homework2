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
            structure.append({'ingredient': name.strip(), 'qantity': int(qantity.strip()), 'measure': measure.strip()})
        cook_book[dish_name] = structure
        file.readline()
    print('Cook book=')
    pprint(cook_book)
    # что то я опять сделал не так...

    def get_shop_list_by_dishes(dishes, person_count):
        person_count = int(input(f'\n Enter the guests count, please: '))
        # dish_order = input('Enter what would u like to meal today: ')
        menu = cook_book
        list = {}

        for dish in dishes:
            for ingr in (menu[dish]):
                count_dish_name_ingr = dict[ingr['ingredient'], {'measure': ingr['measure'], 'quantity': int(ingr['quantity']) * person_count}]
                if list.get(ingr['ingredient']):
                    more_ingr = (list['ingredient']['quantity']) + (count_dish_name_ingr['ingredient']['quantity'])
                else:
                    list.update(count_dish_name_ingr)

        print(f"For dishes for {person_count} guests you need:")
        pprint(list)
        # что-то я опять понаписал не так...

