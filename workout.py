"""Workout Plans and Routines for Kn Fitness Pro 2
Provides detailed daily exercise routines for:
- Build Muscle
- Lose Weight
- Maintain Weight
"""

def get_workout_plan(goal):
    if goal == "Lose Weight":
        return [
            "Day 1: Cardio + HIIT | 30-40 minutes",
            "Day 2: Cardio + Strength Training | 40-50 minutes",
            "Day 3: HIIT + Core Exercises | 30-40 minutes",
            "Day 4: Full Body Metabolic Circuit | 40-50 minutes",
        ]
    elif goal == "Maintain Weight":
        return [
            "Day 1: Full Body Strength | 3 Sets of 10-12 reps",
            "Day 2: Cardio + Functional Training | 30-40 minutes",
            "Day 3: Upper Body Strength & Tone | 3 Sets x 10-12 reps",
            "Day 4: Lower Body Strength & Core | 3 Sets x 10-12 reps",
        ]
    elif goal == "Build Muscle":
        return [
            "Day 1: Chest and Triceps | 4 Sets x 8-12 reps",
            "Day 2: Back and Biceps | 4 Sets x 8-12 reps",
            "Day 3: Shoulders and Arms | 4 Sets x 8-12 reps",
            "Day 4: Legs and Abs | 4 Sets x 8-12 reps",
        ]
    else:
        return []


