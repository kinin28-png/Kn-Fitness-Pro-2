"""
==============================================================================
KN FITNESS PRO 2 — EXERCISE VIDEO & INSTRUCTION LIBRARY (SECTION 3)
==============================================================================
EDITING GUIDE FOR YOU:
You can easily edit, add, or replace video URLs, instructions, and tips below!

Format:
    "Exercise Name": {
        "category": "Chest Exercises",          # Category name
        "video_url": "https://www.youtube.com/...", # YouTube link or local file path
        "target_muscle": "Upper Chest & Triceps",
        "equipment": "Barbell / Incline Bench",
        "difficulty": "Intermediate",           # Beginner / Intermediate / Advanced
        "instructions": [
            "1. Lie on the incline bench set at 30-45 degrees.",
            "2. Grip the barbell with hands slightly wider than shoulder-width.",
            "3. Lower the barbell smoothly to your upper chest with elbows at 45 degrees.",
            "4. Press explosively back to the starting position without locking elbows."
        ],
        "tips": "Keep your shoulder blades pinched together and drive through your chest.",
        "mistakes_to_avoid": "Setting the bench incline too steep (overworks the shoulders)."
    }
==============================================================================
"""

EXERCISE_VIDEO_LIBRARY = {
    # =========================================================================
    # 1. CHEST EXERCISES
    # =========================================================================
    "Incline Barbell Press": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=8iPEnn-ltC8",
        "target_muscle": "Upper Chest (Clavicular Head) & Front Delts",
        "equipment": "Incline Bench, Barbell, Weight Plates",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Lie on an incline bench set to roughly 30-45 degrees.",
            "2. Grasp the barbell with an overhand grip, slightly wider than shoulder-width.",
            "3. Unrack the bar and hold it directly above your upper chest with arms extended.",
            "4. Inhale and lower the bar slowly until it lightly touches your upper chest.",
            "5. Exhale and drive the bar up using your chest muscles until arms are extended."
        ],
        "tips": "Keep your shoulder blades retracted and depressed against the pad for shoulder safety.",
        "mistakes_to_avoid": "Bouncing the barbell off your chest or setting the incline above 45 degrees."
    },
    "Flat Barbell Bench Press": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=rT7DgCr-3pg",
        "target_muscle": "Mid & Lower Chest, Triceps, Anterior Deltoids",
        "equipment": "Flat Bench, Barbell, Rack",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Lie flat on the bench with eyes directly under the racked barbell.",
            "2. Plant your feet firmly into the floor and grip the bar slightly wider than shoulder-width.",
            "3. Unrack the bar with locked arms, keeping your wrists neutral.",
            "4. Lower the bar with control to your mid-sternum, keeping elbows tucked at roughly 45-60 degrees.",
            "5. Press upward driving your feet into the floor until your arms are fully extended."
        ],
        "tips": "Create a stable arch in your upper back and keep your glutes planted on the bench.",
        "mistakes_to_avoid": "Flaring elbows out at 90 degrees, which causes severe shoulder impingement."
    },
    "Dumbbell Chest Flys": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=eozdVDA78K0",
        "target_muscle": "Pectoralis Major (Chest Stretch & Peak Squeeze)",
        "equipment": "Flat Bench, Pair of Dumbbells",
        "difficulty": "Beginner",
        "instructions": [
            "1. Lie flat on a bench holding dumbbells directly above your chest, palms facing each other.",
            "2. Keep a slight, rigid bend in your elbows throughout the movement.",
            "3. Lower the dumbbells out wide in an arc until you feel a deep stretch in your chest.",
            "4. Bring the dumbbells back together at the top in the same wide hugging arc.",
            "5. Squeeze your pecs firmly at the top of the movement for 1 second."
        ],
        "tips": "Focus on the deep stretch at the bottom and the muscular squeeze at the top.",
        "mistakes_to_avoid": "Bending your elbows too much, turning the exercise into a dumbbell press."
    },
    "Cable Crossovers": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=taI4XduLpBe",
        "target_muscle": "Inner & Lower Chest Squeeze",
        "equipment": "Dual Cable Machine, D-handles",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Set cable pulleys to shoulder height or above, grabbing both handles.",
            "2. Step forward into a staggered stance with a slight forward lean at the hips.",
            "3. With elbows slightly bent, pull the handles forward and together in a wide hugging motion.",
            "4. Cross your hands slightly over at the finish point to maximize peak contraction.",
            "5. Slowly return to the starting position under full control."
        ],
        "tips": "Maintain continuous tension throughout the entire repetition; do not let the weights slam.",
        "mistakes_to_avoid": "Using excessive momentum or swinging your torso to pull the cables."
    },
    "Chest Dips": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=2z8JmcrW-As",
        "target_muscle": "Lower Pectorals, Triceps, Core",
        "equipment": "Parallel Dip Bars",
        "difficulty": "Advanced",
        "instructions": [
            "1. Grip parallel bars and push yourself up to the starting position with locked arms.",
            "2. Lean your torso forward roughly 30 degrees and cross your feet behind you.",
            "3. Lower your body slowly by bending elbows until upper arms are parallel to the ground.",
            "4. Push through your chest and triceps to return to the top position."
        ],
        "tips": "Leaning forward emphasizes the chest; staying fully upright emphasizes the triceps.",
        "mistakes_to_avoid": "Dropping down too low below 90 degrees if you have shoulder mobility limits."
    },
    "Standard Push-ups": {
        "category": "Chest Exercises",
        "video_url": "https://www.youtube.com/watch?v=IODxDxX7oi4",
        "target_muscle": "Full Chest, Triceps, Anterior Deltoids, Core",
        "equipment": "Bodyweight",
        "difficulty": "Beginner",
        "instructions": [
            "1. Place hands on the floor slightly wider than shoulder-width apart.",
            "2. Extend legs back so you are supported on your toes in a rigid high plank.",
            "3. Lower your chest until it hovers an inch above the floor.",
            "4. Press forcefully through the floor to return to the top."
        ],
        "tips": "Keep your core tight, glutes squeezed, and body in one straight line.",
        "mistakes_to_avoid": "Sagging hips or looking up (keep your neck neutral)."
    },

    # =========================================================================
    # 2. BACK EXERCISES
    # =========================================================================
    "Lat Pulldowns": {
        "category": "Back Exercises",
        "video_url": "https://www.youtube.com/watch?v=CAwf7n6Luuc",
        "target_muscle": "Latissimus Dorsi (Back Width), Biceps",
        "equipment": "Cable Pulldown Station, Wide Lat Bar",
        "difficulty": "Beginner",
        "instructions": [
            "1. Sit down and secure your thighs firmly beneath the pads.",
            "2. Grip the wide bar with an overhand grip, slightly wider than shoulder-width.",
            "3. Lean back slightly (10-15 degrees) with chest lifted high.",
            "4. Pull the bar down toward your upper chest by driving your elbows down and back.",
            "5. Squeeze your lats for 1 second, then slowly raise the bar back up."
        ],
        "tips": "Think about pulling through your elbows rather than pulling with your hands.",
        "mistakes_to_avoid": "Swinging your lower back backwards to pull heavy weight."
    },
    "Barbell Bent-Over Row": {
        "category": "Back Exercises",
        "video_url": "https://www.youtube.com/watch?v=FWJR5Ve8gkQ",
        "target_muscle": "Rhomboids, Lats, Middle Trapezius, Lower Back",
        "equipment": "Barbell, Weight Plates",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Stand with feet hip-width apart holding a barbell with an overhand grip.",
            "2. Hinge at your hips until your torso is nearly parallel to the floor, back flat.",
            "3. Let the bar hang directly below your shoulders with arms extended.",
            "4. Pull the bar up toward your belly button, driving your elbows back.",
            "5. Squeeze your shoulder blades together at the top, then lower smoothly."
        ],
        "tips": "Brace your core tightly to protect your lumbar spine throughout each rep.",
        "mistakes_to_avoid": "Rounding your spine or standing too upright during the row."
    },
    "Seated Cable Row": {
        "category": "Back Exercises",
        "video_url": "https://www.youtube.com/watch?v=GZbfZ033f74",
        "target_muscle": "Mid Back, Rhomboids, Lats, Rear Deltoids",
        "equipment": "Cable Row Station, V-bar handle",
        "difficulty": "Beginner",
        "instructions": [
            "1. Sit on the bench with knees slightly bent and feet pressed against the footrests.",
            "2. Reach forward and grab the V-bar handle with a neutral grip.",
            "3. Pull your torso back upright perpendicular to the floor with chest up.",
            "4. Pull the handle directly into your lower ribcage, squeezing your shoulder blades.",
            "5. Extend your arms forward under control to feel the stretch in your back."
        ],
        "tips": "Avoid leaning back and forth; keep your torso stationary and let your back work.",
        "mistakes_to_avoid": "Using momentum and rocking your torso violently back and forth."
    },
    "Pull-ups / Chin-ups": {
        "category": "Back Exercises",
        "video_url": "https://www.youtube.com/watch?v=eGo4IYlbE5g",
        "target_muscle": "Latissimus Dorsi, Biceps, Upper Back, Core",
        "equipment": "Pull-up Bar",
        "difficulty": "Advanced",
        "instructions": [
            "1. Grab the pull-up bar with an overhand grip (slightly wider than shoulders).",
            "2. Hang at full extension with core braced and legs straight.",
            "3. Pull your body upward by driving your elbows down toward your hips.",
            "4. Continue pulling until your chin completely clears the top of the bar.",
            "5. Lower yourself with full control until arms are fully extended."
        ],
        "tips": "Initiate each rep by pulling your shoulder blades down before bending elbows.",
        "mistakes_to_avoid": "Kicking or swinging your legs (kipping) to cheat the repetition."
    },
    "Conventional Deadlift": {
        "category": "Back Exercises",
        "video_url": "https://www.youtube.com/watch?v=op9kVnSso6Q",
        "target_muscle": "Entire Posterior Chain (Erector Spinae, Glutes, Hamstrings, Traps)",
        "equipment": "Olympic Barbell, Bumper Plates",
        "difficulty": "Advanced",
        "instructions": [
            "1. Stand with feet hip-width apart, barbell cutting over your midfoot.",
            "2. Hinge at hips and grip the bar just outside your shins.",
            "3. Pull your chest up, flatten your back, and take slack out of the barbell.",
            "4. Drive your feet through the floor and extend hips and knees together.",
            "5. Stand tall at the top with glutes squeezed; lower bar back with control."
        ],
        "tips": "Keep the bar glued against your shins and thighs throughout the entire lift.",
        "mistakes_to_avoid": "Rounding your lower back or hyperextending backwards at the top."
    },

    # =========================================================================
    # 3. ARM EXERCISES (BICEPS & TRICEPS)
    # =========================================================================
    "Barbell Bicep Curl": {
        "category": "Arm Exercises",
        "video_url": "https://www.youtube.com/watch?v=kwG2ipFRgfo",
        "target_muscle": "Biceps Brachii (Long and Short Heads)",
        "equipment": "Straight Barbell or EZ-Bar",
        "difficulty": "Beginner",
        "instructions": [
            "1. Stand tall holding the barbell with an underhand shoulder-width grip.",
            "2. Pin your elbows firmly against your ribs and brace your abdominal core.",
            "3. Curl the weight upward toward chest height by contracting your biceps.",
            "4. Hold the peak contraction at the top for 1 second.",
            "5. Lower the bar slowly back to full arm extension."
        ],
        "tips": "Keep your upper arms completely still; only your forearms should move.",
        "mistakes_to_avoid": "Swinging your hips or leaning back to lift the barbell."
    },
    "Dumbbell Hammer Curls": {
        "category": "Arm Exercises",
        "video_url": "https://www.youtube.com/watch?v=zC3nLlEvin4",
        "target_muscle": "Brachialis, Brachioradialis (Forearms & Outer Bicep)",
        "equipment": "Pair of Dumbbells",
        "difficulty": "Beginner",
        "instructions": [
            "1. Stand upright holding dumbbells at your sides with palms facing inward (neutral grip).",
            "2. Keep your upper arms stationary and elbows tucked close to your torso.",
            "3. Curl the dumbbells upward while maintaining the neutral hammer grip.",
            "4. Squeeze your forearms and brachialis at the top.",
            "5. Lower the dumbbells slowly to the starting position."
        ],
        "tips": "Hammer curls build forearm thickness and push the bicep peak higher.",
        "mistakes_to_avoid": "Rotating your wrists during the curl (keep palms facing inward)."
    },
    "Preacher Curls": {
        "category": "Arm Exercises",
        "video_url": "https://www.youtube.com/watch?v=fIWP-FRFNU0",
        "target_muscle": "Biceps Brachii (Strict Isolated Short Head)",
        "equipment": "Preacher Bench, EZ-Curl Bar",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Sit at the preacher bench with armpits resting snugly over the top edge of the pad.",
            "2. Hold the EZ-bar with an underhand grip, arms resting flat against the incline pad.",
            "3. Curl the bar upward toward your shoulders until your biceps are fully contracted.",
            "4. Pause for a split second, then lower the bar with control until arms are almost straight."
        ],
        "tips": "Do not fully hyper-extend elbows at the very bottom under heavy loads.",
        "mistakes_to_avoid": "Lifting your body or chest off the pad to assist the curl."
    },
    "Triceps Rope Pushdowns": {
        "category": "Arm Exercises",
        "video_url": "https://www.youtube.com/watch?v=vB5OHsJ3EME",
        "target_muscle": "Triceps (Lateral and Medial Heads)",
        "equipment": "Cable Machine, Rope Attachment",
        "difficulty": "Beginner",
        "instructions": [
            "1. Attach a rope to the top cable pulley and grip with both hands, palms facing each other.",
            "2. Tuck your elbows firmly to your sides and lean forward slightly at the hips.",
            "3. Push the rope downward by extending your elbows.",
            "4. At the bottom of the movement, spread the rope handles apart for a peak squeeze.",
            "5. Slowly let your hands rise back up until your forearms pass 90 degrees."
        ],
        "tips": "Lock your elbows in space; do not let them drift forward and backward.",
        "mistakes_to_avoid": "Allowing your shoulders to rise up or letting elbows flare out wide."
    },
    "Skull Crushers (Lying Triceps Extension)": {
        "category": "Arm Exercises",
        "video_url": "https://www.youtube.com/watch?v=d_KZxkY_0cM",
        "target_muscle": "Triceps (Long Head Focus for Arm Size)",
        "equipment": "Flat Bench, EZ-Bar or Dumbbells",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Lie flat on a bench holding an EZ-bar above your chest with arms extended.",
            "2. Angle your upper arms slightly backward (around 10 degrees behind vertical).",
            "3. Bend your elbows and lower the bar slowly toward your forehead or crown of head.",
            "4. Stop an inch above your forehead, then extend your elbows to push back up."
        ],
        "tips": "Angling your upper arms slightly backwards maintains constant tricep tension at lockout.",
        "mistakes_to_avoid": "Letting your elbows flare outwards (keep them pointing forward)."
    },

    # =========================================================================
    # 4. SHOULDER EXERCISES
    # =========================================================================
    "Overhead Dumbbell Shoulder Press": {
        "category": "Shoulder Exercises",
        "video_url": "https://www.youtube.com/watch?v=qEwKCR5JCog",
        "target_muscle": "Anterior & Lateral Deltoids, Triceps",
        "equipment": "Upright Bench, Pair of Dumbbells",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Sit on an upright bench with dumbbells positioned at shoulder height, palms forward.",
            "2. Plant your feet flat on the floor and brace your abdominal wall.",
            "3. Press the dumbbells upward in a slight arc until arms are extended overhead.",
            "4. Do not clank the dumbbells together at the top.",
            "5. Lower the weights smoothly back to ear/shoulder level."
        ],
        "tips": "Keep your core braced to avoid hyperextending your lower back.",
        "mistakes_to_avoid": "Arching your lower back heavily away from the backrest."
    },
    "Dumbbell Lateral Raises": {
        "category": "Shoulder Exercises",
        "video_url": "https://www.youtube.com/watch?v=3VcKaXpzqRo",
        "target_muscle": "Lateral Deltoids (Side Shoulders for Width)",
        "equipment": "Pair of Light Dumbbells",
        "difficulty": "Beginner",
        "instructions": [
            "1. Stand tall with light dumbbells held at your sides, palms facing inward.",
            "2. Hinge slightly forward at your hips (around 10 degrees) with soft knees.",
            "3. Raise your arms out to the sides leading with your elbows.",
            "4. Stop when your arms reach parallel to the floor (shoulder height).",
            "5. Lower the dumbbells slowly and deliberately over a 2-second count."
        ],
        "tips": "Lead the movement with your elbows and pinkies for maximum side-delt activation.",
        "mistakes_to_avoid": "Using heavy weights and swinging with your legs or torso."
    },
    "Face Pulls": {
        "category": "Shoulder Exercises",
        "video_url": "https://www.youtube.com/watch?v=rep-qVOkqgk",
        "target_muscle": "Rear Deltoids, Infraspinatus, Rotator Cuff, Upper Traps",
        "equipment": "Cable Machine, Rope Attachment",
        "difficulty": "Beginner",
        "instructions": [
            "1. Set the cable pulley to eye level and attach a rope.",
            "2. Grip the rope with an overhand grip (thumbs pointing backward).",
            "3. Step back into a stable stance and pull the rope directly toward your bridge of nose.",
            "4. At the finish point, pull your hands wide apart and externally rotate your shoulders.",
            "5. Hold the squeeze for 1 second, then slowly return."
        ],
        "tips": "Crucial exercise for shoulder health, posture, and preventing injuries.",
        "mistakes_to_avoid": "Pulling the rope downward toward your chin instead of eye level."
    },
    "Arnold Press": {
        "category": "Shoulder Exercises",
        "video_url": "https://www.youtube.com/watch?v=6Z15_WdXmVw",
        "target_muscle": "All Three Deltoid Heads (Front, Side, Rear)",
        "equipment": "Bench, Pair of Dumbbells",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Sit upright holding dumbbells in front of your chest with palms facing you (chin level).",
            "2. As you press the weights overhead, rotate your wrists outward so palms face forward.",
            "3. Lock out overhead with palms facing forward.",
            "4. Reverse the rotation smoothly as you lower the dumbbells back in front of your chest."
        ],
        "tips": "Keep the rotation smooth and synchronized with the pressing motion.",
        "mistakes_to_avoid": "Rushing the rotation or banging the dumbbells together overhead."
    },

    # =========================================================================
    # 5. LEG EXERCISES
    # =========================================================================
    "Barbell Back Squat": {
        "category": "Leg Exercises",
        "video_url": "https://www.youtube.com/watch?v=bEv6CCg2BC8",
        "target_muscle": "Quadriceps, Glutes, Hamstrings, Core",
        "equipment": "Squat Rack, Olympic Barbell",
        "difficulty": "Advanced",
        "instructions": [
            "1. Step under the bar and rest it across your upper traps; grip bar firmly with both hands.",
            "2. Unrack and take 2-3 steps back, placing feet shoulder-width apart, toes angled out slightly.",
            "3. Inhale deeply into your abdomen, brace your core, and push hips back and knees out.",
            "4. Descend until your hip crease drops below the top of your knees (parallel or below).",
            "5. Drive up through the floor, keeping your chest tall until standing straight."
        ],
        "tips": "Keep your knees tracking in line with your toes and maintain a neutral spine.",
        "mistakes_to_avoid": "Letting your knees cave inwards (knee valgus) or rising on your toes."
    },
    "Romanian Deadlift (RDL)": {
        "category": "Leg Exercises",
        "video_url": "https://www.youtube.com/watch?v=JCXUYuzwNrM",
        "target_muscle": "Hamstrings, Gluteus Maximus, Lower Back",
        "equipment": "Barbell or Dumbbells",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Stand tall holding the weight with an overhand grip, feet hip-width apart.",
            "2. Keep a soft, slight bend in your knees and lock that angle in place.",
            "3. Push your hips back as far as possible while keeping the weight close to your legs.",
            "4. Lower until you feel a strong stretch in your hamstrings (usually mid-shin level).",
            "5. Squeeze your glutes and drive your hips forward to return to standing."
        ],
        "tips": "This is a hip-hinge movement, not a squat. Think about pushing your butt toward the wall behind you.",
        "mistakes_to_avoid": "Rounding your back or turning it into a squat by bending your knees too much."
    },
    "Leg Press": {
        "category": "Leg Exercises",
        "video_url": "https://www.youtube.com/watch?v=IZxyjW7MPJQ",
        "target_muscle": "Quadriceps, Glutes, Hamstrings",
        "equipment": "45-Degree Incline Leg Press Machine",
        "difficulty": "Beginner",
        "instructions": [
            "1. Sit on the machine with your back and head resting comfortably against the padded support.",
            "2. Place feet shoulder-width apart on the sled platform.",
            "3. Release safety pins and lower the sled slowly until knees are bent at 90 degrees.",
            "4. Push through the middle and heels of your feet to press the sled back up.",
            "5. Stop just shy of full knee lockout."
        ],
        "tips": "Higher foot placement targets glutes/hamstrings; lower placement emphasizes quadriceps.",
        "mistakes_to_avoid": "Locking your knees out aggressively at the top or lifting your lower back off pad."
    },
    "Lying Hamstring Leg Curls": {
        "category": "Leg Exercises",
        "video_url": "https://www.youtube.com/watch?v=1Tq3QdYUuHs",
        "target_muscle": "Hamstrings (Biceps Femoris isolation)",
        "equipment": "Lying Leg Curl Machine",
        "difficulty": "Beginner",
        "instructions": [
            "1. Lie face down on the machine with pad resting against the backs of your lower calves.",
            "2. Grasp the handles and keep your hips pressed flat against the bench pad.",
            "3. Curl your heels up toward your glutes in a smooth, powerful motion.",
            "4. Squeeze your hamstrings at the top for 1 second.",
            "5. Lower the weight over 2-3 seconds until legs are fully extended."
        ],
        "tips": "Keep your pelvis anchored to the bench to prevent your lower back from compensating.",
        "mistakes_to_avoid": "Lifting your hips off the pad during the curl."
    },
    "Standing Calf Raises": {
        "category": "Leg Exercises",
        "video_url": "https://www.youtube.com/watch?v=-M4-G8p8fmc",
        "target_muscle": "Gastrocnemius & Soleus (Calves)",
        "equipment": "Standing Calf Machine or Raised Block + Dumbbells",
        "difficulty": "Beginner",
        "instructions": [
            "1. Position the balls of your feet on the step edge with heels hanging off.",
            "2. Lower your heels slowly until you feel a full stretch in your calves (hold 1s).",
            "3. Push through the balls of your feet and raise up as high as possible on your toes.",
            "4. Hold the peak contraction at the very top for 2 seconds, then lower."
        ],
        "tips": "Eliminate bouncing; a slow tempo with pauses produces far superior calf hypertrophy.",
        "mistakes_to_avoid": "Bouncing quickly using the Achilles tendon reflex instead of muscle contraction."
    },

    # =========================================================================
    # 6. ABS & CORE EXERCISES
    # =========================================================================
    "Hanging Leg Raises": {
        "category": "Abs & Core Exercises",
        "video_url": "https://www.youtube.com/watch?v=Pr1ieGZ5tkE",
        "target_muscle": "Lower Rectus Abdominis, Hip Flexors, Grip",
        "equipment": "Pull-up Bar or Captain's Chair",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Hang from a pull-up bar with an overhand grip and legs straight down.",
            "2. Without swinging, curl your pelvis upward and lift your legs toward 90 degrees.",
            "3. Squeeze your abdominal muscles at the top.",
            "4. Lower your legs slowly back to the starting hang without swinging."
        ],
        "tips": "Focus on rolling your pelvis upward toward your sternum, not just lifting legs.",
        "mistakes_to_avoid": "Using swinging momentum to throw your legs up."
    },
    "Bicycle Crunches": {
        "category": "Abs & Core Exercises",
        "video_url": "https://www.youtube.com/watch?v=9FGilxCbdz8",
        "target_muscle": "Obliques and Rectus Abdominis",
        "equipment": "Exercise Mat (Bodyweight)",
        "difficulty": "Beginner",
        "instructions": [
            "1. Lie flat on your back with knees bent and hands lightly behind your head.",
            "2. Lift your shoulder blades off the floor into a crunch position.",
            "3. Bring your right elbow toward your left knee while extending your right leg straight out.",
            "4. Alternate sides in a smooth, continuous pedaling motion."
        ],
        "tips": "Do not yank on your neck; let your torso rotation do the work.",
        "mistakes_to_avoid": "Moving too fast without full muscle contraction on each rotation."
    },
    "Russian Twists": {
        "category": "Abs & Core Exercises",
        "video_url": "https://www.youtube.com/watch?v=wkD8rjkodUI",
        "target_muscle": "Internal & External Obliques, Transverse Abdominis",
        "equipment": "Medicine Ball, Dumbbell, or Bodyweight",
        "difficulty": "Beginner",
        "instructions": [
            "1. Sit on the floor with knees bent and feet slightly elevated off the floor.",
            "2. Lean your torso back roughly 45 degrees to engage your abdominal core.",
            "3. Hold your hands or a weight in front of your chest.",
            "4. Rotate your torso from side to side, touching the weight to the floor on each side."
        ],
        "tips": "Rotate your entire ribcage and shoulders, not just your arms.",
        "mistakes_to_avoid": "Rounding your spine slouching; maintain a proud, braced chest."
    },
    "Forearm Plank": {
        "category": "Abs & Core Exercises",
        "video_url": "https://www.youtube.com/watch?v=ASdvN_XEl_c",
        "target_muscle": "Transverse Abdominis, Core Stability, Glutes",
        "equipment": "Exercise Mat",
        "difficulty": "Beginner",
        "instructions": [
            "1. Place forearms on the floor with elbows directly under shoulders.",
            "2. Extend legs straight back with toes on the floor.",
            "3. Squeeze your glutes, draw your navel in, and keep your body in a straight line.",
            "4. Hold the isometric position while taking controlled, steady breaths."
        ],
        "tips": "Imagine pulling your elbows toward your toes to activate maximum core tension.",
        "mistakes_to_avoid": "Allowing your hips to sag toward the floor or sticking your butt up in the air."
    },

    # =========================================================================
    # 7. GLUTE EXERCISES
    # =========================================================================
    "Barbell Hip Thrust": {
        "category": "Glute Exercises",
        "video_url": "https://www.youtube.com/watch?v=LM8XHLYJoYs",
        "target_muscle": "Gluteus Maximus (Primary Glute Builder)",
        "equipment": "Bench, Barbell, Barbell Pad",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Sit on the floor with your upper back against the edge of a sturdy bench.",
            "2. Roll a padded barbell directly over your hips.",
            "3. Place feet flat on the floor, shoulder-width apart, knees bent at 90 degrees at top.",
            "4. Drive through your heels to thrust hips upward until thighs and torso form a straight line.",
            "5. Squeeze your glutes hard at the top for 1-2 seconds, then lower under control."
        ],
        "tips": "Keep your chin tucked and ribs down to avoid hyperextending your lumbar spine.",
        "mistakes_to_avoid": "Arching your lower back at the top instead of squeezing glutes."
    },
    "Bulgarian Split Squats": {
        "category": "Glute Exercises",
        "video_url": "https://www.youtube.com/watch?v=2C-uNgKwPLE",
        "target_muscle": "Glutes, Quadriceps, Adductors, Balance",
        "equipment": "Flat Bench, Pair of Dumbbells",
        "difficulty": "Intermediate",
        "instructions": [
            "1. Stand 2-3 feet in front of a bench and place the top of one foot on the bench behind you.",
            "2. Hold dumbbells at your sides and maintain a tall, proud chest.",
            "3. Lower your hips down by bending your front knee until the back knee hovers above floor.",
            "4. Drive through the heel of your front foot to return to the starting position."
        ],
        "tips": "A slight forward torso lean places significantly more tension on the glutes.",
        "mistakes_to_avoid": "Pushing off the rear foot; 90% of the work should be done by the front leg."
    },
    "Cable Glute Kickbacks": {
        "category": "Glute Exercises",
        "video_url": "https://www.youtube.com/watch?v=0kF_3tW_z9g",
        "target_muscle": "Gluteus Maximus and Gluteus Medius",
        "equipment": "Cable Machine, Ankle Cuff",
        "difficulty": "Beginner",
        "instructions": [
            "1. Attach an ankle cuff to a low cable pulley and strap it around your ankle.",
            "2. Face the weight stack, holding the frame for support with a slight forward lean.",
            "3. Kick your leg backward in an arc by squeezing your glute.",
            "4. Hold the peak contraction at the top for 1 second.",
            "5. Slowly return your foot to the start without letting the weight stack touch."
        ],
        "tips": "Keep your pelvis square and avoid twisting your hips during the kick.",
        "mistakes_to_avoid": "Swinging your leg with momentum or arching your lower back."
    }
}


# ==============================================================================
# Helper Functions for Application Integration
# ==============================================================================

def get_all_categories():
    """Returns sorted unique category list."""
    categories = set()
    for item in EXERCISE_VIDEO_LIBRARY.values():
        categories.add(item["category"])
    return sorted(list(categories))


def get_exercises_by_category(category_name):
    """Returns list of exercises belonging to a category, or all if 'All'."""
    if not category_name or category_name == "All Categories":
        return list(EXERCISE_VIDEO_LIBRARY.keys())
    
    results = []
    for name, data in EXERCISE_VIDEO_LIBRARY.items():
        if data["category"].lower() == category_name.lower():
            results.append(name)
    return results


def get_exercise_details(exercise_name):
    """Returns detailed dictionary for a single exercise."""
    return EXERCISE_VIDEO_LIBRARY.get(exercise_name, None)


def search_exercises(query):
    """Searches exercises by name, target muscle, or equipment."""
    if not query:
        return list(EXERCISE_VIDEO_LIBRARY.keys())
    
    q = query.strip().lower()
    matches = []
    for name, data in EXERCISE_VIDEO_LIBRARY.items():
        if (q in name.lower() or 
            q in data["target_muscle"].lower() or 
            q in data["category"].lower() or 
            q in data.get("equipment", "").lower()):
            matches.append(name)
    return matches


if __name__ == "__main__":
    print(f"Loaded {len(EXERCISE_VIDEO_LIBRARY)} exercises across {len(get_all_categories())} categories.")
    for cat in get_all_categories():
        count = len(get_exercises_by_category(cat))
        print(f" - {cat}: {count} exercises")

