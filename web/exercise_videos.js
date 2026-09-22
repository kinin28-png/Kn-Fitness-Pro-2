/**
 * ==============================================================================
 * KN FITNESS PRO 2 — EXERCISE VIDEO LIBRARY FOR WEB & MOBILE (SECTION 3)
 * ==============================================================================
 * You can easily EDIT, ADD, or CHANGE video URLs, instructions, and tips here!
 */

const EXERCISE_VIDEO_LIBRARY = {
  // 1. CHEST
  "Incline Barbell Press": {
    category: "Chest Exercises",
    video_url: "https://youtu.be/CTX7pRfoAik?si=C2aKfWS1SMjrq_CY",
    watch_url: "https://www.youtube.com/watch?v=8iPEnn-ltC8",
    target_muscle: "Upper Chest (Clavicular Head) & Front Delts",
    equipment: "Incline Bench, Barbell",
    difficulty: "Intermediate",
    instructions: [
      "Set bench angle to 30-45 degrees.",
      "Grasp barbell slightly wider than shoulder width.",
      "Lower bar smoothly until it touches upper chest.",
      "Press explosively back up without locking elbows harshly."
    ],
    tips: "Retract shoulder blades to protect shoulders.",
    mistakes: "Setting bench too steep (above 45° shifts load to front delts)."
  },
  "Flat Barbell Bench Press": {
    category: "Chest Exercises",
    video_url: "https://www.youtube.com/embed/rT7DgCr-3pg",
    watch_url: "https://www.youtube.com/watch?v=rT7DgCr-3pg",
    target_muscle: "Mid & Lower Chest, Triceps",
    equipment: "Flat Bench, Barbell",
    difficulty: "Intermediate",
    instructions: [
      "Plant feet firmly into floor and grip bar just outside shoulders.",
      "Lower bar with control to mid-chest, elbows at 45-60 degrees.",
      "Drive feet into the floor and press the bar straight up."
    ],
    tips: "Keep glutes on bench and squeeze shoulder blades.",
    mistakes: "Flaring elbows 90 degrees out (causes shoulder pain)."
  },
  "Dumbbell Chest Flys": {
    category: "Chest Exercises",
    video_url: "https://www.youtube.com/embed/eozdVDA78K0",
    watch_url: "https://www.youtube.com/watch?v=eozdVDA78K0",
    target_muscle: "Pectoralis Major (Stretch & Squeeze)",
    equipment: "Dumbbells, Flat Bench",
    difficulty: "Beginner",
    instructions: [
      "Lie flat holding dumbbells above chest with slight elbow bend.",
      "Lower weights out wide until you feel a deep chest stretch.",
      "Bring dumbbells back up in a wide hugging arc."
    ],
    tips: "Focus on the chest stretch at the bottom.",
    mistakes: "Bending elbows too much and turning it into a press."
  },
  "Cable Crossovers": {
    category: "Chest Exercises",
    video_url: "https://www.youtube.com/embed/taI4XduLpBe",
    watch_url: "https://www.youtube.com/watch?v=taI4XduLpBe",
    target_muscle: "Inner & Lower Chest",
    equipment: "Cable Machine, D-handles",
    difficulty: "Intermediate",
    instructions: [
      "Set pulleys at or above shoulder height and lean forward slightly.",
      "Bring handles forward and down in a wide hugging motion.",
      "Cross hands slightly at bottom for peak contraction."
    ],
    tips: "Control the eccentric return; don't let weights slam.",
    mistakes: "Using body momentum to swing the cables."
  },
  "Chest Dips": {
    category: "Chest Exercises",
    video_url: "https://www.youtube.com/embed/2z8JmcrW-As",
    watch_url: "https://www.youtube.com/watch?v=2z8JmcrW-As",
    target_muscle: "Lower Chest & Triceps",
    equipment: "Parallel Dip Bars",
    difficulty: "Advanced",
    instructions: [
      "Grip dip bars, lean torso forward 30 degrees.",
      "Lower body until elbows are at 90 degrees.",
      "Press through chest and triceps back to top."
    ],
    tips: "Lean forward to target chest rather than just triceps.",
    mistakes: "Dropping down too low if shoulder mobility is limited."
  },

  // 2. BACK
  "Lat Pulldowns": {
    category: "Back Exercises",
    video_url: "https://www.youtube.com/embed/CAwf7n6Luuc",
    watch_url: "https://www.youtube.com/watch?v=CAwf7n6Luuc",
    target_muscle: "Latissimus Dorsi (Back Width)",
    equipment: "Lat Pulldown Cable Machine",
    difficulty: "Beginner",
    instructions: [
      "Grip wide bar with overhand grip and sit with thighs secured.",
      "Lean back slightly (10-15°) with chest high.",
      "Pull bar down to upper chest by driving elbows down and back.",
      "Slowly raise bar back up to full stretch."
    ],
    tips: "Pull through your elbows, not just with your hands.",
    mistakes: "Swinging your lower back to use momentum."
  },
  "Barbell Bent-Over Row": {
    category: "Back Exercises",
    video_url: "https://www.youtube.com/embed/FWJR5Ve8gkQ",
    watch_url: "https://www.youtube.com/watch?v=FWJR5Ve8gkQ",
    target_muscle: "Rhomboids, Lats, Mid Traps",
    equipment: "Barbell, Plates",
    difficulty: "Intermediate",
    instructions: [
      "Hinge at hips with a flat back until torso is 45° or parallel.",
      "Pull bar up toward lower ribcage / navel.",
      "Squeeze shoulder blades together at top, lower smoothly."
    ],
    tips: "Brace core tightly to protect lumbar spine.",
    mistakes: "Rounding lower back or standing too upright."
  },
  "Seated Cable Row": {
    category: "Back Exercises",
    video_url: "https://www.youtube.com/embed/GZbfZ033f74",
    watch_url: "https://www.youtube.com/watch?v=GZbfZ033f74",
    target_muscle: "Mid Back, Rhomboids, Rear Delts",
    equipment: "Cable Row Station, V-bar",
    difficulty: "Beginner",
    instructions: [
      "Sit upright with feet on footplates and knees softly bent.",
      "Pull handle into lower ribcage while keeping chest proud.",
      "Squeeze shoulder blades, then return with control."
    ],
    tips: "Keep torso steady; do not rock back and forth.",
    mistakes: "Jerking weight backward with lower back."
  },
  "Pull-ups / Chin-ups": {
    category: "Back Exercises",
    video_url: "https://www.youtube.com/embed/eGo4IYlbE5g",
    watch_url: "https://www.youtube.com/watch?v=eGo4IYlbE5g",
    target_muscle: "Lats, Upper Back, Biceps",
    equipment: "Pull-up Bar",
    difficulty: "Advanced",
    instructions: [
      "Hang from bar with overhand grip wider than shoulders.",
      "Pull elbows down toward ribs until chin clears the bar.",
      "Lower under control to full arm hang."
    ],
    tips: "Engage lats before bending arms at bottom.",
    mistakes: "Kicking legs or kipping to swing up."
  },
  "Conventional Deadlift": {
    category: "Back Exercises",
    video_url: "https://www.youtube.com/embed/op9kVnSso6Q",
    watch_url: "https://www.youtube.com/watch?v=op9kVnSso6Q",
    target_muscle: "Entire Posterior Chain, Glutes, Erector Spinae",
    equipment: "Olympic Barbell, Plates",
    difficulty: "Advanced",
    instructions: [
      "Stand with feet hip-width apart, bar over midfoot.",
      "Hinge hips, grip bar just outside knees, chest tall.",
      "Drive floor away with legs, extend hips and knees together.",
      "Stand tall with glutes squeezed at top."
    ],
    tips: "Keep bar dragging against shins and thighs.",
    mistakes: "Rounding the lower spine."
  },

  // 3. ARMS
  "Barbell Bicep Curl": {
    category: "Arm Exercises",
    video_url: "https://www.youtube.com/embed/kwG2ipFRgfo",
    watch_url: "https://www.youtube.com/watch?v=kwG2ipFRgfo",
    target_muscle: "Biceps Brachii",
    equipment: "Barbell or EZ-Bar",
    difficulty: "Beginner",
    instructions: [
      "Stand tall with underhand grip and elbows pinned to ribs.",
      "Curl bar upward to chest level by contracting biceps.",
      "Hold squeeze 1 second, lower under control."
    ],
    tips: "Only forearms should move; keep upper arms fixed.",
    mistakes: "Swinging hips or leaning backward."
  },
  "Dumbbell Hammer Curls": {
    category: "Arm Exercises",
    video_url: "https://www.youtube.com/embed/zC3nLlEvin4",
    watch_url: "https://www.youtube.com/watch?v=zC3nLlEvin4",
    target_muscle: "Brachialis & Forearms",
    equipment: "Pair of Dumbbells",
    difficulty: "Beginner",
    instructions: [
      "Hold dumbbells with palms facing inward (neutral grip).",
      "Curl weights upward while maintaining neutral grip.",
      "Squeeze forearms and outer bicep at the top."
    ],
    tips: "Builds arm thickness and pushes bicep peak up.",
    mistakes: "Rotating wrists during the curl."
  },
  "Triceps Rope Pushdowns": {
    category: "Arm Exercises",
    video_url: "https://www.youtube.com/embed/vB5OHsJ3EME",
    watch_url: "https://www.youtube.com/watch?v=vB5OHsJ3EME",
    target_muscle: "Triceps Lateral & Medial Heads",
    equipment: "Cable Machine, Rope",
    difficulty: "Beginner",
    instructions: [
      "Grip rope handles, pin elbows to ribs, lean slightly forward.",
      "Push rope straight down until arms are fully extended.",
      "Spread rope ends apart at the bottom for extra peak contraction."
    ],
    tips: "Lock elbows in place without letting them drift forward.",
    mistakes: "Flaring elbows out to the sides."
  },
  "Skull Crushers": {
    category: "Arm Exercises",
    video_url: "https://www.youtube.com/embed/d_KZxkY_0cM",
    watch_url: "https://www.youtube.com/watch?v=d_KZxkY_0cM",
    target_muscle: "Triceps Long Head",
    equipment: "Bench, EZ-Bar or Dumbbells",
    difficulty: "Intermediate",
    instructions: [
      "Lie on bench holding bar above chest, angle arms slightly back.",
      "Bend elbows and lower weight toward top of forehead.",
      "Extend elbows back to starting position."
    ],
    tips: "Angling upper arms backward maintains constant tension.",
    mistakes: "Letting elbows flare outwards."
  },

  // 4. SHOULDERS
  "Overhead Dumbbell Press": {
    category: "Shoulder Exercises",
    video_url: "https://www.youtube.com/embed/qEwKCR5JCog",
    watch_url: "https://www.youtube.com/watch?v=qEwKCR5JCog",
    target_muscle: "Front & Side Deltoids",
    equipment: "Upright Bench, Dumbbells",
    difficulty: "Intermediate",
    instructions: [
      "Hold dumbbells at shoulder height with palms facing forward.",
      "Press dumbbells upward in an arc until arms are extended overhead.",
      "Lower smoothly back to ear/shoulder level."
    ],
    tips: "Brace core to prevent arching your lower back.",
    mistakes: "Clanking dumbbells together violently at top."
  },
  "Dumbbell Lateral Raises": {
    category: "Shoulder Exercises",
    video_url: "https://www.youtube.com/embed/3VcKaXpzqRo",
    watch_url: "https://www.youtube.com/watch?v=3VcKaXpzqRo",
    target_muscle: "Lateral Deltoids (Shoulder Width)",
    equipment: "Light Dumbbells",
    difficulty: "Beginner",
    instructions: [
      "Stand with light dumbbells at sides, slight hinge at hips.",
      "Raise arms out to sides leading with your elbows.",
      "Stop when arms reach parallel to floor, lower over 2 seconds."
    ],
    tips: "Lead with elbows and pinkies for maximum delt engagement.",
    mistakes: "Using heavy weights and swinging body."
  },
  "Face Pulls": {
    category: "Shoulder Exercises",
    video_url: "https://www.youtube.com/embed/rep-qVOkqgk",
    watch_url: "https://www.youtube.com/watch?v=rep-qVOkqgk",
    target_muscle: "Rear Deltoids & Rotator Cuff",
    equipment: "Cable Machine, Rope",
    difficulty: "Beginner",
    instructions: [
      "Set cable to eye level, grip rope with overhand grip.",
      "Pull rope straight toward bridge of nose, pulling hands wide apart.",
      "Hold squeeze for 1 second, then return slowly."
    ],
    tips: "Essential for healthy shoulders and good posture.",
    mistakes: "Pulling rope down to chin instead of nose."
  },

  // 5. LEGS
  "Barbell Back Squat": {
    category: "Leg Exercises",
    video_url: "https://www.youtube.com/embed/bEv6CCg2BC8",
    watch_url: "https://www.youtube.com/watch?v=bEv6CCg2BC8",
    target_muscle: "Quadriceps, Glutes, Hamstrings",
    equipment: "Squat Rack, Barbell",
    difficulty: "Advanced",
    instructions: [
      "Rest bar across upper traps, feet shoulder-width, toes slightly out.",
      "Inhale, brace core, sit hips down and push knees out.",
      "Descend to parallel or below, drive up through midfoot."
    ],
    tips: "Keep chest tall and knees tracking in line with toes.",
    mistakes: "Knees caving inwards on the way up."
  },
  "Romanian Deadlift (RDL)": {
    category: "Leg Exercises",
    video_url: "https://www.youtube.com/embed/JCXUYuzwNrM",
    watch_url: "https://www.youtube.com/watch?v=JCXUYuzwNrM",
    target_muscle: "Hamstrings, Glutes",
    equipment: "Barbell or Dumbbells",
    difficulty: "Intermediate",
    instructions: [
      "Hold weight at hips with soft bend in knees.",
      "Hinge hips backward while keeping bar close to legs.",
      "Lower to mid-shins feeling deep hamstring stretch, squeeze glutes to stand."
    ],
    tips: "Push hips straight back like touching a wall behind you.",
    mistakes: "Squatting instead of hinging at hips."
  },
  "Leg Press": {
    category: "Leg Exercises",
    video_url: "https://www.youtube.com/embed/IZxyjW7MPJQ",
    watch_url: "https://www.youtube.com/watch?v=IZxyjW7MPJQ",
    target_muscle: "Quadriceps, Glutes",
    equipment: "Leg Press Machine",
    difficulty: "Beginner",
    instructions: [
      "Place feet shoulder-width on platform, release safety handles.",
      "Lower sled until knees are bent 90 degrees.",
      "Press through midfoot and heels back up without locking knees."
    ],
    tips: "Place feet higher on plate to hit more glutes and hamstrings.",
    mistakes: "Locking knees aggressively at top."
  },

  // 6. ABS & CORE
  "Hanging Leg Raises": {
    category: "Abs & Core Exercises",
    video_url: "https://www.youtube.com/embed/Pr1ieGZ5tkE",
    watch_url: "https://www.youtube.com/watch?v=Pr1ieGZ5tkE",
    target_muscle: "Lower Abs & Hip Flexors",
    equipment: "Pull-up Bar",
    difficulty: "Intermediate",
    instructions: [
      "Hang from pull-up bar with legs straight.",
      "Curl pelvis upward and raise legs toward 90 degrees without swinging.",
      "Squeeze abs at top, lower slowly."
    ],
    tips: "Roll pelvis up toward ribs for real ab contraction.",
    mistakes: "Using swinging momentum to fling legs up."
  },
  "Bicycle Crunches": {
    category: "Abs & Core Exercises",
    video_url: "https://www.youtube.com/embed/9FGilxCbdz8",
    watch_url: "https://www.youtube.com/watch?v=9FGilxCbdz8",
    target_muscle: "Obliques & Rectus Abdominis",
    equipment: "Exercise Mat",
    difficulty: "Beginner",
    instructions: [
      "Lie on back with knees bent and hands behind head.",
      "Bring right elbow toward left knee while extending right leg straight.",
      "Alternate sides in smooth, controlled pedaling motion."
    ],
    tips: "Rotate shoulders and ribcage, do not pull on neck.",
    mistakes: "Going too fast without pausing to squeeze."
  },
  "Forearm Plank": {
    category: "Abs & Core Exercises",
    video_url: "https://www.youtube.com/embed/ASdvN_XEl_c",
    watch_url: "https://www.youtube.com/watch?v=ASdvN_XEl_c",
    target_muscle: "Transverse Abdominis, Core Stability",
    equipment: "Exercise Mat",
    difficulty: "Beginner",
    instructions: [
      "Place forearms on floor, elbows under shoulders.",
      "Extend legs back, squeeze glutes, pull belly button inward.",
      "Hold rigid straight line from head to heels."
    ],
    tips: "Pull elbows toward toes isometrically to amplify core tension.",
    mistakes: "Letting lower back sag toward floor."
  },

  // 7. GLUTES
  "Barbell Hip Thrust": {
    category: "Glute Exercises",
    video_url: "https://www.youtube.com/embed/LM8XHLYJoYs",
    watch_url: "https://www.youtube.com/watch?v=LM8XHLYJoYs",
    target_muscle: "Gluteus Maximus (Primary Glute Mass)",
    equipment: "Bench, Barbell, Pad",
    difficulty: "Intermediate",
    instructions: [
      "Upper back against sturdy bench, padded bar over hips.",
      "Feet flat on floor, drive through heels to thrust hips upward.",
      "Form straight line from knees to shoulders, hold top squeeze 2s."
    ],
    tips: "Keep chin tucked toward chest to prevent hyperextending back.",
    mistakes: "Arching lower back instead of squeezing glutes."
  },
  "Bulgarian Split Squats": {
    category: "Glute Exercises",
    video_url: "https://www.youtube.com/embed/2C-uNgKwPLE",
    watch_url: "https://www.youtube.com/watch?v=2C-uNgKwPLE",
    target_muscle: "Glutes, Quads, Balance",
    equipment: "Bench, Dumbbells",
    difficulty: "Intermediate",
    instructions: [
      "Stand 2-3 feet in front of bench, place one foot top-down on bench behind you.",
      "Lower hips down until back knee hovers above floor.",
      "Drive through front heel to return to top."
    ],
    tips: "Lean torso slightly forward to bias tension onto front glute.",
    mistakes: "Pushing off rear foot instead of driving through front leg."
  },
  "Cable Glute Kickbacks": {
    category: "Glute Exercises",
    video_url: "https://www.youtube.com/embed/0kF_3tW_z9g",
    watch_url: "https://www.youtube.com/watch?v=0kF_3tW_z9g",
    target_muscle: "Gluteus Maximus & Medius",
    equipment: "Cable Machine, Ankle Strap",
    difficulty: "Beginner",
    instructions: [
      "Attach cuff to ankle from low cable pulley.",
      "Lean forward slightly, kick leg backward in an arc using glute.",
      "Hold peak squeeze 1 second, slowly return."
    ],
    tips: "Keep hips square; do not twist pelvis as leg kicks back.",
    mistakes: "Arching lower back to swing leg."
  }
};

