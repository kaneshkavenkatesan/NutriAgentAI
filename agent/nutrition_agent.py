from agent.ingredient_agent import get_ingredients
def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return round(bmi, 2)


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_calories(weight, height, age, gender, goal):

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    maintenance = int(bmr * 1.55)

    if goal == "Weight Gain":
        return maintenance + 400

    elif goal == "Weight Loss":
        return maintenance - 500

    else:
        return maintenance


def get_recommendation(goal):
    if goal == "Weight Gain":
        return "Increase calorie intake and consume protein-rich foods."
    elif goal == "Weight Loss":
        return "Maintain a calorie deficit and increase physical activity."
    else:
        return "Maintain a balanced diet and healthy lifestyle."


def health_score(bmi):
    if bmi < 18.5:
        return 60
    elif bmi < 25:
        return 90
    elif bmi < 30:
        return 70
    else:
        return 50


def meal_plan(goal, food_preference, allergies):
   

    peanut_item = "Peanut Butter"
    milk_item = "Milk"
    egg_item = "Eggs"
    fish_item = "Fish Curry"

    if "Peanut" in allergies:
        peanut_item = "Almond Butter"

    if "Milk" in allergies:
        milk_item = "Soy Milk"

    if "Egg" in allergies:
        egg_item = "Tofu"

    if "Fish" in allergies:
        fish_item = "Paneer Curry"

    # Your Weight Gain, Weight Loss and Maintenance plans come below

    # WEIGHT GAIN - VEGETARIAN

    if goal == "Weight Gain" and food_preference == "Vegetarian":

        return {

            "Monday": {
                "Breakfast": f"Oats + Banana + {peanut_item}",
                "Lunch": "Rice + Dal + Paneer",
                "Snack": f"{milk_item} + Mixed Nuts",
                "Dinner": "Chapati + Paneer Curry"
            },

            "Tuesday": {
                "Breakfast": f"{milk_item} + Dates + Oats",
                "Lunch": "Rice + Rajma",
                "Snack": "Banana Shake",
                "Dinner": "Paneer Wrap"
            },

            "Wednesday": {
                "Breakfast": "Vegetable Sandwich",
                "Lunch": "Rice + Soya Chunks",
                "Snack": "Peanuts",
                "Dinner": "Chapati + Dal"
            },

            "Thursday": {
                "Breakfast": f"Oats + {milk_item}",
                "Lunch": "Paneer Fried Rice",
                "Snack": "Fruit Smoothie",
                "Dinner": "Chapati + Paneer"
            },

            "Friday": {
                "Breakfast": "Banana Smoothie",
                "Lunch": "Rice + Chole",
                "Snack": "Mixed Nuts",
                "Dinner": "Paneer Curry"
            },

            "Saturday": {
                "Breakfast": f"{peanut_item} Toast",
                "Lunch": "Rice + Dal",
                "Snack": f"{milk_item} + Almonds",
                "Dinner": "Soya Curry"
            },

            "Sunday": {
                "Breakfast": "Oats + Fruits",
                "Lunch": "Paneer Biryani",
                "Snack": "Fruit Shake",
                "Dinner": "Chapati + Dal"
            }
        }

    # WEIGHT GAIN - NON VEGETARIAN

    elif goal == "Weight Gain" and food_preference == "Non-Vegetarian":

        return {

            "Monday": {
                "Breakfast": f"{egg_item} + {milk_item} + Banana",
                "Lunch": "Rice + Chicken Curry",
                "Snack": "Protein Shake",
                "Dinner": "Chapati + Chicken"
            },

            "Tuesday": {
                "Breakfast": f"{egg_item} Omelette + Toast",
                "Lunch": f"Rice + {fish_item}",
                "Snack": "Banana Shake",
                "Dinner": "Chicken Wrap"
            },


            "Wednesday": {
                "Breakfast": f"{egg_item} Sandwich",
                "Lunch": "Chicken Biryani",
                "Snack": "Mixed Nuts",
                "Dinner": f"Rice + {egg_item} Curry"
            },

            "Thursday": {
                "Breakfast": f"{milk_item} + {egg_item}",
                "Lunch": "Rice + Chicken",
                "Snack": "Protein Shake",
                "Dinner": fish_item
            },

            "Friday": {
                "Breakfast": "Banana Smoothie",
                "Lunch": f"Rice + {fish_item}",
                "Snack": peanut_item,
                "Dinner": "Chicken Curry"
            },

            "Saturday": {
                "Breakfast": f"{egg_item} Toast",
                "Lunch": "Chicken Fried Rice",
                "Snack": f"{milk_item} + Nuts",
                "Dinner": f"Rice + {fish_item}"
            },

            "Sunday": {
                "Breakfast": f"Pancakes + {egg_item}",
                "Lunch": "Chicken Biryani",
                "Snack": "Protein Shake",
                "Dinner": f"{egg_item} Curry"
            }
        }

    # WEIGHT LOSS - VEGETARIAN

    elif goal == "Weight Loss" and food_preference == "Vegetarian":

        return {

            "Monday": {
                "Breakfast": "Oats + Apple",
                "Lunch": "Salad + Paneer",
                "Snack": "Green Tea",
                "Dinner": "Vegetable Soup"
            },

            "Tuesday": {
                "Breakfast": "Fruit Bowl",
                "Lunch": "Brown Rice + Vegetables",
                "Snack": "Almonds",
                "Dinner": "Paneer Salad"
            },

            "Wednesday": {
                "Breakfast": "Oats",
                "Lunch": "Vegetable Salad",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            },

            "Thursday": {
                "Breakfast": "Apple + Oats",
                "Lunch": "Brown Rice + Dal",
                "Snack": "Fruit",
                "Dinner": "Vegetable Soup"
            },

            "Friday": {
                "Breakfast": "Fruit Smoothie",
                "Lunch": "Paneer Salad",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            },

            "Saturday": {
                "Breakfast": "Oats + Fruits",
                "Lunch": "Vegetable Bowl",
                "Snack": "Almonds",
                "Dinner": "Salad"
            },

            "Sunday": {
                "Breakfast": "Fruit Bowl",
                "Lunch": "Paneer Salad",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            }
        }

    # WEIGHT LOSS - NON VEGETARIAN
        

    elif goal == "Weight Loss" and food_preference == "Non-Vegetarian":

        return {

            "Monday": {
                "Breakfast": f"Boiled {egg_item}",
                "Lunch": "Grilled Chicken + Salad",
                "Snack": "Green Tea",
                "Dinner": "Vegetable Soup"
            },

            "Tuesday": {
                "Breakfast": egg_item,
                "Lunch": f"{fish_item} + Vegetables",
                "Snack": "Almonds",
                "Dinner": "Chicken Salad"
            },

            "Wednesday": {
                "Breakfast": f"Fruit + {egg_item}",
                "Lunch": "Grilled Chicken",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            },

            "Thursday": {
                "Breakfast": f"Boiled {egg_item}",
                "Lunch": f"{fish_item} Salad",
                "Snack": "Apple",
                "Dinner": "Vegetables"
            },

            "Friday": {
                "Breakfast": egg_item,
                "Lunch": "Chicken Salad",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            },

            "Saturday": {
                "Breakfast": "Fruit Bowl",
                "Lunch": f"Grilled {fish_item}",
                "Snack": "Almonds",
                "Dinner": "Vegetables"
            },

            "Sunday": {
                "Breakfast": f"Boiled {egg_item}",
                "Lunch": "Chicken Salad",
                "Snack": "Green Tea",
                "Dinner": "Soup"
            }
        }

    # MAINTENANCE

    return {

        "Monday": {
            "Breakfast": f"{milk_item} + Oats",
            "Lunch": "Rice + Vegetables",
            "Snack": "Fruit",
            "Dinner": "Chapati + Dal"
        },

        "Tuesday": {
            "Breakfast": f"{egg_item} + Toast",
            "Lunch": "Rice + Chicken",
            "Snack": "Nuts",
            "Dinner": "Vegetables"
        },

        "Wednesday": {
            "Breakfast": "Smoothie",
            "Lunch": "Rice + Dal",
            "Snack": "Apple",
            "Dinner": "Chapati + Paneer"
        },

        "Thursday": {
            "Breakfast": "Oats + Banana",
            "Lunch": "Rice + Sambar",
            "Snack": "Almonds",
            "Dinner": "Chapati + Vegetables"
        },

        "Friday": {
            "Breakfast": "Fruit Bowl",
            "Lunch": "Brown Rice + Dal",
            "Snack": "Mixed Nuts",
            "Dinner": "Paneer Curry"
        },

        "Saturday": {
            "Breakfast": f"{milk_item} + Cornflakes",
            "Lunch": "Rice + Chicken",
            "Snack": "Fruit Juice",
            "Dinner": "Chapati + Egg Curry"
        },

        "Sunday": {
            "Breakfast": "Vegetable Sandwich",
            "Lunch": "Vegetable Biryani",
            "Snack": peanut_item,
            "Dinner": "Soup + Salad"
        }
    }
    