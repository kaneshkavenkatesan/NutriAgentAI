from apscheduler.schedulers.background import BackgroundScheduler

from database.db import get_latest_user
from agent.reminder_agent import send_meal_reminder

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")


def breakfast_job():

    user = get_latest_user()

    if user is None:
        return

    email = user[2]
    goal = user[7]
    food_preference = user[8]

    allergies = []

    send_meal_reminder(
        email,
        goal,
        food_preference,
        allergies,
        "Breakfast"
    )


def snack_job():

    user = get_latest_user()

    if user is None:
        return

    email = user[2]
    goal = user[7]
    food_preference = user[8]

    allergies = []

    send_meal_reminder(
        email,
        goal,
        food_preference,
        allergies,
        "Snack"
    )


def lunch_job():

    user = get_latest_user()

    if user is None:
        return

    email = user[2]
    goal = user[7]
    food_preference = user[8]

    allergies = []

    send_meal_reminder(
        email,
        goal,
        food_preference,
        allergies,
        "Lunch"
    )


def dinner_job():

    user = get_latest_user()

    if user is None:
        return

    email = user[2]
    goal = user[7]
    food_preference = user[8]

    allergies = []

    send_meal_reminder(
        email,
        goal,
        food_preference,
        allergies,
        "Dinner"
    )


scheduler.add_job(
    breakfast_job,
    "cron",
    hour=8,
    minute=0
)

scheduler.add_job(
    snack_job,
    "cron",
    hour=11,
    minute=0
)

scheduler.add_job(
    lunch_job,
    "cron",
    hour=12,
    minute=30
)

scheduler.add_job(
    snack_job,
    "cron",
    hour=17,
    minute=0
)

scheduler.add_job(
    dinner_job,
    "cron",
    hour=20,
    minute=0
)

scheduler.start()

print("NutriAgent AI Reminder Scheduler Started")