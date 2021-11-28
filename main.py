from pprint import pprint
import os

path = os.path.join(os.getcwd(), 'recipes.txt')

with open(path, encoding="utf8") as cookbook:
    # print(file.read())
    result = {}
    for dish in cookbook:
        dish_name = dish.strip()
        count_ingr = int(cookbook.readline().strip())
        structure = []
        for items in range(count_ingr):
            name, qantity, measure = cookbook.readline().split(" | ")
            structure.append({'ingridient': name.strip(), 'qantity': int(qantity.strip()), 'measure': measure.strip()})
        result[dish_name] = structure
        cookbook.readline()
    pprint(result)

