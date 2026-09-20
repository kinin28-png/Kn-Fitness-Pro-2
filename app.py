import sys
import os

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QFrame,
    QScrollArea,
    QTabWidget,
    QDialog,
    QDialogButtonBox
)
from PySide6.QtGui import QIcon, QFont, QDesktopServices
from PySide6.QtCore import Qt, QUrl

from workout import get_workout_details
from exercise_videos import (
    EXERCISE_VIDEO_LIBRARY,
    get_all_categories,
    get_exercises_by_category,
    get_exercise_details,
    search_exercises
)


# ==============================================================================
# SECTION 3: VIDEO INSTRUCTION DEMO DIALOG MODAL
# ==============================================================================
class ExerciseDemoDialog(QDialog):
    """Popup modal showing video link, target muscles, instructions, and pro tips.
    Data is loaded from the separate exercise_videos.py file.
    """
    def __init__(self, exercise_name, parent=None):
        super().__init__(parent)
        self.exercise_name = exercise_name
        self.data = get_exercise_details(exercise_name) or {}

        self.setWindowTitle(f"Exercise Demo — {exercise_name}")
        self.setMinimumSize(620, 560)
        self.resize(700, 620)
        self.setStyleSheet("""
            QDialog {
                background-color: #101418;
                color: #F5F7FA;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            }
            QLabel {
                color: #DCE2E7;
            }
            QFrame#card {
                background-color: #181E24;
                border: 1px solid #28333D;
                border-radius: 12px;
                padding: 16px;
            }
            QFrame#tip_card {
                background-color: #13241A;
                border: 1px solid #245A36;
                border-radius: 10px;
                padding: 12px;
            }
            QFrame#mistake_card {
                background-color: #261617;
                border: 1px solid #5A272A;
                border-radius: 10px;
                padding: 12px;
            }
            QPushButton#play_button {
                background-color: #35E06F;
                color: #0E171E;
                font-size: 15px;
                font-weight: 800;
                border-radius: 10px;
                padding: 14px 20px;
                border: none;
            }
            QPushButton#play_button:hover {
                background-color: #55EE8B;
            }
            QPushButton#close_btn {
                background-color: #222B34;
                color: #CFD8DC;
                border: 1px solid #364452;
                border-radius: 8px;
                padding: 8px 18px;
                font-weight: 600;
            }
            QPushButton#close_btn:hover {
                background-color: #2D3A47;
                color: #FFFFFF;
            }
            QScrollArea {
                border: none;
                background-color: #101418;
            }
        """)

        self.init_ui()

    def init_ui(self):
        dialog_layout = QVBoxLayout(self)
        dialog_layout.setContentsMargins(20, 20, 20, 20)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setSpacing(14)

        # Header Title
        title = QLabel(self.exercise_name)
        title.setStyleSheet("font-size: 24px; font-weight: 800; color: #35E06F;")
        layout.addWidget(title)

        # Category and badges
        category = self.data.get("category", "General")
        target_muscle = self.data.get("target_muscle", "Full Body")
        equipment = self.data.get("equipment", "Standard")
        difficulty = self.data.get("difficulty", "Intermediate")

        badge_bar = QHBoxLayout()
        badge_bar.setSpacing(10)

        cat_badge = QLabel(f"🏷️ {category}")
        cat_badge.setStyleSheet("background: #1F2730; padding: 4px 10px; border-radius: 6px; font-size: 12px; color: #9AA4AE; font-weight: bold;")
        badge_bar.addWidget(cat_badge)

        diff_badge = QLabel(f"⚡ {difficulty}")
        diff_badge.setStyleSheet("background: rgba(53, 224, 111, 0.15); padding: 4px 10px; border-radius: 6px; font-size: 12px; color: #35E06F; font-weight: bold; border: 1px solid #35E06F;")
        badge_bar.addWidget(diff_badge)

        badge_bar.addStretch()
        layout.addLayout(badge_bar)

        # Target Muscle & Equipment info card
        info_card = QFrame()
        info_card.setObjectName("card")
        info_layout = QVBoxLayout(info_card)
        info_layout.setSpacing(6)

        m_label = QLabel(f"<b>🎯 Primary Target Muscle:</b> {target_muscle}")
        m_label.setStyleSheet("font-size: 14px; color: #ECEFF1;")
        info_layout.addWidget(m_label)

        eq_label = QLabel(f"<b>🏋️ Equipment Required:</b> {equipment}")
        eq_label.setStyleSheet("font-size: 13px; color: #9AA4AE;")
        info_layout.addWidget(eq_label)
        layout.addWidget(info_card)

        # Big Video Demo Button (Supports both YouTube links and local files in src/videos/)
        video_url = self.data.get("video_url", "https://www.youtube.com")
        is_web = video_url.startswith("http://") or video_url.startswith("https://")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        local_full_path = os.path.normpath(os.path.join(base_dir, video_url)) if not is_web else None
        file_exists = os.path.exists(local_full_path) if local_full_path else False

        if is_web:
            btn_text = "▶️ WATCH VIDEO DEMO ON YOUTUBE"
            caption_text = f"Demo Link: <a href='{video_url}' style='color: #40C4FF;'>{video_url}</a>"
        else:
            if file_exists:
                btn_text = "▶️ PLAY LOCAL VIDEO DEMO"
                caption_text = f"📁 Local Video: <span style='color:#35E06F;'>{video_url} (Ready)</span>"
            else:
                btn_text = "▶️ PLAY LOCAL VIDEO DEMO"
                caption_text = f"📁 Local Video: <span style='color:#FFB020;'>{video_url} (Place .mp4 in src/videos/)</span>"

        play_button = QPushButton(btn_text)
        play_button.setObjectName("play_button")
        play_button.setCursor(Qt.PointingHandCursor)
        play_button.clicked.connect(lambda: self.launch_video(video_url, is_web, local_full_path))
        layout.addWidget(play_button)

        url_caption = QLabel(caption_text)
        url_caption.setOpenExternalLinks(True)
        url_caption.setStyleSheet("font-size: 11px; color: #78909C;")
        layout.addWidget(url_caption)

        # Step-by-step instructions
        inst_title = QLabel("📝 STEP-BY-STEP TECHNIQUE INSTRUCTIONS")
        inst_title.setStyleSheet("font-size: 15px; font-weight: 700; color: #35E06F; margin-top: 6px;")
        layout.addWidget(inst_title)

        inst_card = QFrame()
        inst_card.setObjectName("card")
        inst_layout = QVBoxLayout(inst_card)
        inst_layout.setSpacing(8)

        instructions = self.data.get("instructions", ["Perform with controlled tempo."])
        for step in instructions:
            step_lbl = QLabel(step)
            step_lbl.setWordWrap(True)
            step_lbl.setStyleSheet("font-size: 13px; color: #ECEFF1; line-height: 1.4;")
            inst_layout.addWidget(step_lbl)
        layout.addWidget(inst_card)

        # Coaching Tips
        tips_text = self.data.get("tips", "Focus on mind-muscle connection.")
        tip_card = QFrame()
        tip_card.setObjectName("tip_card")
        tip_layout = QVBoxLayout(tip_card)
        tip_title = QLabel("💡 PRO COACHING TIP")
        tip_title.setStyleSheet("font-size: 12px; font-weight: 800; color: #55EE8B; letter-spacing: 0.5px;")
        tip_body = QLabel(tips_text)
        tip_body.setWordWrap(True)
        tip_body.setStyleSheet("font-size: 13px; color: #E8F5E9;")
        tip_layout.addWidget(tip_title)
        tip_layout.addWidget(tip_body)
        layout.addWidget(tip_card)

        # Mistakes to avoid
        mistake_text = self.data.get("mistakes_to_avoid", "Avoid using excessive swinging momentum.")
        mistake_card = QFrame()
        mistake_card.setObjectName("mistake_card")
        mistake_layout = QVBoxLayout(mistake_card)
        mistake_title = QLabel("⚠️ COMMON MISTAKE TO AVOID")
        mistake_title.setStyleSheet("font-size: 12px; font-weight: 800; color: #FF8A80; letter-spacing: 0.5px;")
        mistake_body = QLabel(mistake_text)
        mistake_body.setWordWrap(True)
        mistake_body.setStyleSheet("font-size: 13px; color: #FFEBEE;")
        mistake_layout.addWidget(mistake_title)
        mistake_layout.addWidget(mistake_body)
        layout.addWidget(mistake_card)

        # Customization notice
        note = QLabel("✏️ <i>You can edit video URLs and instructions anytime in <b>exercise_videos.py</b></i>")
        note.setStyleSheet("font-size: 11px; color: #78909C; margin-top: 6px;")
        layout.addWidget(note)

        scroll.setWidget(container)
        dialog_layout.addWidget(scroll)

        # Bottom close button
        btn_bar = QHBoxLayout()
        btn_bar.addStretch()
        close_btn = QPushButton("Close")
        close_btn.setObjectName("close_btn")
        close_btn.clicked.connect(self.accept)
        btn_bar.addWidget(close_btn)
        dialog_layout.addLayout(btn_bar)

    def launch_video(self, video_url, is_web, local_full_path):
        if is_web:
            QDesktopServices.openUrl(QUrl(video_url))
        else:
            if local_full_path and os.path.exists(local_full_path):
                QDesktopServices.openUrl(QUrl.fromLocalFile(local_full_path))
            elif os.path.exists(video_url):
                QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.abspath(video_url)))
            else:
                QDesktopServices.openUrl(QUrl.fromLocalFile(local_full_path or video_url))



