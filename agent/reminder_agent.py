from datetime import datetime
import pandas as pd

from agent.nutrition_agent import meal_plan
from agent.email_agent import send_email


def get_meal_nutrition(meal_name):

    df = pd.read_excel("data/food_nutrition.xlsx")

    meal = df[df["meal_name"].str.strip().str.lower() == meal_name.strip().lower()]

    if meal.empty:
        return None

    meal = meal.iloc[0]

    return {
        "calories": int(meal["calories"]),
        "protein": float(meal["protein_g"]),
        "carbs": float(meal["carbs_g"]),
        "fat": float(meal["fat_g"])
    }


def send_meal_reminder(
    email,
    goal,
    food_preference,
    allergies,
    meal_type
):

    today = datetime.now().strftime("%A")

    weekly_plan = meal_plan(
        goal,
        food_preference,
        allergies
    )

    meal = weekly_plan[today][meal_type]

    nutrition = get_meal_nutrition(meal)

    if nutrition:

        subject = f"🍽 {meal_type} Reminder | NutriAgent AI"

        message = f"""
🌞 Good {'Morning' if meal_type == 'Breakfast' else 'Day'}

Today's {meal_type}

🍽 Meal
{meal}

━━━━━━━━━━━━━━━━━━━━

🔥 Calories : {nutrition['calories']} kcal

🥩 Protein : {nutrition['protein']} g

🍚 Carbohydrates : {nutrition['carbs']} g

🥑 Fat : {nutrition['fat']} g

━━━━━━━━━━━━━━━━━━━━

🎯 Goal
{goal}

🥗 Food Preference
{food_preference}

💧 Drink at least 2 glasses of water before eating.

Have a healthy day ❤️

NutriAgent AI
"""

    else:

        subject = f"🍽 {meal_type} Reminder | NutriAgent AI"

        message = f"""
Today's {meal_type}

🍽 {meal}

Nutrition information not available.

NutriAgent AI
"""

    send_email(
        email,
        subject,
        message
    )