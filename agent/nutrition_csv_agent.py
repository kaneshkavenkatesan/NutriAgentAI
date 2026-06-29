import pandas as pd

df = pd.read_excel("data/food_nutrition.xlsx")

def get_nutrition(meal_name):

    result = df[df["meal_name"] == meal_name]

    if len(result) > 0:

        food = result.iloc[0]

        return {
            "calories": food["calories"],
            "protein": food["protein_g"],
            "carbs": food["carbs_g"],
            "fat": food["fat_g"]
        }

    return {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0
    }