workout_data = {
    "Build Muscle": {
        "Day 1": [
            {
                "Exercise": "Incline Barbell Press",
                "Sets": 4,
                "Reps": "8-12",
                "Rest": "90 seconds",
                "Tips": "Keep your chest up and control the weight."
            },
            {
                "Exercise": "Chest Fly",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Stretch and squeeze your chest."
            },
            {
                "Exercise": "Shoulder Press",
                "Sets": 3,
                "Reps": "8-12",
                "Rest": "60 seconds",
                "Tips": "Keep your core tight and avoid arching your back."
            },
            {
                "Exercise": "Lateral Raises",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "60 seconds",
                "Tips": "Control the weight and avoid swinging."
            },
            {
                "Exercise": "Triceps Rope Pushdowns",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Keep your elbows close to your body and avoid flaring them out."
            }
        ],
        "Day 2": [
            {
                "Exercise": "Squat",
                "Sets": 4,
                "Reps": "8-12",
                "Rest": "90 seconds",
                "Tips": "Keep your chest up and control the movement."
            },
            {
                "Exercise": "Romanian Deadlift",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "90 seconds",
                "Tips": "Keep your back straight and push your hips back."
            },
            {
                "Exercise": "Leg Press",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "90 seconds",
                "Tips": "Keep your knees aligned with your toes."
            },
            {
                "Exercise": "Leg Curl",
                "Sets": 3,
                "Reps": "8-12",
                "Rest": "90 seconds",
                "Tips": "Control the weight during both directions."
            },
            {
                "Exercise": "Calf Raises",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Pause and squeeze at the top."
            }
        ],
        "Day 3": [
            {
                "Exercise": "Lat Pulldown / Pull-ups",
                "Sets": 4,
                "Reps": "8-12",
                "Rest": "90 seconds",
                "Tips": "Pull through elbows and squeeze your lats."
            },
            {
                "Exercise": "Barbell Bent-Over Row",
                "Sets": 4,
                "Reps": "8-10",
                "Rest": "90 seconds",
                "Tips": "Keep neutral spine, pull bar to lower ribcage."
            },
            {
                "Exercise": "Seated Cable Row",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Avoid leaning too far forward or backward."
            },
            {
                "Exercise": "Barbell Bicep Curl",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Pin elbows to your ribs, do not swing."
            },
            {
                "Exercise": "Hammer Curls",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "60 seconds",
                "Tips": "Targets brachialis and forearms."
            }
        ],
        "Day 4": [
            {
                "Exercise": "Dumbbell Overhead Shoulder Press",
                "Sets": 4,
                "Reps": "8-12",
                "Rest": "90 seconds",
                "Tips": "Press upward without locking elbows harshly."
            },
            {
                "Exercise": "Dips (Chest/Triceps focus)",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Lower down with control until 90 degree arm angle."
            },
            {
                "Exercise": "Hanging Leg Raises",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "60 seconds",
                "Tips": "Avoid swinging; lift using core contraction."
            },
            {
                "Exercise": "Cable Woodchoppers",
                "Sets": 3,
                "Reps": "15 per side",
                "Rest": "60 seconds",
                "Tips": "Rotate through your torso and engage obliques."
            },
            {
                "Exercise": "Plank",
                "Sets": 3,
                "Reps": "60 seconds",
                "Rest": "45 seconds",
                "Tips": "Maintain a flat back and brace your core."
            }
        ]
    },
    "Lose Weight": {
        "Day 1": [
            {
                "Exercise": "Treadmill Interval Sprints",
                "Sets": 8,
                "Reps": "30s sprint / 60s walk",
                "Rest": "60 seconds",
                "Tips": "Sprint at 85%+ effort, recover with brisk walk."
            },
            {
                "Exercise": "Kettlebell Swings",
                "Sets": 4,
                "Reps": "15-20",
                "Rest": "45 seconds",
                "Tips": "Snap hips forward; power comes from glutes, not arms."
            },
            {
                "Exercise": "Burpees",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "60 seconds",
                "Tips": "Land softly with knees slightly bent."
            },
            {
                "Exercise": "Jump Rope",
                "Sets": 4,
                "Reps": "60 seconds",
                "Rest": "30 seconds",
                "Tips": "Stay on balls of feet with wrists turning the rope."
            },
            {
                "Exercise": "Mountain Climbers",
                "Sets": 3,
                "Reps": "30 seconds",
                "Rest": "30 seconds",
                "Tips": "Keep hips low and drive knees rapidly toward chest."
            }
        ],
        "Day 2": [
            {
                "Exercise": "Goblet Squats",
                "Sets": 4,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Hold dumbbell at chest level; full depth squat."
            },
            {
                "Exercise": "Push-ups",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Keep body in straight line; touch chest to floor."
            },
            {
                "Exercise": "Dumbbell Bent-Over Row",
                "Sets": 4,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Hinge at hips, pull elbows straight up."
            },
            {
                "Exercise": "Walking Lunges",
                "Sets": 3,
                "Reps": "12 per leg",
                "Rest": "45 seconds",
                "Tips": "Keep torso upright and do not let knee slam floor."
            },
            {
                "Exercise": "Plank Shoulder Taps",
                "Sets": 3,
                "Reps": "20 taps",
                "Rest": "30 seconds",
                "Tips": "Minimize hip sway while tapping opposite shoulders."
            }
        ],
        "Day 3": [
            {
                "Exercise": "Rowing Machine Intervals",
                "Sets": 5,
                "Reps": "500m intervals",
                "Rest": "60 seconds",
                "Tips": "Drive hard with legs first, then lean back and pull."
            },
            {
                "Exercise": "Bicycle Crunches",
                "Sets": 3,
                "Reps": "20 per side",
                "Rest": "30 seconds",
                "Tips": "Slow and controlled rotation, touch elbow to knee."
            },
            {
                "Exercise": "Russian Twists",
                "Sets": 3,
                "Reps": "20 twists",
                "Rest": "30 seconds",
                "Tips": "Keep feet elevated for maximum abdominal activation."
            },
            {
                "Exercise": "Box Jumps / Step-ups",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Land softly in a quarter-squat position."
            },
            {
                "Exercise": "High Knees",
                "Sets": 3,
                "Reps": "40 seconds",
                "Rest": "30 seconds",
                "Tips": "Pump arms and bring knees above hip height."
            }
        ],
        "Day 4": [
            {
                "Exercise": "Dumbbell Thrusters",
                "Sets": 4,
                "Reps": "12-15",
                "Rest": "60 seconds",
                "Tips": "Squat deeply and use leg momentum to press overhead."
            },
            {
                "Exercise": "Kettlebell Romanian Deadlift",
                "Sets": 3,
                "Reps": "15",
                "Rest": "45 seconds",
                "Tips": "Feel hamstring stretch, maintain flat spine."
            },
            {
                "Exercise": "Renegade Rows",
                "Sets": 3,
                "Reps": "10 per side",
                "Rest": "45 seconds",
                "Tips": "Widen feet for stability, row without twisting torso."
            },
            {
                "Exercise": "Battle Ropes",
                "Sets": 4,
                "Reps": "30 seconds",
                "Rest": "30 seconds",
                "Tips": "Keep athletic stance and whip ropes vigorously."
            },
            {
                "Exercise": "Forearm Plank",
                "Sets": 3,
                "Reps": "45-60 seconds",
                "Rest": "30 seconds",
                "Tips": "Keep elbows under shoulders and squeeze glutes."
            }
        ]
    },
    "Maintain Weight": {
        "Day 1": [
            {
                "Exercise": "Barbell Back Squat",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "75 seconds",
                "Tips": "Warm up well; maintain balanced weight on midfoot."
            },
            {
                "Exercise": "Flat Dumbbell Bench Press",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Keep shoulders retracted and lower dumbbells with control."
            },
            {
                "Exercise": "Lat Pulldowns",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Pull bar to upper chest and squeeze back muscles."
            },
            {
                "Exercise": "Dumbbell Lateral Raises",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Slight forward lean, raise arms to shoulder level."
            },
            {
                "Exercise": "Hanging Knee Raises",
                "Sets": 3,
                "Reps": "15",
                "Rest": "45 seconds",
                "Tips": "Curl knees to chest to engage lower abdominals."
            }
        ],
        "Day 2": [
            {
                "Exercise": "Incline Treadmill Walk / Jog",
                "Sets": 1,
                "Reps": "25-30 mins",
                "Rest": "N/A",
                "Tips": "Set incline 5-8%, maintain steady aerobic heart rate."
            },
            {
                "Exercise": "Kettlebell Goblet Squat",
                "Sets": 3,
                "Reps": "12",
                "Rest": "60 seconds",
                "Tips": "Keep chest high and elbows inside knees at bottom."
            },
            {
                "Exercise": "Farmer's Walk",
                "Sets": 3,
                "Reps": "40 meters",
                "Rest": "60 seconds",
                "Tips": "Heavy dumbbells or kettlebells, stand tall, walk smooth."
            },
            {
                "Exercise": "Push-ups (Strict)",
                "Sets": 3,
                "Reps": "15",
                "Rest": "45 seconds",
                "Tips": "Full range of motion, pause briefly at the bottom."
            },
            {
                "Exercise": "Side Plank",
                "Sets": 3,
                "Reps": "30s per side",
                "Rest": "30 seconds",
                "Tips": "Stack feet and keep hips elevated in a straight line."
            }
        ],
        "Day 3": [
            {
                "Exercise": "Incline Dumbbell Press",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Focus on upper chest contraction."
            },
            {
                "Exercise": "Seated Cable Row",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Keep shoulders down and drive elbows back."
            },
            {
                "Exercise": "Overhead Dumbbell Press",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Engage core to prevent arching the lower back."
            },
            {
                "Exercise": "Alternating Dumbbell Curls",
                "Sets": 3,
                "Reps": "10-12 per arm",
                "Rest": "45 seconds",
                "Tips": "Rotate wrist as you curl for maximum peak contraction."
            },
            {
                "Exercise": "Triceps Overhead Extension",
                "Sets": 3,
                "Reps": "12-15",
                "Rest": "45 seconds",
                "Tips": "Keep elbows close together and lower weight behind head."
            }
        ],
        "Day 4": [
            {
                "Exercise": "Romanian Deadlift",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "75 seconds",
                "Tips": "Hinge hips backward, keep dumbbells close to shins."
            },
            {
                "Exercise": "Leg Press",
                "Sets": 3,
                "Reps": "10-12",
                "Rest": "60 seconds",
                "Tips": "Place feet shoulder-width; do not lock knees."
            },
            {
                "Exercise": "Hamstring Leg Curls",
                "Sets": 3,
                "Reps": "12",
                "Rest": "45 seconds",
                "Tips": "Control the eccentric (lowering) phase."
            },
            {
                "Exercise": "Standing Calf Raises",
                "Sets": 3,
                "Reps": "15-20",
                "Rest": "45 seconds",
                "Tips": "Hold 1 second at top stretch."
            },
            {
                "Exercise": "Abdominal Bicycle Crunches",
                "Sets": 3,
                "Reps": "20 total",
                "Rest": "30 seconds",
                "Tips": "Focus on the cross-body squeeze, don't pull your neck."
            }
        ]
    }
}


def get_workout_details(goal, day):
    """Returns list of exercises for the given goal and day.
    Falls back gracefully if goal or day is not found.
    """
    goal_workouts = workout_data.get(goal, {})
    if not goal_workouts:
        # Fallback to Build Muscle if goal is not found
        goal_workouts = workout_data.get("Build Muscle", {})
    return goal_workouts.get(day, [])


if __name__ == "__main__":
    print("Testing workout.py:")
    for goal in ["Build Muscle", "Lose Weight", "Maintain Weight"]:
        for day in ["Day 1", "Day 2", "Day 3", "Day 4"]:
            details = get_workout_details(goal, day)
            print(f"[{goal}] {day} -> {len(details)} exercises loaded.")