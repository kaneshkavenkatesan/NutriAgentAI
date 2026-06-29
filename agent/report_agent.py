def generate_report(name, bmi, status, goal, calories):

    report = f"""

NUTRIAGENT AI REPORT

---------------------------------

Name: {name}

BMI: {bmi}

Health Status: {status}

Goal: {goal}

Daily Calories Needed: {calories}

---------------------------------

AGENT ANALYSIS

Based on the information provided,
your current health status is
classified as {status}.

Your selected goal is {goal}.

The Nutrition Agent recommends
following the suggested meal plan
and maintaining consistency.

---------------------------------

FINAL RECOMMENDATION

Focus on healthy eating habits,
adequate hydration, and regular
physical activity.

"""

    return report