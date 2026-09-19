"""Body Part Workout Module
Provides exercise lists and routines categorized by body part / muscle group.
"""

BODY_PART_WORKOUTS = {
    "Chest": [
        "Barbell Bench Press - 4 sets x 8-12 reps",
        "Incline Dumbbell Press - 3 sets x 10-12 reps",
        "Cable Chest Flys - 3 sets x 12-15 reps",
        "Dips (Chest Focus) - 3 sets x 10-12 reps",
        "Push-ups - 3 sets to failure",
    ],
    "Back": [
        "Pull-ups / Lat Pulldown - 4 sets x 8-12 reps",
        "Barbell Bent-Over Row - 4 sets x 8-10 reps",
        "Seated Cable Row - 3 sets x 10-12 reps",
        "Single-Arm Dumbbell Row - 3 sets x 10-12 reps per side",
        "Face Pulls - 3 sets x 15 reps",
    ],
    "Shoulders": [
        "Overhead Barbell / Dumbbell Press - 4 sets x 8-10 reps",
        "Dumbbell Lateral Raises - 4 sets x 12-15 reps",
        "Front Dumbbell Raises - 3 sets x 12 reps",
        "Rear Delt Flys / Reverse Pec Deck - 3 sets x 15 reps",
        "Arnold Press - 3 sets x 10-12 reps",
    ],
    "Biceps": [
        "Barbell Bicep Curls - 4 sets x 10-12 reps",
        "Dumbbell Hammer Curls - 3 sets x 10-12 reps",
        "Incline Dumbbell Curls - 3 sets x 12 reps",
        "Preacher Curls - 3 sets x 10-12 reps",
        "Concentration Curls - 3 sets x 12 reps per arm",
    ],
    "Triceps": [
        "Tricep Rope Pushdowns - 4 sets x 12-15 reps",
        "Skull Crushers (Lying Triceps Extension) - 3 sets x 10-12 reps",
        "Overhead Dumbbell Extension - 3 sets x 10-12 reps",
        "Close-Grip Bench Press - 3 sets x 8-10 reps",
        "Bench Dips - 3 sets x 12-15 reps",
    ],
    "Legs": [
        "Barbell Back Squats - 4 sets x 8-10 reps",
        "Romanian Deadlifts (RDL) - 4 sets x 8-10 reps",
        "Leg Press - 3 sets x 10-12 reps",
        "Walking Lunges - 3 sets x 12 reps per leg",
        "Leg Extensions - 3 sets x 12-15 reps",
        "Lying / Seated Hamstring Curls - 3 sets x 12-15 reps",
        "Standing Calf Raises - 4 sets x 15-20 reps",
    ],
    "Abs & Core": [
        "Hanging Leg Raises - 3 sets x 12-15 reps",
        "Cable Woodchoppers / Crunches - 3 sets x 15 reps",
        "Plank - 3 sets x 45-60 seconds",
        "Russian Twists - 3 sets x 20 reps (10 per side)",
        "Bicycle Crunches - 3 sets x 20 reps",
    ],
    "Glutes": [
        "Barbell Hip Thrusts - 4 sets x 10-12 reps",
        "Bulgarian Split Squats - 3 sets x 10 reps per leg",
        "Cable Glute Kickbacks - 3 sets x 12-15 reps per leg",
        "Sumo Squats - 3 sets x 10-12 reps",
    ],
    "Full Body": [
        "Barbell Squats - 3 sets x 8-10 reps",
        "Bench Press - 3 sets x 8-10 reps",
        "Barbell Bent-Over Row - 3 sets x 8-10 reps",
        "Overhead Shoulder Press - 3 sets x 10 reps",
        "Plank - 3 sets x 60 seconds",
    ],
    "Cardio & HIIT": [
        "Jump Rope - 5 sets x 1 minute (30s rest)",
        "Treadmill Interval Sprints - 10 rounds (30s sprint / 60s walk)",
        "Burpees - 4 sets x 15 reps",
        "Rowing Machine - 20 minutes steady or interval",
        "Mountain Climbers - 4 sets x 30 seconds",
    ],
}


BODY_PART_CATEGORIES = {
    "Upper Body": [
        "Chest",
        "Back",
        "Shoulders",
        "Biceps",
        "Triceps",
    ],
    "Lower Body & Core": [
        "Legs",
        "Abs & Core",
        "Glutes",
        "Full Body",
        "Cardio & HIIT",
    ],
}


def get_categories():
    """Returns a list of main body segment categories."""
    return list(BODY_PART_CATEGORIES.keys())


def get_body_parts_by_category(category):
    """Returns list of body parts belonging to a category."""
    return BODY_PART_CATEGORIES.get(category, [])


def get_all_body_parts():
    """Returns a list of all available body parts."""
    return list(BODY_PART_WORKOUTS.keys())


def get_bodypart_workout(body_part):
    """Returns the list of exercises for the specified body part.
    Case-insensitive search.
    """
    if not body_part:
        return []
    
    # Direct lookup
    if body_part in BODY_PART_WORKOUTS:
        return BODY_PART_WORKOUTS[body_part]
    
    # Case-insensitive / partial matching
    cleaned_input = body_part.strip().lower()
    for key, exercises in BODY_PART_WORKOUTS.items():
        if key.lower() == cleaned_input:
            return exercises
        if cleaned_input in key.lower() or key.lower() in cleaned_input:
            return exercises
            
    return []


# Alias for flexibility
get_body_part_workout = get_bodypart_workout


if __name__ == "__main__":
    print("Categories:", get_categories())
    print("\nUpper Body Parts:", get_body_parts_by_category("Upper Body"))
    print("Lower Body & Core Parts:", get_body_parts_by_category("Lower Body & Core"))
    print("\n--- Chest Workout ---")
    for ex in get_bodypart_workout("Chest"):
        print(f"  • {ex}")
