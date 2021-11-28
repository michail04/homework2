import os
path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path) as file:
    file = open('recipes.txt', encoding="utf8")
    # print(file.read())
    result = {}
    for dish in file:
        dish_name = dish.strip()
        count_ingr = int(file.readline().strip())
        for items in range(count_ingr):
            structure = []
            name, qantity, unit = file.readline().split('|')
            structure.append({'name': name, 'qantity': qantity, 'unit': unit})
        result = dish_name, structure
        file.readline()
        print(result)

