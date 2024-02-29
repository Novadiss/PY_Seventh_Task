with open('test.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredients_count = int(f.readline().strip())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = f.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient[0],
                'quantity': int(ingredient[1]),
                'measure': ingredient[2]
            })
        cook_book[dish_name] = ingredients
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = int(ingredient['quantity']) * person_count
            measure = ingredient['measure']
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += quantity
            else:
                shop_list[ingredient_name] = {
                    'measure': measure,
                    'quantity': quantity
                }
    return shop_list

def print_shop_list(shop_list):
    for ingredient_name, ingredient_info in shop_list.items():
        print(f'{ingredient_name}: {ingredient_info["quantity"]} {ingredient_info["measure"]}')

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()
