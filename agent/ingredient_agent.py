def get_ingredients(food_name):

    ingredients = {

       # WEIGHT GAIN VEGETARIAN

"Oats + Banana + Peanut Butter": ["Oats", "Banana", "Peanut Butter"],
"Milk + Dates + Oats": ["Milk", "Dates", "Oats"],
"Rice + Dal + Paneer": ["Rice", "Toor Dal", "Paneer"],
"Milk + Mixed Nuts": ["Milk", "Almonds", "Cashews", "Walnuts"],
"Rice + Rajma": ["Rice", "Rajma", "Onion", "Tomato"],
"Banana Shake": ["Banana", "Milk", "Honey"],
"Paneer Wrap": ["Paneer", "Wheat Roti", "Onion", "Capsicum"],
"Vegetable Sandwich": ["Bread", "Tomato", "Cucumber", "Carrot"],
"Rice + Soya Chunks": ["Rice", "Soya Chunks", "Onion", "Tomato"],
"Peanuts": ["Peanuts"],
"Chapati + Dal": ["Wheat Flour", "Toor Dal", "Onion", "Tomato"],
"Paneer Fried Rice": ["Rice", "Paneer", "Carrot", "Beans"],
"Fruit Smoothie": ["Banana", "Apple", "Milk"],
"Banana Smoothie": ["Banana", "Milk"],
"Rice + Chole": ["Rice", "Chickpeas", "Onion", "Tomato"],
"Mixed Nuts": ["Almonds", "Cashews", "Walnuts"],
"Peanut Butter Toast": ["Bread", "Peanut Butter"],
"Rice + Dal": ["Rice", "Toor Dal"],
"Milk + Almonds": ["Milk", "Almonds"],
"Soya Curry": ["Soya Chunks", "Onion", "Tomato"],
"Oats + Fruits": ["Oats", "Apple", "Banana"],
"Paneer Biryani": ["Rice", "Paneer", "Onion", "Tomato", "Spices"],
"Fruit Shake": ["Banana", "Apple", "Milk"],
"Greek Yogurt Bowl": ["Greek Yogurt", "Banana", "Honey"],
"Protein Shake": ["Milk", "Protein Powder", "Banana"],
"Paneer Salad": ["Paneer", "Lettuce", "Tomato", "Cucumber"],
"Veg Fried Rice": ["Rice", "Carrot", "Beans", "Capsicum"],
"Veg Pulao": ["Rice", "Carrot", "Beans", "Peas"],
"Tofu Stir Fry": ["Tofu", "Capsicum", "Onion", "Carrot"],
"Mushroom Rice": ["Rice", "Mushroom", "Onion"],
"Veg Wrap": ["Wheat Roti", "Paneer", "Capsicum", "Carrot"],

# WEIGHT GAIN NON-VEG

"Egg Omelette": ["Eggs", "Onion", "Pepper"],
"Rice + Chicken Curry": ["Rice", "Chicken", "Onion", "Tomato", "Spices"],
"Rice + Egg Curry": ["Rice", "Eggs", "Onion", "Tomato"],
"Rice + Fish Curry": ["Rice", "Fish", "Onion", "Tomato"],
"Chicken Sandwich": ["Bread", "Chicken", "Onion", "Mayonnaise"],
"Boiled Eggs": ["Eggs"],
"Chicken Soup": ["Chicken", "Garlic", "Pepper", "Onion"],
"Chicken Wrap": ["Wheat Roti", "Chicken", "Onion", "Capsicum"],
"Grilled Chicken": ["Chicken Breast", "Pepper", "Lemon"],
"Chicken Fried Rice": ["Rice", "Chicken", "Carrot", "Beans"],
"Chicken Biryani": ["Rice", "Chicken", "Onion", "Tomato", "Spices"],
"Fish Rice": ["Rice", "Fish", "Onion", "Tomato"],
"Tuna Sandwich": ["Bread", "Tuna", "Lettuce"],
"Scrambled Eggs": ["Eggs", "Butter", "Pepper"],
"Egg Sandwich": ["Bread", "Eggs", "Onion"],
"Boiled Chicken": ["Chicken", "Pepper", "Salt"],

# WEIGHT LOSS VEGETARIAN

"Oats + Milk": ["Oats", "Milk"],
"Brown Rice + Dal": ["Brown Rice", "Toor Dal"],
"Fruit Bowl": ["Banana", "Apple", "Papaya"],
"Green Salad": ["Lettuce", "Tomato", "Cucumber"],
"Veg Soup": ["Carrot", "Beans", "Cabbage"],
"Sprouts Salad": ["Sprouts", "Tomato", "Onion"],
"Apple + Almonds": ["Apple", "Almonds"],
"Vegetable Stir Fry": ["Carrot", "Beans", "Capsicum"],
"Low Fat Yogurt": ["Curd"],
"Whole Wheat Toast": ["Whole Wheat Bread"],

# WEIGHT LOSS NON-VEG

"Egg White Omelette": ["Egg Whites", "Onion", "Pepper"],
"Chicken Salad": ["Chicken Breast", "Lettuce", "Tomato", "Cucumber"],
"Grilled Fish": ["Fish", "Pepper", "Lemon"],
"Tuna Salad": ["Tuna", "Lettuce", "Tomato", "Cucumber"],
"Brown Rice + Chicken": ["Brown Rice", "Chicken"],
"Brown Rice + Fish": ["Brown Rice", "Fish"],
"Boiled Egg": ["Eggs"],
"Chicken Clear Soup": ["Chicken", "Pepper", "Garlic"],

# MAINTENANCE

"Chapati + Paneer": ["Wheat Flour", "Paneer"],
"Chapati + Paneer Curry": ["Wheat Flour", "Paneer", "Onion", "Tomato", "Spices"],
"Almond Milk": ["Almonds", "Milk"],
"Dry Fruits": ["Almonds", "Cashews", "Raisins"],
"Rice + Vegetables": ["Rice", "Carrot", "Beans", "Peas"],
"Paneer Sandwich": ["Bread", "Paneer", "Tomato"],
"Milk + Banana": ["Milk", "Banana"],
"Vegetable Rice": ["Rice", "Carrot", "Beans", "Peas"]

,
"Oats + Apple": [
    "Oats",
    "Apple"
],

"Salad + Paneer": [
    "Paneer",
    "Lettuce",
    "Tomato",
    "Cucumber"
],

"Green Tea": [
    "Green Tea Leaves",
    "Water"
],

"Fruit": [
    "Apple"
],

"Soup": [
    "Carrot",
    "Beans",
    "Cabbage"
],

"Vegetable Bowl": [
    "Carrot",
    "Beans",
    "Capsicum",
    "Broccoli"
],

"Vegetable Salad": [
    "Lettuce",
    "Tomato",
    "Cucumber"
],

"Brown Rice + Vegetables": [
    "Brown Rice",
    "Carrot",
    "Beans",
    "Peas"
],

"Almonds": [
    "Almonds"
],

"Apple + Oats": [
    "Apple",
    "Oats"
],

"Chapati + Chicken": [
    "Wheat Flour",
    "Chicken",
    "Onion",
    "Tomato"
],

"Egg Omelette + Toast": [
    "Eggs",
    "Bread",
    "Onion",
    "Pepper"
],

"Rice + Fish": [
    "Rice",
    "Fish",
    "Onion",
    "Tomato"
],

"Milk + Egg": [
    "Milk",
    "Eggs"
],

"Rice + Chicken": [
    "Rice",
    "Chicken",
    "Onion",
    "Tomato"
],

"Chicken Curry": [
    "Chicken",
    "Onion",
    "Tomato",
    "Spices"
],

"Egg Curry": [
    "Eggs",
    "Onion",
    "Tomato",
    "Spices"
],

"Egg Toast": [
    "Eggs",
    "Bread"
],

"Pancakes + Egg": [
    "Flour",
    "Eggs",
    "Milk"
],

"Grilled Chicken + Salad": [
    "Chicken Breast",
    "Lettuce",
    "Tomato",
    "Cucumber"
],

"Fish + Vegetables": [
    "Fish",
    "Carrot",
    "Beans",
    "Capsicum"
],

"Fish Salad": [
    "Fish",
    "Lettuce",
    "Tomato",
    "Cucumber"
],

"Vegetables": [
    "Carrot",
    "Beans",
    "Capsicum"
],

"Milk + Oats": [
    "Milk",
    "Oats"
],

"Egg + Toast": [
    "Eggs",
    "Bread"
],

"Nuts": [
    "Almonds",
    "Cashews",
    "Walnuts"
],

"Smoothie": [
    "Banana",
    "Apple",
    "Milk"
],

"Oats + Banana": [
    "Oats",
    "Banana"
],

"Rice + Sambar": [
    "Rice",
    "Toor Dal",
    "Onion",
    "Tomato"
],

"Milk + Cornflakes": [
    "Milk",
    "Cornflakes"
],

"Fruit Juice": [
    "Orange",
    "Apple"
],

"Chapati + Egg Curry": [
    "Wheat Flour",
    "Eggs",
    "Onion",
    "Tomato"
],

"Vegetable Biryani": [
    "Rice",
    "Carrot",
    "Beans",
    "Peas",
    "Spices"
],

"Soup + Salad": [
    "Carrot",
    "Beans",
    "Cabbage",
    "Lettuce",
    "Tomato",
    "Cucumber"
],

"Chapati + Vegetables": [
    "Wheat Flour",
    "Carrot",
    "Beans",
    "Capsicum"
],

"Egg": ["Eggs"],
"Milk": ["Milk"],
"Fish": ["Fish"],
"Peanut Butter": ["Peanuts"]
    }

    return ingredients.get(
        food_name,
        ["Ingredients Not Available"]
    )