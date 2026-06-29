def generate_grocery_list(plan, ingredients):

    grocery_items = []

    for day in ingredients:

        for meal in ingredients[day]:

            grocery_items.extend(
                ingredients[day][meal]
            )

    grocery_items = list(set(grocery_items))

    return sorted(grocery_items)