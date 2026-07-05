from flask import Flask, render_template, request, redirect,session
from datetime import datetime

from agent.ingredient_agent import get_ingredients
from agent.grocery_agent import generate_grocery_list

from agent.nutrition_agent import (
    calculate_bmi,
    bmi_status,
    calculate_calories,
    get_recommendation,
    health_score,
    meal_plan
)

from agent.ai_agent import ai_decision
from agent.email_agent import send_email
from scheduler import schedule_reminder


from database.db import (
    create_table,
    save_user,
    get_users,
    delete_user,
    get_latest_user
)

from agent.reminder_agent import send_meal_reminder

app = Flask(__name__)
app.secret_key = "nutriagent_secret_key"

create_table()

user_data = {}
sent_goals = []




@app.route("/")
def home():

    user_data = session.get("user_data", {})

    return render_template(
        "index.html",
        user_data=user_data
    )


@app.route("/analyze", methods=["POST"])
def analyze():

    global user_data

    name = "Kaneshka"
    email = "kaneshkavenkat@gmail.com"
    age = 21
    gender = "Female"

    height = float(request.form["height"])
    weight = float(request.form["weight"])

    goal = request.form["goal"]
    global sent_goals
    food_preference = request.form["food_preference"]
    allergies = request.form.getlist("allergy")

    bmi = calculate_bmi(weight, height)
    status = bmi_status(bmi)

    calories = calculate_calories(
        weight,
        height,
        age,
        gender,
        goal
    )

    recommendation = get_recommendation(goal)
    score = health_score(bmi)

    plan = meal_plan(
        goal,
        food_preference,
        allergies
    )

    meal_ingredients = {}

    for day, meals in plan.items():

        meal_ingredients[day] = {}

        for meal_type, food in meals.items():

            meal_ingredients[day][meal_type] = get_ingredients(food)
    grocery_list = generate_grocery_list(
    plan,
    meal_ingredients
)        
           

    ai_result = ai_decision(goal, bmi, status)

    if goal not in sent_goals:

        send_email(
            email,
            f"NutriAgent AI - {goal}",
            f"""
Hello {name},

Your {goal} nutrition plan has been generated.

BMI: {bmi}
Status: {status}
Calories Needed: {calories}

Please check your meal plan in NutriAgent AI.
"""
        )

        sent_goals.append(goal)

    save_user(
        name,
        email,
        age,
        gender,
        height,
        weight,
        goal,
        food_preference,
        bmi,
        status,
        calories
    )

    user_data = {
    "name": name,
    "email": email,
    "height": height,
    "weight": weight,
    "age": age,
    "gender": gender,
    "bmi": bmi,
    "status": status,
    "calories": calories,
    "goal": goal,
    "food_preference": food_preference,
    "allergies": allergies,
    "score": score,
    "recommendation": recommendation,
    "plan": plan,
    "ingredients": meal_ingredients,
    "grocery_list": grocery_list,
    "ai_result": ai_result
}
    session["user_data"] = user_data

   
        
    return redirect("/bmi")
     

@app.route("/bmi")
def bmi_page():

    user_data = session.get("user_data")

    if not user_data:
        return redirect("/")

    return render_template(
        "bmi.html",
        name=user_data["name"],
        bmi=user_data["bmi"],
        status=user_data["status"],
        calories=user_data["calories"],
        goal=user_data["goal"],
        food_preference=user_data["food_preference"],
        score=user_data["score"],
        recommendation=user_data["recommendation"],
        ai_result=user_data["ai_result"]
    )

@app.route("/mealplan")
def mealplan():

    user_data = session.get("user_data")

    if not user_data:
        return "Please submit the form first."

    return render_template(
        "mealplan.html",
        plan=user_data["plan"],
        ingredients=user_data["ingredients"],
        goal=user_data["goal"],
        food_preference=user_data["food_preference"]
    )


@app.route("/exercise")
def exercise():

    user_data = session.get("user_data")

    if not user_data:
        return "Please submit the form first."

    return render_template(
        "exercise.html",
        goal=user_data["goal"]
    )


@app.route("/report")
def report():

    user_data = session.get("user_data")

    if not user_data:
        return "Please submit the form first."

    return render_template(
        "report.html",
        ai_result=user_data["ai_result"]
    )
@app.route("/grocery")
def grocery():

    user_data = session.get("user_data")

    if not user_data:
        return "Please submit the form first."

    return render_template(
        "grocery.html",
        grocery_list=user_data["grocery_list"]
    )

@app.route("/users")
def users():

    all_users = get_users()

    return render_template(
        "users.html",
        users=all_users
    )


@app.route("/delete_user/<int:user_id>")
def remove_user(user_id):

    delete_user(user_id)

    return redirect("/users")

@app.route("/send-reminder/<meal_type>")
def send_reminder(meal_type):

    user = get_latest_user()

    if user is None:
        return "No user found"

    email = user[2]
    goal = user[7]
    food_preference = user[8]

    allergies = []

    send_meal_reminder(
        email,
        goal,
        food_preference,
        allergies,
        meal_type
    )

    return f"{meal_type} reminder sent successfully"
    


@app.route("/set-reminder", methods=["POST"])
def set_reminder():

    user = get_latest_user()

    if user is None:
        return "No user found"

    reminder_time = request.form["reminder_time"]

    reminder_datetime = datetime.strptime(
        reminder_time,
        "%Y-%m-%dT%H:%M"
    )

    schedule_reminder(
        reminder_datetime,
        user[2],      # email
        user[7],      # goal
        user[8],      # food preference
        []            # allergies
    )

    return "Reminder Scheduled Successfully!"


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )






