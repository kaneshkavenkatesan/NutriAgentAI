def ai_decision(goal, bmi, status):

    if bmi < 18.5:
        return """
User is currently Underweight.

AI Recommendation:
• Increase calorie intake.
• Consume protein-rich foods.
• Follow strength training exercises.
• Monitor body weight every week.

Expected Outcome:
Healthy weight gain and muscle development.
"""

    elif bmi > 25:
        return """
User is currently Overweight.

AI Recommendation:
• Follow a calorie deficit diet.
• Perform cardio exercises regularly.
• Increase daily physical activity.
• Consume high-fiber foods.

Expected Outcome:
Gradual fat loss and improved fitness.
"""

    else:
        return """
User is currently Healthy.

AI Recommendation:
• Maintain balanced nutrition.
• Continue regular exercise.
• Stay hydrated.
• Monitor health periodically.

Expected Outcome:
Long-term health maintenance.
"""