# ==============================================================================
# MAIN APPLICATION WINDOW
# ==============================================================================
class FitnessApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kn Gym Assistant - Fitness Pro 2")
        self.setMinimumSize(900, 650)
        self.resize(1150, 800)

        # Set Window Icon
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "kn_fitness_pro.png")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 12, 15, 15)
        main_layout.setSpacing(10)

        # App Header Banner
        header = QHBoxLayout()
        header_text = QVBoxLayout()
        header_text.setSpacing(2)

        title = QLabel("KN GYM ASSISTANT")
        title.setObjectName("title")

        subtitle = QLabel("Personal Fitness & Workout Assistant • Multi-Device Edition")
        subtitle.setObjectName("subtitle")

        header_text.addWidget(title)
        header_text.addWidget(subtitle)
        header.addLayout(header_text)
        header.addStretch()

        main_layout.addLayout(header)

        # =====================================================================
        # TOP NAVIGATION TABS (Completely isolates Sections 1 & 2 from Section 3)
        # =====================================================================
        self.tabs = QTabWidget()
        self.tabs.setObjectName("main_tabs")

        # TAB 1: SECTION 1 (Calculator) & SECTION 2 (Daily Workout Routine)
        tab1_widget = self.create_calculator_and_workout_tab()
        self.tabs.addTab(tab1_widget, "📊  SECTION 1 & 2: FITNESS PLAN & CALCULATOR")

        # TAB 2: SECTION 3 (Exercise Categories & Video Demos)
        tab2_widget = self.create_exercise_categories_tab()
        self.tabs.addTab(tab2_widget, "🎬  SECTION 3: EXERCISE CATEGORIES & VIDEO DEMOS")

        main_layout.addWidget(self.tabs)

        # Apply Global Stylesheet
        self.apply_styles()

        # Initial workout table preview
        self.update_workout_table("Build Muscle", "Day 1")

    # =========================================================================
    # TAB 1: SECTIONS 1 & 2 (FITNESS CALCULATOR & ROUTINES)
    # =========================================================================
    def create_calculator_and_workout_tab(self):
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(15, 15, 15, 15)
        container_layout.setSpacing(16)

        # 2-Column Responsive Body Layout
        body_layout = QHBoxLayout()
        body_layout.setSpacing(20)

        # LEFT COLUMN: User Inputs
        left_column = QVBoxLayout()
        left_column.setSpacing(12)

        input_card = QFrame()
        input_card.setObjectName("card")
        input_card_layout = QVBoxLayout(input_card)
        input_card_layout.setSpacing(8)
        input_card_layout.setContentsMargins(18, 16, 18, 16)

        card_title = QLabel("USER INFORMATION (SECTION 1)")
        card_title.setObjectName("section_title")
        input_card_layout.addWidget(card_title)

        # Name
        input_card_layout.addWidget(QLabel("Name"))
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        input_card_layout.addWidget(self.name_input)

        # Weight & Height
        dim_layout = QHBoxLayout()
        dim_layout.setSpacing(10)

        w_layout = QVBoxLayout()
        w_layout.setSpacing(4)
        w_layout.addWidget(QLabel("Weight (kg)"))
        self.weight_input = QLineEdit()
        self.weight_input.setPlaceholderText("e.g. 70")
        w_layout.addWidget(self.weight_input)
        dim_layout.addLayout(w_layout)

        h_layout = QVBoxLayout()
        h_layout.setSpacing(4)
        h_layout.addWidget(QLabel("Height (m)"))
        self.height_input = QLineEdit()
        self.height_input.setPlaceholderText("e.g. 1.75")
        h_layout.addWidget(self.height_input)
        dim_layout.addLayout(h_layout)

        input_card_layout.addLayout(dim_layout)

        # Age & Gender
        ag_layout = QHBoxLayout()
        ag_layout.setSpacing(10)

        age_box = QVBoxLayout()
        age_box.setSpacing(4)
        age_box.addWidget(QLabel("Age"))
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("e.g. 28")
        age_box.addWidget(self.age_input)
        ag_layout.addLayout(age_box)

        gender_box = QVBoxLayout()
        gender_box.setSpacing(4)
        gender_box.addWidget(QLabel("Gender"))
        self.gender_select = QComboBox()
        self.gender_select.addItems(["Male", "Female"])
        gender_box.addWidget(self.gender_select)
        ag_layout.addLayout(gender_box)

        input_card_layout.addLayout(ag_layout)

        # Goal
        input_card_layout.addWidget(QLabel("Fitness Goal"))
        self.goal_input = QComboBox()
        self.goal_input.addItems([
            "Build Muscle",
            "Lose Weight",
            "Maintain Weight"
        ])
        input_card_layout.addWidget(self.goal_input)

        # Activity Level
        input_card_layout.addWidget(QLabel("Activity Level"))
        self.activity_input = QComboBox()
        self.activity_input.addItems([
            "Sedentary (little/no exercise)",
            "Lightly Active (1-3 days/wk)",
            "Moderately Active (3-5 days/wk)",
            "Active (6-7 days/wk)",
            "Very Active (twice per day)"
        ])
        input_card_layout.addWidget(self.activity_input)

        # Workout Day
        input_card_layout.addWidget(QLabel("Workout Day (Section 2)"))
        self.day_select = QComboBox()
        self.day_select.addItems(["Day 1", "Day 2", "Day 3", "Day 4"])
        input_card_layout.addWidget(self.day_select)

        self.goal_input.currentIndexChanged.connect(self.on_plan_params_changed)
        self.day_select.currentIndexChanged.connect(self.on_plan_params_changed)

        left_column.addWidget(input_card)

        # Action Buttons
        self.calculate_button = QPushButton("CALCULATE FITNESS PLAN")
        self.calculate_button.setObjectName("calculate_button")
        self.calculate_button.clicked.connect(self.calculate)
        left_column.addWidget(self.calculate_button)

        self.reset_button = QPushButton("Reset Form")
        self.reset_button.setObjectName("secondary_button")
        self.reset_button.clicked.connect(self.reset_form)
        left_column.addWidget(self.reset_button)

        left_column.addStretch()
        body_layout.addLayout(left_column, 4)

        # RIGHT COLUMN: Results & Section 2 Table
        right_column = QVBoxLayout()
        right_column.setSpacing(14)

        # Result Card
        result_card = QFrame()
        result_card.setObjectName("result_card")
        result_layout = QVBoxLayout(result_card)
        result_layout.setSpacing(8)
        result_layout.setContentsMargins(18, 16, 18, 16)

        result_title = QLabel("YOUR FITNESS RESULTS")
        result_title.setObjectName("section_title")
        result_layout.addWidget(result_title)

        self.result = QLabel("Fill in your details and click 'CALCULATE FITNESS PLAN' to generate your custom metrics and routine.")
        self.result.setObjectName("result")
        self.result.setWordWrap(True)
        result_layout.addWidget(self.result)

        right_column.addWidget(result_card)

        # Workout Title
        self.workout_title = QLabel("WORKOUT PLAN (SECTION 2)")
        self.workout_title.setObjectName("section_title")
        right_column.addWidget(self.workout_title)

        # Workout Table
        self.workout_table = QTableWidget()
        self.workout_table.setColumnCount(5)
        self.workout_table.setHorizontalHeaderLabels([
            "Exercise",
            "Sets",
            "Reps",
            "Rest",
            "Tips"
        ])
        self.workout_table.setMinimumHeight(280)
        self.workout_table.setAlternatingRowColors(True)
        self.workout_table.setWordWrap(True)

        header = self.workout_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

        self.workout_table.verticalHeader().setDefaultSectionSize(42)
        right_column.addWidget(self.workout_table)

        body_layout.addLayout(right_column, 6)
        container_layout.addLayout(body_layout)

        scroll_area.setWidget(container)
        return scroll_area

    # =========================================================================
    # TAB 2: SECTION 3 (EXERCISE CATEGORIES & VIDEO DEMOS)
    # =========================================================================
    def create_exercise_categories_tab(self):
        """Independent Section 3: Browse exercises by category, search, and click
        to open video instruction demos. Does NOT involve Section 1 & 2.
        """
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 16, 20, 20)
        layout.setSpacing(14)

        # Section 3 Header Card
        header_card = QFrame()
        header_card.setObjectName("card")
        header_card_layout = QVBoxLayout(header_card)
        header_card_layout.setSpacing(6)

        sec3_title = QLabel("🎬 EXERCISE CATEGORIES & VIDEO DEMO LIBRARY")
        sec3_title.setObjectName("section_title")
        header_card_layout.addWidget(sec3_title)

        sec3_sub = QLabel("Select an exercise category below to view video demonstrations, target muscles, and step-by-step coaching form.")
        sec3_sub.setStyleSheet("font-size: 13px; color: #8C9BAE;")
        header_card_layout.addWidget(sec3_sub)
        layout.addWidget(header_card)

        # Filters Bar (Category Dropdown + Search Input)
        filter_bar = QHBoxLayout()
        filter_bar.setSpacing(12)

        cat_lbl = QLabel("Category:")
        cat_lbl.setStyleSheet("font-weight: bold; color: #35E06F;")
        filter_bar.addWidget(cat_lbl)

        self.category_combo = QComboBox()
        self.category_combo.addItem("All Categories")
        for cat in get_all_categories():
            self.category_combo.addItem(cat)
        self.category_combo.currentIndexChanged.connect(self.filter_exercise_library)
        filter_bar.addWidget(self.category_combo, 2)

        search_lbl = QLabel("Search:")
        search_lbl.setStyleSheet("font-weight: bold; color: #35E06F;")
        filter_bar.addWidget(search_lbl)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search exercise, muscle, or equipment...")
        self.search_input.textChanged.connect(self.filter_exercise_library)
        filter_bar.addWidget(self.search_input, 3)

        layout.addLayout(filter_bar)

        # Quick Category Pills Bar
        pills_layout = QHBoxLayout()
        pills_layout.setSpacing(6)

        quick_cats = ["All Categories", "Chest Exercises", "Back Exercises", "Arm Exercises", "Shoulder Exercises", "Leg Exercises", "Abs & Core Exercises", "Glute Exercises"]
        for qc in quick_cats:
            btn = QPushButton(qc.replace(" Exercises", ""))
            btn.setObjectName("secondary_button")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, c=qc: self.select_quick_category(c))
            pills_layout.addWidget(btn)

        layout.addLayout(pills_layout)

        # Section 3 Exercise Table
        self.library_table = QTableWidget()
        self.library_table.setColumnCount(5)
        self.library_table.setHorizontalHeaderLabels([
            "Exercise Name",
            "Category",
            "Target Muscle",
            "Equipment",
            "Video Demo"
        ])
        self.library_table.setAlternatingRowColors(True)
        self.library_table.setWordWrap(True)

        header = self.library_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

        self.library_table.verticalHeader().setDefaultSectionSize(48)
        self.library_table.cellDoubleClicked.connect(self.on_table_row_double_clicked)
        layout.addWidget(self.library_table)

        # Initial populate
        self.populate_library_table(list(EXERCISE_VIDEO_LIBRARY.keys()))

        return container

    def select_quick_category(self, cat_name):
        idx = self.category_combo.findText(cat_name)
        if idx >= 0:
            self.category_combo.setCurrentIndex(idx)
        else:
            self.category_combo.setCurrentIndex(0)

    def filter_exercise_library(self):
        selected_cat = self.category_combo.currentText()
        query = self.search_input.text().strip()

        # Step 1: Category filter
        cat_matches = get_exercises_by_category(selected_cat)

        # Step 2: Query filter
        if query:
            query_matches = search_exercises(query)
            final_matches = [name for name in cat_matches if name in query_matches]
        else:
            final_matches = cat_matches

        self.populate_library_table(final_matches)

    def populate_library_table(self, exercise_names):
        self.library_table.setRowCount(0)
        self.library_table.setRowCount(len(exercise_names))

        for row, name in enumerate(exercise_names):
            data = get_exercise_details(name) or {}

            # 0. Name
            name_item = QTableWidgetItem(name)
            name_item.setFont(QFont("Arial", 10, QFont.Bold))
            self.library_table.setItem(row, 0, name_item)

            # 1. Category
            cat_item = QTableWidgetItem(data.get("category", ""))
            self.library_table.setItem(row, 1, cat_item)

            # 2. Target Muscle
            muscle_item = QTableWidgetItem(data.get("target_muscle", ""))
            self.library_table.setItem(row, 2, muscle_item)

            # 3. Equipment
            eq_item = QTableWidgetItem(data.get("equipment", ""))
            self.library_table.setItem(row, 3, eq_item)

            # 4. Action Button: "▶️ Watch Demo"
            btn = QPushButton("▶️ Watch Demo")
            btn.setObjectName("demo_btn")
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, n=name: self.open_exercise_demo_dialog(n))
            self.library_table.setCellWidget(row, 4, btn)

        self.library_table.resizeRowsToContents()

    def on_table_row_double_clicked(self, row, col):
        item = self.library_table.item(row, 0)
        if item:
            self.open_exercise_demo_dialog(item.text())

    def open_exercise_demo_dialog(self, exercise_name):
        dialog = ExerciseDemoDialog(exercise_name, self)
        dialog.exec()

    # =========================================================================
    # CALCULATOR LOGIC (SECTION 1 & SECTION 2)
    # =========================================================================
    def on_plan_params_changed(self):
        goal = self.goal_input.currentText()
        day = self.day_select.currentText()
        self.update_workout_table(goal, day)

    def update_workout_table(self, goal, day):
        self.workout_title.setText(f"WORKOUT PLAN — {goal.upper()} ({day.upper()})")
        day_workout = get_workout_details(goal, day)

        self.workout_table.setRowCount(0)
        self.workout_table.setRowCount(len(day_workout))

        for row, item in enumerate(day_workout):
            self.workout_table.setItem(row, 0, QTableWidgetItem(item.get("Exercise", "")))
            self.workout_table.setItem(row, 1, QTableWidgetItem(str(item.get("Sets", ""))))
            self.workout_table.setItem(row, 2, QTableWidgetItem(str(item.get("Reps", ""))))
            self.workout_table.setItem(row, 3, QTableWidgetItem(item.get("Rest", "")))
            self.workout_table.setItem(row, 4, QTableWidgetItem(item.get("Tips", "")))

        self.workout_table.resizeRowsToContents()

    def reset_form(self):
        self.name_input.clear()
        self.weight_input.clear()
        self.height_input.clear()
        self.age_input.clear()
        self.gender_select.setCurrentIndex(0)
        self.goal_input.setCurrentIndex(0)
        self.activity_input.setCurrentIndex(0)
        self.day_select.setCurrentIndex(0)
        self.result.setText("Fill in your details and click 'CALCULATE FITNESS PLAN' to generate your custom metrics and routine.")
        self.update_workout_table("Build Muscle", "Day 1")

    def calculate(self):
        try:
            name = self.name_input.text().strip() or "Athlete"
            weight_text = self.weight_input.text().strip()
            height_text = self.height_input.text().strip()
            age_text = self.age_input.text().strip()

            if not weight_text or not height_text or not age_text:
                self.result.setText("⚠️ Please fill in Weight, Height, and Age to calculate your plan.")
                return

            weight = float(weight_text)
            height = float(height_text)
            age = int(age_text)

            if weight <= 0 or height <= 0 or age <= 0:
                self.result.setText("⚠️ Please enter positive values for Weight, Height, and Age.")
                return

            # Convert cm to meters if user typed e.g. 175
            if height > 3.0:
                height = height / 100.0

            gender = self.gender_select.currentText()
            goal = self.goal_input.currentText()
            activity_label = self.activity_input.currentText()
            day = self.day_select.currentText()

            # BMI Calculation
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                bmi_status = "Underweight"
            elif bmi < 25:
                bmi_status = "Normal weight"
            elif bmi < 30:
                bmi_status = "Overweight"
            else:
                bmi_status = "Obese"

            # BMR Calculation (Mifflin-St Jeor Formula)
            height_cm = height * 100.0
            if gender == "Male":
                bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
            else:
                bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

            # Activity Multiplier
            if "Sedentary" in activity_label:
                factor = 1.2
            elif "Lightly" in activity_label:
                factor = 1.375
            elif "Moderately" in activity_label:
                factor = 1.55
            elif "Very Active" in activity_label:
                factor = 1.9
            else:
                factor = 1.725

            tdee = bmr * factor

            # Goal adjustment
            if goal == "Lose Weight":
                target_calories = tdee - 500
            elif goal == "Build Muscle":
                target_calories = tdee + 300
            else:
                target_calories = tdee

            # Macros & Water
            protein = weight * 2.0
            water_ml = weight * 35.0

            result_html = f"""
            <b>Athlete:</b> {name} &nbsp;|&nbsp; <b>Age:</b> {age} &nbsp;|&nbsp; <b>Gender:</b> {gender}<br>
            <b>Goal:</b> <span style="color:#35E06F;">{goal}</span><br><br>

            <b>BMI:</b> {bmi:.2f} &nbsp;(<span style="color:#35E06F;">{bmi_status}</span>)<br>
            <b>Basal Metabolic Rate (BMR):</b> {bmr:.0f} kcal/day<br>
            <b>Daily Energy Target:</b> <span style="color:#35E06F; font-size:16px;"><b>{target_calories:.0f} kcal/day</b></span><br>
            <b>Daily Protein Target:</b> {protein:.0f} g/day<br>
            <b>Daily Water Intake:</b> {water_ml / 1000.0:.2f} Liters/day ({water_ml:.0f} ml)
            """

            self.result.setText(result_html)
            self.update_workout_table(goal, day)

        except ValueError:
            self.result.setText("⚠️ Please enter valid numeric numbers for Weight, Height, and Age.")

    # =========================================================================
    # STYLESHEET
    # =========================================================================
    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #101418;
                color: #F5F7FA;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                font-size: 14px;
            }

            QTabWidget::pane {
                border: 1px solid #28333D;
                background-color: #101418;
                border-radius: 10px;
                top: -1px;
            }

            QTabBar::tab {
                background-color: #181E24;
                color: #8C9BAE;
                border: 1px solid #28333D;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: 700;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                margin-right: 4px;
            }

            QTabBar::tab:selected {
                background-color: #242E38;
                color: #35E06F;
                border-bottom: 2px solid #35E06F;
            }

            QTabBar::tab:hover {
                color: #FFFFFF;
                background-color: #1F2730;
            }

            QScrollArea {
                background-color: #101418;
                border: none;
            }

            QLabel#title {
                font-size: 26px;
                font-weight: 800;
                color: #35E06F;
                letter-spacing: 1px;
            }

            QLabel#subtitle {
                font-size: 13px;
                color: #8C9BAE;
            }

            QLabel {
                color: #CFD8DC;
                font-weight: 600;
                font-size: 13px;
            }

            QFrame#card {
                background-color: #181E24;
                border: 1px solid #28333D;
                border-radius: 12px;
            }

            QFrame#result_card {
                background-color: #161D23;
                border: 1px solid #2B3844;
                border-radius: 12px;
            }

            QLabel#section_title {
                font-size: 15px;
                font-weight: 700;
                color: #35E06F;
                letter-spacing: 0.5px;
            }

            QLabel#result {
                color: #ECEFF1;
                font-size: 14px;
                line-height: 1.6;
            }

            QLineEdit {
                background-color: #222B34;
                border: 1px solid #364452;
                border-radius: 8px;
                padding: 8px 10px;
                color: #FFFFFF;
                font-size: 14px;
            }

            QLineEdit:focus {
                border: 2px solid #35E06F;
                background-color: #26313C;
            }

            QComboBox {
                background-color: #222B34;
                border: 1px solid #364452;
                border-radius: 8px;
                padding: 8px 10px;
                color: #FFFFFF;
                font-size: 14px;
            }

            QComboBox:hover {
                border: 1px solid #35E06F;
            }

            QComboBox QAbstractItemView {
                background-color: #1C242C;
                color: #FFFFFF;
                border: 1px solid #364452;
                selection-background-color: #35E06F;
                selection-color: #101418;
                padding: 4px;
            }

            QPushButton#calculate_button {
                background-color: #35E06F;
                color: #0E171E;
                border: none;
                border-radius: 9px;
                padding: 12px;
                font-size: 14px;
                font-weight: 800;
                letter-spacing: 0.5px;
            }

            QPushButton#calculate_button:hover {
                background-color: #55EE8B;
            }

            QPushButton#calculate_button:pressed {
                background-color: #28BF5C;
            }

            QPushButton#secondary_button {
                background-color: #222B34;
                color: #B0BEC5;
                border: 1px solid #364452;
                border-radius: 8px;
                padding: 7px 12px;
                font-size: 12px;
                font-weight: 600;
            }

            QPushButton#secondary_button:hover {
                background-color: #2C3844;
                color: #FFFFFF;
                border-color: #35E06F;
            }

            QPushButton#demo_btn {
                background-color: rgba(53, 224, 111, 0.15);
                color: #35E06F;
                border: 1px solid #35E06F;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 12px;
                font-weight: 700;
            }

            QPushButton#demo_btn:hover {
                background-color: #35E06F;
                color: #101418;
            }

            QTableWidget {
                background-color: #181E24;
                alternate-background-color: #1F2730;
                border: 1px solid #2B3844;
                border-radius: 10px;
                gridline-color: #2B3844;
                color: #F5F7FA;
                font-size: 13px;
            }

            QTableWidget::item {
                padding: 6px 8px;
            }

            QTableWidget::item:selected {
                background-color: #1F4A2C;
                color: #FFFFFF;
            }

            QHeaderView::section {
                background-color: #242E38;
                color: #35E06F;
                padding: 8px;
                border: none;
                font-weight: 700;
                font-size: 13px;
            }

            QScrollBar:vertical, QScrollBar:horizontal {
                background: #101418;
                width: 10px;
                height: 10px;
                margin: 0px;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #2D3A47;
                border-radius: 5px;
                min-height: 25px;
                min-width: 25px;
            }

            QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
                background: #35E06F;
            }
        """)


def main():
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    window = FitnessApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()