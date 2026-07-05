from apscheduler.schedulers.background import BackgroundScheduler

from agent.reminder_agent import send_meal_reminder

scheduler = BackgroundScheduler(timezone="Asia/Kolkata")

if not scheduler.running:
    scheduler.start()

print("NutriAgent AI Reminder Scheduler Started")


def schedule_reminder(
    reminder_time,
    email,
    goal,
    food_preference,
    allergies
):

    hour = reminder_time.hour

    if 6 <= hour < 10:
        meal_type = "Breakfast"

    elif 10 <= hour < 12:
        meal_type = "Snack"

    elif 12 <= hour < 16:
        meal_type = "Lunch"

    elif 16 <= hour < 19:
        meal_type = "Snack"

    else:
        meal_type = "Dinner"

    try:
        scheduler.remove_job("meal_reminder")
    except Exception:
        pass

    scheduler.add_job(
        func=send_meal_reminder,
        trigger="date",
        run_date=reminder_time,
        args=[
            email,
            goal,
            food_preference,
            allergies,
            meal_type
        ],
        id="meal_reminder"
    )

    print("Reminder Scheduled:", reminder_time)