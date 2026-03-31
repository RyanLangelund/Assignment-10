"""
ASSIGNMENT 10B: SPRINT 3 - REFACTORING & DATA ACCOUNTABILITY
Project: Workout Tracker System
Developer: Ryan Langelund
"""

WORKOUT_FILE = "workout_history.txt"
DEFAULT_WEIGHT = 0


def get_user_info():
    """Gets the user's name."""
    return "Ryan"


def record_workout():
    """Collects workout data."""
    workout = {"exercise": "Bench Press", "sets": 3, "reps": 10, "weight": 135}
    return workout


def preview_workout(user, workout):
    """Shows workout preview."""
    print("WORKOUT PREVIEW")
    print("User:", user)
    print("Exercise:", workout["exercise"])
    print("Sets:", workout["sets"])
    print("Reps:", workout["reps"])
    print("Weight:", workout["weight"], "lbs")


def save_workout(user, workout, file_name=WORKOUT_FILE):
    """Shows final workout summary."""
    print("WORKOUT SUMMARY")
    print("User:", user)
    print("Exercise:", workout["exercise"])
    print("Sets:", workout["sets"])
    print("Reps:", workout["reps"])
    print("Weight:", workout["weight"], "lbs")


def main():
    user = get_user_info()
    workout = record_workout()
    preview_workout(user, workout)

    save_workout(user=user, workout=workout, file_name=WORKOUT_FILE)


main()
